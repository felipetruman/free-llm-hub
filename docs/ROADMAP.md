# 🗺️ Roadmap — free-llm-hub

> Mission: be the largest open-source registry of free/low-cost LLM APIs
> and developer tooling, helping devs save money while building with AI.

## ✅ Phase A — Foundation (DONE)
- [x] hub.yaml schema with 188 curated entries
- [x] Render pipeline (EN + PT-BR)
- [x] Endpoint verifier
- [x] CI workflow with cron + manual dispatch

## ✅ Phase B — Auto-discovery (DONE — PR #2)
- [x] api_endpoints.yaml mapping 28 OpenAI-compat providers
- [x] discover_models.py async probe (1.528 models found)
- [x] README section auto-generated

## 🚧 Phase C — Community
- [ ] CONTRIBUTING.md (how to add provider/tool)
- [ ] Issue templates (bug, new-provider, new-tool, model-update)
- [ ] PR template
- [ ] CODE_OF_CONDUCT.md (Contributor Covenant 2.1)
- [ ] Status badges (stars, last-updated, models count, CI)

## 🔮 Phase D — Restructure (the big one)
Goal: README becomes a navigation hub, deep content moves to docs/.

### New structure
- README.md → landing page (mission, top picks, quick links, badges)
- docs/providers/{free-tier,byok-gateways,self-hosted,trial}.md
- docs/tools/proxies/{litellm,9router,omniroute,cli-proxy-api,one-api}.md
- docs/tools/clients/{aider,continue,cline,opencode}.md
- docs/guides/{cost-optimization,byok-strategy,local-vs-cloud}.md
- docs/compare/{pricing-matrix,feature-matrix}.md

### New data file
- data/tools.yaml → catalog of proxies/CLIs/clients (separate from APIs)

### New script
- scripts/render_docs.py → generates docs/providers/*.md and docs/tools/*.md
  from YAML, keeping README.md as a curated landing page.

## 🌟 Phase E — Enrichment
- [ ] Cross-ref with models.dev/api.json for pricing enrichment
- [ ] Diff between discovery runs (alert when provider disappears)
- [ ] Static site (Astro/MkDocs) with search
- [ ] "Cost calculator" — paste use case, get cheapest combo

## 🎯 Tools backlog (Phase D priority)

### Proxies/Gateways (must-have)
- [ ] LiteLLM (BerriAI) — Python SDK + Proxy, 100+ LLMs
- [ ] CLI Proxy API (router-for-me) — 31k⭐ wrap Gemini/Codex/Claude CLIs
- [ ] OmniRoute (diegosouzapw) — 4.2k⭐ 160+ providers, 95% compression
- [ ] 9Router (decolua) — 5.4k⭐ 3-tier fallback, RTK token saver
- [ ] One API (songquanpeng) — ~20k⭐ classic gateway
- [ ] Portkey AI Gateway
- [ ] Helicone (observability + proxy)

### CLI Coding Agents (clients)
- [ ] Aider, Continue.dev, Cline, OpenCode, Claude Code, Codex CLI
- [ ] Cursor, Windsurf (commercial but BYOK)

### Frameworks
- [ ] LangChain, LlamaIndex, DSPy, Haystack, CrewAI, AutoGen
