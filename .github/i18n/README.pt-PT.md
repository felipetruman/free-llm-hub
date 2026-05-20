# 🌟 Hub de LLMs Gratuitos

**🌍 Read this in other languages:** [🇺🇸 English](../../README.md) • [🇧🇷 Português (BR)](README.pt-BR.md) • **🇵🇹 Português (PT)** • [🇪🇸 Español](README.es.md) • [🇫🇷 Français](README.fr.md) • [🇨🇳 中文 (简体)](README.zh-CN.md) • [🇯🇵 日本語](README.ja.md)

![Anchors](https://github.com/felipetruman/free-llm-hub/actions/workflows/check-anchors.yml/badge.svg)

> Um catálogo unificado e impulsionado pela comunidade de APIs de LLM, motores de inferência, gateways e todo o ecossistema de LLMs OSS.

**Total de entradas:** 187 • **Última atualização:** auto-gerada


## 📑 Índice

- [📡 APIs de Fornecedores](#provider-apis) (18)
- [🔌 Fornecedores de Inferência](#inference-providers) (24)
- [💰 Planos de Subscrição](#subscription-plans) (47)
- [🛠️ Motores de Inferência (OSS)](#inference-engines-oss) (13)
- [🚪 Gateways / Routers](#gateways-routers) (11)
- [🎨 APIs Especializadas](#specialty-apis) (22)
- [🤖 Frameworks de Agentes](#agent-frameworks) (5)
- [📚 Frameworks de LLM](#llm-frameworks) (6)
- [🗄️ Bases de Dados Vetoriais](#vector-databases) (8)
- [📊 Frameworks de Avaliação](#eval-frameworks) (4)
- [📦 Catálogos de Modelos](#model-catalogs) (4)
- [💻 Ferramentas de Codificação](#coding-tools) (5)
- [🖥️ UIs de Desktop](#desktop-uis) (6)
- [🧬 Famílias de Pesos Abertos](#open-weights-families) (14)

---


## 📡 APIs de Fornecedores

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **Google AI Studio (Gemini)** | US | 🟢 Freemium | 15 RPM, 1000 RPD | gemini-2.5-pro, gemini-2.5-flash, gemini-2.5-flash-lite | [🔗](https://aistudio.google.com) |
| **Mistral AI (La Plateforme)** | FR | 🟢 Freemium | 60 RPM, 1,000,000,000 tok/mo | mistral-large-3, mistral-small-3.1, ministral-8b | [🔗](https://console.mistral.ai) |
| **Cohere** | CA | 🟢 Freemium | 20 RPM | command-a, command-r-plus, command-r7b | [🔗](https://cohere.com) |
| **Zhipu AI (Z.AI / GLM)** | CN | 🟢 Freemium | — | glm-4.7-flash, glm-4.5-flash, glm-4.6v-flash | [🔗](https://open.bigmodel.cn) |
| **DeepSeek Platform** | CN | 💵 $0.14/$0.28 por MTok | — | deepseek-v3.2, deepseek-r1, deepseek-v4-pro | [🔗](https://platform.deepseek.com) |
| **Moonshot AI (Kimi)** | CN | 🟢 Freemium | — | kimi-k2.5, kimi-k2.6, kimi-long-context | [🔗](https://platform.moonshot.cn) |
| **DashScope (Alibaba)** | CN | 🟢 Freemium | — | qwen-max, qwen-plus, qwen-vl | [🔗](https://dashscope.aliyun.com) |
| **MiniMax** | CN | 🎁 Teste | — | minimax-m2.5, minimax-m2.1, abab6.5 | [🔗](https://api.minimax.chat) |
| **01.AI (Yi / 零一万物)** | CN | 🎁 Teste | — | yi-large, yi-lightning, yi-vision | [🔗](https://platform.01.ai) |
| **StepFun (阶跃星辰)** | CN | 🎁 Teste | — | step-3.5-flash, step-2 | [🔗](https://platform.stepfun.com) |
| **Baidu Qianfan (ERNIE)** | CN | 🟢 Freemium | — | ernie-4.0, ernie-speed | [🔗](https://qianfan.cloud.baidu.com) |
| **Tencent Hunyuan** | CN | 🟢 Freemium | — | hunyuan-lite, hunyuan-pro, hunyuan-turbo | [🔗](https://hunyuan.tencent.com) |
| **InternLM (Shanghai AI Lab)** | CN | 🟢 Freemium | — | internlm2.5, internvl | [🔗](https://internlm.intern-ai.org.cn) |
| **OpenAI API** | US | 💵 $1.25/$10.0 por MTok | — | gpt-5, gpt-5.1, gpt-5.2 | [🔗](https://platform.openai.com) |
| **Anthropic API** | US | 💵 $3.0/$15.0 por MTok | — | claude-sonnet-4.6, claude-opus-4.6, claude-haiku-4 | [🔗](https://console.anthropic.com) |
| **xAI Grok API** | US | 💵 $3.0/$15.0 por MTok | — | grok-3, grok-2 | [🔗](https://console.x.ai) |
| **Perplexity Sonar API** | US | 💵 Pagamento por token | — | sonar, sonar-pro | [🔗](https://docs.perplexity.ai) |
| **Reka AI** | US | 🎁 Teste | — | reka-core, reka-flash, reka-edge | [🔗](https://reka.ai) |

## 🔌 Fornecedores de Inferência

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **Groq** | US | 🟢 Freemium | 30 RPM, 1000 RPD | llama-3.3-70b, llama-4-scout, kimi-k2 | [🔗](https://groq.com) |
| **Cerebras** | US | 🟢 Freemium | 30 RPM, 14400 RPD | llama-3.3-70b, qwen3-235b, gpt-oss-120b | [🔗](https://cloud.cerebras.ai) |
| **NVIDIA NIM** | US | 🟢 Freemium | 40 RPM | llama-3.3-70b, mistral-large, qwen3-235b | [🔗](https://build.nvidia.com) |
| **Cloudflare Workers AI** | US | 🟢 Freemium | — | llama-3.3-70b, qwen-qwq-32b, +47 mais | [🔗](https://developers.cloudflare.com/workers-ai) |
| **HuggingFace Inference Providers** | US | 🟢 Freemium | — | llama-3.3-70b, qwen2.5-72b, mistral-7b | [🔗](https://huggingface.co/docs/inference-providers) |
| **OpenCode Zen** | US | 🟢 Freemium | — | — | [🔗](https://opencode.ai) |
| **Ollama Cloud** | US | 🟢 Freemium | — | deepseek-v3.2, qwen3.5, kimi-k2.5 | [🔗](https://ollama.com/cloud) |
| **LLM7.io** | GB | 🟢 Gratuito | 30 RPM | deepseek-r1, qwen2.5-coder, +27 mais | [🔗](https://llm7.io) |
| **Kluster AI** | US | 🟢 Freemium | — | deepseek-r1, llama-4-maverick, qwen3-235b | [🔗](https://kluster.ai) |
| **Together AI** | US | 🎁 $5 teste | — | llama-3.3, mixtral, qwen-2.5 | [🔗](https://together.ai) |
| **Fireworks AI** | US | 🎁 $1 teste | 600 RPM | llama-3.3-70b, qwen-2.5-72b, deepseek-v3 | [🔗](https://fireworks.ai) |
| **DeepInfra** | US | 💵 $0.14/$0.28 por MTok | — | deepseek-v4-flash, kimi-k2.6, glm-5 | [🔗](https://deepinfra.com) |
| **Baseten** | US | 🎁 $30 teste | — | — | [🔗](https://baseten.co) |
| **Nebius** | NL | 🎁 Teste | — | — | [🔗](https://nebius.ai) |
| **Novita AI** | SG | 🎁 Teste | — | — | [🔗](https://novita.ai) |
| **Hyperbolic** | US | 🎁 Teste | — | llama-3.3, deepseek | [🔗](https://hyperbolic.xyz) |
| **SambaNova Cloud** | US | 🟢 Freemium | — | llama-4 | [🔗](https://cloud.sambanova.ai) |
| **Scaleway Generative APIs** | FR | 🟢 Freemium | — | — | [🔗](https://www.scaleway.com/en/generative-apis) |
| **Lepton AI** | US | 🎁 $10 teste | — | — | [🔗](https://lepton.ai) |
| **Avian.io** | US | 🟢 Freemium | — | llama-3.1-405b, qwen | [🔗](https://avian.io) |
| **Featherless AI** | US | 💳 $10/mês | — | 4000+ HF models | [🔗](https://featherless.ai) |
| **Targon (Bittensor)** | US | 🟢 Freemium | — | deepseek, llama | [🔗](https://targon.com) |
| **Chutes** | — | 🎁 Teste | — | — | [🔗](https://chutes.ai) |
| **SiliconFlow (硅基流动)** | CN | 🟢 Freemium | 1000 RPM, 50000 TPM | qwen3-8b, deepseek-r1-distill, glm-4.1v-9b | [🔗](https://cloud.siliconflow.cn) |

## 💰 Planos de Subscrição

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **ElevenLabs Starter** | — | 💳 $5/mês | — | 30K caracteres TTS/mês | [🔗](https://elevenlabs.io/pricing) |
| **Suno Pro** | — | 💳 $10/mês | — | 500 créditos diários | [🔗](https://suno.com/pricing) |
| **Midjourney Basic** | — | 💳 $10/mês | — | ~200 imagens/mês | [🔗](https://midjourney.com) |
| **GitHub Copilot Pro** | — | 💳 $10/mês | — | gpt-5, claude-opus-4.6, gemini-3 | [🔗](https://github.com/features/copilot) |
| **Tabnine Pro** | — | 💳 $12/mês | — | Code completion full-length, multi-LLM chat | [🔗](https://www.tabnine.com/pricing) |
| **Leonardo.ai Apprentice** | — | 💳 $12/mês | — | — | [🔗](https://leonardo.ai) |
| **Descript Hobbyist** | — | 💳 $12/mês | — | 10h transcrição/mês | [🔗](https://descript.com) |
| **Runway Standard** | — | 💳 $15/mês | — | — | [🔗](https://runwayml.com/pricing) |
| **Windsurf Pro** | — | 💳 $15/mês | — | claude-opus-4.6, gpt-5.4, gemini-3-pro | [🔗](https://windsurf.com/pricing) |
| **Mistral Le Chat Pro** | — | 💳 $15/mês | — | mistral-large-3 | [🔗](https://chat.mistral.ai) |
| **Augment Code Indie** | — | 💳 $15/mês | — | — | [🔗](https://augmentcode.com) |
| **Writesonic** | — | 💳 $16/mês | — | — | [🔗](https://writesonic.com) |
| **GitHub Copilot Business** | — | 💳 $19/mês | — | — | [🔗](https://github.com/features/copilot) |
| **Amazon Q Developer Pro** | — | 💳 $19/mês | — | — | [🔗](https://aws.amazon.com/q/developer) |
| **NotebookLM Plus** | — | 💳 $19.99/mês | — | — | [🔗](https://notebooklm.google) |
| **ChatGPT Plus** | — | 💳 $20/mês | — | gpt-5.4, codex, dall-e-3 | [🔗](https://chatgpt.com) |
| **Claude Pro** | — | 💳 $20/mês | — | claude-opus-4.6, claude-sonnet-4.6 | [🔗](https://claude.ai) |
| **Gemini Advanced** | — | 💳 $20/mês | — | gemini-3-pro | [🔗](https://gemini.google.com) |
| **Perplexity Pro** | — | 💳 $20/mês | — | — | [🔗](https://perplexity.ai/pro) |
| **Cursor Pro** | — | 💳 $20/mês | — | claude-opus-4.6, gpt-5.4, gemini-3-pro | [🔗](https://cursor.com/pricing) |
| **v0 Premium (Vercel)** | — | 💳 $20/mês | — | — | [🔗](https://v0.dev) |
| **Lovable** | — | 💳 $20/mês | — | — | [🔗](https://lovable.dev) |
| **Claude Code Pro** | — | 💳 $20/mês | — | — | [🔗](https://www.anthropic.com/claude-code) |
| **Grok Premium (X)** | — | 💳 $22/mês | — | grok-3 | [🔗](https://x.com/i/grok) |
| **HeyGen Creator** | — | 💳 $29/mês | — | — | [🔗](https://heygen.com) |
| **Synthesia Starter** | — | 💳 $29/mês | — | — | [🔗](https://synthesia.io) |
| **Midjourney Standard** | — | 💳 $30/mês | — | — | [🔗](https://midjourney.com) |
| **Tabnine Enterprise** | — | 💳 $39/mês | — | Self-host VPC/on-prem | [🔗](https://www.tabnine.com/pricing) |
| **GitHub Copilot Enterprise** | — | 💳 $39/mês | — | — | [🔗](https://github.com/features/copilot) |
| **Cursor Teams** | — | 💳 $40/mês | — | — | [🔗](https://cursor.com/pricing) |
| **Jasper Creator** | — | 💳 $49/mês | — | — | [🔗](https://jasper.ai) |
| **Copy.ai Pro** | — | 💳 $49/mês | — | — | [🔗](https://copy.ai) |
| **Cursor Pro+** | — | 💳 $60/mês | — | 3x usage Claude/GPT/Gemini | [🔗](https://cursor.com/pricing) |
| **Windsurf Team** | — | 💳 $100/mês | — | 1500 créditos/utilizador, SSO | [🔗](https://windsurf.com/pricing) |
| **ChatGPT Pro (new)** | — | 💳 $100/mês | — | 5x Plus, 10x Codex | [🔗](https://chatgpt.com) |
| **Claude Max 5x** | — | 💳 $100/mês | — | — | [🔗](https://claude.ai) |
| **ChatGPT Pro (original)** | — | 💳 $200/mês | — | 20x Plus, Sora, exclusive Pro models | [🔗](https://chatgpt.com) |
| **Claude Max 20x** | — | 💳 $200/mês | — | — | [🔗](https://claude.ai) |
| **Cursor Ultra** | — | 💳 $200/mês | — | — | [🔗](https://cursor.com/pricing) |
| **Windsurf Max** | — | 💳 $200/mês | — | Créditos ilimitados, 1M contexto | [🔗](https://windsurf.com/pricing) |
| **Gemini Ultra** | — | 💳 $250/mês | — | gemini-3-pro-deep-think | [🔗](https://gemini.google.com) |
| **Devin (Cognition AI)** | — | 💳 $500/mês | — | Agente de codificação autónomo | [🔗](https://devin.ai) |
| **OpenAI Enterprise** | — | 💳 Personalizado | — | Preços personalizados, SOC2 | [🔗](https://openai.com/enterprise) |
| **Anthropic Enterprise** | — | 💳 Personalizado | — | — | [🔗](https://anthropic.com/enterprise) |
| **AWS Bedrock** | — | 💵 Pagamento por token | — | claude, llama, mistral | [🔗](https://aws.amazon.com/bedrock) |
| **Azure OpenAI** | — | 💵 Pagamento por token | — | — | [🔗](https://azure.microsoft.com/en-us/products/ai-services/openai-service) |
| **Google Vertex AI** | — | 💵 Pagamento por token | — | — | [🔗](https://cloud.google.com/vertex-ai) |

## 🛠️ Motores de Inferência (OSS)

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **vLLM** | — | 🏠 Auto-hospedado | — | — | [🔗](https://vllm.ai) |
| **Ollama** | — | 🏠 Auto-hospedado | — | — | [🔗](https://ollama.com) |
| **llama.cpp** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/ggml-org/llama.cpp) |
| **Text Generation Inference (TGI)** | — | 🏠 Auto-hospedado | — | — | [🔗](https://huggingface.co/docs/text-generation-inference) |
| **SGLang** | — | 🏠 Auto-hospedado | — | — | [🔗](https://sgl-project.github.io) |
| **TensorRT-LLM** | — | 🏠 Auto-hospedado | — | — | [🔗](https://nvidia.github.io/TensorRT-LLM) |
| **LocalAI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://localai.io) |
| **LMDeploy** | — | 🏠 Auto-hospedado | — | — | [🔗](https://lmdeploy.readthedocs.io) |
| **MLC-LLM** | — | 🏠 Auto-hospedado | — | — | [🔗](https://llm.mlc.ai) |
| **KTransformers** | — | 🏠 Auto-hospedado | — | — | [🔗](https://kvcache-ai.github.io/ktransformers) |
| **ExLlamaV2** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/turboderp-org/exllamav2) |
| **Aphrodite Engine** | — | 🏠 Auto-hospedado | — | — | [🔗](https://aphrodite.pygmalion.chat) |
| **CTranslate2** | — | 🏠 Auto-hospedado | — | — | [🔗](https://opennmt.net/CTranslate2) |

## 🚪 Gateways / Routers

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **OpenRouter** | US | 🟢 Freemium | 20 RPM, 50 RPD | deepseek-r1-free, llama-3.3-70b-free, gpt-oss-120b-free | [🔗](https://openrouter.ai) |
| **GitHub Models** | US | 🟢 Freemium | 15 RPM, 150 RPD | gpt-5, claude-sonnet-4, llama-3.3-70b | [🔗](https://github.com/marketplace/models) |
| **Vercel AI Gateway** | US | 🟢 Freemium | — | multiple | [🔗](https://vercel.com/ai-gateway) |
| **LiteLLM** | — | 🏠 Auto-hospedado | — | — | [🔗](https://litellm.ai) |
| **Portkey AI Gateway** | — | 🟢 Freemium | — | — | [🔗](https://portkey.ai) |
| **OneAPI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/songquanpeng/one-api) |
| **NewAPI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/Calcium-Ion/new-api) |
| **Helicone** | — | 🟢 Freemium | — | — | [🔗](https://helicone.ai) |
| **Langfuse** | — | 🟢 Freemium | — | — | [🔗](https://langfuse.com) |
| **RouteLLM** | — | 🏠 Auto-hospedado | — | — | [🔗](https://lmsys.org/blog/2024-07-01-routellm) |
| **Arize Phoenix** | — | 🏠 Auto-hospedado | — | — | [🔗](https://docs.arize.com/phoenix) |

## 🎨 APIs Especializadas

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **ElevenLabs** | US | 🟢 Freemium | — | 10K chars/mês gratuito | [🔗](https://elevenlabs.io) |
| **PlayHT** | — | 🟢 Freemium | — | 12.5K chars/mês gratuito | [🔗](https://play.ht) |
| **Cartesia (Sonic)** | — | 🟢 Freemium | — | 10K chars/mês gratuito | [🔗](https://cartesia.ai) |
| **Resemble AI** | — | 🎁 Teste | — | — | [🔗](https://resemble.ai) |
| **Coqui XTTS** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/coqui-ai/TTS) |
| **Kokoro TTS** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/hexgrad/kokoro) |
| **Deepgram** | — | 🎁 $200 teste | — | — | [🔗](https://deepgram.com) |
| **AssemblyAI** | — | 🎁 $50 teste | — | — | [🔗](https://assemblyai.com) |
| **Whisper** | — | 🏠 Auto-hospedado | — | — | [🔗](https://openai.com/research/whisper) |
| **faster-whisper** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/SYSTRAN/faster-whisper) |
| **Voyage AI** | — | 🟢 Freemium | — | 50M tokens gratuitos | [🔗](https://voyageai.com) |
| **Jina AI** | — | 🟢 Freemium | — | 1M tokens gratuitos | [🔗](https://jina.ai) |
| **Mixedbread** | DE | 🟢 Freemium | — | — | [🔗](https://mixedbread.ai) |
| **Nomic Atlas** | — | 🟢 Freemium | — | — | [🔗](https://atlas.nomic.ai) |
| **fal.ai** | — | 🎁 Teste | — | — | [🔗](https://fal.ai) |
| **Pollinations** | — | 🟢 Gratuito | — | — | [🔗](https://pollinations.ai) |
| **Replicate** | — | 🎁 $0.5 teste | — | — | [🔗](https://replicate.com) |
| **ComfyUI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://www.comfy.org) |
| **AUTOMATIC1111 WebUI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/AUTOMATIC1111/stable-diffusion-webui) |
| **Runway** | — | 💳 $15/mês | — | — | [🔗](https://runwayml.com) |
| **Kling** | CN | 🟢 Freemium | — | — | [🔗](https://kling.ai) |
| **Black Forest Labs (FLUX)** | DE | 🎁 Teste | — | — | [🔗](https://bfl.ai) |

## 🤖 Frameworks de Agentes

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **CrewAI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://crewai.com) |
| **AutoGen** | — | 🏠 Auto-hospedado | — | — | [🔗](https://microsoft.github.io/autogen) |
| **LangGraph** | — | 🏠 Auto-hospedado | — | — | [🔗](https://langchain-ai.github.io/langgraph) |
| **Pydantic AI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://ai.pydantic.dev) |
| **Mastra** | — | 🏠 Auto-hospedado | — | — | [🔗](https://mastra.ai) |

## 📚 Frameworks de LLM

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **LangChain** | — | 🏠 Auto-hospedado | — | — | [🔗](https://langchain.com) |
| **LlamaIndex** | — | 🏠 Auto-hospedado | — | — | [🔗](https://llamaindex.ai) |
| **Haystack** | — | 🏠 Auto-hospedado | — | — | [🔗](https://haystack.deepset.ai) |
| **DSPy** | — | 🏠 Auto-hospedado | — | — | [🔗](https://dspy.ai) |
| **Semantic Kernel** | — | 🏠 Auto-hospedado | — | — | [🔗](https://learn.microsoft.com/semantic-kernel) |
| **Vercel AI SDK** | — | 🟢 Gratuito | — | — | [🔗](https://sdk.vercel.ai) |

## 🗄️ Bases de Dados Vetoriais

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **Qdrant** | — | 🟢 Freemium | — | 1GB cloud gratuito | [🔗](https://qdrant.tech) |
| **Weaviate** | — | 🟢 Freemium | — | — | [🔗](https://weaviate.io) |
| **Milvus** | — | 🏠 Auto-hospedado | — | — | [🔗](https://milvus.io) |
| **Chroma** | — | 🏠 Auto-hospedado | — | — | [🔗](https://trychroma.com) |
| **pgvector** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/pgvector/pgvector) |
| **Pinecone** | — | 🟢 Freemium | — | 1 índice gratuito | [🔗](https://pinecone.io) |
| **LanceDB** | — | 🏠 Auto-hospedado | — | — | [🔗](https://lancedb.com) |
| **Vespa** | — | 🏠 Auto-hospedado | — | — | [🔗](https://vespa.ai) |

## 📊 Frameworks de Avaliação

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **Promptfoo** | — | 🏠 Auto-hospedado | — | — | [🔗](https://promptfoo.dev) |
| **DeepEval** | — | 🏠 Auto-hospedado | — | — | [🔗](https://deepeval.com) |
| **Ragas** | — | 🏠 Auto-hospedado | — | — | [🔗](https://ragas.io) |
| **OpenAI Evals** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/openai/evals) |

## 📦 Catálogos de Modelos

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **HuggingFace Hub** | — | 🟢 Freemium | — | — | [🔗](https://huggingface.co) |
| **ModelScope (Alibaba)** | CN | 🟢 Freemium | — | — | [🔗](https://modelscope.cn) |
| **models.dev** | — | 🟢 Gratuito | — | — | [🔗](https://models.dev) |
| **Civitai** | — | 🟢 Freemium | — | — | [🔗](https://civitai.com) |

## 💻 Ferramentas de Codificação

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **Aider** | — | 🏠 Auto-hospedado | — | — | [🔗](https://aider.chat) |
| **Cline** | — | 🏠 Auto-hospedado | — | — | [🔗](https://cline.bot) |
| **OpenHands** | — | 🏠 Auto-hospedado | — | — | [🔗](https://www.all-hands.dev) |
| **Continue.dev** | — | 🏠 Auto-hospedado | — | — | [🔗](https://continue.dev) |
| **Codex CLI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/openai/codex) |

## 🖥️ UIs de Desktop

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **Open WebUI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://openwebui.com) |
| **Text Generation WebUI** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/oobabooga/text-generation-webui) |
| **Jan** | — | 🏠 Auto-hospedado | — | — | [🔗](https://jan.ai) |
| **GPT4All** | — | 🏠 Auto-hospedado | — | — | [🔗](https://gpt4all.io) |
| **LM Studio** | — | 🟢 Gratuito | — | — | [🔗](https://lmstudio.ai) |
| **KoboldCpp** | — | 🏠 Auto-hospedado | — | — | [🔗](https://github.com/LostRuins/koboldcpp) |

## 🧬 Famílias de Pesos Abertos

| Nome | País | Preços | Limites de Taxa | Modelos / Notas | Link |
|------|:-:|:-:|:-:|------|:-:|
| **Llama (Meta)** | — | — | — | llama-3.3-70b, llama-4-scout, llama-4-maverick | [🔗](https://llama.com) |
| **Qwen (Alibaba)** | — | — | — | qwen3-0.6b, qwen3-8b, qwen3-72b | [🔗](https://qwenlm.github.io) |
| **DeepSeek** | — | — | — | deepseek-v3, deepseek-r1, deepseek-v4-pro | [🔗](https://deepseek.com) |
| **Mistral / Mixtral** | — | — | — | mistral-7b, mixtral-8x7b, mixtral-8x22b | [🔗](https://mistral.ai) |
| **Gemma (Google)** | — | — | — | gemma-3-1b, gemma-3-4b, gemma-3-12b | [🔗](https://ai.google.dev/gemma) |
| **Phi (Microsoft)** | — | — | — | phi-4, phi-4-mini | [🔗](https://huggingface.co/microsoft/phi-4) |
| **Yi (01.AI)** | — | — | — | yi-6b, yi-9b, yi-34b | [🔗](https://01.ai) |
| **InternLM** | — | — | — | internlm2.5-7b, internlm3-20b | [🔗](https://github.com/InternLM/InternLM) |
| **GLM (Zhipu)** | — | — | — | glm-4-9b, glm-4-32b, glm-4.5-flash | [🔗](https://github.com/THUDM/GLM-4) |
| **Hermes (Nous Research)** | — | — | — | hermes-3-405b, hermes-4 | [🔗](https://nousresearch.com) |
| **gpt-oss (OpenAI)** | — | — | — | gpt-oss-20b, gpt-oss-120b | [🔗](https://openai.com/index/introducing-gpt-oss) |
| **Granite (IBM)** | — | — | — | granite-3.0, granite-code | [🔗](https://www.ibm.com/granite) |
| **OLMo (AllenAI)** | — | — | — | olmo-2-1b, olmo-2-13b, olmo-2-32b | [🔗](https://allenai.org/olmo) |
| **SmolLM (HuggingFace)** | — | — | — | smollm-135m, smollm-360m, smollm-1.7b | [🔗](https://huggingface.co/blog/smollm) |

---

## 🔍 Modelos Auto-descobertos

> Auto-gerado por `scripts/discover_models.py` a sondar endpoints públicos `/v1/models`. **9 fornecedores** a responder publicamente, **1157 modelos** no total.

### 🟢 Endpoints públicos (sem autenticação necessária)

| Fornecedor | Modelos | Endpoint |
|----------|------:|----------|
| `openrouter` | 358 | `https://openrouter.ai/api/v1` |
| `vercel-ai-gateway` | 274 | `https://ai-gateway.vercel.sh/v1` |
| `deepinfra` | 141 | `https://api.deepinfra.com/v1/openai` |
| `huggingface-inference` | 131 | `https://router.huggingface.co/v1` |
| `nvidia-nim` | 119 | `https://integrate.api.nvidia.com/v1` |
| `novita` | 104 | `https://api.novita.ai/v3/openai` |
| `kluster` | 15 | `https://api.kluster.ai/v1` |
| `llm7` | 8 | `https://api.llm7.io/v1` |
| `sambanova` | 7 | `https://api.sambanova.ai/v1` |

<details>
<summary>🔒 **15 fornecedores requerem autenticação** (endpoint válido, chave necessária)</summary>

| Fornecedor | Status |
|----------|--------|
| `cerebras` | auth_required_403 |
| `dashscope` | auth_required_401 |
| `deepseek` | auth_required_401 |
| `fireworks` | auth_required_401 |
| `github-models` | auth_required_401 |
| `groq` | auth_required_401 |
| `minimax` | auth_required_401 |
| `mistral` | auth_required_401 |
| `moonshot` | auth_required_401 |
| `openai-api` | auth_required_401 |
| `scaleway` | auth_required_401 |
| `siliconflow` | auth_required_401 |
| `together` | auth_required_401 |
| `xai-grok` | auth_required_401 |
| `zhipu` | auth_required_401 |

</details>

<details>
<summary>⚠️ **3 endpoints com erros** (TODO: investigar)</summary>

| Fornecedor | Status |
|----------|--------|
| `ollama-cloud` | not_found_404 |
| `opencode-zen` | not_found_404 |
| `perplexity-api` | not_found_404 |

</details>


---

## 🤝 Contribuir

Edite `data/0X-*.yaml`, execute `./scripts/merge.sh && python scripts/render_readme.py`, abra um PR.

## 📜 Licença
MIT
