# 🧠 AI 系统知识库（Knowledge Base）

> **定位**：系统性 AI 知识图谱索引，每个知识点带结构化注释，支持快速理解和文章扩展
>
> **原则**：紧跟前沿 × 覆盖基础 × 面试高频 × 知识点带注释不展开
>
> **使用方式**：SYLLABUS.md 只做导航，详细内容在 `modules/` 目录下各模块文件中
>
> **更新时间**：2026-03

---

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
            大模型家族  Agent/MCP                                                    调试/选型
```

---

## 📂 模块导航

| 模块 | 文件 | 核心内容 | 知识点数 |
|------|------|----------|----------|
| ① 基础层 | [01_foundations.md](./modules/01_foundations.md) | 数学 → ML → DL → 归一化 → 训练技巧 | ~30 |
| ② 模型层 | [02_models.md](./modules/02_models.md) | Transformer → 注意力变体 → 大模型家族 → Tokenizer → 预训练 → 对齐微调 | ~60 |
| ③ 应用层 | [03_applications.md](./modules/03_applications.md) | Prompt → RAG → **Agent(5个子模块)** → MCP → 多模态 | ~155（含9个子文件） |
| ④ 工程层 | [04_engineering.md](./modules/04_engineering.md) | 量化 → 推理优化 → 框架选型 → 服务化 → 评估 | ~30 |
| ⑤ 前沿层 | [05_frontier.md](./modules/05_frontier.md) | 推理模型 → Agent落地 → 新架构 → AI安全 | ~20 |
| ⑥ 面试区 | [06_interview.md](./modules/06_interview.md) | Transformer/ML·DL/Tokenizer/训练/RAG/Agent/部署/评估安全/场景设计/前沿 | ~205 |
| ⑦ 工具链 | [07_tools.md](./modules/07_tools.md) | 开发框架 / 训练微调 / 推理部署 / 向量DB / 评估监控 | ~30 |
| ⑧ 论文库 | [08_papers.md](./modules/08_papers.md) | 基础架构 / 训练 / 对齐 / 应用 / 新架构 关键论文 | ~25 |
| ⑨ 实操技能 | [09_skills.md](./modules/09_skills.md) | 数据处理 → Prompt实战 → 模型选型 → RAG实战 → Agent开发 → 微调 → 调试 → 项目方法论 | ~80 |

---

## 📋 各模块知识点速览

### ① 基础层
`线性代数` `概率统计` `信息论` `最优化` → `监督/无监督` `损失函数` `优化器` → `CNN/RNN/Transformer` `归一化` `训练技巧`

### ② 模型层
`Self-Attention` `MHA→MQA→GQA→MLA` `RoPE` `Flash Attention` `MoE` → `Tokenizer` `Embedding` `预训练` → `SFT` `RLHF` `DPO` `GRPO`

### ③ 应用层
`CoT/ToT/ReAct` `DSPy` → `RAG Pipeline` `Chunking` `Reranking` `GraphRAG` → `Agent架构` `规划范式` `记忆系统` `Function Calling` `多Agent` `Agent应用(Coding/Research/客服)` `Agent面试40题` `Agent前沿` **`Agent Skills(Voyager/Skill Library/Skill Discovery)`** `Agent学习大纲` → `MCP协议` `A2A` → `VLM` `Diffusion`

### ④ 工程层
`量化(GPTQ/AWQ/GGUF)` `蒸馏` `剪枝` → `KV Cache` `PagedAttention` `Speculative Decoding` → `vLLM/SGLang` `容器化` `监控`

### ⑤ 前沿层
`推理模型(o3/R1)` `GRPO` `Test-time Scaling` → `Coding Agent` `MCP/A2A` → `Mamba/SSM` `MoE演进` `BitNet`

### ⑨ 实操技能
`数据清洗/去重` `SFT数据构造` `合成数据` → `Prompt调试方法论` `System Prompt设计` `结构化输出` → `模型选型决策` `成本优化` → `RAG文档处理` `分块/检索/Reranker` → `Agent工具设计` `可靠性工程` → `LoRA微调实战` → `分层调试法` `可观测性` → `项目全流程` `数据飞轮`

---

## 📝 已写文章追踪

| 文章标题 | 对应知识点 | 模块 |
|----------|-----------|------|
| 《Transformer为何选择LayerNorm？》 | LayerNorm vs BatchNorm（#10） | ①基础层 / ⑥面试区 |

---

## 🔄 维护说明

- **SYLLABUS.md** 只做索引导航，不放具体知识点内容
- **modules/** 下各文件独立维护，每个知识点带 `核心思想/为什么重要/核心问题/延伸` 注释
- 写完文章后：① 在对应模块文件的知识点后加 `📝`；② 在上方「已写文章追踪」表中添加记录；③ 面试题表格中更新状态
- 优先攻克 ⭐ 标记的知识点（面试高频 + 理解难点）
- 持续更新，保持与前沿同步（每月至少更新一次）
