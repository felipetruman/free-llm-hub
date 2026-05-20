"""Shared selector module.

Used by both render_readme.py (generates README.md from data/) and
translate_readme.py (translates README.md to 6 languages).

Keeps the language selector as a single source of truth so the auto-update
workflow never strips it when regenerating the README.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

SELECTOR_MARKER = "🌍 Read this in other languages"


@dataclass(frozen=True)
class LangInfo:
    code: str
    name: str
    flag: str
    native: str


LANGUAGES: dict[str, LangInfo] = {
    "pt-BR": LangInfo("pt-BR", "Brazilian Portuguese", "🇧🇷", "Português (BR)"),
    "pt-PT": LangInfo("pt-PT", "European Portuguese",  "🇵🇹", "Português (PT)"),
    "es":    LangInfo("es",    "Spanish",              "🇪🇸", "Español"),
    "fr":    LangInfo("fr",    "French",               "🇫🇷", "Français"),
    "zh-CN": LangInfo("zh-CN", "Simplified Chinese",   "🇨🇳", "中文 (简体)"),
    "ja":    LangInfo("ja",    "Japanese",             "🇯🇵", "日本語"),
}


def build_selector(current_lang: str | None) -> str:
    """Build the language selector line.

    current_lang=None  → README.md (root)        — links go to .github/i18n/README.X.md
    current_lang='X'   → .github/i18n/README.X.md — links go to README.Y.md siblings + ../../README.md
    """
    is_root = current_lang is None
    links: list[str] = []

    if is_root:
        links.append("🇺🇸 **English**")
    else:
        links.append("[🇺🇸 English](../../README.md)")

    for code, info in LANGUAGES.items():
        label = f"{info.flag} {info.native}"
        if code == current_lang:
            links.append(f"**{label}**")
        else:
            path = f".github/i18n/README.{code}.md" if is_root else f"README.{code}.md"
            links.append(f"[{label}]({path})")

    return f"**{SELECTOR_MARKER}:** " + " • ".join(links)


# Detect selector line in any language by flag-cluster signature:
# 🇺🇸 plus 2+ other regional flags. Catches translated headers
# ("Leia isto em outros idiomas", "他の言語で読む", etc.)
_SELECTOR_SIG_RE = re.compile(
    r"🇺🇸.*(?:🇧🇷|🇵🇹|🇪🇸|🇫🇷|🇨🇳|🇯🇵).*(?:🇧🇷|🇵🇹|🇪🇸|🇫🇷|🇨🇳|🇯🇵)"
)


def strip_existing_selector(content: str) -> str:
    """Remove selector line (English marker or flag-cluster in any language)."""
    lines = content.splitlines()
    out: list[str] = []
    skip_next_blank = False
    for line in lines:
        if SELECTOR_MARKER in line or _SELECTOR_SIG_RE.search(line):
            if out and out[-1] == "":
                out.pop()
            skip_next_blank = True
            continue
        if skip_next_blank and line == "":
            skip_next_blank = False
            continue
        skip_next_blank = False
        out.append(line)
    return "\n".join(out)


def inject_selector(content: str, current_lang: str | None) -> str:
    """Insert language selector after first H1.

    Ensures blank line BEFORE and AFTER selector — without them, GitHub
    merges adjacent badges/images into the same paragraph.
    """
    content = strip_existing_selector(content)
    selector = build_selector(current_lang)
    lines = content.splitlines()
    out: list[str] = []
    inserted = False
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        if not inserted and line.startswith("# "):
            out.append("")
            out.append(selector)
            out.append("")
            inserted = True
            # If the source already had blank line(s) after the H1, skip them
            # so we don't end up with 2+ blank lines after the selector.
            j = i + 1
            while j < len(lines) and lines[j] == "":
                j += 1
            i = j
            continue
        i += 1
    result = "\n".join(out)
    result = re.sub(r"\n{4,}", "\n\n\n", result)
    return result.rstrip() + "\n"
