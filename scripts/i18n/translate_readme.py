#!/usr/bin/env python3
"""Translate README.md → .github/i18n/README.<lang>.md using Google Gemini.

Usage:
    python scripts/i18n/translate_readme.py                  # all languages
    python scripts/i18n/translate_readme.py pt-BR es         # specific ones
    python scripts/i18n/translate_readme.py --force pt-BR    # ignore cache
    python scripts/i18n/translate_readme.py --dry-run        # no API calls
    python scripts/i18n/translate_readme.py --check          # CI guardrail (no API)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import TYPE_CHECKING

from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent))
from _selector import (  # type: ignore[import-not-found]  # noqa: E402 — sibling module
    LANGUAGES,
    LangInfo,
    inject_selector,
    strip_existing_selector,
)

if TYPE_CHECKING:
    from google.genai import Client as GenaiClient  # noqa: F401

# ─── Config ─────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "README.md"
I18N_DIR = ROOT / ".github" / "i18n"
HASH_FILE = I18N_DIR / ".source-hash"
CACHE_FILE = ROOT / "scripts" / "i18n" / ".translation_cache.json"

load_dotenv(ROOT / ".env")

def _env_int(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw == "":
        return default
    try:
        return int(raw)
    except ValueError:
        sys.stderr.write(f"warn: invalid int for {name}={raw!r}, using default {default}\n")
        return default


API_KEY = os.getenv("GEMINI_API_KEY")
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
MAX_OUTPUT_TOKENS = _env_int("GEMINI_MAX_OUTPUT_TOKENS", 32768)
MAX_WORKERS = _env_int("I18N_MAX_WORKERS", 3)
MAX_RETRIES = 4
BASE_BACKOFF = 2.0

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("i18n")

PROMPT_TEMPLATE = """You are a professional technical translator specializing in open-source documentation.

Translate the following Markdown README from English to **{lang_name}**.

CRITICAL RULES:
1. **DO NOT translate**: code blocks, inline code, URLs, file paths, command-line flags, variable names, library/tool names (e.g., "GitHub Actions", "Ollama", "LangChain", "FastAPI").
2. **DO translate**: headings, prose, table headers/cells (text only), descriptions, comments inside code blocks ONLY if they are natural language.
3. **PRESERVE EXACTLY**: all Markdown syntax, emojis, badges, image links, anchor IDs (#section-name), HTML tags, tables structure, indentation.
4. **Anchor links** like `[text](#some-anchor)` → translate `text` only, keep `#some-anchor` unchanged.
5. **File references** like `[text](README.pt-BR.md)` or `[text](../../README.md)` → keep file paths unchanged.
6. **Numbers, statistics, dates** → keep as-is.
7. **Tone**: technical, clear, professional. Use native conventions of {lang_name}.
8. **Output ONLY the translated Markdown**. NO preamble, NO explanation, NO outer code fences wrapping the whole output.

--- BEGIN README ---
{content}
--- END README ---
"""


# ─── Hashing / Cache ────────────────────────────────────────────────────
def file_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def load_cache() -> set[str]:
    if CACHE_FILE.exists():
        try:
            data = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return set(data)
            if isinstance(data, dict):
                # backward compat with prior dict format
                return set(data.keys())
        except json.JSONDecodeError as e:
            log.warning("Cache file corrupted (%s), ignoring: %s", CACHE_FILE.name, e)
    return set()


def save_cache(cache: set[str]) -> None:
    tmp = CACHE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(sorted(cache), indent=2), encoding="utf-8")
    tmp.replace(CACHE_FILE)


def atomic_write(path: Path, content: str) -> None:
    """Write file atomically — prevents partial writes on crash."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


# ─── Validation ─────────────────────────────────────────────────────────
CODE_FENCE_RE = re.compile(r"^```", re.MULTILINE)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
ANCHOR_RE = re.compile(r"\(#([a-z0-9-]+)\)")


def strip_outer_fence(text: str) -> str:
    """Strip outer ```markdown ... ``` if LLM wrapped output."""
    stripped = text.strip()
    if stripped.startswith("```"):
        first_nl = stripped.find("\n")
        if first_nl != -1 and stripped.endswith("```"):
            return stripped[first_nl + 1 : -3].strip()
    return stripped


def validate_translation(source: str, translated: str) -> list[str]:
    problems: list[str] = []

    src_fences = len(CODE_FENCE_RE.findall(source))
    tgt_fences = len(CODE_FENCE_RE.findall(translated))
    if src_fences != tgt_fences:
        problems.append(f"code fence count mismatch: src={src_fences} tgt={tgt_fences}")

    src_anchors = set(ANCHOR_RE.findall(source))
    tgt_anchors = set(ANCHOR_RE.findall(translated))
    missing = src_anchors - tgt_anchors
    if missing:
        problems.append(f"missing anchors: {sorted(missing)[:5]}")

    src_links = len(LINK_RE.findall(source))
    tgt_links = len(LINK_RE.findall(translated))
    if abs(src_links - tgt_links) > max(5, src_links * 0.1):
        problems.append(f"link count drift: src={src_links} tgt={tgt_links}")

    if len(translated) < len(source) * 0.5:
        problems.append(f"output too short: {len(translated)} vs source {len(source)}")

    return problems


# ─── Check mode (CI guardrail, no API) ──────────────────────────────────
def check_sync() -> int:
    """Verify all translations exist and source hash matches stored hash."""
    if not SOURCE.exists():
        log.error("README.md not found")
        return 1

    current_hash = file_hash(SOURCE.read_text(encoding="utf-8"))
    stored_hash = HASH_FILE.read_text(encoding="utf-8").strip() if HASH_FILE.exists() else ""

    missing = [code for code in LANGUAGES if not (I18N_DIR / f"README.{code}.md").exists()]
    if missing:
        log.error("Missing translations: %s", missing)
        return 1

    if current_hash != stored_hash:
        log.error("README.md changed since last translation")
        log.error("Stored hash:  %s", stored_hash[:12] if stored_hash else "(none)")
        log.error("Current hash: %s", current_hash[:12])
        log.error("Run: python scripts/i18n/translate_readme.py")
        return 1

    log.info("All translations in sync with README.md")
    return 0


# ─── Translation ────────────────────────────────────────────────────────
# Substring patterns in exception messages that indicate non-transient failures
# (auth, quota exhausted, invalid request). Avoid hard SDK imports — match by text.
_NON_TRANSIENT_PATTERNS = (
    "api key",
    "api_key",
    "permission",
    "permission_denied",
    "unauthenticated",
    "unauthorized",
    "invalid argument",
    "invalid_argument",
    "not found",
    "404",
    "401",
    "403",
)


def _is_non_transient(exc: BaseException) -> bool:
    msg = str(exc).lower()
    return any(p in msg for p in _NON_TRANSIENT_PATTERNS)


def call_gemini(client: "GenaiClient", prompt: str, lang_code: str) -> str:
    from google.genai import types  # noqa: PLC0415 — deferred so --check works without google-genai installed

    last_err: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=0.2,
                    top_p=0.95,
                    max_output_tokens=MAX_OUTPUT_TOKENS,
                ),
            )
            if not response.candidates:
                raise RuntimeError("no candidates returned")

            cand = response.candidates[0]
            finish = getattr(cand, "finish_reason", None)
            finish_name = getattr(finish, "name", str(finish))
            if finish_name not in (None, "STOP"):
                # MAX_TOKENS, SAFETY, RECITATION, OTHER — treat as retryable failure
                # (truncated output should NOT be silently saved as success)
                raise RuntimeError(f"finish_reason={finish_name}")

            text = response.text
            if not text:
                raise RuntimeError("empty response text")
            return text

        except Exception as e:  # noqa: BLE001 — Gemini SDK raises many concrete types across versions
            last_err = e
            if _is_non_transient(e):
                log.error("[%s] non-transient error, aborting retries: %s", lang_code, e)
                raise RuntimeError(f"non-transient error: {e}") from e
            if attempt == MAX_RETRIES:
                break
            wait = BASE_BACKOFF * (2 ** (attempt - 1))
            log.warning("[%s] attempt %d failed: %s — retry in %.1fs", lang_code, attempt, e, wait)
            time.sleep(wait)

    raise RuntimeError(f"all {MAX_RETRIES} attempts failed: {last_err}") from last_err


def translate_one(
    client: "GenaiClient",
    info: LangInfo,
    source_for_llm: str,
    cache: set[str],
    src_hash: str,
    force: bool,
    dry_run: bool,
) -> tuple[str, bool, str]:
    code = info.code
    target_file = I18N_DIR / f"README.{code}.md"
    cache_key = f"{code}:{src_hash}"

    if not force and cache_key in cache and target_file.exists():
        return code, True, f"cached (hash {src_hash[:8]})"

    if dry_run:
        return code, True, "dry-run — would translate"

    prompt = PROMPT_TEMPLATE.format(lang_name=info.name, content=source_for_llm)
    raw = call_gemini(client, prompt, code)
    translated = strip_outer_fence(raw)
    translated = inject_selector(translated, current_lang=code)

    problems = validate_translation(source_for_llm, translated)
    if problems:
        return code, False, f"validation failed: {'; '.join(problems)}"

    atomic_write(target_file, translated)
    cache.add(cache_key)
    return code, True, f"{len(translated)} chars → .github/i18n/{target_file.name}"


# ─── Main ───────────────────────────────────────────────────────────────
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("languages", nargs="*", help="Target language codes (default: all)")
    p.add_argument("--force", action="store_true", help="Ignore cache, re-translate")
    p.add_argument("--dry-run", action="store_true", help="Skip API calls")
    p.add_argument("--check", action="store_true", help="CI guardrail — verify sync only")
    p.add_argument("--workers", type=int, default=MAX_WORKERS, help=f"Parallel workers (default {MAX_WORKERS})")
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if args.check:
        return check_sync()

    if not API_KEY:
        log.error("GEMINI_API_KEY not found in environment / .env")
        return 1
    if not SOURCE.exists():
        log.error("Source not found: %s", SOURCE)
        return 1

    I18N_DIR.mkdir(parents=True, exist_ok=True)

    targets = args.languages or list(LANGUAGES.keys())
    invalid = [t for t in targets if t not in LANGUAGES]
    if invalid:
        log.error("Unknown languages: %s — available: %s", invalid, list(LANGUAGES.keys()))
        return 1

    source_content = SOURCE.read_text(encoding="utf-8")
    log.info("Source: %s (%d chars)", SOURCE.name, len(source_content))

    # Normalize root README with selector
    root_with_selector = inject_selector(source_content, current_lang=None)
    if root_with_selector != source_content:
        if args.dry_run:
            log.info("[dry-run] Language selector would be normalized in %s", SOURCE.name)
        else:
            atomic_write(SOURCE, root_with_selector)
            log.info("Language selector normalized in %s", SOURCE.name)
        source_content = root_with_selector

    # Strip selector before sending to LLM — we re-inject per-language after
    source_for_llm = strip_existing_selector(source_content)
    src_hash = file_hash(source_content)

    from google import genai  # noqa: PLC0415 — deferred so --check works without google-genai installed
    cache = load_cache()
    client = genai.Client(api_key=API_KEY)

    log.info(
        "Translating to %d language(s) via %s (workers=%d, max_tokens=%d): %s",
        len(targets), MODEL_NAME, args.workers, MAX_OUTPUT_TOKENS, targets,
    )

    results: dict[str, tuple[bool, str]] = {}
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futures = {
            ex.submit(
                translate_one, client, LANGUAGES[code], source_for_llm,
                cache, src_hash, args.force, args.dry_run,
            ): code
            for code in targets
        }
        for fut in as_completed(futures):
            code = futures[fut]
            info = LANGUAGES[code]
            try:
                code, ok, msg = fut.result()
            except Exception as e:  # noqa: BLE001 — preserve partial progress on worker crash
                ok, msg = False, f"worker exception: {e}"
                log.error("%s [%s] EXCEPTION — %s", info.flag, code, e)
            results[code] = (ok, msg)
            if ok:
                log.info("%s [%s] OK — %s", info.flag, code, msg)
            else:
                log.error("%s [%s] FAIL — %s", info.flag, code, msg)

    save_cache(cache)

    failed = [c for c, (ok, _) in results.items() if not ok]
    if failed:
        log.error("Failures: %s", failed)
        return 2

    # Persist source hash so --check can verify sync
    if not args.dry_run:
        atomic_write(HASH_FILE, src_hash)
        log.info("Source hash saved: %s", HASH_FILE.relative_to(ROOT))

    log.info("Done — %d translation(s) succeeded", len(results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
