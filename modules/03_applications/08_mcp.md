# 3.8 MCP 协议（Model Context Protocol）🔥🔥

> AI 的 USB-C 接口，标准化 AI 应用与工具/数据源的集成方式
>
> 返回 [应用层索引](../03_applications.md) | [知识库索引](../../SYLLABUS.md)

---

## MCP 是什么 ⭐

- *核心思想*：标准化 AI 应用与工具/数据源的集成方式
- *解决的问题*：每个 AI 应用都要单独集成每个工具，M×N 问题 → 标准协议后变成 M+N
- *类比*：LSP（Language Server Protocol）统一了编辑器和语言服务器的集成

---

## 协议架构

- **Client**：AI 应用（Claude Desktop / Cursor / 自定义应用）
- **Server**：工具提供方（文件系统 / 数据库 / API 服务）
- **Transport**：通信方式（stdio 本地进程 / SSE 远程服务 / HTTP Streamable）

---

## 核心概念

- **Tools**：模型可以调用的函数（类似 Function Calling）
- **Resources**：模型可以读取的数据（文件/数据库记录）
- **Prompts**：预定义的 Prompt 模板
- **Sampling**：Server 可以请求 Client 做 LLM 推理（反向调用）
- **Roots**：Client 告知 Server 可访问的根目录范围

---

## 与 Function Calling 的区别 ⭐

| 维度 | Function Calling | MCP |
|------|-----------------|-----|
| 耦合度 | 工具定义在应用代码里，紧耦合 | 工具定义在独立 Server 里，松耦合 |
| 复用性 | 每个应用单独集成 | 跨应用共享，一次开发到处使用 |
| 发现机制 | 无，需手动传入 | Server 自动声明能力 |
| 生态 | 应用各自维护 | 社区共建 MCP Server 生态 |

---

## A2A 协议（Agent-to-Agent）🔥

- *核心思想*：Google 提出，标准化 Agent 之间的通信协议
- *vs MCP*：MCP 是 AI 连接工具（垂直），A2A 是 AI 连接 AI（水平）
- *关键概念*：Agent Card / Task / Message Parts
- *应用场景*：企业内多个独立 Agent 协作

---

> 💡 **面试拷问 — MCP**
> - MCP 和 Function Calling 的本质区别是什么？为什么需要这个协议？⭐
> - MCP 的 Transport 层有哪几种？stdio 和 SSE 分别适合什么场景？
> - A2A 和 MCP 的关系是什么？能否同时使用？⭐
> - MCP 的 Sampling 机制（Server 请求 Client 推理）有什么应用场景？
> - 如何设计一个好的 MCP Server？Tool 描述有什么最佳实践？⭐
