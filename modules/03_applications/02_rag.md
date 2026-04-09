# 3.2 RAG（检索增强生成）🔥🔥

> 大模型的"外挂知识库"，解决幻觉和时效性问题的核心方案
>
> 返回 [应用层索引](/modules/03_applications) | [知识库索引](/SYLLABUS)

---

## 基础 Pipeline ⭐

```
文档加载 → 切分(Chunking) → 嵌入(Embedding) → 存储(向量DB) → 检索(Retrieval) → 重排(Reranking) → 生成(Generation)
```

- *核心问题*：RAG 的每个环节都是优化点，哪个环节对最终效果影响最大？（检索质量 > 生成质量）

---

## Chunking 策略 ⭐

- **固定大小切分**：简单，但可能切断语义
- **递归字符切分**：按段落→句子→词语递归切分，LangChain 默认方案
- **语义切分**：用 Embedding 相似度判断语义边界，效果好但慢
- **Sentence Window**：检索小块，但喂给 LLM 时扩展到周围更大的窗口
- **Parent-Child**：小块用于检索（精准），大块用于生成（上下文完整）
- **Late Chunking** 🔥：先对整个文档做 Embedding，再切分，保留跨块的上下文信息
- *核心问题*：chunk size 怎么定？（太小 → 上下文不足；太大 → 噪声多，检索不精准）

---

## Embedding 模型选型

- **主流模型**：BGE-M3 / E5-Mistral / GTE / Cohere Embed v3 🔥
  - BGE-M3：多语言、多粒度（稠密+稀疏+多向量），中文最强
  - E5-Mistral：英文最强，基于 Mistral 微调
- **评估基准**：MTEB Leaderboard（56 个任务，覆盖检索/分类/聚类等）
- *核心问题*：如何选 Embedding 模型？（看 MTEB 上对应任务类型的排名，不要只看总分）

---

## 向量数据库与索引

- **HNSW 索引** ⭐
  - *核心思想*：分层图结构，高层稀疏（快速定位区域），低层密集（精确搜索）
  - *核心问题*：HNSW 的 ef_construction 和 M 参数如何影响精度和速度？

- **混合检索（Hybrid Search）** 🔥 ⭐
  - *核心思想*：向量检索（语义）+ BM25（关键词）并行，RRF 算法融合排名
  - *为什么重要*：纯向量检索对专有名词/数字/代码效果差，混合检索互补
  - *核心问题*：RRF（Reciprocal Rank Fusion）的公式是什么？如何调权重？

---

## 高级 RAG 技术

- **Reranking（重排序）** 🔥 ⭐
  - *核心思想*：检索召回 Top-K（粗排），再用 Cross-Encoder 精排 Top-N
  - **Bi-Encoder**（向量检索）：快，但精度有限（向量压缩了信息）
  - **Cross-Encoder**（重排）：慢，但精度高（query 和 doc 一起输入，充分交互）
  - *核心问题*：为什么不直接用 Cross-Encoder 做检索？（O(n) 复杂度，无法扩展到大规模）

- **HyDE（假设文档嵌入）** ⭐
  - *核心思想*：先让 LLM 生成一个假设答案，用假设答案的 Embedding 去检索
  - *为什么有效*：假设答案和真实文档在向量空间更近（都是答案形式），而不是问题和答案
  - *适用场景*：问题和文档表述差异大的场景

- **GraphRAG** 🔥 ⭐
  - *核心思想*：将文档构建为知识图谱，检索时利用图结构做多跳推理
  - *为什么重要*：普通 RAG 无法处理需要跨文档推理的问题
  - *核心问题*：GraphRAG 的构建成本很高，什么场景值得用？（企业知识库、多文档关联分析）

- **Self-RAG / Corrective RAG（CRAG）** 🔥
  - *核心思想*：模型自我评估检索结果是否有用，决定是否重新检索或直接生成
  - *为什么重要*：解决检索到无关内容时模型仍然强行使用的问题

- **Agentic RAG** 🔥🔥
  - *核心思想*：用 Agent 驱动检索，支持多步检索、动态查询改写、工具调用
  - *为什么重要*：复杂问题需要多轮检索，静态 RAG Pipeline 不够用

---

## RAG 评估

- **RAGAS 框架** ⭐
  - Faithfulness（忠实度）：回答是否基于检索内容，不幻觉
  - Answer Relevance（答案相关性）：回答是否回答了问题
  - Context Precision（上下文精确率）：检索内容中有多少是有用的
  - Context Recall（上下文召回率）：有用的内容是否都被检索到了
  - *核心问题*：这四个指标如何权衡？（Faithfulness 最重要，幻觉是最大风险）

- **Lost in the Middle** ⭐
  - *核心问题*：LLM 对长上下文中间部分的注意力较弱，重要信息放中间会被忽略
  - *缓解方案*：重要内容放首尾 / 减少无关上下文 / 使用 Reranking 精选

---

> 💡 **面试拷问 — RAG**
> - RAG 和 Fine-tuning 什么时候用哪个？有没有能两个都用的场景？⭐
> - RAG 和长上下文窗口哪个更好？各自的优劣势？⭐
> - 向量检索对专有名词和精确数字为什么效果差？怎么解决？⭐
> - Chunk Overlap 的作用是什么？重叠太多和太少分别有什么问题？
> - Parent-Child Chunking 和 Sentence Window 的区别？各适合什么场景？⭐
> - Late Chunking 为什么能保留跨块上下文？和普通 Chunking 的本质区别？⭐
> - HNSW 为什么比暴力搜索快？分层图结构的直觉是什么？⭐
> - RRF 融合和加权融合有什么区别？为什么 RRF 通常更稳健？
> - Cross-Encoder 重排比向量检索精准在哪里？为什么不能直接用 Cross-Encoder 做全库检索？⭐
> - HyDE 生成的假设答案质量差怎么办？会不会反而干扰检索？
> - GraphRAG 构建的知识图谱和传统知识图谱有什么区别？⭐
> - Agentic RAG 和普通 RAG Pipeline 的核心区别是什么？什么场景下必须用 Agentic RAG？⭐
> - RAGAS 的 Faithfulness 怎么计算？是否需要人工标注？
> - RAG 的幻觉和 LLM 本身的幻觉有什么区别？分别怎么解决？⭐
