# ⑤ 前沿层：2025-2026 热点方向

> 紧跟最前沿，这些是面试加分项和行业趋势
>
> 返回 [知识库索引](../SYLLABUS.md)

---

## 5.1 推理模型（Reasoning Model）🔥🔥🔥

- **OpenAI o 系列**：o1 → o3 → o3-mini / o4-mini
  - *核心思想*：推理时用更多计算（更长思维链 + 更多采样）换取更高精度
  - *核心问题*：o1 和 GPT-4o 的本质区别？（o1 在生成答案前有大量隐藏的思考过程）

- **DeepSeek-R1** 🔥🔥 ⭐
  - *核心思想*：用 GRPO 训练，让模型自发涌现出"反思"和"验证"等推理行为
  - *R1-Zero*：纯 RL 训练，无 SFT 冷启动，证明推理能力可以从 RL 中涌现
  - *R1*：SFT 冷启动 + GRPO，更稳定，效果更好
  - *R1-Distill*：用 R1 生成的思维链数据蒸馏小模型（7B/14B/32B），效果惊人
  - *核心问题*：为什么 R1-Zero 会涌现出"aha moment"（自我反思）？

- **Test-time Compute Scaling** 🔥 ⭐
  - *核心思想*：推理时增加计算量（更长思维链 / Best-of-N / MCTS）可以持续提升性能
  - *为什么重要*：打开了新的 Scaling 维度，不只是训练时 Scaling
  - *核心问题*：什么时候推理时 Scaling 有效？（有明确验证标准的任务：数学/代码）

- **Long CoT vs Short CoT**
  - *核心问题*：什么时候需要长思维链？（复杂推理任务）什么时候反而有害？（简单任务过度思考）
  - *Overthinking 问题*：推理模型在简单问题上浪费大量 token，成本高

---

## 5.2 AI Agent 规模化落地 🔥🔥

- **Coding Agent** 🔥🔥
  - Cursor / Windsurf：IDE 级别的 AI 编程助手
  - Devin / SWE-agent：自主完成 GitHub Issue 的 Agent
  - *核心问题*：Coding Agent 的核心挑战是什么？（长上下文理解 + 工具调用 + 错误恢复）

- **Computer Use Agent** 🔥
  - Claude Computer Use / OpenAI Operator
  - *核心思想*：Agent 直接操作计算机界面（截图 → 分析 → 点击/输入）
  - *核心问题*：Computer Use 的主要挑战？（UI 理解精度 + 操作安全性 + 速度）

- **Deep Research Agent** 🔥
  - OpenAI Deep Research / Gemini Deep Research
  - *核心思想*：自主搜索 → 阅读 → 综合 → 生成报告，替代人工研究
  - *核心问题*：Deep Research 和普通 RAG 的区别？（多轮迭代检索 + 主动规划搜索策略）

---

## 5.3 新架构探索

- **Mamba / SSM（状态空间模型）** 🔥 ⭐
  - *核心思想*：用递推的状态空间方程替代 Attention，线性复杂度 O(n)
  - *优势*：长序列推理速度快，内存占用低
  - *劣势*：In-Context Learning 能力弱于 Transformer，无法"回头看"
  - *核心问题*：Mamba 为什么没有取代 Transformer？（表达能力有差距，尤其是 ICL）

- **Hybrid Architecture（混合架构）** 🔥
  - Jamba / Zamba：Mamba + Attention 交替，兼顾效率和能力
  - *核心思想*：用 Mamba 处理大部分 token（高效），用 Attention 处理关键位置（高质量）

- **MoE 深度演进** 🔥 ⭐
  - DeepSeek MoE：细粒度专家（更多更小的专家）+ 共享专家（所有 token 都激活）
  - *核心问题*：细粒度专家 vs 粗粒度专家的权衡？（细粒度专家组合更灵活，但路由更复杂）

- **BitNet b1.58** 🔥 ⭐
  - *核心思想*：权重只有 {-1, 0, 1} 三个值，用加减法替代乘法
  - *为什么重要*：理论上可以极大降低推理能耗，端侧部署的终极方案
  - *核心问题*：1-bit 量化会损失多少精度？（在足够大的模型上损失可接受）

- **Test-Time Training（TTT）**
  - *核心思想*：推理时用当前输入更新模型参数，让模型适应当前任务
  - *核心问题*：TTT 和 Fine-tuning 的区别？（TTT 是推理时的临时更新，不持久化）

---

## 5.4 AI 安全与对齐 🔥

- **幻觉（Hallucination）** 🔥 ⭐
  - *核心思想*：模型生成看似合理但实际错误的内容
  - *类型*：事实性幻觉（编造事实）/ 忠实性幻觉（不忠于输入）
  - *缓解方案*：RAG（接地气）/ 自我一致性检查 / 引用来源 / 不确定性表达
  - *核心问题*：为什么 LLM 会幻觉？（训练目标是预测下一个 token，不是保证事实正确）

- **Mechanistic Interpretability（机制可解释性）** 🔥
  - *核心思想*：理解模型内部的计算机制，找到"电路"（Circuit）
  - *代表工作*：Anthropic 的 Superposition / Sparse Autoencoder（SAE）
  - *为什么重要*：理解模型才能更好地对齐和控制模型

- **合成数据的 Model Collapse** ⭐
  - *核心思想*：用合成数据训练的模型生成更多合成数据，迭代后模型退化
  - *核心问题*：如何避免 Model Collapse？（保留真实数据 / 多样性控制 / 质量过滤）

> 💡 **面试拷问 — 前沿热点** 🔥🔥🔥
> - 推理模型（o3/R1）和普通 LLM 的本质区别是什么？⭐
> - CoT 和推理模型的思维链有什么本质区别？⭐
> - Test-time Compute Scaling 是什么？什么条件下有效？⭐
> - 推理模型在简单问题上的 Overthinking 问题怎么解决？
> - DeepSeek-R1-Zero 为什么会涌现出 "aha moment"（自我反思）？⭐
> - DeepSeek-V3 的 MoE + MLA 架构为什么训练成本这么低？⭐
> - LLaMA 4 的 MoE 和 DeepSeek-V3 有什么区别？⭐
> - Claude 3.7 的 Extended Thinking 和 DeepSeek-R1 有什么区别？⭐
> - Gemini 2.5 Pro 的 1M context 是怎么做到的？长上下文的技术难点？⭐
> - Mechanistic Interpretability 能做什么？Sparse Autoencoder 是什么？⭐
> - 合成数据训练的 Model Collapse 是什么？怎么避免？⭐
> - Phi-4 用合成数据训出小模型大能力，合成数据的关键是什么？⭐
> - In-Context Learning 的本质是什么？是"学习"还是"检索"？⭐
> - BitNet b1.58 用三值量化，为什么在足够大的模型上损失可接受？
> - Mamba 为什么没有取代 Transformer？混合架构（Jamba）是出路吗？⭐
> - World Model / Video Generation Model 是通往 AGI 的路径吗？
> - 多模态大模型（GPT-4o/Gemini）的"原生多模态"和"模块拼接"本质区别？⭐
> - Coding Agent 的核心技术挑战是什么？（长上下文理解 + 工具调用 + 错误恢复）⭐
> - Computer Use Agent 的主要挑战？UI 理解精度怎么保证？
> - AI Agent 的 Benchmark（SWE-bench/WebArena）是怎么评估的？
