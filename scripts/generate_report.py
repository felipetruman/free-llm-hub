#!/usr/bin/env python3
"""
Generate an analytical Markdown report from data/hub.yaml.
Output: docs/REPORT.md (and optionally REPORT.pdf via pandoc).

Usage:
  python scripts/generate_report.py            # markdown only
  python scripts/generate_report.py --pdf      # also build PDF (requires pandoc + wkhtmltopdf or weasyprint)
"""
from __future__ import annotations
import sys
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
HUB = ROOT / "data" / "hub.yaml"
DISCOVERED = ROOT / "data" / "discovered_models.json"
OUT_MD = ROOT / "docs" / "REPORT.md"
OUT_PDF = ROOT / "docs" / "REPORT.pdf"


def load_hub() -> list[dict]:
    data = yaml.safe_load(HUB.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return data.get("entries") or data.get("providers") or []
    return data or []


def load_discovered() -> dict:
    import json
    if not DISCOVERED.exists():
        return {}
    return json.loads(DISCOVERED.read_text(encoding="utf-8"))


def section_executive_summary(entries: list[dict], discovered: dict) -> str:
    total = len(entries)
    categories = Counter(e.get("category") or e.get("type") or "uncategorized" for e in entries)
    disc = discovered.get("providers", {}) if isinstance(discovered, dict) else {}
    public = sum(1 for v in disc.values() if isinstance(v, dict) and v.get("status") == "ok")
    total_models = sum(
        v.get("count", 0) for v in disc.values()
        if isinstance(v, dict) and v.get("status") == "ok"
    )

    return f"""# Free LLM Hub — Analytical Report

> Auto-generated from `data/hub.yaml` and `data/discovered_models.json`
> Date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}

## Executive Summary

The free, cheap, and BYOK LLM API ecosystem is fragmenting fast. This report
catalogs every option we track and surfaces what's actually accessible today.

**Key numbers:**
- **{total} entries** curated in the hub
- **{len(categories)} distinct categories**
- **{public} providers** responding publicly to `/v1/models`
- **{total_models:,} models** auto-discovered live

**Top categories:**
{chr(10).join(f"- `{cat}`: {n}" for cat, n in categories.most_common(8))}
"""


def section_breakdown(entries: list[dict]) -> str:
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_cat[e.get("category") or e.get("type") or "uncategorized"].append(e)

    out = ["\n## Provider Breakdown by Category\n"]
    for cat in sorted(by_cat):
        items = by_cat[cat]
        out.append(f"\n### {cat} ({len(items)})\n")
        out.append("| Name | Pricing | URL |")
        out.append("|------|---------|-----|")
        for e in sorted(items, key=lambda x: (x.get("name") or "").lower())[:25]:
            name = e.get("name", "—")
            pricing = e.get("pricing") or e.get("free_tier") or "—"
            url = e.get("url") or e.get("homepage") or "—"
            out.append(f"| {name} | {pricing} | {url} |")
        if len(items) > 25:
            out.append(f"\n_… and {len(items) - 25} more._\n")
    return "\n".join(out)


def section_discovered(discovered: dict) -> str:
    disc = discovered.get("providers", {}) if isinstance(discovered, dict) else {}
    if not disc:
        return "\n## Auto-Discovered Models\n\n_(no discovery data yet)_\n"
    ok = [(k, v) for k, v in disc.items() if isinstance(v, dict) and v.get("status") == "ok"]
    ok.sort(key=lambda x: -x[1].get("count", 0))

    out = ["\n## Auto-Discovered Models (Top 15 Public Endpoints)\n"]
    out.append("| Provider | Models | Endpoint |")
    out.append("|----------|-------:|----------|")
    for name, info in ok[:15]:
        out.append(f"| {name} | {info.get('count', 0)} | `{info.get('endpoint', '—')}` |")
    return "\n".join(out)


def section_methodology() -> str:
    return """
## Methodology

- **Curation:** Manual entries in `data/hub.yaml` reviewed for accuracy.
- **Discovery:** Async GET requests to public `/v1/models` endpoints with
  8-second timeout and concurrency limit of 10. No credentials sent.
- **Refresh cadence:** Automated via GitHub Actions on every workflow run.
- **Categories:** free-tier, byok-gateway, self-hosted, trial, open-models, tool.

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) (coming soon — Phase C of roadmap).

## License

MIT — data and scripts. Individual provider terms apply.
"""


def main() -> None:
    entries = load_hub()
    discovered = load_discovered()

    md = (
        section_executive_summary(entries, discovered)
        + section_breakdown(entries)
        + section_discovered(discovered)
        + section_methodology()
    )

    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(md, encoding="utf-8")
    print(f"✅ {OUT_MD} written ({len(md):,} chars)")

    if "--pdf" in sys.argv:
        try:
            subprocess.run(
                ["pandoc", str(OUT_MD), "-o", str(OUT_PDF),
                 "--pdf-engine=weasyprint",
                 "--metadata", "title=Free LLM Hub Report"],
                check=True,
            )
            print(f"✅ {OUT_PDF} written")
        except (FileNotFoundError, subprocess.CalledProcessError) as e:
            print(f"⚠️  PDF generation skipped: {e}", file=sys.stderr)
            print("    Install: brew install pandoc weasyprint  (or apt)")


if __name__ == "__main__":
    main()
