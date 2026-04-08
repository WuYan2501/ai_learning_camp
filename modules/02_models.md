# ② 模型层：架构 / 训练 / 大模型家族

> Transformer 是一切的基础，这里是最核心的模块
>
> 返回 [知识库索引](../SYLLABUS.md)

---

## 2.1 Transformer 架构 🔥🔥🔥

### 核心机制

- **Self-Attention（自注意力）** ⭐
  - *核心思想*：每个 token 对序列中所有 token 计算相关性权重，加权求和得到新表示
  - *数学*：`Attention(Q,K,V) = softmax(QKᵀ/√d_k)V`
  - *核心问题*：为什么要除以 √d_k？（防止点积过大导致 softmax 梯度消失）⭐
  - *复杂度*：时间 O(n²d)，空间 O(n²)，这是长序列的瓶颈

- **Multi-Head Attention（多头注意力）**
  - *核心思想*：并行运行 h 个独立的 Attention，捕获不同子空间的关系，最后拼接投影
  - *核心问题*：多头的意义是什么？（不同头关注不同类型的依赖关系：语法/语义/位置）

- **Feed-Forward Network（FFN）** ⭐
  - *标准结构*：两层线性 + 激活函数（原始 Transformer 用 ReLU）
  - *现代变体*：SwiGLU = `(xW₁) ⊙ SiLU(xW₂)` × W₃，LLaMA/DeepSeek 标配
  - *核心问题*：FFN 在 Transformer 中的作用是什么？（存储知识，类似记忆模块）
  - *参数占比*：FFN 参数量约占整个 Transformer 的 2/3

- **残差连接 + 归一化（Add & Norm）**
  - **Post-Norm**（原始 Transformer）：`LayerNorm(x + Sublayer(x))`，训练不稳定
  - **Pre-Norm**（现代 LLM 标配）：`x + Sublayer(LayerNorm(x))`，梯度更稳定 ⭐
  - *核心问题*：Pre-Norm 为什么训练更稳定？（梯度可以直接通过残差路径回传，不经过归一化层）

### 位置编码

- **绝对位置编码（正弦/余弦）**
  - *原始 Transformer 方案*，固定公式，不可学习，无法外推到训练长度之外

- **可学习位置编码**
  - BERT / GPT-2 使用，简单但无法外推

- **相对位置编码**
  - ALiBi：在 Attention score 上加线性偏置，距离越远惩罚越大，天然支持外推
  - T5 Bias：可学习的相对位置偏置

- **RoPE（旋转位置编码）** 🔥 ⭐
  - *核心思想*：用旋转矩阵将位置信息编码到 Q/K 中，使得 QᵢKⱼ 的内积只依赖相对位置 i-j
  - *为什么重要*：LLaMA / DeepSeek / Qwen / Mistral 全系列标配
  - *核心问题*：RoPE 为什么比绝对位置编码更适合长度外推？
  - *延伸*：NTK-aware / YaRN / Dynamic NTK — 不重训的情况下扩展上下文窗口

### 注意力变体

- **Causal Attention（因果注意力）**
  - *核心思想*：下三角掩码，每个 token 只能看到自己和之前的 token
  - *为什么重要*：Decoder-only 架构的核心，保证自回归生成的合法性

- **MQA / GQA** 🔥 ⭐
  - **MHA**：每个头有独立的 Q/K/V（标准方案，参数多，KV Cache 大）
  - **MQA**（Multi-Query Attention）：多个 Q 头共享一组 K/V，大幅减少 KV Cache
  - **GQA**（Grouped-Query Attention）：Q 头分组，每组共享一组 K/V，平衡质量和效率
  - *为什么重要*：LLaMA 3 / Mistral / Qwen 都用 GQA，推理时 KV Cache 减少 8x
  - *核心问题*：GQA 如何在不损失太多质量的情况下减少 KV Cache？

- **MLA（Multi-head Latent Attention）** 🔥 ⭐
  - *核心思想*：将 K/V 压缩到低维潜空间（latent vector），推理时只缓存低维向量
  - *为什么重要*：DeepSeek-V2/V3 核心创新，KV Cache 压缩比高达 5-13x
  - *核心问题*：MLA 和 GQA 的本质区别？（MLA 是低秩压缩，GQA 是头共享）

- **Flash Attention** 🔥 ⭐
  - *核心思想*：IO 感知算法，将 Attention 计算分块，避免将 n×n 矩阵写入 HBM
  - *为什么重要*：训练速度提升 2-4x，显存从 O(n²) 降到 O(n)，已成标配
  - *核心问题*：Flash Attention 解决的是计算瓶颈还是内存瓶颈？（内存带宽瓶颈）
  - *版本*：FA1 → FA2（更好的并行化）→ FA3（Hopper GPU 优化）

- **Sparse Attention / Sliding Window**
  - Sliding Window（Mistral）：每个 token 只关注局部窗口，O(n·w) 复杂度
  - Longformer：局部 + 全局 token 混合注意力
  - BigBird：随机 + 局部 + 全局，理论上可处理任意长序列

- **Linear Attention / Mamba**
  - *核心思想*：用递推形式替代 softmax attention，复杂度降到 O(n)
  - *代表*：Mamba（SSM）、RWKV、RetNet
  - *核心问题*：线性注意力为什么没有完全取代 Transformer？（表达能力有损失）

### 架构对比

- **Encoder-only（BERT 系）**
  - 双向注意力，适合理解任务（分类/NER/问答抽取）
  - *为什么不适合生成*：没有因果掩码，无法自回归

- **Decoder-only（GPT / LLaMA / DeepSeek）** 🔥 ⭐
  - 因果注意力，自回归生成
  - *为什么成主流*：统一了理解和生成；In-Context Learning 能力强；Scaling 效果好
  - *核心问题*：Decoder-only 做理解任务（如分类）时有什么劣势？

- **Encoder-Decoder（T5 / BART）**
  - 编码器处理输入，解码器生成输出，适合翻译/摘要等 seq2seq 任务
  - *为什么式微*：Decoder-only 在足够大的规模下表现更好，且架构更简单

- **Mixture of Experts（MoE）** 🔥 ⭐
  - *核心思想*：FFN 层替换为多个专家网络，每次只激活 Top-K 个专家（稀疏激活）
  - *为什么重要*：参数量大但计算量不变，DeepSeek-V3（671B 参数，37B 激活）
  - *核心问题*：MoE 的路由机制（Router）如何训练？负载均衡问题怎么解决？
  - *挑战*：专家坍塌（Expert Collapse）/ 通信开销（多机训练时）

> 💡 **面试拷问 — Transformer 架构**
> - Transformer 的输入到输出完整计算流程？手画架构图并讲解？⭐
> - Attention 的 Q/K/V 分别是什么？为什么要拆成三个矩阵？能不能只用两个？⭐
> - 为什么 Attention 用点积而不是加法？两者在表达能力上有什么区别？
> - softmax 在 Attention 中的作用是什么？如果去掉 softmax 会怎样？⭐
> - Multi-Head Attention 的 "多头" 有什么物理含义？不同头学到的东西一样吗？怎么验证？
> - FFN 参数量占 Transformer 的 2/3，为什么不压缩 FFN 而是压缩 Attention？
> - 为什么 Transformer 需要残差连接？如果去掉残差连接会怎样？⭐
> - Encoder-only vs Decoder-only vs Encoder-Decoder，三种架构分别适合什么任务？⭐
> - 为什么 GPT 不用 Encoder-Decoder？为什么 Decoder-only 最终胜出？⭐
> - RoPE 的旋转矩阵是怎么把位置信息编码进 Q/K 的？用简单数学说明？⭐
> - ALiBi 和 RoPE 的核心区别？各自的优劣势？
> - MHA → MQA → GQA → MLA，这条演进路线的驱动力是什么？⭐
> - GQA 为什么不直接用 MQA？从质量-效率权衡角度分析？
> - MLA 的低秩压缩和 LoRA 的低秩思想有什么关联？⭐
> - Flash Attention 的 "tiling" 策略是什么？为什么分块能减少 IO？⭐
> - Flash Attention 能和 Sparse Attention 结合吗？有什么工作？
> - MoE 中 Router 的训练信号来自哪里？为什么容易出现负载不均衡？⭐
> - MoE 的 Expert Collapse 是什么？DeepSeek 怎么解决的？⭐
> - Sliding Window Attention 在超长文本上为什么比全局 Attention 差？信息丢失在哪？
> - Mamba 的选择性状态空间是什么？和 RNN 的隐状态有什么本质区别？⭐

---

## 2.2 大模型家族谱系

- **闭源模型**
  - OpenAI：GPT-4o（多模态）/ GPT-4.5 / o1 / o3 / o3-mini / o4-mini（推理系列）
  - Anthropic：Claude 3.5 Sonnet / Claude 3.7 Sonnet（Extended Thinking）/ Claude 3.5 Opus
  - Google：Gemini 2.0 Flash / Gemini 2.0 Pro / Gemini 2.5 Pro（1M context）
  - xAI：Grok-3 / Grok-3-mini

- **开源模型**
  - Meta LLaMA 系列：LLaMA 3（8B/70B/405B）/ LLaMA 3.1 / LLaMA 3.3 / LLaMA 4 🔥
    - *架构特点*：GQA + RoPE + SwiGLU + RMSNorm，成为开源标准架构
  - DeepSeek 系列：DeepSeek-V2 / V3 / R1 🔥🔥
    - *架构特点*：MLA + MoE，训练成本极低（V3 仅用 557 万美元）
  - Qwen 系列：Qwen2.5 / Qwen2.5-Coder / Qwen2.5-Math / QwQ-32B 🔥
    - *特点*：中文最强开源，代码/数学专项能力突出
  - Mistral 系列：Mistral Large / Mixtral 8x7B（MoE）/ Mistral Small 3
  - 国内：GLM-4（智谱）/ Baichuan2（百川）/ Yi（01.AI）

- **小模型/端侧模型**
  - Phi-4 / Phi-4-mini（Microsoft）🔥：合成数据策略，小模型大能力
  - Gemma 2 / Gemma 3（Google）/ SmolLM2（HuggingFace）
  - Qwen2.5-0.5B/1.5B/3B/7B / MiniCPM-3（面壁智能）

---

## 2.3 Tokenizer

- **BPE（Byte Pair Encoding）** ⭐
  - *核心思想*：从字符开始，迭代合并最高频的相邻 token 对，直到达到词表大小
  - *使用者*：GPT 系列、LLaMA、DeepSeek
  - *核心问题*：BPE 的贪心合并策略有什么问题？（同一个词可能有多种分词方式）

- **WordPiece**
  - *核心思想*：类似 BPE，但合并标准是最大化语言模型似然，而非频率
  - *使用者*：BERT

- **SentencePiece / Unigram**
  - *特点*：语言无关，直接从原始文本训练，支持中日韩等无空格语言
  - *使用者*：T5、LLaMA（基于 SentencePiece）

- **tiktoken**（OpenAI）
  - cl100k_base（GPT-4）/ o200k_base（GPT-4o），词表更大，中文效率更高

- **关键设计问题** ⭐
  - 词表大小权衡：太小 → 序列过长，计算慢；太大 → Embedding 层参数爆炸
  - 中文 token 效率：GPT-4 约 1.5 汉字/token，Qwen 约 2.5 汉字/token
  - *核心问题*：Tokenizer 的 fertility（生育率）指标是什么？如何影响模型效率？

> 💡 **面试拷问 — Tokenizer & Embedding**
> - BPE 和 WordPiece 的合并标准有什么不同？分别有什么优劣？⭐
> - 同一个中文句子在 GPT-4 和 Qwen 中 token 数差多少？为什么？⭐
> - 词表大小对模型性能和效率有什么影响？LLaMA 为什么选 32K 词表？
> - Tokenizer 训练数据和模型预训练数据不一致会有什么问题？
> - 为什么 LLM 不直接用字符级别的 Tokenizer？（序列太长 vs 语义粒度太细）
> - Word2Vec 的 Skip-gram 和 CBOW 哪个更好？各适合什么场景？
> - 为什么 Sentence Embedding 需要对比学习？直接用 [CLS] token 不行吗？⭐
> - Matryoshka Embedding 怎么做到一个模型支持多种维度？训练目标是什么？⭐
> - CLIP 的对比学习目标函数是什么？InfoNCE loss 的直觉是什么？⭐

---

## 2.4 Embedding

- **Word2Vec（CBOW / Skip-gram）**
  - *历史地位*：静态词向量的开山之作，证明了词语的分布式表示
  - *局限*：一词一向量，无法处理多义词

- **Contextual Embedding（BERT / GPT）**
  - *核心思想*：同一个词在不同上下文中有不同的向量表示
  - *为什么重要*：解决了多义词问题，是现代 NLP 的基础

- **Sentence Embedding** 🔥
  - Sentence-BERT / E5 / BGE / GTE / Cohere Embed v3
  - *用途*：RAG 检索、语义相似度、聚类
  - *核心问题*：如何训练好的 Sentence Embedding？（对比学习 + 难负例挖掘）
  - *评估*：MTEB Leaderboard（56 个任务的综合评估）

- **Matryoshka Representation Learning（MRL）** 🔥
  - *核心思想*：训练时同时优化不同维度截断的 Embedding，推理时可按需截断
  - *为什么重要*：一个模型支持多种维度，节省存储和计算（OpenAI text-embedding-3 使用）

- **多模态 Embedding**
  - CLIP / SigLIP / ALIGN：图文对齐，对比学习
  - *核心思想*：将图像和文本映射到同一向量空间

---

## 2.5 预训练

- **预训练目标**
  - **CLM（Causal Language Modeling）** ⭐：预测下一个 token，GPT 系列标配
    - *核心问题*：为什么 Next Token Prediction 能让模型学到如此多的知识？
  - **MLM（Masked Language Modeling）**：随机 mask 15% token 后预测，BERT 标配
  - **Denoising（T5）**：随机 mask 连续 span 后重建
  - **对比学习**：SimCSE / CLIP，拉近正样本、推远负样本

- **预训练数据** ⭐
  - 数据配比：代码（提升推理）/ 数学 / 多语言 / 网页文本 / 书籍
  - 数据清洗：去重（MinHash）/ 质量过滤（Perplexity 过滤）/ 有害内容过滤
  - 合成数据：Phi 系列证明高质量合成数据可以大幅提升小模型能力 🔥
  - *核心问题*：数据配比如何影响模型能力？（代码数据提升推理能力的机制）

- **Scaling Law** ⭐
  - **Kaplan Law（2020）**：模型性能与参数量/数据量/算力呈幂律关系
  - **Chinchilla Law（2022）**：最优配比是 20 tokens/参数，之前的模型都训练不足
  - **推理时 Scaling（2024）** 🔥：增加推理计算（更长思维链/更多采样）也能提升性能
  - *核心问题*：Chinchilla Law 的结论对工业界有什么影响？（LLaMA 用更多数据训更小模型）

- **分布式训练** 🔥 ⭐
  - **数据并行（DDP）**：每个 GPU 有完整模型，数据分片，梯度 All-Reduce 同步
  - **模型并行（张量并行）**：将单层的矩阵运算切分到多个 GPU
  - **流水线并行**：将不同层分配到不同 GPU，流水线执行
  - **DeepSpeed ZeRO**：
    - ZeRO-1：分片优化器状态（节省 4x 显存）
    - ZeRO-2：分片优化器状态 + 梯度（节省 8x 显存）
    - ZeRO-3：分片优化器状态 + 梯度 + 参数（节省 64x 显存）
  - *核心问题*：ZeRO-3 和模型并行的区别？（ZeRO-3 是数据并行的显存优化，不是模型并行）

---

## 2.6 模型对齐与微调 🔥🔥

- **SFT（监督微调）**
  - *核心思想*：用高质量的指令-回复对，让模型学会遵循指令
  - **LoRA** 🔥 ⭐：在权重矩阵旁边加低秩分支 `W = W₀ + BA`，只训练 B 和 A
    - *核心问题*：为什么低秩矩阵能近似全参数更新？（预训练权重的更新矩阵本身是低秩的）
    - *变体*：QLoRA（4-bit 量化 + LoRA）/ DoRA（分解幅度和方向）/ LoRA+
  - *数据质量 > 数据数量* ⭐：1000 条高质量数据 > 100000 条低质量数据
  - *灾难性遗忘*：微调时模型忘记预训练知识，缓解方法：EWC / 混入预训练数据 / LoRA

- **RLHF（人类反馈强化学习）**
  - *流程*：SFT → 训练奖励模型（RM）→ PPO 优化策略模型
  - **PPO** ⭐：近端策略优化，clip 约束防止策略更新过大
  - *问题*：训练不稳定、需要 4 个模型（Actor/Critic/RM/Reference）、计算成本高

- **DPO（直接偏好优化）** 🔥 ⭐
  - *核心思想*：绕过显式奖励模型，直接从偏好数据优化策略
  - *为什么重要*：比 RLHF 简单稳定，只需 2 个模型，已成主流
  - *核心问题*：DPO 的数学推导？（将 RM 的最优解代入 RLHF 目标，消去 RM）
  - *变体*：SimPO / KTO / IPO / ORPO / CPO

- **GRPO（Group Relative Policy Optimization）** 🔥🔥 ⭐
  - *核心思想*：对同一问题采样 G 个回答，用组内相对奖励替代绝对奖励，去掉 Critic 模型
  - *为什么重要*：DeepSeek-R1 的核心训练方法，让模型自发涌现推理能力
  - *核心问题*：GRPO 和 PPO 的本质区别？（无需 Critic，用 Group 均值作为 baseline）

- **推理增强训练**
  - **PRM vs ORM** 🔥 ⭐
    - ORM（结果奖励）：只看最终答案对不对，简单但信号稀疏
    - PRM（过程奖励）：对每个推理步骤打分，信号密集但标注成本高
    - *核心问题*：什么时候用 PRM？（数学/代码等有明确中间步骤的任务）
  - **Best-of-N Sampling**：采样 N 个回答，用 RM 选最好的，简单有效的推理增强
  - **MCTS + LLM**：用蒙特卡洛树搜索做规划，AlphaGo 思路迁移到语言模型

> 💡 **面试拷问 — 预训练与对齐**
> - 为什么 Next Token Prediction 这么简单的目标能让模型学到世界知识？⭐
> - 预训练数据中加入代码为什么能提升推理能力？内在机制是什么？⭐
> - Scaling Law 在什么条件下会失效？有反例吗？⭐
> - 如果预算固定，应该训更大模型还是用更多数据？Chinchilla vs LLaMA 给出了什么不同答案？⭐
> - LoRA 的 rank 设成多少合适？rank 太高/太低分别有什么问题？⭐
> - LoRA 应该加在哪些层？只加 Q/V 和全加的区别？
> - 为什么 DPO 不需要奖励模型？从数学推导上解释？⭐
> - DPO 的偏好数据质量差会怎样？比 RLHF 更容易受数据质量影响吗？
> - GRPO 的 "Group Relative" 是什么意思？和 PPO 的 advantage 有什么区别？⭐
> - DeepSeek-R1 的 "aha moment" 是什么？为什么纯 RL 训练能涌现自我反思？⭐
> - SFT 数据量多少合适？1000 条和 10 万条的效果差距到底有多大？⭐
> - 灾难性遗忘在 LoRA 微调中也会发生吗？程度比全参数微调轻多少？
> - PRM 的训练数据怎么构造？人工标注每一步的成本有多高？⭐
> - Best-of-N Sampling 的 N 设成多少合适？N 和效果提升是什么关系（log/linear）？
> - ZeRO-3 训练时每步前向传播都要通信获取参数，通信开销大不大？怎么优化？⭐
> - 张量并行和流水线并行可以同时用吗？3D 并行是什么？⭐
