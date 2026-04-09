# 3.1 Prompt Engineering 🔥

> Prompt 是与大模型交互的第一入口，也是最低成本的优化手段
>
> 返回 [应用层索引](/modules/03_applications) | [知识库索引](/SYLLABUS)

---

## 基础技巧

- **Zero-shot / Few-shot / One-shot**
  - *核心思想*：通过示例数量控制模型的上下文学习（In-Context Learning）
  - *核心问题*：Few-shot 示例的质量和顺序对结果影响有多大？（顺序很重要，最后的示例影响最大）

- **System Prompt 设计**
  - *核心思想*：定义模型角色、约束行为、设定输出格式
  - *最佳实践*：角色定义 + 任务说明 + 约束条件 + 输出格式，四段式结构

- **输出格式控制**
  - JSON Mode / Structured Output（OpenAI）/ XML Tags（Anthropic）
  - *核心问题*：Structured Output 和 JSON Mode 的区别？（Structured Output 用 grammar 约束解码，100% 保证格式）

---

## 高级推理策略

- **Chain of Thought（CoT）** 🔥 ⭐
  - *核心思想*：让模型先输出推理过程再给答案，"Let's think step by step"
  - *为什么有效*：将复杂问题分解为多步，每步都在模型能力范围内
  - *核心问题*：CoT 为什么能提升推理能力？（中间步骤提供了额外的计算 token）
  - *延伸*：Zero-shot CoT vs Few-shot CoT；Long CoT（推理模型的核心）

- **Self-Consistency（自洽性）** ⭐
  - *核心思想*：对同一问题采样多条推理路径，投票选最一致的答案
  - *为什么有效*：单次 CoT 可能走错路，多路径投票降低随机性
  - *成本*：推理成本 × N，适合高精度要求场景

- **Tree of Thought（ToT）**
  - *核心思想*：将推理过程建模为树，支持回溯和剪枝
  - *适用场景*：需要探索多种可能性的规划问题

- **ReAct（Reasoning + Acting）** 🔥 ⭐
  - *核心思想*：交替输出推理（Thought）和行动（Action），行动结果作为新的观察
  - *为什么重要*：Agent 的基础范式，将推理和工具调用统一
  - *核心问题*：ReAct 和纯 CoT 的区别？（ReAct 可以与外部环境交互）

- **Step-Back Prompting**
  - *核心思想*：先问一个更抽象的问题，再用抽象答案指导具体问题的解答
  - *适用场景*：需要先建立原则再解决具体问题

---

## 自动化 Prompt

- **DSPy** 🔥
  - *核心思想*：声明式 Prompt 框架，将 Prompt 优化变成编程问题
  - *为什么重要*：告别手工调 Prompt，用优化算法自动找最优 Prompt
  - *核心问题*：DSPy 的 Teleprompter 是什么？（自动优化 Prompt 的算法模块）

- **TextGrad**
  - *核心思想*：用文本梯度（LLM 生成的改进建议）替代数值梯度，优化 Prompt
  - *类比*：反向传播的文本版本

---

## Prompt 安全

- **Prompt 注入攻击** ⭐
  - *核心思想*：攻击者通过输入内容覆盖系统 Prompt，劫持模型行为
  - *类型*：直接注入（用户输入）/ 间接注入（通过检索内容注入）
  - *防御*：输入过滤 / 输出检测 / 沙箱隔离 / 特权分离（系统Prompt和用户输入分开处理）

---

> 💡 **面试拷问 — Prompt Engineering**
> - CoT 和推理模型（o3/R1）的思维链有什么本质区别？⭐
> - Few-shot 的示例放在前面和后面效果不同，这背后的原理是什么？（Recency Bias）⭐
> - In-Context Learning 的本质是什么？是"学习"还是"检索"？⭐
> - Self-Consistency 和 Best-of-N Sampling 有什么区别？⭐
> - DSPy 和手工调 Prompt 相比，什么场景下 DSPy 才特别有价值？
> - Prompt 注入和越狱攻击的区别是什么？间接注入为什么更危险？⭐
> - 如何让 LLM 100% 输出合法 JSON？Structured Output 和 JSON Mode 的原理分别是什么？⭐
