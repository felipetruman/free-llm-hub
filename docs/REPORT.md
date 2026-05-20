# Free LLM Hub — Analytical Report

> Auto-generated from `data/hub.yaml` and `data/discovered_models.json`
> Date: 2026-05-20

## Executive Summary

The free, cheap, and BYOK LLM API ecosystem is fragmenting fast. This report
catalogs every option we track and surfaces what's actually accessible today.

**Key numbers:**
- **188 entries** curated in the hub
- **14 distinct categories**
- **0 providers** responding publicly to `/v1/models`
- **0 models** auto-discovered live

**Top categories:**
- `subscription-plan`: 47
- `inference-provider`: 24
- `specialty-api`: 22
- `provider-api`: 18
- `open-weights-family`: 14
- `inference-engine`: 13
- `gateway`: 12
- `vector-db`: 8

## Provider Breakdown by Category


### agent-framework (5)

| Name | Pricing | URL |
|------|---------|-----|
| AutoGen | {'model': 'self-hosted'} | — |
| CrewAI | {'model': 'self-hosted'} | — |
| LangGraph | {'model': 'self-hosted'} | — |
| Mastra | {'model': 'self-hosted'} | — |
| Pydantic AI | {'model': 'self-hosted'} | — |

### coding-tool (5)

| Name | Pricing | URL |
|------|---------|-----|
| Aider | {'model': 'self-hosted'} | — |
| Cline | {'model': 'self-hosted'} | — |
| Codex CLI | {'model': 'self-hosted'} | — |
| Continue.dev | {'model': 'self-hosted'} | — |
| OpenHands | {'model': 'self-hosted'} | — |

### desktop-ui (6)

| Name | Pricing | URL |
|------|---------|-----|
| GPT4All | {'model': 'self-hosted'} | — |
| Jan | {'model': 'self-hosted'} | — |
| KoboldCpp | {'model': 'self-hosted'} | — |
| LM Studio | {'model': 'free'} | — |
| Open WebUI | {'model': 'self-hosted'} | — |
| Text Generation WebUI | {'model': 'self-hosted'} | — |

### eval-framework (4)

| Name | Pricing | URL |
|------|---------|-----|
| DeepEval | {'model': 'self-hosted'} | — |
| OpenAI Evals | {'model': 'self-hosted'} | — |
| Promptfoo | {'model': 'self-hosted'} | — |
| Ragas | {'model': 'self-hosted'} | — |

### gateway (12)

| Name | Pricing | URL |
|------|---------|-----|
| Arize Phoenix | {'model': 'self-hosted'} | — |
| GitHub Models | {'model': 'freemium', 'free_tier': True} | — |
| Helicone | {'model': 'freemium'} | — |
| Kilo Code Gateway | {'model': 'freemium', 'free_tier': True, 'requires_credit_card': False, 'trial_credits_usd': 5} | — |
| Langfuse | {'model': 'freemium'} | — |
| LiteLLM | {'model': 'self-hosted'} | — |
| NewAPI | {'model': 'self-hosted'} | — |
| OneAPI | {'model': 'self-hosted'} | — |
| OpenRouter | {'model': 'freemium', 'free_tier': True} | — |
| Portkey AI Gateway | {'model': 'freemium'} | — |
| RouteLLM | {'model': 'self-hosted'} | — |
| Vercel AI Gateway | {'model': 'freemium', 'free_tier': True} | — |

### inference-engine (13)

| Name | Pricing | URL |
|------|---------|-----|
| Aphrodite Engine | {'model': 'self-hosted'} | — |
| CTranslate2 | {'model': 'self-hosted'} | — |
| ExLlamaV2 | {'model': 'self-hosted'} | — |
| KTransformers | {'model': 'self-hosted'} | — |
| llama.cpp | {'model': 'self-hosted'} | — |
| LMDeploy | {'model': 'self-hosted'} | — |
| LocalAI | {'model': 'self-hosted'} | — |
| MLC-LLM | {'model': 'self-hosted'} | — |
| Ollama | {'model': 'self-hosted'} | — |
| SGLang | {'model': 'self-hosted'} | — |
| TensorRT-LLM | {'model': 'self-hosted'} | — |
| Text Generation Inference (TGI) | {'model': 'self-hosted'} | — |
| vLLM | {'model': 'self-hosted'} | — |

### inference-provider (24)

| Name | Pricing | URL |
|------|---------|-----|
| Avian.io | {'model': 'freemium', 'free_tier': True} | — |
| Baseten | {'model': 'trial-credits', 'trial_credits_usd': 30} | — |
| Cerebras | {'model': 'freemium', 'free_tier': True, 'requires_credit_card': False} | — |
| Chutes | {'model': 'trial-credits'} | — |
| Cloudflare Workers AI | {'model': 'freemium', 'free_tier': True} | — |
| DeepInfra | {'model': 'pay-per-token', 'input_per_mtok_usd': 0.14, 'output_per_mtok_usd': 0.28} | — |
| Featherless AI | {'model': 'subscription', 'monthly_usd': 10} | — |
| Fireworks AI | {'model': 'trial-credits', 'trial_credits_usd': 1} | — |
| Groq | {'model': 'freemium', 'free_tier': True, 'requires_credit_card': False} | — |
| HuggingFace Inference Providers | {'model': 'freemium', 'free_tier': True, 'trial_credits_usd': 0.1} | — |
| Hyperbolic | {'model': 'trial-credits'} | — |
| Kluster AI | {'model': 'freemium', 'free_tier': True} | — |
| Lepton AI | {'model': 'trial-credits', 'trial_credits_usd': 10} | — |
| LLM7.io | {'model': 'free'} | — |
| Nebius | {'model': 'trial-credits'} | — |
| Novita AI | {'model': 'trial-credits'} | — |
| NVIDIA NIM | {'model': 'freemium', 'free_tier': True} | — |
| Ollama Cloud | {'model': 'freemium', 'free_tier': True} | — |
| OpenCode Zen | {'model': 'freemium', 'free_tier': True} | — |
| SambaNova Cloud | {'model': 'freemium', 'free_tier': True} | — |
| Scaleway Generative APIs | {'model': 'freemium', 'free_tier': True} | — |
| SiliconFlow (硅基流动) | {'model': 'freemium', 'free_tier': True} | — |
| Targon (Bittensor) | {'model': 'freemium', 'free_tier': True} | — |
| Together AI | {'model': 'trial-credits', 'trial_credits_usd': 5} | — |

### llm-framework (6)

| Name | Pricing | URL |
|------|---------|-----|
| DSPy | {'model': 'self-hosted'} | — |
| Haystack | {'model': 'self-hosted'} | — |
| LangChain | {'model': 'self-hosted'} | — |
| LlamaIndex | {'model': 'self-hosted'} | — |
| Semantic Kernel | {'model': 'self-hosted'} | — |
| Vercel AI SDK | {'model': 'free'} | — |

### model-catalog (4)

| Name | Pricing | URL |
|------|---------|-----|
| Civitai | {'model': 'freemium'} | — |
| HuggingFace Hub | {'model': 'freemium', 'free_tier': True} | — |
| models.dev | {'model': 'free'} | — |
| ModelScope (Alibaba) | {'model': 'freemium', 'free_tier': True} | — |

### open-weights-family (14)

| Name | Pricing | URL |
|------|---------|-----|
| DeepSeek | — | — |
| Gemma (Google) | — | — |
| GLM (Zhipu) | — | — |
| gpt-oss (OpenAI) | — | — |
| Granite (IBM) | — | — |
| Hermes (Nous Research) | — | — |
| InternLM | — | — |
| Llama (Meta) | — | — |
| Mistral / Mixtral | — | — |
| OLMo (AllenAI) | — | — |
| Phi (Microsoft) | — | — |
| Qwen (Alibaba) | — | — |
| SmolLM (HuggingFace) | — | — |
| Yi (01.AI) | — | — |

### provider-api (18)

| Name | Pricing | URL |
|------|---------|-----|
| 01.AI (Yi / 零一万物) | {'model': 'trial-credits'} | — |
| Anthropic API | {'model': 'pay-per-token', 'input_per_mtok_usd': 3.0, 'output_per_mtok_usd': 15.0} | — |
| Baidu Qianfan (ERNIE) | {'model': 'freemium', 'free_tier': True} | — |
| Cohere | {'model': 'freemium', 'free_tier': True} | — |
| DashScope (Alibaba) | {'model': 'freemium', 'free_tier': True} | — |
| DeepSeek Platform | {'model': 'pay-per-token', 'input_per_mtok_usd': 0.14, 'output_per_mtok_usd': 0.28} | — |
| Google AI Studio (Gemini) | {'model': 'freemium', 'free_tier': True, 'requires_credit_card': False} | — |
| InternLM (Shanghai AI Lab) | {'model': 'freemium', 'free_tier': True} | — |
| MiniMax | {'model': 'trial-credits'} | — |
| Mistral AI (La Plateforme) | {'model': 'freemium', 'free_tier': True} | — |
| Moonshot AI (Kimi) | {'model': 'freemium', 'trial_credits_usd': None} | — |
| OpenAI API | {'model': 'pay-per-token', 'input_per_mtok_usd': 1.25, 'output_per_mtok_usd': 10.0} | — |
| Perplexity Sonar API | {'model': 'pay-per-token', 'trial_credits_usd': 5} | — |
| Reka AI | {'model': 'trial-credits'} | — |
| StepFun (阶跃星辰) | {'model': 'trial-credits', 'input_per_mtok_usd': 0.1, 'output_per_mtok_usd': 0.3} | — |
| Tencent Hunyuan | {'model': 'freemium', 'free_tier': True} | — |
| xAI Grok API | {'model': 'pay-per-token', 'input_per_mtok_usd': 3.0, 'output_per_mtok_usd': 15.0} | — |
| Zhipu AI (Z.AI / GLM) | {'model': 'freemium', 'free_tier': True} | — |

### specialty-api (22)

| Name | Pricing | URL |
|------|---------|-----|
| AssemblyAI | {'model': 'trial-credits', 'trial_credits_usd': 50} | — |
| AUTOMATIC1111 WebUI | {'model': 'self-hosted'} | — |
| Black Forest Labs (FLUX) | {'model': 'trial-credits'} | — |
| Cartesia (Sonic) | {'model': 'freemium', 'free_tier': True} | — |
| ComfyUI | {'model': 'self-hosted'} | — |
| Coqui XTTS | {'model': 'self-hosted'} | — |
| Deepgram | {'model': 'trial-credits', 'trial_credits_usd': 200} | — |
| ElevenLabs | {'model': 'freemium', 'free_tier': True, 'monthly_usd': None} | — |
| fal.ai | {'model': 'trial-credits'} | — |
| faster-whisper | {'model': 'self-hosted'} | — |
| Jina AI | {'model': 'freemium', 'free_tier': True} | — |
| Kling | {'model': 'freemium', 'free_tier': True} | — |
| Kokoro TTS | {'model': 'self-hosted'} | — |
| Mixedbread | {'model': 'freemium', 'free_tier': True} | — |
| Nomic Atlas | {'model': 'freemium', 'free_tier': True} | — |
| PlayHT | {'model': 'freemium', 'free_tier': True} | — |
| Pollinations | {'model': 'free'} | — |
| Replicate | {'model': 'trial-credits', 'trial_credits_usd': 0.5} | — |
| Resemble AI | {'model': 'trial-credits'} | — |
| Runway | {'model': 'subscription', 'monthly_usd': 15} | — |
| Voyage AI | {'model': 'freemium', 'free_tier': True} | — |
| Whisper | {'model': 'self-hosted'} | — |

### subscription-plan (47)

| Name | Pricing | URL |
|------|---------|-----|
| Amazon Q Developer Pro | {'model': 'subscription', 'monthly_usd': 19} | — |
| Anthropic Enterprise | {'model': 'subscription', 'monthly_usd': None} | — |
| Augment Code Indie | {'model': 'subscription', 'monthly_usd': 15} | — |
| AWS Bedrock | {'model': 'pay-per-token'} | — |
| Azure OpenAI | {'model': 'pay-per-token'} | — |
| ChatGPT Plus | {'model': 'subscription', 'monthly_usd': 20} | — |
| ChatGPT Pro (new) | {'model': 'subscription', 'monthly_usd': 100} | — |
| ChatGPT Pro (original) | {'model': 'subscription', 'monthly_usd': 200} | — |
| Claude Code Pro | {'model': 'subscription', 'monthly_usd': 20} | — |
| Claude Max 20x | {'model': 'subscription', 'monthly_usd': 200} | — |
| Claude Max 5x | {'model': 'subscription', 'monthly_usd': 100} | — |
| Claude Pro | {'model': 'subscription', 'monthly_usd': 20} | — |
| Copy.ai Pro | {'model': 'subscription', 'monthly_usd': 49} | — |
| Cursor Pro | {'model': 'subscription', 'monthly_usd': 20} | — |
| Cursor Pro+ | {'model': 'subscription', 'monthly_usd': 60} | — |
| Cursor Teams | {'model': 'subscription', 'monthly_usd': 40} | — |
| Cursor Ultra | {'model': 'subscription', 'monthly_usd': 200} | — |
| Descript Hobbyist | {'model': 'subscription', 'monthly_usd': 12} | — |
| Devin (Cognition AI) | {'model': 'subscription', 'monthly_usd': 500} | — |
| ElevenLabs Starter | {'model': 'subscription', 'monthly_usd': 5} | — |
| Gemini Advanced | {'model': 'subscription', 'monthly_usd': 20} | — |
| Gemini Ultra | {'model': 'subscription', 'monthly_usd': 250} | — |
| GitHub Copilot Business | {'model': 'subscription', 'monthly_usd': 19} | — |
| GitHub Copilot Enterprise | {'model': 'subscription', 'monthly_usd': 39} | — |
| GitHub Copilot Pro | {'model': 'subscription', 'monthly_usd': 10} | — |

_… and 22 more._


### vector-db (8)

| Name | Pricing | URL |
|------|---------|-----|
| Chroma | {'model': 'self-hosted'} | — |
| LanceDB | {'model': 'self-hosted'} | — |
| Milvus | {'model': 'self-hosted'} | — |
| pgvector | {'model': 'self-hosted'} | — |
| Pinecone | {'model': 'freemium', 'free_tier': True} | — |
| Qdrant | {'model': 'freemium', 'free_tier': True} | — |
| Vespa | {'model': 'self-hosted'} | — |
| Weaviate | {'model': 'freemium', 'free_tier': True} | — |
## Auto-Discovered Models

_(no discovery data yet)_

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
