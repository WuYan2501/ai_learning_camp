# 🗺️ AI工程地图

> **定位**：一份持续更新的 AI 工程地图，覆盖基础认知、模型原理、RAG、Agent、MCP、Harness Engineering、工程落地、实操技能与面试系统整理
>
> **适合谁**：想系统学 AI 的初学者、想转型 AI 的程序员 / 产品 / 运营，以及希望把 AI 变成效率和收入的人
>
> **你能在这里得到什么**：不是零散资料，而是一条从“看懂 AI”到“真正用上 AI”的路线图
>
> **使用方式**：本页只做总导航，详细内容在 `modules/` 目录；如果你是从知乎来的，建议先看下方「快速开始」和「热门主题入口」
>
> **更新时间**：2026-04

---

## 🚀 快速开始

### 如果你是第一次来

- **想先建立 AI 整体框架**：从 [01_foundations.md](./modules/01_foundations.md) → [02_models.md](./modules/02_models.md) → [03_applications.md](./modules/03_applications.md) 开始
- **想直接看热门方向**：先看 [02_rag.md](./modules/03_applications/02_rag.md)、[03_agent_core.md](./modules/03_applications/03_agent_core.md)、[08_mcp.md](./modules/03_applications/08_mcp.md)、[04_engineering.md](./modules/04_engineering.md)
- **想补工程落地能力**：先看 [04_engineering.md](./modules/04_engineering.md) 和 [09_skills.md](./modules/09_skills.md)，重点关注 Harness Engineering、评测和调试方法论
- **想准备面试 / 查漏补缺**：直接看 [06_interview.md](./modules/06_interview.md)；如果想按公司 / 时间维度刷公开面经，再看 [02_tier1_companies.md](./modules/06_interview/02_tier1_companies.md) 和 [05_by_time.md](./modules/06_interview/05_by_time.md)

## 🎯 这份地图解决什么问题

- **内容太碎**：把热点、原理、实操和工程串成一条完整路径
- **只懂概念不会落地**：从 RAG / Agent / MCP 一直延伸到部署、评估、成本和可靠性
- **收藏很多却不知道先看什么**：每个模块都按主题归档，可以按目标快速跳转

## 🔥 热门主题入口

- **RAG**：[02_rag.md](./modules/03_applications/02_rag.md)
- **Agent 核心**：[03_agent_core.md](./modules/03_applications/03_agent_core.md)
- **Agent 应用**：[04_agent_applications.md](./modules/03_applications/04_agent_applications.md)
- **MCP**：[08_mcp.md](./modules/03_applications/08_mcp.md)
- **Harness Engineering / 工程落地**：[04_engineering.md](./modules/04_engineering.md)
- **公开面经分类整理**：[06_interview.md](./modules/06_interview.md)
- **AI 实操技能 / Skills**：[09_skills.md](./modules/09_skills.md)
- **高频面试**：[06_interview.md](./modules/06_interview.md)

## 📖 标记体系

| 标记 | 含义 |
|------|------|
| 🔥 | 面试高频 / 行业热点 |
| 🔥🔥 | 必须掌握 |
| 🔥🔥🔥 | 当前最热焦点 |
| ⭐ | 优先写文章（理解难点 + 面试高频）|
| 📝 | 已写文章 |

---

## 🗺️ 知识全景图

```
                              ┌─────────────────────────────────────┐
                              │           AI 系统知识库              │
                              └──────────────┬──────────────────────┘
    ┌──────────┬──────────┬─────────┬───┴───┬──────────┬──────────┬──────────┬──────────┐
    ▼          ▼          ▼         ▼       ▼          ▼          ▼          ▼          ▼
① 基础层   ② 模型层   ③ 应用层  ④ 工程层 ⑤ 前沿层  ⑥ 面试区  ⑦ 工具链  ⑧ 论文库  ⑨ 实操技能
数学/ML/DL  架构/训练  三板斧    部署/优化 最新突破  高频考点  生态速查  核心论文  实战技能
            效率/对齐   Agent/MCP                                                    调试/选型
```

---

## 📂 模块导航

| 模块 | 文件 | 核心内容 | 知识点数 |
|------|------|----------|----------|
| ① 基础层 | [01_foundations.md](./modules/01_foundations.md) | 数学 → ML → DL → 归一化 → 训练技巧 | ~30 |
| ② 模型层 | [02_models.md](./modules/02_models.md) | Transformer → 效率优化 → Tokenizer/Embedding → 预训练 → 对齐微调 → 模型选型 | ~60（含6个子文件） |
| ③ 应用层 | [03_applications.md](./modules/03_applications.md) | Prompt → RAG → **Agent(5个子模块)** → MCP → 多模态 | ~155（含9个子文件） |
| ④ 工程层 | [04_engineering.md](./modules/04_engineering.md) | 量化 → 推理优化 → 框架选型 → 服务化 → 评估 → Harness Engineering | ~45 |
| ⑤ 前沿层 | [05_frontier.md](./modules/05_frontier.md) | 推理模型 → Agent落地 → 新架构 → AI安全 | ~20 |
| ⑥ 面试区 | [06_interview.md](./modules/06_interview.md) | 高频题库总表 + 一线大厂 / 二线垂类 / 外企 / 时间维度公开面经分类整理 | ~205（题库） + 分类页持续更新 |
| ⑦ 工具链 | [07_tools.md](./modules/07_tools.md) | 开发框架 / 训练微调 / 推理部署 / 向量DB / 评估监控 | ~30 |
| ⑧ 论文库 | [08_papers.md](./modules/08_papers.md) | 基础架构 / 训练 / 对齐 / 应用 / 新架构 关键论文 | ~25 |
| ⑨ 实操技能 | [09_skills.md](./modules/09_skills.md) | 数据处理 → Prompt实战 → 模型选型 → RAG实战 → Agent开发 → Harness实战 → 微调 → 调试 → 项目方法论 | ~95 |

---

## 📋 各模块知识点速览

### ① 基础层
`线性代数` `概率统计` `信息论` `最优化` → `监督/无监督` `损失函数` `优化器` → `CNN/RNN/Transformer` `归一化` `训练技巧`

### ② 模型层
`Self-Attention` `GQA` `RoPE` `Flash Attention` `MoE` → `Tokenizer` `Embedding` `CLM` `Scaling` → `SFT` `LoRA` `DPO` `GRPO`

### ③ 应用层
`CoT/ToT/ReAct` `DSPy` → `RAG Pipeline` `Chunking` `Reranking` `GraphRAG` → `Agent架构` `规划范式` `记忆系统` `Function Calling` `多Agent` `Agent应用(Coding/Research/客服)` `Agent面试40题` `Agent前沿` **`Agent Skills(Voyager/Skill Library/Skill Discovery)`** `Agent学习大纲` → `MCP协议` `A2A` → `VLM` `Diffusion`

### ④ 工程层
`量化(GPTQ/AWQ/GGUF)` `蒸馏` `剪枝` → `KV Cache` `PagedAttention` `Speculative Decoding` → `vLLM/SGLang` `容器化` `监控` → `Harness Engineering` `回放/Regression` `沙箱执行` `评测编排`

### ⑤ 前沿层
`推理模型(o3/R1)` `GRPO` `Test-time Scaling` → `Coding Agent` `MCP/A2A` → `Mamba/SSM` `MoE演进` `BitNet`

### ⑨ 实操技能
`数据清洗/去重` `SFT数据构造` `合成数据` → `Prompt调试方法论` `System Prompt设计` `结构化输出` → `模型选型决策` `成本优化` → `RAG文档处理` `分块/检索/Reranker` → `Agent工具设计` `可靠性工程` → `Harness搭建` `回归集` `Replay/Trace` `LLM-as-Judge` → `LoRA微调实战` → `分层调试法` `可观测性` → `项目全流程` `数据飞轮`

---

## 📝 已写文章追踪

| 文章标题 | 对应知识点 | 模块 |
|----------|-----------|------|
| 《Transformer为何选择LayerNorm？》 | LayerNorm vs BatchNorm（#10） | ①基础层 / ⑥面试区 |
| 《一文搞懂 Harness Engineering，入门就能跑起来》 | Harness Engineering / 最小可用 Harness / 回归测试入门 | ④工程层 |

---

## 🌱 如果你是从知乎来的

很多朋友会私信我要资料，所以我把平时学习和整理 AI 的过程，尽量做成一张公开、持续更新、便于查找的知识地图。

你可以把这里当成一个长期资料入口：

- **想系统学**：按模块顺序往下看
- **想看热门方向**：直接进入 RAG / Agent / MCP / 工程落地
- **想面试复习**：直接看面试区
- **想做实操**：优先看实操技能与工程模块

如果这份地图对你有帮助，也欢迎把它转给同样在学 AI、做 AI、或者想靠 AI 提效的朋友。

## 💡 这份地图后续会持续补什么

我会围绕下面几个方向持续补内容：

- **热点拆解**：一个项目为什么火，它真正重要的点是什么
- **原理白话**：把复杂概念讲成人能听懂的话
- **工程落地**：部署、成本、稳定性、评估和安全
- **实操教程**：从入门到上手的步骤、清单和避坑记录
- **变现思路**：AI 如何真正变成效率、能力，甚至收入来源

---

## 🔄 维护说明

- 优先攻克 ⭐ 标记的知识点（面试高频 + 理解难点）
- 持续更新，保持与前沿同步（每周至少更新一次）