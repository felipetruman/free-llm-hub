# 🌟 免费 LLM 中心

**🌍 Read this in other languages:** [🇺🇸 English](../../README.md) • [🇧🇷 Português (BR)](README.pt-BR.md) • [🇵🇹 Português (PT)](README.pt-PT.md) • [🇪🇸 Español](README.es.md) • [🇫🇷 Français](README.fr.md) • **🇨🇳 中文 (简体)** • [🇯🇵 日本語](README.ja.md)

![Anchors](https://github.com/felipetruman/free-llm-hub/actions/workflows/check-anchors.yml/badge.svg)

> 一个统一的、社区驱动的 LLM API、推理引擎、网关以及整个开源 LLM 生态系统的目录。

**总条目数：** 188 • **上次更新：** 自动生成


## 📑 目录

- [📡 提供商 API](#provider-apis) (18)
- [🔌 推理服务提供商](#inference-providers) (24)
- [💰 订阅计划](#subscription-plans) (47)
- [🛠️ 推理引擎 (开源)](#inference-engines-oss) (13)
- [🚪 网关 / 路由器](#gateways-routers) (12)
- [🎨 专业 API](#specialty-apis) (22)
- [🤖 智能体框架](#agent-frameworks) (5)
- [📚 LLM 框架](#llm-frameworks) (6)
- [🗄️ 向量数据库](#vector-databases) (8)
- [📊 评估框架](#eval-frameworks) (4)
- [📦 模型目录](#model-catalogs) (4)
- [💻 编程工具](#coding-tools) (5)
- [🖥️ 桌面 UI](#desktop-uis) (6)
- [🧬 开源权重模型家族](#open-weights-families) (14)

---


## 📡 提供商 API

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **Google AI Studio (Gemini)** | US | 🟢 免费增值 | 15 RPM, 1000 RPD | gemini-2.5-pro, gemini-2.5-flash, gemini-2.5-flash-lite | [🔗](https://aistudio.google.com) |
| **Mistral AI (La Plateforme)** | FR | 🟢 免费增值 | 60 RPM, 1,000,000,000 tok/mo | mistral-large-3, mistral-small-3.1, ministral-8b | [🔗](https://console.mistral.ai) |
| **Cohere** | CA | 🟢 免费增值 | 20 RPM | command-a, command-r-plus, command-r7b | [🔗](https://cohere.com) |
| **Zhipu AI (Z.AI / GLM)** | CN | 🟢 免费增值 | — | glm-4.7-flash, glm-4.5-flash, glm-4.6v-flash | [🔗](https://open.bigmodel.cn) |
| **DeepSeek Platform** | CN | 💵 $0.14/$0.28 per MTok | — | deepseek-v3.2, deepseek-r1, deepseek-v4-pro | [🔗](https://platform.deepseek.com) |
| **Moonshot AI (Kimi)** | CN | 🟢 免费增值 | — | kimi-k2.5, kimi-k2.6, kimi-long-context | [🔗](https://platform.moonshot.cn) |
| **DashScope (Alibaba)** | CN | 🟢 免费增值 | — | qwen-max, qwen-plus, qwen-vl | [🔗](https://dashscope.aliyun.com) |
| **MiniMax** | CN | 🎁 试用 | — | minimax-m2.5, minimax-m2.1, abab6.5 | [🔗](https://api.minimax.chat) |
| **01.AI (Yi / 零一万物)** | CN | 🎁 试用 | — | yi-large, yi-lightning, yi-vision | [🔗](https://platform.01.ai) |
| **StepFun (阶跃星辰)** | CN | 🎁 试用 | — | step-3.5-flash, step-2 | [🔗](https://platform.stepfun.com) |
| **Baidu Qianfan (ERNIE)** | CN | 🟢 免费增值 | — | ernie-4.0, ernie-speed | [🔗](https://qianfan.cloud.baidu.com) |
| **Tencent Hunyuan** | CN | 🟢 免费增值 | — | hunyuan-lite, hunyuan-pro, hunyuan-turbo | [🔗](https://hunyuan.tencent.com) |
| **InternLM (Shanghai AI Lab)** | CN | 🟢 免费增值 | — | internlm2.5, internvl | [🔗](https://internlm.intern-ai.org.cn) |
| **OpenAI API** | US | 💵 $1.25/$10.0 per MTok | — | gpt-5, gpt-5.1, gpt-5.2 | [🔗](https://platform.openai.com) |
| **Anthropic API** | US | 💵 $3.0/$15.0 per MTok | — | claude-sonnet-4.6, claude-opus-4.6, claude-haiku-4 | [🔗](https://console.anthropic.com) |
| **xAI Grok API** | US | 💵 $3.0/$15.0 per MTok | — | grok-3, grok-2 | [🔗](https://console.x.ai) |
| **Perplexity Sonar API** | US | 💵 按量付费 | — | sonar, sonar-pro | [🔗](https://docs.perplexity.ai) |
| **Reka AI** | US | 🎁 试用 | — | reka-core, reka-flash, reka-edge | [🔗](https://reka.ai) |

## 🔌 推理服务提供商

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **Groq** | US | 🟢 免费增值 | 30 RPM, 1000 RPD | llama-3.3-70b, llama-4-scout, kimi-k2 | [🔗](https://groq.com) |
| **Cerebras** | US | 🟢 免费增值 | 30 RPM, 14400 RPD | llama-3.3-70b, qwen3-235b, gpt-oss-120b | [🔗](https://cloud.cerebras.ai) |
| **NVIDIA NIM** | US | 🟢 免费增值 | 40 RPM | llama-3.3-70b, mistral-large, qwen3-235b | [🔗](https://build.nvidia.com) |
| **Cloudflare Workers AI** | US | 🟢 免费增值 | — | llama-3.3-70b, qwen-qwq-32b, +47 more | [🔗](https://developers.cloudflare.com/workers-ai) |
| **HuggingFace Inference Providers** | US | 🟢 免费增值 | — | llama-3.3-70b, qwen2.5-72b, mistral-7b | [🔗](https://huggingface.co/docs/inference-providers) |
| **OpenCode Zen** | US | 🟢 免费增值 | — | — | [🔗](https://opencode.ai) |
| **Ollama Cloud** | US | 🟢 免费增值 | — | deepseek-v3.2, qwen3.5, kimi-k2.5 | [🔗](https://ollama.com/cloud) |
| **LLM7.io** | GB | 🟢 免费 | 30 RPM | deepseek-r1, qwen2.5-coder, +27 more | [🔗](https://llm7.io) |
| **Kluster AI** | US | 🟢 免费增值 | — | deepseek-r1, llama-4-maverick, qwen3-235b | [🔗](https://kluster.ai) |
| **Together AI** | US | 🎁 $5 试用 | — | llama-3.3, mixtral, qwen-2.5 | [🔗](https://together.ai) |
| **Fireworks AI** | US | 🎁 $1 试用 | 600 RPM | llama-3.3-70b, qwen-2.5-72b, deepseek-v3 | [🔗](https://fireworks.ai) |
| **DeepInfra** | US | 💵 $0.14/$0.28 per MTok | — | deepseek-v4-flash, kimi-k2.6, glm-5 | [🔗](https://deepinfra.com) |
| **Baseten** | US | 🎁 $30 试用 | — | — | [🔗](https://baseten.co) |
| **Nebius** | NL | 🎁 试用 | — | — | [🔗](https://nebius.ai) |
| **Novita AI** | SG | 🎁 试用 | — | — | [🔗](https://novita.ai) |
| **Hyperbolic** | US | 🎁 试用 | — | llama-3.3, deepseek | [🔗](https://hyperbolic.xyz) |
| **SambaNova Cloud** | US | 🟢 免费增值 | — | llama-4 | [🔗](https://cloud.sambanova.ai) |
| **Scaleway Generative APIs** | FR | 🟢 免费增值 | — | — | [🔗](https://www.scaleway.com/en/generative-apis) |
| **Lepton AI** | US | 🎁 $10 试用 | — | — | [🔗](https://lepton.ai) |
| **Avian.io** | US | 🟢 免费增值 | — | llama-3.1-405b, qwen | [🔗](https://avian.io) |
| **Featherless AI** | US | 💳 $10/月 | — | 4000+ HF models | [🔗](https://featherless.ai) |
| **Targon (Bittensor)** | US | 🟢 免费增值 | — | deepseek, llama | [🔗](https://targon.com) |
| **Chutes** | — | 🎁 试用 | — | — | [🔗](https://chutes.ai) |
| **SiliconFlow (硅基流动)** | CN | 🟢 免费增值 | 1000 RPM, 50000 TPM | qwen3-8b, deepseek-r1-distill, glm-4.1v-9b | [🔗](https://cloud.siliconflow.cn) |

## 💰 订阅计划

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **ElevenLabs Starter** | — | 💳 $5/月 | — | 30K 字符 TTS/月 | [🔗](https://elevenlabs.io/pricing) |
| **Suno Pro** | — | 💳 $10/月 | — | 500 每日积分 | [🔗](https://suno.com/pricing) |
| **Midjourney Basic** | — | 💳 $10/月 | — | 约 200 张图片/月 | [🔗](https://midjourney.com) |
| **GitHub Copilot Pro** | — | 💳 $10/月 | — | gpt-5, claude-opus-4.6, gemini-3 | [🔗](https://github.com/features/copilot) |
| **Tabnine Pro** | — | 💳 $12/月 | — | 全长代码补全，多 LLM 聊天 | [🔗](https://www.tabnine.com/pricing) |
| **Leonardo.ai Apprentice** | — | 💳 $12/月 | — | — | [🔗](https://leonardo.ai) |
| **Descript Hobbyist** | — | 💳 $12/月 | — | 10 小时转录/月 | [🔗](https://descript.com) |
| **Runway Standard** | — | 💳 $15/月 | — | — | [🔗](https://runwayml.com/pricing) |
| **Windsurf Pro** | — | 💳 $15/月 | — | claude-opus-4.6, gpt-5.4, gemini-3-pro | [🔗](https://windsurf.com/pricing) |
| **Mistral Le Chat Pro** | — | 💳 $15/月 | — | mistral-large-3 | [🔗](https://chat.mistral.ai) |
| **Augment Code Indie** | — | 💳 $15/月 | — | — | [🔗](https://augmentcode.com) |
| **Writesonic** | — | 💳 $16/月 | — | — | [🔗](https://writesonic.com) |
| **GitHub Copilot Business** | — | 💳 $19/月 | — | — | [🔗](https://github.com/features/copilot) |
| **Amazon Q Developer Pro** | — | 💳 $19/月 | — | — | [🔗](https://aws.amazon.com/q/developer) |
| **NotebookLM Plus** | — | 💳 $19.99/月 | — | — | [🔗](https://notebooklm.google) |
| **ChatGPT Plus** | — | 💳 $20/月 | — | gpt-5.4, codex, dall-e-3 | [🔗](https://chatgpt.com) |
| **Claude Pro** | — | 💳 $20/月 | — | claude-opus-4.6, claude-sonnet-4.6 | [🔗](https://claude.ai) |
| **Gemini Advanced** | — | 💳 $20/月 | — | gemini-3-pro | [🔗](https://gemini.google.com) |
| **Perplexity Pro** | — | 💳 $20/月 | — | — | [🔗](https://perplexity.ai/pro) |
| **Cursor Pro** | — | 💳 $20/月 | — | claude-opus-4.6, gpt-5.4, gemini-3-pro | [🔗](https://cursor.com/pricing) |
| **v0 Premium (Vercel)** | — | 💳 $20/月 | — | — | [🔗](https://v0.dev) |
| **Lovable** | — | 💳 $20/月 | — | — | [🔗](https://lovable.dev) |
| **Claude Code Pro** | — | 💳 $20/月 | — | — | [🔗](https://www.anthropic.com/claude-code) |
| **Grok Premium (X)** | — | 💳 $22/月 | — | grok-3 | [🔗](https://x.com/i/grok) |
| **HeyGen Creator** | — | 💳 $29/月 | — | — | [🔗](https://heygen.com) |
| **Synthesia Starter** | — | 💳 $29/月 | — | — | [🔗](https://synthesia.io) |
| **Midjourney Standard** | — | 💳 $30/月 | — | — | [🔗](https://midjourney.com) |
| **Tabnine Enterprise** | — | 💳 $39/月 | — | VPC/本地自托管 | [🔗](https://www.tabnine.com/pricing) |
| **GitHub Copilot Enterprise** | — | 💳 $39/月 | — | — | [🔗](https://github.com/features/copilot) |
| **Cursor Teams** | — | 💳 $40/月 | — | — | [🔗](https://cursor.com/pricing) |
| **Jasper Creator** | — | 💳 $49/月 | — | — | [🔗](https://jasper.ai) |
| **Copy.ai Pro** | — | 💳 $49/月 | — | — | [🔗](https://copy.ai) |
| **Cursor Pro+** | — | 💳 $60/月 | — | 3 倍 Claude/GPT/Gemini 用量 | [🔗](https://cursor.com/pricing) |
| **Windsurf Team** | — | 💳 $100/月 | — | 1500 积分/用户, SSO | [🔗](https://windsurf.com/pricing) |
| **ChatGPT Pro (new)** | — | 💳 $100/月 | — | 5 倍 Plus, 10 倍 Codex | [🔗](https://chatgpt.com) |
| **Claude Max 5x** | — | 💳 $100/月 | — | — | [🔗](https://claude.ai) |
| **ChatGPT Pro (original)** | — | 💳 $200/月 | — | 20 倍 Plus, Sora, 独家 Pro 模型 | [🔗](https://chatgpt.com) |
| **Claude Max 20x** | — | 💳 $200/月 | — | — | [🔗](https://claude.ai) |
| **Cursor Ultra** | — | 💳 $200/月 | — | — | [🔗](https://cursor.com/pricing) |
| **Windsurf Max** | — | 💳 $200/月 | — | 无限积分, 1M 上下文 | [🔗](https://windsurf.com/pricing) |
| **Gemini Ultra** | — | 💳 $250/月 | — | gemini-3-pro-deep-think | [🔗](https://gemini.google.com) |
| **Devin (Cognition AI)** | — | 💳 $500/月 | — | 自主编程智能体 | [🔗](https://devin.ai) |
| **OpenAI Enterprise** | — | 💳 自定义 | — | 自定义定价, SOC2 | [🔗](https://openai.com/enterprise) |
| **Anthropic Enterprise** | — | 💳 自定义 | — | — | [🔗](https://anthropic.com/enterprise) |
| **AWS Bedrock** | — | 💵 按量付费 | — | claude, llama, mistral | [🔗](https://aws.amazon.com/bedrock) |
| **Azure OpenAI** | — | 💵 按量付费 | — | — | [🔗](https://azure.microsoft.com/en-us/products/ai-services/openai-service) |
| **Google Vertex AI** | — | 💵 按量付费 | — | — | [🔗](https://cloud.google.com/vertex-ai) |

## 🛠️ 推理引擎 (开源)

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **vLLM** | — | 🏠 自托管 | — | — | [🔗](https://vllm.ai) |
| **Ollama** | — | 🏠 自托管 | — | — | [🔗](https://ollama.com) |
| **llama.cpp** | — | 🏠 自托管 | — | — | [🔗](https://github.com/ggml-org/llama.cpp) |
| **Text Generation Inference (TGI)** | — | 🏠 自托管 | — | — | [🔗](https://huggingface.co/docs/text-generation-inference) |
| **SGLang** | — | 🏠 自托管 | — | — | [🔗](https://sgl-project.github.io) |
| **TensorRT-LLM** | — | 🏠 自托管 | — | — | [🔗](https://nvidia.github.io/TensorRT-LLM) |
| **LocalAI** | — | 🏠 自托管 | — | — | [🔗](https://localai.io) |
| **LMDeploy** | — | 🏠 自托管 | — | — | [🔗](https://lmdeploy.readthedocs.io) |
| **MLC-LLM** | — | 🏠 自托管 | — | — | [🔗](https://llm.mlc.ai) |
| **KTransformers** | — | 🏠 自托管 | — | — | [🔗](https://kvcache-ai.github.io/ktransformers) |
| **ExLlamaV2** | — | 🏠 自托管 | — | — | [🔗](https://github.com/turboderp-org/exllamav2) |
| **Aphrodite Engine** | — | 🏠 自托管 | — | — | [🔗](https://aphrodite.pygmalion.chat) |
| **CTranslate2** | — | 🏠 自托管 | — | — | [🔗](https://opennmt.net/CTranslate2) |

## 🚪 网关 / 路由器

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **OpenRouter** | US | 🟢 免费增值 | 20 RPM, 50 RPD | deepseek-r1-free, llama-3.3-70b-free, gpt-oss-120b-free | [🔗](https://openrouter.ai) |
| **GitHub Models** | US | 🟢 免费增值 | 15 RPM, 150 RPD | gpt-5, claude-sonnet-4, llama-3.3-70b | [🔗](https://github.com/marketplace/models) |
| **Vercel AI Gateway** | US | 🟢 免费增值 | — | multiple | [🔗](https://vercel.com/ai-gateway) |
| **LiteLLM** | — | 🏠 自托管 | — | — | [🔗](https://litellm.ai) |
| **Portkey AI Gateway** | — | 🟢 免费增值 | — | — | [🔗](https://portkey.ai) |
| **OneAPI** | — | 🏠 自托管 | — | — | [🔗](https://github.com/songquanpeng/one-api) |
| **NewAPI** | — | 🏠 自托管 | — | — | [🔗](https://github.com/Calcium-Ion/new-api) |
| **Helicone** | — | 🟢 免费增值 | — | — | [🔗](https://helicone.ai) |
| **Langfuse** | — | 🟢 免费增值 | — | — | [🔗](https://langfuse.com) |
| **RouteLLM** | — | 🏠 自托管 | — | — | [🔗](https://lmsys.org/blog/2024-07-01-routellm) |
| **Arize Phoenix** | — | 🏠 自托管 | — | — | [🔗](https://docs.arize.com/phoenix) |
| **Kilo Code Gateway** | US | 🟢 免费增值 | — | anthropic/claude-opus-4.7, anthropic/claude-sonnet-4.6, o... | [🔗](https://kilo.ai/gateway) |

## 🎨 专业 API

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **ElevenLabs** | US | 🟢 免费增值 | — | 10K 字符/月 免费 | [🔗](https://elevenlabs.io) |
| **PlayHT** | — | 🟢 免费增值 | — | 12.5K 字符/月 免费 | [🔗](https://play.ht) |
| **Cartesia (Sonic)** | — | 🟢 免费增值 | — | 10K 字符/月 免费 | [🔗](https://cartesia.ai) |
| **Resemble AI** | — | 🎁 试用 | — | — | [🔗](https://resemble.ai) |
| **Coqui XTTS** | — | 🏠 自托管 | — | — | [🔗](https://github.com/coqui-ai/TTS) |
| **Kokoro TTS** | — | 🏠 自托管 | — | — | [🔗](https://github.com/hexgrad/kokoro) |
| **Deepgram** | — | 🎁 $200 试用 | — | — | [🔗](https://deepgram.com) |
| **AssemblyAI** | — | 🎁 $50 试用 | — | — | [🔗](https://assemblyai.com) |
| **Whisper** | — | 🏠 自托管 | — | — | [🔗](https://openai.com/research/whisper) |
| **faster-whisper** | — | 🏠 自托管 | — | — | [🔗](https://github.com/SYSTRAN/faster-whisper) |
| **Voyage AI** | — | 🟢 免费增值 | — | 50M tokens 免费 | [🔗](https://voyageai.com) |
| **Jina AI** | — | 🟢 免费增值 | — | 1M tokens 免费 | [🔗](https://jina.ai) |
| **Mixedbread** | DE | 🟢 免费增值 | — | — | [🔗](https://mixedbread.ai) |
| **Nomic Atlas** | — | 🟢 免费增值 | — | — | [🔗](https://atlas.nomic.ai) |
| **fal.ai** | — | 🎁 试用 | — | — | [🔗](https://fal.ai) |
| **Pollinations** | — | 🟢 免费 | — | — | [🔗](https://pollinations.ai) |
| **Replicate** | — | 🎁 $0.5 试用 | — | — | [🔗](https://replicate.com) |
| **ComfyUI** | — | 🏠 自托管 | — | — | [🔗](https://www.comfy.org) |
| **AUTOMATIC1111 WebUI** | — | 🏠 自托管 | — | — | [🔗](https://github.com/AUTOMATIC1111/stable-diffusion-webui) |
| **Runway** | — | 💳 $15/月 | — | — | [🔗](https://runwayml.com) |
| **Kling** | CN | 🟢 免费增值 | — | — | [🔗](https://kling.ai) |
| **Black Forest Labs (FLUX)** | DE | 🎁 试用 | — | — | [🔗](https://bfl.ai) |

## 🤖 智能体框架

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **CrewAI** | — | 🏠 自托管 | — | — | [🔗](https://crewai.com) |
| **AutoGen** | — | 🏠 自托管 | — | — | [🔗](https://microsoft.github.io/autogen) |
| **LangGraph** | — | 🏠 自托管 | — | — | [🔗](https://langchain-ai.github.io/langgraph) |
| **Pydantic AI** | — | 🏠 自托管 | — | — | [🔗](https://ai.pydantic.dev) |
| **Mastra** | — | 🏠 自托管 | — | — | [🔗](https://mastra.ai) |

## 📚 LLM 框架

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **LangChain** | — | 🏠 自托管 | — | — | [🔗](https://langchain.com) |
| **LlamaIndex** | — | 🏠 自托管 | — | — | [🔗](https://llamaindex.ai) |
| **Haystack** | — | 🏠 自托管 | — | — | [🔗](https://haystack.deepset.ai) |
| **DSPy** | — | 🏠 自托管 | — | — | [🔗](https://dspy.ai) |
| **Semantic Kernel** | — | 🏠 自托管 | — | — | [🔗](https://learn.microsoft.com/semantic-kernel) |
| **Vercel AI SDK** | — | 🟢 免费 | — | — | [🔗](https://sdk.vercel.ai) |

## 🗄️ 向量数据库

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **Qdrant** | — | 🟢 免费增值 | — | 1GB 免费云服务 | [🔗](https://qdrant.tech) |
| **Weaviate** | — | 🟢 免费增值 | — | — | [🔗](https://weaviate.io) |
| **Milvus** | — | 🏠 自托管 | — | — | [🔗](https://milvus.io) |
| **Chroma** | — | 🏠 自托管 | — | — | [🔗](https://trychroma.com) |
| **pgvector** | — | 🏠 自托管 | — | — | [🔗](https://github.com/pgvector/pgvector) |
| **Pinecone** | — | 🟢 免费增值 | — | 1 个免费索引 | [🔗](https://pinecone.io) |
| **LanceDB** | — | 🏠 自托管 | — | — | [🔗](https://lancedb.com) |
| **Vespa** | — | 🏠 自托管 | — | — | [🔗](https://vespa.ai) |

## 📊 评估框架

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **Promptfoo** | — | 🏠 自托管 | — | — | [🔗](https://promptfoo.dev) |
| **DeepEval** | — | 🏠 自托管 | — | — | [🔗](https://deepeval.com) |
| **Ragas** | — | 🏠 自托管 | — | — | [🔗](https://ragas.io) |
| **OpenAI Evals** | — | 🏠 自托管 | — | — | [🔗](https://github.com/openai/evals) |

## 📦 模型目录

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **HuggingFace Hub** | — | 🟢 免费增值 | — | — | [🔗](https://huggingface.co) |
| **ModelScope (Alibaba)** | CN | 🟢 免费增值 | — | — | [🔗](https://modelscope.cn) |
| **models.dev** | — | 🟢 免费 | — | — | [🔗](https://models.dev) |
| **Civitai** | — | 🟢 免费增值 | — | — | [🔗](https://civitai.com) |

## 💻 编程工具

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **Aider** | — | 🏠 自托管 | — | — | [🔗](https://aider.chat) |
| **Cline** | — | 🏠 自托管 | — | — | [🔗](https://cline.bot) |
| **OpenHands** | — | 🏠 自托管 | — | — | [🔗](https://www.all-hands.dev) |
| **Continue.dev** | — | 🏠 自托管 | — | — | [🔗](https://continue.dev) |
| **Codex CLI** | — | 🏠 自托管 | — | — | [🔗](https://github.com/openai/codex) |

## 🖥️ 桌面 UI

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
|------|:-:|:-:|:-:|------|:-:|
| **Open WebUI** | — | 🏠 自托管 | — | — | [🔗](https://openwebui.com) |
| **Text Generation WebUI** | — | 🏠 自托管 | — | — | [🔗](https://github.com/oobabooga/text-generation-webui) |
| **Jan** | — | 🏠 自托管 | — | — | [🔗](https://jan.ai) |
| **GPT4All** | — | 🏠 自托管 | — | — | [🔗](https://gpt4all.io) |
| **LM Studio** | — | 🟢 免费 | — | — | [🔗](https://lmstudio.ai) |
| **KoboldCpp** | — | 🏠 自托管 | — | — | [🔗](https://github.com/LostRuins/koboldcpp) |

## 🧬 开源权重模型家族

| 名称 | 国家 | 定价 | 速率限制 | 模型 / 备注 | 链接 |
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

## 🔍 自动发现的模型

> 由 `scripts/discover_models.py` 探测公共 `/v1/models` 端点自动生成。**10 个提供商**公开响应，总计 **1528 个模型**。

### 🟢 公共端点 (无需认证)

| 提供商 | 模型数量 | 端点 |
|----------|------:|----------|
| `openrouter` | 367 | `https://openrouter.ai/api/v1` |
| `kilo-gateway` | 356 | `https://api.kilo.ai/api/gateway` |
| `vercel-ai-gateway` | 276 | `https://ai-gateway.vercel.sh/v1` |
| `deepinfra` | 151 | `https://api.deepinfra.com/v1/openai` |
| `nvidia-nim` | 131 | `https://integrate.api.nvidia.com/v1` |
| `huggingface-inference` | 117 | `https://router.huggingface.co/v1` |
| `novita` | 101 | `https://api.novita.ai/v3/openai` |
| `kluster` | 15 | `https://api.kluster.ai/v1` |
| `sambanova` | 9 | `https://api.sambanova.ai/v1` |
| `llm7` | 5 | `https://api.llm7.io/v1` |

<details>
<summary>🔒 <strong>14 个提供商需要认证</strong> (端点有效，需要密钥)</summary>

| 提供商 | 状态 |
|----------|--------|
| `cerebras` | auth_required_403 |
| `dashscope` | auth_required_401 |
| `deepseek` | auth_required_401 |
| `fireworks` | auth_required_401 |
| `github-models` | auth_required_401 |
| `groq` | auth_required_401 |
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
<summary>⚠️ <strong>4 个端点存在错误</strong> (TODO: 调查)</summary>

| 提供商 | 状态 |
|----------|--------|
| `minimax` | empty_response (200 但无模型) |
| `ollama-cloud` | not_found_404 |
| `opencode-zen` | not_found_404 |
| `perplexity-api` | not_found_404 |

</details>


---

## 🤝 贡献

编辑 `data/0X-*.yaml`，运行 `./scripts/merge.sh && python scripts/render_readme.py`，然后提交 PR。

## 📜 许可证
MIT
