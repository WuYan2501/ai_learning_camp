# 3.7 AI Agent 学习大纲 🔥🔥🔥

> 系统学习 AI Agent 的路线图，从入门到实战到前沿
>
> 返回 [应用层索引](../03_applications.md) | [Agent 核心架构](03_agent_core.md) | [知识库索引](../../SYLLABUS.md)

---

## 📋 学习路线总览

```
阶段一：基础概念（1-2 周）
  └→ LLM 基础 → Prompt Engineering → Function Calling → Agent 概念

阶段二：核心原理（2-3 周）
  └→ ReAct → Plan-and-Execute → 记忆系统 → 工具调用深入 → 多 Agent

阶段三：框架实战（2-3 周）
  └→ LangChain → LangGraph → CrewAI → MCP 开发

阶段四：Agent 应用开发（3-4 周）
  └→ RAG Agent → Coding Agent → Research Agent → 自定义 Agent

阶段五：工程化与优化（2-3 周）
  └→ 可观测性 → 错误处理 → 成本优化 → 安全防护 → 评估

阶段六：前沿跟踪（持续）
  └→ 新论文 → 新框架 → 新产品 → 行业趋势
```

---

## 阶段一：基础概念 🟢

### 1.1 LLM 基础回顾

- [ ] 理解 Transformer 架构（不需要手推公式，理解数据流即可）
- [ ] 理解 Token / Prompt / Completion 的概念
- [ ] 理解 Temperature / Top-p 等推理参数
- [ ] 会使用 OpenAI / Anthropic / 国产模型 API
- **推荐资源**：OpenAI 官方文档、Anthropic 官方文档

### 1.2 Prompt Engineering 基础

- [ ] Zero-shot / Few-shot / System Prompt 设计
- [ ] Chain of Thought（CoT）推理
- [ ] 输出格式控制（JSON Mode / Structured Output）
- [ ] ReAct Prompt 模式
- **推荐资源**：[Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)

### 1.3 Function Calling 入门

- [ ] 理解 Function Calling 的原理和流程
- [ ] 用 OpenAI API 实现一个简单的工具调用
- [ ] 理解 Tool Description 的设计最佳实践
- [ ] 实现并行工具调用
- **实战项目**：做一个天气查询 + 计算器的简单 Agent

---

## 阶段二：核心原理 🟡

### 2.1 Agent 规划范式

- [ ] 深入理解 ReAct（Thought-Action-Observation 循环）
- [ ] 理解 Plan-and-Execute（先规划后执行）
- [ ] 理解 Reflexion（自我反思和学习）
- [ ] 了解 LATS（树搜索规划）
- **推荐论文**：ReAct / Reflexion / LATS

### 2.2 记忆系统

- [ ] 短期记忆：上下文管理、摘要压缩
- [ ] 长期记忆：向量数据库存储和检索
- [ ] 工作记忆：Scratchpad 模式
- [ ] 记忆更新策略（显式/隐式/遗忘）
- **推荐资源**：LangChain Memory 文档

### 2.3 工具调用进阶

- [ ] 理解 MCP 协议的架构和核心概念
- [ ] Tool Selection 策略（静态/动态/RAG-based）
- [ ] 嵌套工具调用和工具链
- [ ] 错误处理和降级策略
- **实战项目**：开发一个 MCP Server

### 2.4 多 Agent 协作

- [ ] Leader-Worker / Debate / Pipeline 等协作模式
- [ ] Agent 间通信机制（共享状态 / 消息传递）
- [ ] 多 Agent 的调度和协调
- **推荐资源**：LangGraph Multi-Agent 教程

---

## 阶段三：框架实战 🟠

### 3.1 LangChain 基础

- [ ] Chain / Agent / Memory / Tool 四大概念
- [ ] LCEL（LangChain Expression Language）
- [ ] 自定义 Tool / Chain / Agent
- **实战项目**：用 LangChain 实现 RAG + Agent

### 3.2 LangGraph 深入 🔥

- [ ] 图（Graph）/ 节点（Node）/ 边（Edge）/ 状态（State）
- [ ] 条件路由和循环
- [ ] 子图（Subgraph）和嵌套
- [ ] Human-in-the-Loop 实现
- [ ] Checkpointing 和持久化
- **实战项目**：用 LangGraph 实现一个多步 Research Agent

### 3.3 MCP 开发 🔥

- [ ] MCP Server 开发（Python/TypeScript）
- [ ] Tools / Resources / Prompts 的定义
- [ ] Transport 层（stdio / SSE / HTTP）
- [ ] 与 Claude Desktop / Cursor 集成
- **实战项目**：开发一个数据库查询 MCP Server

### 3.4 其他框架了解

- [ ] CrewAI：快速搭建多 Agent 原型
- [ ] AutoGen/AG2：对话式多 Agent
- [ ] Swarm（OpenAI）：轻量 Agent 路由
- **对比实战**：同一个任务分别用 LangGraph / CrewAI 实现，对比体验

---

## 阶段四：Agent 应用开发 🔴

### 4.1 RAG Agent（Agentic RAG）

- [ ] 多步检索 + 动态查询改写
- [ ] Self-RAG / CRAG 自我评估
- [ ] 混合检索（向量 + BM25 + 知识图谱）
- **实战项目**：企业知识库问答系统

### 4.2 Coding Agent

- [ ] 代码索引和上下文管理
- [ ] 多文件协调编辑
- [ ] 自动测试和错误恢复
- **实战项目**：实现一个简单的 CLI Coding Agent

### 4.3 Research Agent

- [ ] 多轮搜索策略
- [ ] 信息提取和交叉验证
- [ ] 结构化报告生成
- **实战项目**：实现一个 Deep Research Agent

### 4.4 自定义 Agent

- [ ] 根据业务需求设计 Agent 架构
- [ ] 选择合适的规划范式
- [ ] 设计工具集和记忆策略
- **实战项目**：针对自己工作场景设计并实现一个 Agent

---

## 阶段五：工程化与优化 ⚫

### 5.1 可观测性

- [ ] Trace / Span / Metric 体系设计
- [ ] LangSmith / Langfuse / Phoenix 工具使用
- [ ] 关键指标监控（成功率/延迟/成本）

### 5.2 错误处理

- [ ] 错误分类和处理策略
- [ ] 重试 / 降级 / 重规划
- [ ] 超时和熔断机制

### 5.3 成本优化

- [ ] Token 预算管理
- [ ] 模型路由（大小模型混用）
- [ ] 缓存策略设计
- [ ] 工具调用优化

### 5.4 安全防护

- [ ] 权限最小化设计
- [ ] 沙箱执行环境
- [ ] Prompt 注入防护
- [ ] 操作审计和回溯

### 5.5 评估体系

- [ ] 端到端评估方案设计
- [ ] SWE-bench / GAIA 等 Benchmark 了解
- [ ] A/B 测试和持续评估

---

## 阶段六：前沿跟踪 🌟

### 持续关注方向

- [ ] 推理模型（o3/R1 系列）对 Agent 的提升
- [ ] MCP / A2A 生态演进
- [ ] **Agent Skills / Skill Library 技术演进**（Voyager / DEPS / JARVIS-1 后续）
- [ ] 新框架和新工具
- [ ] Agent 安全研究
- [ ] Agent 评估方法论

### 推荐信息源

| 来源 | 类型 | 推荐度 |
|------|------|--------|
| **Anthropic Blog** | 官方博客 | 🔥🔥🔥 |
| **OpenAI Blog** | 官方博客 | 🔥🔥🔥 |
| **LangChain Blog** | 框架动态 | 🔥🔥 |
| **Twitter/X AI 圈** | 实时动态 | 🔥🔥🔥 |
| **arXiv cs.AI** | 论文 | 🔥🔥 |
| **Hacker News** | 社区讨论 | 🔥🔥 |
| **GitHub Trending** | 新项目 | 🔥🔥 |

---

## 📚 推荐学习资源

### 必读论文

| 论文 | 主题 | 重要性 |
|------|------|--------|
| ReAct (2022) | 推理+行动统一范式 | 🔥🔥🔥 |
| Reflexion (2023) | 自我反思 Agent | 🔥🔥 |
| Toolformer (2023) | 模型自主学习使用工具 | 🔥🔥 |
| Voyager (2023) | 开放世界中自主学习的 Agent（**Skill Library 奠基之作**） | 🔥🔥🔥 |
| DEPS (2023) | Agent 规划时的自我解释与纠错 | 🔥🔥 |
| JARVIS-1 (2023) | 多模态记忆增强 Agent，技能序列执行 | 🔥🔥 |
| LATS (2023) | 语言 Agent 树搜索 | 🔥 |
| Agent Hospital (2024) | 医疗 Agent 协作 | 🔥 |
| SWE-agent (2024) | 代码修复 Agent | 🔥🔥 |
| MCP Spec (2024) | Model Context Protocol | 🔥🔥🔥 |

### 推荐课程 / 教程

| 资源 | 来源 | 推荐度 |
|------|------|--------|
| [LangGraph Academy](https://academy.langchain.com/) | LangChain | 🔥🔥🔥 |
| [Building with Claude](https://docs.anthropic.com/) | Anthropic | 🔥🔥🔥 |
| [AI Agent 实战](https://github.com/modelcontextprotocol) | MCP 官方 | 🔥🔥 |
| [DeepLearning.AI Agent 课程](https://www.deeplearning.ai/) | Andrew Ng | 🔥🔥 |
| [LangChain 文档](https://python.langchain.com/) | LangChain | 🔥🔥 |

### 推荐开源项目

| 项目 | 描述 | 学习价值 |
|------|------|----------|
| **LangGraph** | 图状态机 Agent 框架 | 学框架设计 |
| **OpenHands** | 开源 Coding Agent | 学完整 Agent 架构 |
| **SWE-agent** | 代码修复 Agent | 学评估方法 |
| **MCP Servers** | MCP Server 合集 | 学 MCP 开发 |
| **AutoGPT** | 早期全自主 Agent | 了解历史演进 |

---

## ⏱️ 预计学习时间

| 阶段 | 时间 | 说明 |
|------|------|------|
| 阶段一 | 1-2 周 | 基础薄弱者可延长 |
| 阶段二 | 2-3 周 | 核心原理，需要精读论文 |
| 阶段三 | 2-3 周 | 框架实战，多动手 |
| 阶段四 | 3-4 周 | 应用开发，做完整项目 |
| 阶段五 | 2-3 周 | 工程化，结合实际项目 |
| 阶段六 | 持续 | 每周 2-3 小时跟踪 |
| **总计** | **~3 个月核心 + 持续跟踪** | |

> **学习建议**：不要只看不做！每个阶段至少完成一个实战项目。Agent 领域变化极快，边学边做边追前沿。
