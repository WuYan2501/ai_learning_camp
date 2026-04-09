# ④ 工程层：量化 / 推理优化 / 部署 / 评估 / Harness Engineering

> 把模型从实验室搬到生产环境的全部知识，并补上 LLM / Agent 应用在测试、回放、评测、沙箱执行上的工程基座
>
> 返回 [知识库索引](/SYLLABUS)

---

## 4.1 模型压缩

### 量化（Quantization）⭐

- **数值格式**
  - FP32（全精度）→ FP16（半精度）→ BF16（Brain Float，动态范围更大）
  - INT8 → INT4 → NF4（Normal Float 4，QLoRA 使用）→ INT2 / 1-bit
  - *核心问题*：FP16 和 BF16 的区别？（BF16 指数位更多，不容易溢出，LLM 训练首选）
  - *核心问题*：为什么量化会损失精度？（将连续值映射到离散格点，有舍入误差）

- **PTQ vs QAT**
  - PTQ（训练后量化）：训练完再量化，简单，有精度损失
  - QAT（量化感知训练）：训练时模拟量化，精度更好，但需要重训

- **主流量化方案** 🔥 ⭐
  - **GPTQ**：逐层量化，用 Hessian 矩阵补偿量化误差，INT4 精度最好
  - **AWQ**：激活感知量化，保护重要权重不量化，速度快
  - **GGUF**：llama.cpp 的格式，支持 CPU 推理，多种量化粒度（Q4_K_M 最常用）
  - **bitsandbytes**：NF4 量化，QLoRA 的基础
  - *核心问题*：GPTQ vs AWQ 怎么选？（GPTQ 精度略好，AWQ 速度更快）

### 知识蒸馏（Knowledge Distillation）⭐

- *核心思想*：用大模型（Teacher）的软标签（概率分布）训练小模型（Student）
- *为什么软标签比硬标签好*：软标签包含类间关系信息（"猫"和"狗"的相似度）
- **白盒蒸馏**：可以访问 Teacher 的中间层特征，信息更丰富
- **黑盒蒸馏**：只能访问 Teacher 的输出，用大模型生成数据训练小模型
- **CoT 蒸馏**：让大模型生成思维链，小模型学习推理过程（DeepSeek-R1-Distill 的方案）

### 剪枝（Pruning）

- **非结构化剪枝**：将权重中接近 0 的值置零，稀疏矩阵，硬件加速困难
- **结构化剪枝**：删除整个 Attention Head / Layer，直接减少参数量
- **SparseGPT / Wanda**：大模型的高效剪枝方案，无需重训
- *核心问题*：剪枝 vs 量化，哪个更实用？（量化更实用，工具链成熟，精度损失可控）

> 💡 **面试拷问 — 模型压缩**
> - INT4 量化后模型精度损失有多大？哪些任务对量化更敏感？⭐
> - GPTQ 的 Hessian 矩阵补偿是什么原理？为什么能减少量化误差？⭐
> - AWQ 的 "激活感知" 是什么意思？它怎么确定哪些权重重要？⭐
> - GGUF 的 Q4_K_M 和 Q4_0 有什么区别？为什么 K 系列更好？
> - NF4 和普通 INT4 的区别是什么？为什么 QLoRA 用 NF4？⭐
> - 知识蒸馏的软标签温度 T 怎么选？T 太高和太低分别有什么问题？⭐
> - DeepSeek-R1-Distill 是怎么做 CoT 蒸馏的？为什么效果这么好？⭐
> - 量化、蒸馏、剪枝三者可以同时用吗？顺序是什么？

---

## 4.2 推理优化 🔥🔥

### KV Cache ⭐ 🔥

- *核心思想*：推理时缓存已计算的 K/V 矩阵，避免重复计算
- *为什么重要*：没有 KV Cache，每生成一个 token 都要重新计算所有历史 token 的 K/V
- **内存计算公式**：`KV Cache = 2 × num_layers × num_heads × head_dim × seq_len × dtype_bytes`
  - 以 LLaMA-3-70B 为例：2 × 80 × 8 × 128 × 4096 × 2 ≈ 40GB（FP16，4096 context）
- *核心问题*：KV Cache 是推理内存的主要瓶颈，如何优化？
  - GQA/MQA：减少 K/V 头数
  - KV Cache 量化（FP8 KV Cache）
  - PagedAttention：动态分配，避免碎片

### PagedAttention（vLLM 核心）🔥 ⭐

- *核心思想*：借鉴操作系统虚拟内存，将 KV Cache 分成固定大小的 Page，按需分配
- *解决的问题*：静态分配 KV Cache 导致大量内存碎片（平均 60-80% 浪费）
- *为什么重要*：vLLM 吞吐量比 HuggingFace 原生高 24x，PagedAttention 是核心原因
- *核心问题*：Page 大小如何选择？（太小 → 管理开销大；太大 → 碎片多）

### Continuous Batching ⭐

- *核心思想*：请求完成后立即插入新请求，而不是等整个 batch 完成
- *vs Static Batching*：Static Batching 中短请求完成后 GPU 空转等待长请求
- *为什么重要*：GPU 利用率从 30-40% 提升到 80%+

### Speculative Decoding（投机解码）🔥 ⭐

- *核心思想*：用小 Draft Model 快速生成多个 token，大 Target Model 并行验证
- *为什么有效*：LLM 推理瓶颈是内存带宽（每次只生成 1 token），并行验证多个 token 提升利用率
- *核心问题*：Draft Model 怎么选？（同系列小模型 / 专门训练的 Draft Model / 自身的早期层）
- *延伸*：Medusa（多头并行预测）/ EAGLE（Draft Model 用目标模型的特征）

### 解码策略 ⭐

- **Temperature**：控制分布的"尖锐程度"，T→0 趋向贪心，T→∞ 趋向均匀
  - *核心问题*：Temperature 为什么能控制创造性？（高温使低概率 token 更容易被选中）
- **Top-p（Nucleus Sampling）**：只从累积概率达到 p 的最小 token 集合中采样
- **Top-k**：只从概率最高的 k 个 token 中采样
- **Min-p**：设置最低概率阈值，过滤掉概率极低的 token，比 Top-p 更稳定
- *核心问题*：推理模型（o3/R1）为什么用低 Temperature？（推理需要确定性，不需要创造性）

> 💡 **面试拷问 — 推理优化**
> - LLM 推理的两个阶段（Prefill 和 Decode）分别是计算密集还是内存密集？为什么？⭐
> - KV Cache 的内存占用具体怎么算？给一个 70B 模型的具体数字？⭐
> - PagedAttention 借鉴了操作系统的什么概念？为什么能提升 24x 吞吐量？⭐
> - Continuous Batching 中如何处理不同长度的请求？padding 开销怎么解决？
> - Speculative Decoding 为什么能加速？它的加速比取决于什么？（acceptance rate）⭐
> - Speculative Decoding 和 Medusa 的区别是什么？各自的优劣势？
> - vLLM 和 SGLang 的核心区别是什么？什么场景用哪个？⭐
> - SGLang 的 RadixAttention 是什么？为什么对有共享前缀的场景更快？⭐
> - Temperature = 0 和 Greedy Decoding 完全等价吗？有什么细微差别？
> - Top-p 和 Top-k 能同时用吗？组合起来效果怎样？
> - TTFT 和 TPS 的优化方向为什么不同？分别受哪些因素影响？⭐
> - Disaggregated Prefill 为什么能同时优化 TTFT 和 TPS？⭐

---

## 4.3 推理框架选型

| 框架 | 核心优势 | 适用场景 |
|------|----------|----------|
| **vLLM** 🔥🔥🔥 | PagedAttention，高吞吐，OpenAI 兼容 API | 生产环境，高并发服务 |
| **SGLang** 🔥🔥 | RadixAttention（前缀缓存），结构化生成 | 有大量共享前缀的场景（RAG/Agent）|
| **llama.cpp** 🔥🔥 | CPU 推理，GGUF 格式，跨平台 | 本地/端侧，无 GPU 环境 |
| **Ollama** 🔥🔥 | 一键运行，用户友好 | 本地开发，快速原型 |
| **TGI** 🔥 | HuggingFace 生态，Flash Attention | HuggingFace 模型部署 |
| **TensorRT-LLM** 🔥 | NVIDIA GPU 极致优化 | 对延迟要求极高的生产环境 |

- *核心问题*：vLLM vs SGLang 怎么选？（有大量共享前缀用 SGLang，通用高并发用 vLLM）

---

## 4.4 模型服务化

- **流式输出** ⭐
  - SSE（Server-Sent Events）：HTTP 单向流，简单，大多数场景首选
  - WebSocket：双向通信，适合需要客户端发送中断信号的场景
  - *核心问题*：流式输出的 TTFT（首 token 延迟）和 TPS（每秒 token 数）如何优化？

- **关键指标**
  - **TTFT（Time to First Token）**：用户感知延迟，优化方向：减少 Prefill 时间
  - **TPS（Tokens Per Second）**：吞吐量，优化方向：Batching + 量化 + 更快硬件
  - **P99 延迟**：99% 请求的延迟上限，SLO 设计的关键指标

- **Disaggregated Prefill** 🔥
  - *核心思想*：将 Prefill（计算密集）和 Decode（内存带宽密集）分离到不同机器
  - *为什么重要*：两个阶段的硬件需求不同，分离后可以分别优化

---

## 4.5 评估体系

### Benchmark 速查

| Benchmark | 评估维度 | 说明 |
|-----------|----------|------|
| MMLU / MMLU-Pro | 知识理解 | 57 个学科，大学水平 |
| HumanEval / MBPP | 代码生成 | Python 函数补全 |
| SWE-bench | 代码修复 | 真实 GitHub Issue |
| GSM8K / MATH | 数学推理 | 小学/竞赛数学 |
| AIME | 数学竞赛 | 高中数学奥林匹克 |
| GPQA | 专家级问答 | 博士级别科学问题 |
| MT-Bench | 多轮对话 | GPT-4 评分 |
| Chatbot Arena 🔥 | 人类偏好 | ELO 排名，最真实 |
| MTEB | Embedding | 56 个任务综合评估 |
| LiveBench 🔥 | 防污染 | 动态更新，防数据污染 |

- **LLM-as-Judge** 🔥 ⭐
  - *核心思想*：用强 LLM（GPT-4）评估弱 LLM 的输出质量
  - *核心问题*：LLM-as-Judge 的偏见有哪些？（位置偏见/长度偏见/自我偏好）
  - *缓解方案*：交换顺序取平均 / 多个 Judge 投票 / 校准 Prompt

> 💡 **面试拷问 — 评估与服务化**
> - LLM-as-Judge 的位置偏见和长度偏见分别是什么？怎么缓解？⭐
> - Chatbot Arena 的 ELO 排名为什么比 MMLU 更可信？⭐
> - 为什么需要 LiveBench 这样的动态评估？数据污染问题有多严重？
> - 流式输出用 SSE 还是 WebSocket？各自的优劣势？⭐
> - P99 延迟和平均延迟的区别？为什么 SLO 设计用 P99 而不是平均值？⭐
> - 如何设计一个支持百万用户的 LLM 服务？从负载均衡到模型路由？⭐

---

## 4.6 Harness Engineering（测试基座工程） 🔥🔥🔥 📝

### 什么是 Harness Engineering ⭐

- *核心思想*：给 LLM / Agent 系统搭一层“可重复、可回放、可对比、可量化”的测试基座（Harness）
- *它解决的问题*：Prompt 改了、模型换了、工具 Schema 变了、Agent 逻辑重构了，怎么快速知道效果是变好还是变坏
- *为什么现在火*：单轮问答越来越少，Agent / Coding / Browser Use 都需要任务级评测，而不是只看一句回答对不对

### Harness 的核心组成

- **任务集（Task Set / Golden Set）**
  - 收集真实高频 case + 历史失败 case + 边界 case，形成稳定回归集
  - *核心问题*：Case 数量多少才够？（早期 20-50 个高价值 case 就能起步，后续逐步扩到 100+）

- **执行环境（Execution Environment）** ⭐
  - 代码 Agent：沙箱 + 文件系统 + 单元测试 + 依赖环境
  - Browser Agent：浏览器状态、页面快照、用户操作轨迹
  - 工具 Agent：MCP / Function Calling / API Mock / 权限隔离
  - *核心问题*：为什么 Harness 一定要配沙箱？（没有隔离环境，结果不可复现，且存在安全风险）

- **回放与追踪（Replay / Trace）** 🔥
  - 保存 prompt、model version、tool calls、intermediate states、最终输出
  - *为什么重要*：只看最终答案很难定位问题，必须能回放 Agent 的完整执行轨迹

- **评测器（Evaluators）** 🔥 ⭐
  - 规则评测：格式正确率 / JSON schema / 关键词命中 / 单元测试
  - LLM-as-Judge：评估解释质量、完整性、偏好
  - 任务级指标：任务完成率、成功路径长度、工具调用成功率、平均步数
  - *核心问题*：LLM-as-Judge 能完全替代规则评测吗？（不能，最好规则 + LLM Judge + 人工抽检组合）

- **对比实验（A/B / Regression）**
  - Prompt A/B、Model A/B、Tool Version A/B、Orchestrator A/B
  - *核心问题*：Harness 和传统 Benchmark 的区别？（Benchmark 更偏静态排名，Harness 更偏你自己业务场景的持续回归）

### 典型落地场景

- **Coding Agent**
  - 看 patch 是否通过测试、任务是否完成、是否引入新错误
  - 参考：SWE-bench / 自建代码仓回归集

- **RAG / Knowledge QA**
  - 同时看检索命中、答案忠实度、引用是否正确，而不是只看最终答案

- **Browser / Computer Use Agent**
  - 看任务完成率、操作步数、页面状态变化、是否走偏或死循环

- **Tool-Calling Agent**
  - 重点观察工具选择正确率、参数填写正确率、异常恢复能力

### Harness Engineering 设计原则 ⭐

- **可复现**：同一输入、同一环境、同一版本能重复得到可比较结果
- **可归因**：能区分是 Prompt、模型、工具、检索还是编排逻辑出了问题
- **可观测**：完整记录输入、输出、轨迹、耗时、成本和失败类型
- **可隔离**：执行环境必须可控，敏感操作需要沙箱和权限边界
- **可持续**：新 case 要能不断回流，形成真正的回归测试资产

### 常见工具与评测基座方向

- **评测与观测**：LangSmith、Langfuse、DeepEval、OpenAI Evals
- **代码任务**：SWE-bench、单元测试基座、自建仓库任务集
- **浏览器 / 环境型任务**：BrowserGym、OSWorld、WebArena
- **RAG / 生成任务**：RAGAS、规则校验、LLM-as-Judge 组合评测

> 💡 **面试拷问 — Harness Engineering**
> - 什么是 Harness Engineering？它和传统自动化测试、Benchmark 的区别是什么？⭐
> - 你会如何为一个 Agent 系统搭建最小可用 Harness？⭐
> - 为什么 Agent 评测不能只看最终答案，还要看 trajectory / trace？⭐
> - LLM-as-Judge、规则评测、人工抽检三者怎么组合？⭐
> - 如果 Prompt 改版后线上指标波动，你如何用 Harness 快速定位问题？⭐