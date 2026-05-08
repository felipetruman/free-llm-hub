#!/usr/bin/env python3
"""
Auto-discovery de modelos via /v1/models para providers OpenAI-compatible.

Lê:
  - data/hub.yaml          → encontra entradas com openai_compatible=true
  - data/api_endpoints.yaml → mapa curado slug → api_base

Escreve:
  - data/discovered_models.json → resultado de cada discovery

Uso:
  python scripts/discover_models.py
  python scripts/discover_models.py --skip-local   # pula localhost (CI)
"""
from __future__ import annotations

import argparse
import asyncio
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx
import yaml

ROOT = Path(__file__).resolve().parent.parent
HUB = ROOT / "data" / "hub.yaml"
ENDPOINTS = ROOT / "data" / "api_endpoints.yaml"
OUT = ROOT / "data" / "discovered_models.json"

CONCURRENCY = 10
TIMEOUT = 8.0
RETRIES = 1


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def is_local(api_base: str) -> bool:
    return any(h in api_base for h in ("localhost", "127.0.0.1", "0.0.0.0"))


def has_placeholder(api_base: str) -> bool:
    """Detecta URLs com {placeholders} que precisam de config (ex: {account_id})."""
    return bool(re.search(r'\{[^}]+\}', api_base))


def extract_model_ids(payload: Any) -> list[str]:
    if isinstance(payload, dict):
        data = payload.get("data") or payload.get("models") or []
    elif isinstance(payload, list):
        data = payload
    else:
        return []

    ids: list[str] = []
    for item in data:
        if isinstance(item, dict):
            mid = item.get("id") or item.get("name") or item.get("model")
            if mid:
                ids.append(str(mid))
        elif isinstance(item, str):
            ids.append(item)
    return sorted(set(ids))


async def fetch(
    client: httpx.AsyncClient,
    sem: asyncio.Semaphore,
    slug: str,
    api_base: str,
) -> tuple[str, dict[str, Any]]:
    url = f"{api_base.rstrip('/')}/models"
    base_result = {"discovered_at": now_iso(), "url": url}

    async with sem:
        for attempt in range(RETRIES + 1):
            try:
                resp = await client.get(url, timeout=TIMEOUT, follow_redirects=True)

                if resp.status_code == 200:
                    try:
                        models = extract_model_ids(resp.json())
                        return slug, {**base_result, "status": "ok", "count": len(models), "models": models}
                    except (json.JSONDecodeError, ValueError):
                        return slug, {**base_result, "status": "invalid_json", "count": 0, "models": []}

                if resp.status_code in (401, 403):
                    return slug, {**base_result, "status": f"auth_required_{resp.status_code}", "count": 0, "models": []}

                if resp.status_code == 404:
                    return slug, {**base_result, "status": "not_found_404", "count": 0, "models": []}

                if attempt < RETRIES:
                    await asyncio.sleep(0.5 * (attempt + 1))
                    continue
                return slug, {**base_result, "status": f"http_{resp.status_code}", "count": 0, "models": []}

            except (httpx.TimeoutException, httpx.RequestError) as exc:
                if attempt < RETRIES:
                    await asyncio.sleep(0.5 * (attempt + 1))
                    continue
                return slug, {**base_result, "status": f"error_{type(exc).__name__}", "count": 0, "models": []}

    return slug, {**base_result, "status": "unknown", "count": 0, "models": []}


async def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-local", action="store_true", help="Pula endpoints em localhost")
    args = parser.parse_args()

    if not HUB.exists() or not ENDPOINTS.exists():
        print(f"❌ Faltando {HUB} ou {ENDPOINTS}", file=sys.stderr)
        return 1

    hub = yaml.safe_load(HUB.read_text(encoding="utf-8"))
    endpoints_map = yaml.safe_load(ENDPOINTS.read_text(encoding="utf-8")) or {}

    # Filtra: openai_compatible=true E mapeado em api_endpoints.yaml
    oc_slugs = {e["slug"] for e in hub if e.get("openai_compatible")}
    candidates: list[tuple[str, str]] = []
    skipped_local: list[str] = []
    unmapped: list[str] = []

    for slug in sorted(oc_slugs):
        cfg = endpoints_map.get(slug)
        if not cfg or not cfg.get("api_base"):
            unmapped.append(slug)
            continue
        api_base = cfg["api_base"]
        if has_placeholder(api_base):
            skipped_local.append(f'{slug} (placeholder)')
            continue
        if args.skip_local and is_local(api_base):
            skipped_local.append(slug)
            continue
        candidates.append((slug, api_base))

    print(f"🎯 {len(oc_slugs)} providers openai_compatible no hub")
    print(f"📍 {len(candidates)} mapeados e prontos pra discovery")
    if skipped_local:
        print(f"⏭️  {len(skipped_local)} pulados (local): {', '.join(skipped_local)}")
    if unmapped:
        print(f"⚠️  {len(unmapped)} sem mapeamento em api_endpoints.yaml:")
        for s in unmapped:
            print(f"      - {s}")
    print()
    print(f"🔍 Iniciando discovery (concorrência={CONCURRENCY}, timeout={TIMEOUT}s)...")

    sem = asyncio.Semaphore(CONCURRENCY)
    headers = {
        "User-Agent": "free-llm-hub/discover (+https://github.com/felipetruman/free-llm-hub)",
        "Accept": "application/json",
    }

    async with httpx.AsyncClient(headers=headers) as client:
        results = await asyncio.gather(*(fetch(client, sem, s, b) for s, b in candidates))

    out: dict[str, Any] = dict(results)

    # Stats
    print()
    print("═" * 55)
    print("📊 Resultados")
    print("═" * 55)

    from collections import Counter
    status_counter = Counter(r["status"] for r in out.values())
    for status, count in status_counter.most_common():
        emoji = "✅" if status == "ok" else ("🔒" if "auth" in status else "❌")
        print(f"  {emoji} {count:>3} — {status}")

    ok_results = [(s, r) for s, r in out.items() if r["status"] == "ok"]
    total_models = sum(r["count"] for _, r in ok_results)
    print()
    print(f"🎉 {len(ok_results)} providers descobertos com sucesso, {total_models} modelos no total")

    if ok_results:
        print()
        print("🏆 Top providers (por modelos descobertos):")
        for slug, r in sorted(ok_results, key=lambda x: x[1]["count"], reverse=True)[:10]:
            print(f"   {r['count']:>4} modelos — {slug}")

    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print()
    print(f"💾 Salvo em {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
