# 🌟 Hub LLM Gratuit

**🌍 Read this in other languages:** [🇺🇸 English](../../README.md) • [🇧🇷 Português (BR)](README.pt-BR.md) • [🇵🇹 Português (PT)](README.pt-PT.md) • [🇪🇸 Español](README.es.md) • **🇫🇷 Français** • [🇨🇳 中文 (简体)](README.zh-CN.md) • [🇯🇵 日本語](README.ja.md)

![Anchors](https://github.com/felipetruman/free-llm-hub/actions/workflows/check-anchors.yml/badge.svg)

> Un catalogue unifié et communautaire d'API LLM, de moteurs d'inférence, de passerelles et de l'ensemble de l'écosystème LLM open-source.

**Total des entrées :** 187 • **Dernière mise à jour :** généré automatiquement


## 📑 Table des Matières

- [📡 API de Fournisseurs](#provider-apis) (18)
- [🔌 Fournisseurs d'Inférence](#inference-providers) (24)
- [💰 Plans d'Abonnement](#subscription-plans) (47)
- [🛠️ Moteurs d'Inférence (OSS)](#inference-engines-oss) (13)
- [🚪 Passerelles / Routeurs](#gateways-routers) (11)
- [🎨 API Spécialisées](#specialty-apis) (22)
- [🤖 Frameworks d'Agents](#agent-frameworks) (5)
- [📚 Frameworks LLM](#llm-frameworks) (6)
- [🗄️ Bases de Données Vectorielles](#vector-databases) (8)
- [📊 Frameworks d'Évaluation](#eval-frameworks) (4)
- [📦 Catalogues de Modèles](#model-catalogs) (4)
- [💻 Outils de Codage](#coding-tools) (5)
- [🖥️ Interfaces Utilisateur de Bureau](#desktop-uis) (6)
- [🧬 Familles de Modèles Open-Weights](#open-weights-families) (14)

---


## 📡 API de Fournisseurs

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **Google AI Studio (Gemini)** | US | 🟢 Freemium | 15 RPM, 1000 RPD | gemini-2.5-pro, gemini-2.5-flash, gemini-2.5-flash-lite | [🔗](https://aistudio.google.com) |
| **Mistral AI (La Plateforme)** | FR | 🟢 Freemium | 60 RPM, 1,000,000,000 tok/mo | mistral-large-3, mistral-small-3.1, ministral-8b | [🔗](https://console.mistral.ai) |
| **Cohere** | CA | 🟢 Freemium | 20 RPM | command-a, command-r-plus, command-r7b | [🔗](https://cohere.com) |
| **Zhipu AI (Z.AI / GLM)** | CN | 🟢 Freemium | — | glm-4.7-flash, glm-4.5-flash, glm-4.6v-flash | [🔗](https://open.bigmodel.cn) |
| **DeepSeek Platform** | CN | 💵 $0.14/$0.28 par MTok | — | deepseek-v3.2, deepseek-r1, deepseek-v4-pro | [🔗](https://platform.deepseek.com) |
| **Moonshot AI (Kimi)** | CN | 🟢 Freemium | — | kimi-k2.5, kimi-k2.6, kimi-long-context | [🔗](https://platform.moonshot.cn) |
| **DashScope (Alibaba)** | CN | 🟢 Freemium | — | qwen-max, qwen-plus, qwen-vl | [🔗](https://dashscope.aliyun.com) |
| **MiniMax** | CN | 🎁 Essai | — | minimax-m2.5, minimax-m2.1, abab6.5 | [🔗](https://api.minimax.chat) |
| **01.AI (Yi / 零一万物)** | CN | 🎁 Essai | — | yi-large, yi-lightning, yi-vision | [🔗](https://platform.01.ai) |
| **StepFun (阶跃星辰)** | CN | 🎁 Essai | — | step-3.5-flash, step-2 | [🔗](https://platform.stepfun.com) |
| **Baidu Qianfan (ERNIE)** | CN | 🟢 Freemium | — | ernie-4.0, ernie-speed | [🔗](https://qianfan.cloud.baidu.com) |
| **Tencent Hunyuan** | CN | 🟢 Freemium | — | hunyuan-lite, hunyuan-pro, hunyuan-turbo | [🔗](https://hunyuan.tencent.com) |
| **InternLM (Shanghai AI Lab)** | CN | 🟢 Freemium | — | internlm2.5, internvl | [🔗](https://internlm.intern-ai.org.cn) |
| **OpenAI API** | US | 💵 $1.25/$10.0 par MTok | — | gpt-5, gpt-5.1, gpt-5.2 | [🔗](https://platform.openai.com) |
| **Anthropic API** | US | 💵 $3.0/$15.0 par MTok | — | claude-sonnet-4.6, claude-opus-4.6, claude-haiku-4 | [🔗](https://console.anthropic.com) |
| **xAI Grok API** | US | 💵 $3.0/$15.0 par MTok | — | grok-3, grok-2 | [🔗](https://console.x.ai) |
| **Perplexity Sonar API** | US | 💵 Paiement au jeton | — | sonar, sonar-pro | [🔗](https://docs.perplexity.ai) |
| **Reka AI** | US | 🎁 Essai | — | reka-core, reka-flash, reka-edge | [🔗](https://reka.ai) |

## 🔌 Fournisseurs d'Inférence

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **Groq** | US | 🟢 Freemium | 30 RPM, 1000 RPD | llama-3.3-70b, llama-4-scout, kimi-k2 | [🔗](https://groq.com) |
| **Cerebras** | US | 🟢 Freemium | 30 RPM, 14400 RPD | llama-3.3-70b, qwen3-235b, gpt-oss-120b | [🔗](https://cloud.cerebras.ai) |
| **NVIDIA NIM** | US | 🟢 Freemium | 40 RPM | llama-3.3-70b, mistral-large, qwen3-235b | [🔗](https://build.nvidia.com) |
| **Cloudflare Workers AI** | US | 🟢 Freemium | — | llama-3.3-70b, qwen-qwq-32b, +47 more | [🔗](https://developers.cloudflare.com/workers-ai) |
| **HuggingFace Inference Providers** | US | 🟢 Freemium | — | llama-3.3-70b, qwen2.5-72b, mistral-7b | [🔗](https://huggingface.co/docs/inference-providers) |
| **OpenCode Zen** | US | 🟢 Freemium | — | — | [🔗](https://opencode.ai) |
| **Ollama Cloud** | US | 🟢 Freemium | — | deepseek-v3.2, qwen3.5, kimi-k2.5 | [🔗](https://ollama.com/cloud) |
| **LLM7.io** | GB | 🟢 Gratuit | 30 RPM | deepseek-r1, qwen2.5-coder, +27 more | [🔗](https://llm7.io) |
| **Kluster AI** | US | 🟢 Freemium | — | deepseek-r1, llama-4-maverick, qwen3-235b | [🔗](https://kluster.ai) |
| **Together AI** | US | 🎁 Essai de 5 $ | — | llama-3.3, mixtral, qwen-2.5 | [🔗](https://together.ai) |
| **Fireworks AI** | US | 🎁 Essai de 1 $ | 600 RPM | llama-3.3-70b, qwen-2.5-72b, deepseek-v3 | [🔗](https://fireworks.ai) |
| **DeepInfra** | US | 💵 $0.14/$0.28 par MTok | — | deepseek-v4-flash, kimi-k2.6, glm-5 | [🔗](https://deepinfra.com) |
| **Baseten** | US | 🎁 Essai de 30 $ | — | — | [🔗](https://baseten.co) |
| **Nebius** | NL | 🎁 Essai | — | — | [🔗](https://nebius.ai) |
| **Novita AI** | SG | 🎁 Essai | — | — | [🔗](https://novita.ai) |
| **Hyperbolic** | US | 🎁 Essai | — | llama-3.3, deepseek | [🔗](https://hyperbolic.xyz) |
| **SambaNova Cloud** | US | 🟢 Freemium | — | llama-4 | [🔗](https://cloud.sambanova.ai) |
| **Scaleway Generative APIs** | FR | 🟢 Freemium | — | — | [🔗](https://www.scaleway.com/en/generative-apis) |
| **Lepton AI** | US | 🎁 Essai de 10 $ | — | — | [🔗](https://lepton.ai) |
| **Avian.io** | US | 🟢 Freemium | — | llama-3.1-405b, qwen | [🔗](https://avian.io) |
| **Featherless AI** | US | 💳 10 $/mois | — | 4000+ HF models | [🔗](https://featherless.ai) |
| **Targon (Bittensor)** | US | 🟢 Freemium | — | deepseek, llama | [🔗](https://targon.com) |
| **Chutes** | — | 🎁 Essai | — | — | [🔗](https://chutes.ai) |
| **SiliconFlow (硅基流动)** | CN | 🟢 Freemium | 1000 RPM, 50000 TPM | qwen3-8b, deepseek-r1-distill, glm-4.1v-9b | [🔗](https://cloud.siliconflow.cn) |

## 💰 Plans d'Abonnement

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **ElevenLabs Starter** | — | 💳 5 $/mois | — | 30K caracteres TTS/mês | [🔗](https://elevenlabs.io/pricing) |
| **Suno Pro** | — | 💳 10 $/mois | — | 500 crédits quotidiens | [🔗](https://suno.com/pricing) |
| **Midjourney Basic** | — | 💳 10 $/mois | — | ~200 images/mês | [🔗](https://midjourney.com) |
| **GitHub Copilot Pro** | — | 💳 10 $/mois | — | gpt-5, claude-opus-4.6, gemini-3 | [🔗](https://github.com/features/copilot) |
| **Tabnine Pro** | — | 💳 12 $/mois | — | Code completion full-length, multi-LLM chat | [🔗](https://www.tabnine.com/pricing) |
| **Leonardo.ai Apprentice** | — | 💳 12 $/mois | — | — | [🔗](https://leonardo.ai) |
| **Descript Hobbyist** | — | 💳 12 $/mois | — | 10h de transcription/mois | [🔗](https://descript.com) |
| **Runway Standard** | — | 💳 15 $/mois | — | — | [🔗](https://runwayml.com/pricing) |
| **Windsurf Pro** | — | 💳 15 $/mois | — | claude-opus-4.6, gpt-5.4, gemini-3-pro | [🔗](https://windsurf.com/pricing) |
| **Mistral Le Chat Pro** | — | 💳 15 $/mois | — | mistral-large-3 | [🔗](https://chat.mistral.ai) |
| **Augment Code Indie** | — | 💳 15 $/mois | — | — | [🔗](https://augmentcode.com) |
| **Writesonic** | — | 💳 16 $/mois | — | — | [🔗](https://writesonic.com) |
| **GitHub Copilot Business** | — | 💳 19 $/mois | — | — | [🔗](https://github.com/features/copilot) |
| **Amazon Q Developer Pro** | — | 💳 19 $/mois | — | — | [🔗](https://aws.amazon.com/q/developer) |
| **NotebookLM Plus** | — | 💳 19.99 $/mois | — | — | [🔗](https://notebooklm.google) |
| **ChatGPT Plus** | — | 💳 20 $/mois | — | gpt-5.4, codex, dall-e-3 | [🔗](https://chatgpt.com) |
| **Claude Pro** | — | 💳 20 $/mois | — | claude-opus-4.6, claude-sonnet-4.6 | [🔗](https://claude.ai) |
| **Gemini Advanced** | — | 💳 20 $/mois | — | gemini-3-pro | [🔗](https://gemini.google.com) |
| **Perplexity Pro** | — | 💳 20 $/mois | — | — | [🔗](https://perplexity.ai/pro) |
| **Cursor Pro** | — | 💳 20 $/mois | — | claude-opus-4.6, gpt-5.4, gemini-3-pro | [🔗](https://cursor.com/pricing) |
| **v0 Premium (Vercel)** | — | 💳 20 $/mois | — | — | [🔗](https://v0.dev) |
| **Lovable** | — | 💳 20 $/mois | — | — | [🔗](https://lovable.dev) |
| **Claude Code Pro** | — | 💳 20 $/mois | — | — | [🔗](https://www.anthropic.com/claude-code) |
| **Grok Premium (X)** | — | 💳 22 $/mois | — | grok-3 | [🔗](https://x.com/i/grok) |
| **HeyGen Creator** | — | 💳 29 $/mois | — | — | [🔗](https://heygen.com) |
| **Synthesia Starter** | — | 💳 29 $/mois | — | — | [🔗](https://synthesia.io) |
| **Midjourney Standard** | — | 💳 30 $/mois | — | — | [🔗](https://midjourney.com) |
| **Tabnine Enterprise** | — | 💳 39 $/mois | — | Auto-hébergement VPC/sur site | [🔗](https://www.tabnine.com/pricing) |
| **GitHub Copilot Enterprise** | — | 💳 39 $/mois | — | — | [🔗](https://github.com/features/copilot) |
| **Cursor Teams** | — | 💳 40 $/mois | — | — | [🔗](https://cursor.com/pricing) |
| **Jasper Creator** | — | 💳 49 $/mois | — | — | [🔗](https://jasper.ai) |
| **Copy.ai Pro** | — | 💳 49 $/mois | — | — | [🔗](https://copy.ai) |
| **Cursor Pro+** | — | 💳 60 $/mois | — | 3x usage Claude/GPT/Gemini | [🔗](https://cursor.com/pricing) |
| **Windsurf Team** | — | 💳 100 $/mois | — | 1500 credits/user, SSO | [🔗](https://windsurf.com/pricing) |
| **ChatGPT Pro (new)** | — | 💳 100 $/mois | — | 5x Plus, 10x Codex | [🔗](https://chatgpt.com) |
| **Claude Max 5x** | — | 💳 100 $/mois | — | — | [🔗](https://claude.ai) |
| **ChatGPT Pro (original)** | — | 💳 200 $/mois | — | 20x Plus, Sora, exclusive Pro models | [🔗](https://chatgpt.com) |
| **Claude Max 20x** | — | 💳 200 $/mois | — | — | [🔗](https://claude.ai) |
| **Cursor Ultra** | — | 💳 200 $/mois | — | — | [🔗](https://cursor.com/pricing) |
| **Windsurf Max** | — | 💳 200 $/mois | — | Unlimited credits, 1M context | [🔗](https://windsurf.com/pricing) |
| **Gemini Ultra** | — | 💳 250 $/mois | — | gemini-3-pro-deep-think | [🔗](https://gemini.google.com) |
| **Devin (Cognition AI)** | — | 💳 500 $/mois | — | Agent de codage autonome | [🔗](https://devin.ai) |
| **OpenAI Enterprise** | — | 💳 Personnalisé | — | Tarification personnalisée, SOC2 | [🔗](https://openai.com/enterprise) |
| **Anthropic Enterprise** | — | 💳 Personnalisé | — | — | [🔗](https://anthropic.com/enterprise) |
| **AWS Bedrock** | — | 💵 Paiement au jeton | — | claude, llama, mistral | [🔗](https://aws.amazon.com/bedrock) |
| **Azure OpenAI** | — | 💵 Paiement au jeton | — | — | [🔗](https://azure.microsoft.com/en-us/products/ai-services/openai-service) |
| **Google Vertex AI** | — | 💵 Paiement au jeton | — | — | [🔗](https://cloud.google.com/vertex-ai) |

## 🛠️ Moteurs d'Inférence (OSS)

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **vLLM** | — | 🏠 Auto-hébergé | — | — | [🔗](https://vllm.ai) |
| **Ollama** | — | 🏠 Auto-hébergé | — | — | [🔗](https://ollama.com) |
| **llama.cpp** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/ggml-org/llama.cpp) |
| **Text Generation Inference (TGI)** | — | 🏠 Auto-hébergé | — | — | [🔗](https://huggingface.co/docs/text-generation-inference) |
| **SGLang** | — | 🏠 Auto-hébergé | — | — | [🔗](https://sgl-project.github.io) |
| **TensorRT-LLM** | — | 🏠 Auto-hébergé | — | — | [🔗](https://nvidia.github.io/TensorRT-LLM) |
| **LocalAI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://localai.io) |
| **LMDeploy** | — | 🏠 Auto-hébergé | — | — | [🔗](https://lmdeploy.readthedocs.io) |
| **MLC-LLM** | — | 🏠 Auto-hébergé | — | — | [🔗](https://llm.mlc.ai) |
| **KTransformers** | — | 🏠 Auto-hébergé | — | — | [🔗](https://kvcache-ai.github.io/ktransformers) |
| **ExLlamaV2** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/turboderp-org/exllamav2) |
| **Aphrodite Engine** | — | 🏠 Auto-hébergé | — | — | [🔗](https://aphrodite.pygmalion.chat) |
| **CTranslate2** | — | 🏠 Auto-hébergé | — | — | [🔗](https://opennmt.net/CTranslate2) |

## 🚪 Passerelles / Routeurs

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **OpenRouter** | US | 🟢 Freemium | 20 RPM, 50 RPD | deepseek-r1-free, llama-3.3-70b-free, gpt-oss-120b-free | [🔗](https://openrouter.ai) |
| **GitHub Models** | US | 🟢 Freemium | 15 RPM, 150 RPD | gpt-5, claude-sonnet-4, llama-3.3-70b | [🔗](https://github.com/marketplace/models) |
| **Vercel AI Gateway** | US | 🟢 Freemium | — | multiple | [🔗](https://vercel.com/ai-gateway) |
| **LiteLLM** | — | 🏠 Auto-hébergé | — | — | [🔗](https://litellm.ai) |
| **Portkey AI Gateway** | — | 🟢 Freemium | — | — | [🔗](https://portkey.ai) |
| **OneAPI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/songquanpeng/one-api) |
| **NewAPI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/Calcium-Ion/new-api) |
| **Helicone** | — | 🟢 Freemium | — | — | [🔗](https://helicone.ai) |
| **Langfuse** | — | 🟢 Freemium | — | — | [🔗](https://langfuse.com) |
| **RouteLLM** | — | 🏠 Auto-hébergé | — | — | [🔗](https://lmsys.org/blog/2024-07-01-routellm) |
| **Arize Phoenix** | — | 🏠 Auto-hébergé | — | — | [🔗](https://docs.arize.com/phoenix) |

## 🎨 API Spécialisées

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **ElevenLabs** | US | 🟢 Freemium | — | 10K caractères/mois gratuits | [🔗](https://elevenlabs.io) |
| **PlayHT** | — | 🟢 Freemium | — | 12.5K caractères/mois gratuits | [🔗](https://play.ht) |
| **Cartesia (Sonic)** | — | 🟢 Freemium | — | 10K caractères/mois gratuits | [🔗](https://cartesia.ai) |
| **Resemble AI** | — | 🎁 Essai | — | — | [🔗](https://resemble.ai) |
| **Coqui XTTS** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/coqui-ai/TTS) |
| **Kokoro TTS** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/hexgrad/kokoro) |
| **Deepgram** | — | 🎁 Essai de 200 $ | — | — | [🔗](https://deepgram.com) |
| **AssemblyAI** | — | 🎁 Essai de 50 $ | — | — | [🔗](https://assemblyai.com) |
| **Whisper** | — | 🏠 Auto-hébergé | — | — | [🔗](https://openai.com/research/whisper) |
| **faster-whisper** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/SYSTRAN/faster-whisper) |
| **Voyage AI** | — | 🟢 Freemium | — | 50M tokens gratuits | [🔗](https://voyageai.com) |
| **Jina AI** | — | 🟢 Freemium | — | 1M tokens gratuits | [🔗](https://jina.ai) |
| **Mixedbread** | DE | 🟢 Freemium | — | — | [🔗](https://mixedbread.ai) |
| **Nomic Atlas** | — | 🟢 Freemium | — | — | [🔗](https://atlas.nomic.ai) |
| **fal.ai** | — | 🎁 Essai | — | — | [🔗](https://fal.ai) |
| **Pollinations** | — | 🟢 Gratuit | — | — | [🔗](https://pollinations.ai) |
| **Replicate** | — | 🎁 Essai de 0.5 $ | — | — | [🔗](https://replicate.com) |
| **ComfyUI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://www.comfy.org) |
| **AUTOMATIC1111 WebUI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/AUTOMATIC1111/stable-diffusion-webui) |
| **Runway** | — | 💳 15 $/mois | — | — | [🔗](https://runwayml.com) |
| **Kling** | CN | 🟢 Freemium | — | — | [🔗](https://kling.ai) |
| **Black Forest Labs (FLUX)** | DE | 🎁 Essai | — | — | [🔗](https://bfl.ai) |

## 🤖 Frameworks d'Agents

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **CrewAI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://crewai.com) |
| **AutoGen** | — | 🏠 Auto-hébergé | — | — | [🔗](https://microsoft.github.io/autogen) |
| **LangGraph** | — | 🏠 Auto-hébergé | — | — | [🔗](https://langchain-ai.github.io/langgraph) |
| **Pydantic AI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://ai.pydantic.dev) |
| **Mastra** | — | 🏠 Auto-hébergé | — | — | [🔗](https://mastra.ai) |

## 📚 Frameworks LLM

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **LangChain** | — | 🏠 Auto-hébergé | — | — | [🔗](https://langchain.com) |
| **LlamaIndex** | — | 🏠 Auto-hébergé | — | — | [🔗](https://llamaindex.ai) |
| **Haystack** | — | 🏠 Auto-hébergé | — | — | [🔗](https://haystack.deepset.ai) |
| **DSPy** | — | 🏠 Auto-hébergé | — | — | [🔗](https://dspy.ai) |
| **Semantic Kernel** | — | 🏠 Auto-hébergé | — | — | [🔗](https://learn.microsoft.com/semantic-kernel) |
| **Vercel AI SDK** | — | 🟢 Gratuit | — | — | [🔗](https://sdk.vercel.ai) |

## 🗄️ Bases de Données Vectorielles

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **Qdrant** | — | 🟢 Freemium | — | 1 Go cloud gratuit | [🔗](https://qdrant.tech) |
| **Weaviate** | — | 🟢 Freemium | — | — | [🔗](https://weaviate.io) |
| **Milvus** | — | 🏠 Auto-hébergé | — | — | [🔗](https://milvus.io) |
| **Chroma** | — | 🏠 Auto-hébergé | — | — | [🔗](https://trychroma.com) |
| **pgvector** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/pgvector/pgvector) |
| **Pinecone** | — | 🟢 Freemium | — | 1 index gratuit | [🔗](https://pinecone.io) |
| **LanceDB** | — | 🏠 Auto-hébergé | — | — | [🔗](https://lancedb.com) |
| **Vespa** | — | 🏠 Auto-hébergé | — | — | [🔗](https://vespa.ai) |

## 📊 Frameworks d'Évaluation

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **Promptfoo** | — | 🏠 Auto-hébergé | — | — | [🔗](https://promptfoo.dev) |
| **DeepEval** | — | 🏠 Auto-hébergé | — | — | [🔗](https://deepeval.com) |
| **Ragas** | — | 🏠 Auto-hébergé | — | — | [🔗](https://ragas.io) |
| **OpenAI Evals** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/openai/evals) |

## 📦 Catalogues de Modèles

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **HuggingFace Hub** | — | 🟢 Freemium | — | — | [🔗](https://huggingface.co) |
| **ModelScope (Alibaba)** | CN | 🟢 Freemium | — | — | [🔗](https://modelscope.cn) |
| **models.dev** | — | 🟢 Gratuit | — | — | [🔗](https://models.dev) |
| **Civitai** | — | 🟢 Freemium | — | — | [🔗](https://civitai.com) |

## 💻 Outils de Codage

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **Aider** | — | 🏠 Auto-hébergé | — | — | [🔗](https://aider.chat) |
| **Cline** | — | 🏠 Auto-hébergé | — | — | [🔗](https://cline.bot) |
| **OpenHands** | — | 🏠 Auto-hébergé | — | — | [🔗](https://www.all-hands.dev) |
| **Continue.dev** | — | 🏠 Auto-hébergé | — | — | [🔗](https://continue.dev) |
| **Codex CLI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/openai/codex) |

## 🖥️ Interfaces Utilisateur de Bureau

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
|------|:-:|:-:|:-:|------|:-:|
| **Open WebUI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://openwebui.com) |
| **Text Generation WebUI** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/oobabooga/text-generation-webui) |
| **Jan** | — | 🏠 Auto-hébergé | — | — | [🔗](https://jan.ai) |
| **GPT4All** | — | 🏠 Auto-hébergé | — | — | [🔗](https://gpt4all.io) |
| **LM Studio** | — | 🟢 Gratuit | — | — | [🔗](https://lmstudio.ai) |
| **KoboldCpp** | — | 🏠 Auto-hébergé | — | — | [🔗](https://github.com/LostRuins/koboldcpp) |

## 🧬 Familles de Modèles Open-Weights

| Nom | Pays | Tarification | Limites de Taux | Modèles / Notes | Lien |
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

## 🔍 Modèles Découverts Automatiquement

> Généré automatiquement par `scripts/discover_models.py` sondant les points d'accès publics `/v1/models`. **9 fournisseurs** répondant publiquement, **1157 modèles** au total.

### 🟢 Points d'accès publics (aucune authentification requise)

| Fournisseur | Modèles | Point d'accès |
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
<summary>🔒 **15 fournisseurs nécessitent une authentification** (point d'accès valide, clé requise)</summary>

| Fournisseur | Statut |
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
<summary>⚠️ **3 points d'accès avec erreurs** (À FAIRE : investiguer)</summary>

| Fournisseur | Statut |
|----------|--------|
| `ollama-cloud` | not_found_404 |
| `opencode-zen` | not_found_404 |
| `perplexity-api` | not_found_404 |

</details>


---

## 🤝 Contribuer

Modifiez `data/0X-*.yaml`, exécutez `./scripts/merge.sh && python scripts/render_readme.py`, ouvrez une PR.

## 📜 Licence
MIT
