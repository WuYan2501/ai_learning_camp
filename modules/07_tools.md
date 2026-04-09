# ⑦ 工具生态速查

> 快速查找工具，不用每次都去搜
>
> 返回 [知识库索引](/SYLLABUS)

---

## 开发框架

| 工具 | 核心定位 | 热度 |
|------|----------|------|
| LangChain / LangGraph | Agent/RAG 开发，LangGraph = 图状态机 | 🔥🔥 |
| LlamaIndex | 数据索引 + RAG，数据中心型 | 🔥 |
| Hugging Face Transformers | 模型加载/微调/推理，生态最全 | 🔥🔥🔥 |
| DSPy | Prompt 自动优化，声明式编程 | 🔥 |
| CrewAI | 多 Agent 角色协作 | 🔥 |
| AutoGen / AG2 | 对话式多 Agent | 🔥 |
| Dify | 低代码 AI 平台，可视化编排 | 🔥🔥 |
| n8n | 工作流自动化，AI + 传统工具 | 🔥 |

---

## 训练/微调

| 工具 | 核心定位 | 热度 |
|------|----------|------|
| Hugging Face TRL | SFT/RLHF/DPO/GRPO 训练库 | 🔥🔥 |
| Unsloth | 高效微调，2x 速度，节省 60% 显存 | 🔥🔥 |
| LLaMA-Factory | 一站式微调，WebUI，支持多种格式 | 🔥🔥 |
| Axolotl | 微调配置框架，灵活 | 🔥 |
| DeepSpeed | 分布式训练，ZeRO 优化 | 🔥🔥 |
| PEFT | 参数高效微调库（LoRA/Adapter 等）| 🔥🔥 |
| torchtune | PyTorch 官方微调库 | 🔥 |

---

## 推理/部署

| 工具 | 核心定位 | 热度 |
|------|----------|------|
| vLLM | 高性能推理，PagedAttention，生产首选 | 🔥🔥🔥 |
| SGLang | RadixAttention，结构化生成 | 🔥🔥 |
| Ollama | 本地模型一键运行，用户友好 | 🔥🔥 |
| llama.cpp | CPU/端侧推理，GGUF 格式 | 🔥🔥 |
| LiteLLM | 多模型统一 API 代理，100+ 模型 | 🔥 |
| TensorRT-LLM | NVIDIA GPU 极致优化 | 🔥 |

---

## 向量数据库

| 工具 | 核心特点 | 热度 |
|------|----------|------|
| Chroma | 轻量，本地开发首选，Python 原生 | 🔥🔥 |
| Qdrant | 高性能，Rust 实现，过滤能力强 | 🔥🔥 |
| Milvus | 企业级，云原生，大规模 | 🔥🔥 |
| FAISS | Meta 出品，本地高效，研究常用 | 🔥🔥 |
| Weaviate | 混合检索，GraphQL 接口 | 🔥 |
| Pinecone | 全托管，易用，贵 | 🔥 |
| PGVector | PostgreSQL 扩展，已有 PG 的首选 | 🔥 |

---

## 评估/监控

| 工具 | 核心定位 | 热度 |
|------|----------|------|
| LangFuse | LLM 可观测性，链路追踪，开源 | 🔥🔥 |
| RAGAS | RAG 评估框架，四个核心指标 | 🔥 |
| lm-eval-harness | 模型 Benchmark 标准工具 | 🔥 |
| OpenCompass | 国内评估平台，中文友好 | 🔥 |
| Chatbot Arena | 人类偏好 ELO 排名，最真实 | 🔥🔥 |
