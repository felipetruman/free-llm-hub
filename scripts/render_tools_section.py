#!/usr/bin/env python3
"""
Render Tools section + Positioning section into README.

Reads:
  - data/tools.yaml
  - docs/snippets/positioning.md

Writes Markdown to stdout, intended to be injected into README.md
between markers:
  <!-- TOOLS:START --> ... <!-- TOOLS:END -->
  <!-- POSITIONING:START --> ... <!-- POSITIONING:END -->
"""
from __future__ import annotations
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
TOOLS_PATH = ROOT / "data" / "tools.yaml"
POSITIONING_PATH = ROOT / "docs" / "snippets" / "positioning.md"


def render_tools() -> str:
    if not TOOLS_PATH.exists():
        return "_(no tools.yaml found)_\n"
    data = yaml.safe_load(TOOLS_PATH.read_text(encoding="utf-8"))
    tools = data.get("tools", [])
    if not tools:
        return "_(no tools registered)_\n"

    by_cat: dict[str, list[dict]] = {}
    for t in tools:
        by_cat.setdefault(t.get("category", "other"), []).append(t)

    out: list[str] = []
    out.append("## 🛠️ Tools Catalog\n")
    out.append(
        f"Proxies, gateways, routers and frameworks that complement the API "
        f"providers listed above. **{len(tools)} tools** indexed across "
        f"{len(by_cat)} categories.\n"
    )

    cat_order = ["proxy", "gateway", "router", "framework", "cli", "observability", "other"]
    seen = set()
    ordered = [c for c in cat_order if c in by_cat] + [
        c for c in by_cat if c not in cat_order
    ]

    for cat in ordered:
        if cat in seen:
            continue
        seen.add(cat)
        out.append(f"\n### {cat.title()}\n")
        out.append("| Tool | Stars | Language | License | OpenAI-compat | Description |")
        out.append("|------|------:|----------|---------|:-------------:|-------------|")
        for t in sorted(by_cat[cat], key=lambda x: -(x.get("stars") or 0)):
            name = f"[{t['name']}]({t['repo']})"
            stars = t.get("stars", "—")
            lang = t.get("language", "—")
            lic = t.get("license", "—")
            compat = "✅" if t.get("openai_compatible") else "—"
            desc = (t.get("description_en") or "").strip().replace("\n", " ")
            if len(desc) > 140:
                desc = desc[:137] + "..."
            out.append(f"| {name} | {stars} | {lang} | {lic} | {compat} | {desc} |")

    return "\n".join(out) + "\n"


def render_positioning() -> str:
    if not POSITIONING_PATH.exists():
        return "_(no positioning snippet found)_\n"
    return POSITIONING_PATH.read_text(encoding="utf-8")


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "--positioning":
        print(render_positioning())
    elif len(sys.argv) > 1 and sys.argv[1] == "--tools":
        print(render_tools())
    else:
        print("<!-- TOOLS:START -->")
        print(render_tools())
        print("<!-- TOOLS:END -->\n")
        print("<!-- POSITIONING:START -->")
        print(render_positioning())
        print("<!-- POSITIONING:END -->")


if __name__ == "__main__":
    main()
