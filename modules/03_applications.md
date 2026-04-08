# ③ 应用层：Prompt / RAG / Agent / MCP / 多模态

> 大模型落地的三板斧：Prompt + RAG + Agent，再加上 MCP 协议和多模态
>
> 返回 [知识库索引](../SYLLABUS.md)

---

## 📂 应用层模块导航

> 应用层内容丰富，已拆分为子目录 `03_applications/` 管理，本文件作为索引导航

| # | 模块 | 文件 | 核心内容 | 知识点数 |
|---|------|------|----------|----------|
| 3.1 | Prompt Engineering | [01_prompt_engineering.md](./03_applications/01_prompt_engineering.md) | 基础技巧 → 高级推理 → 自动化 Prompt → 安全 | ~15 |
| 3.2 | RAG | [02_rag.md](./03_applications/02_rag.md) | Pipeline → Chunking → Embedding → 高级RAG → 评估 | ~25 |
| 3.3 | **Agent 核心架构** 🔥🔥🔥 | [03_agent_core.md](./03_applications/03_agent_core.md) | 规划范式 → 工具调用 → 记忆系统 → 多Agent → 可靠性 | ~40 |
| 3.4 | **Agent 应用场景** 🔥🔥🔥 | [04_agent_applications.md](./03_applications/04_agent_applications.md) | Coding Agent → Computer Use → Deep Research → 客服 → 数据分析 | ~30 |
| 3.5 | **Agent 面试专题** 🔥🔥🔥 | [05_agent_interview.md](./03_applications/05_agent_interview.md) | 40道Agent面试题：原理/工具/记忆/工程/多Agent/架构/前沿 | 40题 |
| 3.6 | **Agent 前沿动态** 🔥🔥🔥 | [06_agent_frontier.md](./03_applications/06_agent_frontier.md) | MCP生态 → A2A → Coding Agent革命 → 评估体系 → 安全 | ~20 |
| 3.7 | **Agent 学习大纲** 🔥🔥🔥 | [07_agent_syllabus.md](./03_applications/07_agent_syllabus.md) | 6阶段学习路线 → 推荐资源 → 论文 → 课程 → 开源项目 | 路线图 |
| 3.8 | MCP 协议 | [08_mcp.md](./03_applications/08_mcp.md) | 协议架构 → 核心概念 → vs FC → A2A | ~10 |
| 3.9 | 多模态 | [09_multimodal.md](./03_applications/09_multimodal.md) | VLM → 图像生成 → 视频生成 → 音频 | ~15 |

---

## 🗺️ 应用层知识全景图

```
                              ┌──────────────────┐
                              │    ③ 应用层       │
                              └────────┬─────────┘
         ┌──────────┬──────────┬───────┴───────┬──────────┐
         ▼          ▼          ▼               ▼          ▼
    Prompt Eng   RAG 🔥🔥    Agent 🔥🔥🔥     MCP 🔥🔥   多模态
    CoT/ReAct    Pipeline    ┌─────────────┐  协议架构   VLM
    DSPy         Chunking    │ Agent 子模块 │  vs FC     Diffusion
    安全          Reranking   │             │  A2A       DiT
                 GraphRAG    │ 核心架构     │            视频/音频
                 Agentic     │ 应用场景     │
                             │ 面试专题     │
                             │ 前沿动态     │
                             │ 学习大纲     │
                             └─────────────┘
```

---

## 📊 知识点统计

| 方向 | 知识点数 | 面试题数 | 重要度 |
|------|----------|----------|--------|
| Prompt Engineering | ~15 | 7 | 🔥 |
| RAG | ~25 | 14 | 🔥🔥 |
| **AI Agent（合计）** | **~90** | **40** | **🔥🔥🔥** |
| MCP 协议 | ~10 | 5 | 🔥🔥 |
| 多模态 | ~15 | 6 | 🔥 |
| **总计** | **~155** | **72** | |

---

## 🎯 学习优先级建议

1. **最优先**：Agent 核心架构 + Agent 应用场景（当前面试最热 + 行业落地重点）
2. **必学**：RAG（落地最广泛）+ MCP 协议（新标准，快速普及）
3. **重要**：Prompt Engineering（基本功）+ Agent 面试专题（面试冲刺）
4. **进阶**：Agent 前沿动态（加分项）+ 多模态（了解即可）
5. **持续**：Agent 学习大纲（系统化学习路径）
