## 🆚 How is this different from other projects?

The free/cheap LLM ecosystem has several great projects that solve **adjacent** problems. Here's where `free-llm-hub` fits:

| Project | Type | What it does | What we do differently |
|---------|------|--------------|------------------------|
| [`tashfeenahmed/freellmapi`](https://github.com/tashfeenahmed/freellmapi) | 🔧 Runnable proxy | Aggregates ~14 free-tier keys behind one OpenAI endpoint, with failover | We **catalog 187+ providers and 1,528+ auto-discovered models** without requiring you to run a server |
| [`models.dev`](https://models.dev) | 📚 Model catalog | Lists 2,000+ models from 75+ providers (MIT, open data) | We add **endpoint health, auth metadata, BYOK gateways, self-hosted, and CLI tools** — broader scope |
| [`awesome-totally-open-chatgpt`](https://github.com/nichtdax/awesome-totally-open-chatgpt) | 📋 Static list | Curated awesome-list of open models | We are **auto-refreshed via CI** with live `/v1/models` discovery, not a static list |
| [`LiteLLM`](https://github.com/BerriAI/litellm) | 🛠️ SDK + proxy | Unifies 100+ APIs into OpenAI format | We **index LiteLLM itself** (and similar tools) — we're a registry, not another proxy |

### TL;DR positioning

> `free-llm-hub` is the **broadest auto-refreshed registry** of free, BYOK, self-hosted, and trial LLM APIs — plus the tools that route between them. Use it to **discover what exists**; use the projects above to **actually run** your requests.

We're **neutral and complementary**: most of the proxies and routers above appear inside our `data/tools.yaml` catalog.
