# 🌟 無料LLMハブ

**🌍 Read this in other languages:** [🇺🇸 English](../../README.md) • [🇧🇷 Português (BR)](README.pt-BR.md) • [🇵🇹 Português (PT)](README.pt-PT.md) • [🇪🇸 Español](README.es.md) • [🇫🇷 Français](README.fr.md) • [🇨🇳 中文 (简体)](README.zh-CN.md) • **🇯🇵 日本語**

![Anchors](https://github.com/felipetruman/free-llm-hub/actions/workflows/check-anchors.yml/badge.svg)

> LLM API、推論エンジン、ゲートウェイ、およびOSS LLMエコシステム全体の統一されたコミュニティ主導型カタログ。

**総エントリ数:** 187 • **最終更新日:** 自動生成


## 📑 目次

- [📡 プロバイダーAPI](#provider-apis) (18)
- [🔌 推論プロバイダー](#inference-providers) (24)
- [💰 サブスクリプションプラン](#subscription-plans) (47)
- [🛠️ 推論エンジン (OSS)](#inference-engines-oss) (13)
- [🚪 ゲートウェイ / ルーター](#gateways-routers) (11)
- [🎨 特殊API](#specialty-apis) (22)
- [🤖 エージェントフレームワーク](#agent-frameworks) (5)
- [📚 LLMフレームワーク](#llm-frameworks) (6)
- [🗄️ ベクトルデータベース](#vector-databases) (8)
- [📊 評価フレームワーク](#eval-frameworks) (4)
- [📦 モデルカタログ](#model-catalogs) (4)
- [💻 コーディングツール](#coding-tools) (5)
- [🖥️ デスクトップUI](#desktop-uis) (6)
- [🧬 オープンウェイトモデルファミリー](#open-weights-families) (14)

---


## 📡 プロバイダーAPI

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **Google AI Studio (Gemini)** | US | 🟢 フリーミアム | 15 RPM, 1000 RPD | gemini-2.5-pro, gemini-2.5-flash, gemini-2.5-flash-lite | [🔗](https://aistudio.google.com) |
| **Mistral AI (La Plateforme)** | FR | 🟢 フリーミアム | 60 RPM, 1,000,000,000 tok/mo | mistral-large-3, mistral-small-3.1, ministral-8b | [🔗](https://console.mistral.ai) |
| **Cohere** | CA | 🟢 フリーミアム | 20 RPM | command-a, command-r-plus, command-r7b | [🔗](https://cohere.com) |
| **Zhipu AI (Z.AI / GLM)** | CN | 🟢 フリーミアム | — | glm-4.7-flash, glm-4.5-flash, glm-4.6v-flash | [🔗](https://open.bigmodel.cn) |
| **DeepSeek Platform** | CN | 💵 $0.14/$0.28 / MTok | — | deepseek-v3.2, deepseek-r1, deepseek-v4-pro | [🔗](https://platform.deepseek.com) |
| **Moonshot AI (Kimi)** | CN | 🟢 フリーミアム | — | kimi-k2.5, kimi-k2.6, kimi-long-context | [🔗](https://platform.moonshot.cn) |
| **DashScope (Alibaba)** | CN | 🟢 フリーミアム | — | qwen-max, qwen-plus, qwen-vl | [🔗](https://dashscope.aliyun.com) |
| **MiniMax** | CN | 🎁 トライアル | — | minimax-m2.5, minimax-m2.1, abab6.5 | [🔗](https://api.minimax.chat) |
| **01.AI (Yi / 零一万物)** | CN | 🎁 トライアル | — | yi-large, yi-lightning, yi-vision | [🔗](https://platform.01.ai) |
| **StepFun (阶跃星辰)** | CN | 🎁 トライアル | — | step-3.5-flash, step-2 | [🔗](https://platform.stepfun.com) |
| **Baidu Qianfan (ERNIE)** | CN | 🟢 フリーミアム | — | ernie-4.0, ernie-speed | [🔗](https://qianfan.cloud.baidu.com) |
| **Tencent Hunyuan** | CN | 🟢 フリーミアム | — | hunyuan-lite, hunyuan-pro, hunyuan-turbo | [🔗](https://hunyuan.tencent.com) |
| **InternLM (Shanghai AI Lab)** | CN | 🟢 フリーミアム | — | internlm2.5, internvl | [🔗](https://internlm.intern-ai.org.cn) |
| **OpenAI API** | US | 💵 $1.25/$10.0 / MTok | — | gpt-5, gpt-5.1, gpt-5.2 | [🔗](https://platform.openai.com) |
| **Anthropic API** | US | 💵 $3.0/$15.0 / MTok | — | claude-sonnet-4.6, claude-opus-4.6, claude-haiku-4 | [🔗](https://console.anthropic.com) |
| **xAI Grok API** | US | 💵 $3.0/$15.0 / MTok | — | grok-3, grok-2 | [🔗](https://console.x.ai) |
| **Perplexity Sonar API** | US | 💵 トークンごとの支払い | — | sonar, sonar-pro | [🔗](https://docs.perplexity.ai) |
| **Reka AI** | US | 🎁 トライアル | — | reka-core, reka-flash, reka-edge | [🔗](https://reka.ai) |

## 🔌 推論プロバイダー

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **Groq** | US | 🟢 フリーミアム | 30 RPM, 1000 RPD | llama-3.3-70b, llama-4-scout, kimi-k2 | [🔗](https://groq.com) |
| **Cerebras** | US | 🟢 フリーミアム | 30 RPM, 14400 RPD | llama-3.3-70b, qwen3-235b, gpt-oss-120b | [🔗](https://cloud.cerebras.ai) |
| **NVIDIA NIM** | US | 🟢 フリーミアム | 40 RPM | llama-3.3-70b, mistral-large, qwen3-235b | [🔗](https://build.nvidia.com) |
| **Cloudflare Workers AI** | US | 🟢 フリーミアム | — | llama-3.3-70b, qwen-qwq-32b, +47 more | [🔗](https://developers.cloudflare.com/workers-ai) |
| **HuggingFace Inference Providers** | US | 🟢 フリーミアム | — | llama-3.3-70b, qwen2.5-72b, mistral-7b | [🔗](https://huggingface.co/docs/inference-providers) |
| **OpenCode Zen** | US | 🟢 フリーミアム | — | — | [🔗](https://opencode.ai) |
| **Ollama Cloud** | US | 🟢 フリーミアム | — | deepseek-v3.2, qwen3.5, kimi-k2.5 | [🔗](https://ollama.com/cloud) |
| **LLM7.io** | GB | 🟢 無料 | 30 RPM | deepseek-r1, qwen2.5-coder, +27 more | [🔗](https://llm7.io) |
| **Kluster AI** | US | 🟢 フリーミアム | — | deepseek-r1, llama-4-maverick, qwen3-235b | [🔗](https://kluster.ai) |
| **Together AI** | US | 🎁 $5 トライアル | — | llama-3.3, mixtral, qwen-2.5 | [🔗](https://together.ai) |
| **Fireworks AI** | US | 🎁 $1 トライアル | 600 RPM | llama-3.3-70b, qwen-2.5-72b, deepseek-v3 | [🔗](https://fireworks.ai) |
| **DeepInfra** | US | 💵 $0.14/$0.28 / MTok | — | deepseek-v4-flash, kimi-k2.6, glm-5 | [🔗](https://deepinfra.com) |
| **Baseten** | US | 🎁 $30 トライアル | — | — | [🔗](https://baseten.co) |
| **Nebius** | NL | 🎁 トライアル | — | — | [🔗](https://nebius.ai) |
| **Novita AI** | SG | 🎁 トライアル | — | — | [🔗](https://novita.ai) |
| **Hyperbolic** | US | 🎁 トライアル | — | llama-3.3, deepseek | [🔗](https://hyperbolic.xyz) |
| **SambaNova Cloud** | US | 🟢 フリーミアム | — | llama-4 | [🔗](https://cloud.sambanova.ai) |
| **Scaleway Generative APIs** | FR | 🟢 フリーミアム | — | — | [🔗](https://www.scaleway.com/en/generative-apis) |
| **Lepton AI** | US | 🎁 $10 トライアル | — | — | [🔗](https://lepton.ai) |
| **Avian.io** | US | 🟢 フリーミアム | — | llama-3.1-405b, qwen | [🔗](https://avian.io) |
| **Featherless AI** | US | 💳 $10/月 | — | 4000+ HF models | [🔗](https://featherless.ai) |
| **Targon (Bittensor)** | US | 🟢 フリーミアム | — | deepseek, llama | [🔗](https://targon.com) |
| **Chutes** | — | 🎁 トライアル | — | — | [🔗](https://chutes.ai) |
| **SiliconFlow (硅基流动)** | CN | 🟢 フリーミアム | 1000 RPM, 50000 TPM | qwen3-8b, deepseek-r1-distill, glm-4.1v-9b | [🔗](https://cloud.siliconflow.cn) |

## 💰 サブスクリプションプラン

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **ElevenLabs Starter** | — | 💳 $5/月 | — | 30K 文字 TTS/月 | [🔗](https://elevenlabs.io/pricing) |
| **Suno Pro** | — | 💳 $10/月 | — | 500 クレジット/日 | [🔗](https://suno.com/pricing) |
| **Midjourney Basic** | — | 💳 $10/月 | — | ~200 画像/月 | [🔗](https://midjourney.com) |
| **GitHub Copilot Pro** | — | 💳 $10/月 | — | gpt-5, claude-opus-4.6, gemini-3 | [🔗](https://github.com/features/copilot) |
| **Tabnine Pro** | — | 💳 $12/月 | — | フルレングスのコード補完、マルチLLMチャット | [🔗](https://www.tabnine.com/pricing) |
| **Leonardo.ai Apprentice** | — | 💳 $12/月 | — | — | [🔗](https://leonardo.ai) |
| **Descript Hobbyist** | — | 💳 $12/月 | — | 10時間 転写/月 | [🔗](https://descript.com) |
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
| **Tabnine Enterprise** | — | 💳 $39/月 | — | VPC/オンプレミスでのセルフホスト | [🔗](https://www.tabnine.com/pricing) |
| **GitHub Copilot Enterprise** | — | 💳 $39/月 | — | — | [🔗](https://github.com/features/copilot) |
| **Cursor Teams** | — | 💳 $40/月 | — | — | [🔗](https://cursor.com/pricing) |
| **Jasper Creator** | — | 💳 $49/月 | — | — | [🔗](https://jasper.ai) |
| **Copy.ai Pro** | — | 💳 $49/月 | — | — | [🔗](https://copy.ai) |
| **Cursor Pro+** | — | 💳 $60/月 | — | Claude/GPT/Geminiの利用量が3倍 | [🔗](https://cursor.com/pricing) |
| **Windsurf Team** | — | 💳 $100/月 | — | 1500 クレジット/ユーザー、SSO | [🔗](https://windsurf.com/pricing) |
| **ChatGPT Pro (new)** | — | 💳 $100/月 | — | Plusの5倍、Codexの10倍 | [🔗](https://chatgpt.com) |
| **Claude Max 5x** | — | 💳 $100/月 | — | — | [🔗](https://claude.ai) |
| **ChatGPT Pro (original)** | — | 💳 $200/月 | — | Plusの20倍、Sora、Pro専用モデル | [🔗](https://chatgpt.com) |
| **Claude Max 20x** | — | 💳 $200/月 | — | — | [🔗](https://claude.ai) |
| **Cursor Ultra** | — | 💳 $200/月 | — | — | [🔗](https://cursor.com/pricing) |
| **Windsurf Max** | — | 💳 $200/月 | — | 無制限クレジット、1Mコンテキスト | [🔗](https://windsurf.com/pricing) |
| **Gemini Ultra** | — | 💳 $250/月 | — | gemini-3-pro-deep-think | [🔗](https://gemini.google.com) |
| **Devin (Cognition AI)** | — | 💳 $500/月 | — | 自律型コーディングエージェント | [🔗](https://devin.ai) |
| **OpenAI Enterprise** | — | 💳 カスタム | — | カスタム価格、SOC2 | [🔗](https://openai.com/enterprise) |
| **Anthropic Enterprise** | — | 💳 カスタム | — | — | [🔗](https://anthropic.com/enterprise) |
| **AWS Bedrock** | — | 💵 トークンごとの支払い | — | claude, llama, mistral | [🔗](https://aws.amazon.com/bedrock) |
| **Azure OpenAI** | — | 💵 トークンごとの支払い | — | — | [🔗](https://azure.microsoft.com/en-us/products/ai-services/openai-service) |
| **Google Vertex AI** | — | 💵 トークンごとの支払い | — | — | [🔗](https://cloud.google.com/vertex-ai) |

## 🛠️ 推論エンジン (OSS)

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **vLLM** | — | 🏠 セルフホスト | — | — | [🔗](https://vllm.ai) |
| **Ollama** | — | 🏠 セルフホスト | — | — | [🔗](https://ollama.com) |
| **llama.cpp** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/ggml-org/llama.cpp) |
| **Text Generation Inference (TGI)** | — | 🏠 セルフホスト | — | — | [🔗](https://huggingface.co/docs/text-generation-inference) |
| **SGLang** | — | 🏠 セルフホスト | — | — | [🔗](https://sgl-project.github.io) |
| **TensorRT-LLM** | — | 🏠 セルフホスト | — | — | [🔗](https://nvidia.github.io/TensorRT-LLM) |
| **LocalAI** | — | 🏠 セルフホスト | — | — | [🔗](https://localai.io) |
| **LMDeploy** | — | 🏠 セルフホスト | — | — | [🔗](https://lmdeploy.readthedocs.io) |
| **MLC-LLM** | — | 🏠 セルフホスト | — | — | [🔗](https://llm.mlc.ai) |
| **KTransformers** | — | 🏠 セルフホスト | — | — | [🔗](https://kvcache-ai.github.io/ktransformers) |
| **ExLlamaV2** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/turboderp-org/exllamav2) |
| **Aphrodite Engine** | — | 🏠 セルフホスト | — | — | [🔗](https://aphrodite.pygmalion.chat) |
| **CTranslate2** | — | 🏠 セルフホスト | — | — | [🔗](https://opennmt.net/CTranslate2) |

## 🚪 ゲートウェイ / ルーター

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **OpenRouter** | US | 🟢 フリーミアム | 20 RPM, 50 RPD | deepseek-r1-free, llama-3.3-70b-free, gpt-oss-120b-free | [🔗](https://openrouter.ai) |
| **GitHub Models** | US | 🟢 フリーミアム | 15 RPM, 150 RPD | gpt-5, claude-sonnet-4, llama-3.3-70b | [🔗](https://github.com/marketplace/models) |
| **Vercel AI Gateway** | US | 🟢 フリーミアム | — | 複数 | [🔗](https://vercel.com/ai-gateway) |
| **LiteLLM** | — | 🏠 セルフホスト | — | — | [🔗](https://litellm.ai) |
| **Portkey AI Gateway** | — | 🟢 フリーミアム | — | — | [🔗](https://portkey.ai) |
| **OneAPI** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/songquanpeng/one-api) |
| **NewAPI** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/Calcium-Ion/new-api) |
| **Helicone** | — | 🟢 フリーミアム | — | — | [🔗](https://helicone.ai) |
| **Langfuse** | — | 🟢 フリーミアム | — | — | [🔗](https://langfuse.com) |
| **RouteLLM** | — | 🏠 セルフホスト | — | — | [🔗](https://lmsys.org/blog/2024-07-01-routellm) |
| **Arize Phoenix** | — | 🏠 セルフホスト | — | — | [🔗](https://docs.arize.com/phoenix) |

## 🎨 特殊API

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **ElevenLabs** | US | 🟢 フリーミアム | — | 10K 文字/月 無料 | [🔗](https://elevenlabs.io) |
| **PlayHT** | — | 🟢 フリーミアム | — | 12.5K 文字/月 無料 | [🔗](https://play.ht) |
| **Cartesia (Sonic)** | — | 🟢 フリーミアム | — | 10K 文字/月 無料 | [🔗](https://cartesia.ai) |
| **Resemble AI** | — | 🎁 トライアル | — | — | [🔗](https://resemble.ai) |
| **Coqui XTTS** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/coqui-ai/TTS) |
| **Kokoro TTS** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/hexgrad/kokoro) |
| **Deepgram** | — | 🎁 $200 トライアル | — | — | [🔗](https://deepgram.com) |
| **AssemblyAI** | — | 🎁 $50 トライアル | — | — | [🔗](https://assemblyai.com) |
| **Whisper** | — | 🏠 セルフホスト | — | — | [🔗](https://openai.com/research/whisper) |
| **faster-whisper** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/SYSTRAN/faster-whisper) |
| **Voyage AI** | — | 🟢 フリーミアム | — | 50M トークン 無料 | [🔗](https://voyageai.com) |
| **Jina AI** | — | 🟢 フリーミアム | — | 1M トークン 無料 | [🔗](https://jina.ai) |
| **Mixedbread** | DE | 🟢 フリーミアム | — | — | [🔗](https://mixedbread.ai) |
| **Nomic Atlas** | — | 🟢 フリーミアム | — | — | [🔗](https://atlas.nomic.ai) |
| **fal.ai** | — | 🎁 トライアル | — | — | [🔗](https://fal.ai) |
| **Pollinations** | — | 🟢 無料 | — | — | [🔗](https://pollinations.ai) |
| **Replicate** | — | 🎁 $0.5 トライアル | — | — | [🔗](https://replicate.com) |
| **ComfyUI** | — | 🏠 セルフホスト | — | — | [🔗](https://www.comfy.org) |
| **AUTOMATIC1111 WebUI** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/AUTOMATIC1111/stable-diffusion-webui) |
| **Runway** | — | 💳 $15/月 | — | — | [🔗](https://runwayml.com) |
| **Kling** | CN | 🟢 フリーミアム | — | — | [🔗](https://kling.ai) |
| **Black Forest Labs (FLUX)** | DE | 🎁 トライアル | — | — | [🔗](https://bfl.ai) |

## 🤖 エージェントフレームワーク

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **CrewAI** | — | 🏠 セルフホスト | — | — | [🔗](https://crewai.com) |
| **AutoGen** | — | 🏠 セルフホスト | — | — | [🔗](https://microsoft.github.io/autogen) |
| **LangGraph** | — | 🏠 セルフホスト | — | — | [🔗](https://langchain-ai.github.io/langgraph) |
| **Pydantic AI** | — | 🏠 セルフホスト | — | — | [🔗](https://ai.pydantic.dev) |
| **Mastra** | — | 🏠 セルフホスト | — | — | [🔗](https://mastra.ai) |

## 📚 LLMフレームワーク

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **LangChain** | — | 🏠 セルフホスト | — | — | [🔗](https://langchain.com) |
| **LlamaIndex** | — | 🏠 セルフホスト | — | — | [🔗](https://llamaindex.ai) |
| **Haystack** | — | 🏠 セルフホスト | — | — | [🔗](https://haystack.deepset.ai) |
| **DSPy** | — | 🏠 セルフホスト | — | — | [🔗](https://dspy.ai) |
| **Semantic Kernel** | — | 🏠 セルフホスト | — | — | [🔗](https://learn.microsoft.com/semantic-kernel) |
| **Vercel AI SDK** | — | 🟢 無料 | — | — | [🔗](https://sdk.vercel.ai) |

## 🗄️ ベクトルデータベース

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **Qdrant** | — | 🟢 フリーミアム | — | 1GB 無料クラウド | [🔗](https://qdrant.tech) |
| **Weaviate** | — | 🟢 フリーミアム | — | — | [🔗](https://weaviate.io) |
| **Milvus** | — | 🏠 セルフホスト | — | — | [🔗](https://milvus.io) |
| **Chroma** | — | 🏠 セルフホスト | — | — | [🔗](https://trychroma.com) |
| **pgvector** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/pgvector/pgvector) |
| **Pinecone** | — | 🟢 フリーミアム | — | 1 無料インデックス | [🔗](https://pinecone.io) |
| **LanceDB** | — | 🏠 セルフホスト | — | — | [🔗](https://lancedb.com) |
| **Vespa** | — | 🏠 セルフホスト | — | — | [🔗](https://vespa.ai) |

## 📊 評価フレームワーク

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **Promptfoo** | — | 🏠 セルフホスト | — | — | [🔗](https://promptfoo.dev) |
| **DeepEval** | — | 🏠 セルフホスト | — | — | [🔗](https://deepeval.com) |
| **Ragas** | — | 🏠 セルフホスト | — | — | [🔗](https://ragas.io) |
| **OpenAI Evals** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/openai/evals) |

## 📦 モデルカタログ

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **HuggingFace Hub** | — | 🟢 フリーミアム | — | — | [🔗](https://huggingface.co) |
| **ModelScope (Alibaba)** | CN | 🟢 フリーミアム | — | — | [🔗](https://modelscope.cn) |
| **models.dev** | — | 🟢 無料 | — | — | [🔗](https://models.dev) |
| **Civitai** | — | 🟢 フリーミアム | — | — | [🔗](https://civitai.com) |

## 💻 コーディングツール

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **Aider** | — | 🏠 セルフホスト | — | — | [🔗](https://aider.chat) |
| **Cline** | — | 🏠 セルフホスト | — | — | [🔗](https://cline.bot) |
| **OpenHands** | — | 🏠 セルフホスト | — | — | [🔗](https://www.all-hands.dev) |
| **Continue.dev** | — | 🏠 セルフホスト | — | — | [🔗](https://continue.dev) |
| **Codex CLI** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/openai/codex) |

## 🖥️ デスクトップUI

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
|------|:-:|:-:|:-:|------|:-:|
| **Open WebUI** | — | 🏠 セルフホスト | — | — | [🔗](https://openwebui.com) |
| **Text Generation WebUI** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/oobabooga/text-generation-webui) |
| **Jan** | — | 🏠 セルフホスト | — | — | [🔗](https://jan.ai) |
| **GPT4All** | — | 🏠 セルフホスト | — | — | [🔗](https://gpt4all.io) |
| **LM Studio** | — | 🟢 無料 | — | — | [🔗](https://lmstudio.ai) |
| **KoboldCpp** | — | 🏠 セルフホスト | — | — | [🔗](https://github.com/LostRuins/koboldcpp) |

## 🧬 オープンウェイトモデルファミリー

| 名前 | 国 | 料金 | レート制限 | モデル / 備考 | リンク |
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

## 🔍 自動検出されたモデル

> scripts/discover_models.py が公開されている `/v1/models` エンドポイントをプローブして自動生成されました。**9つのプロバイダー**が公開応答し、合計**1157のモデル**があります。

### 🟢 公開エンドポイント (認証不要)

| プロバイダー | モデル数 | エンドポイント |
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
<summary>🔒 <strong>15のプロバイダーは認証が必要です</strong> (エンドポイントは有効ですが、キーが必要です)</summary>

| プロバイダー | ステータス |
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
<summary>⚠️ <strong>3つのエンドポイントでエラーが発生しました</strong> (TODO: 調査)</summary>

| プロバイダー | ステータス |
|----------|--------|
| `ollama-cloud` | not_found_404 |
| `opencode-zen` | not_found_404 |
| `perplexity-api` | not_found_404 |

</details>


---

## 🤝 貢献

`data/0X-*.yaml` を編集し、`./scripts/merge.sh && python scripts/render_readme.py` を実行して、PRをオープンしてください。

## 📜 ライセンス
MIT
