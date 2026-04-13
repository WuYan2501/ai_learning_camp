# ② 模型层：Transformer / 预训练 / 对齐

> 上一章主要介绍了一些“模型的基础知识、如数学是基座，机器学习是数学的具体实现、深度学习则是机器学习更加具体的分支，这个分支最终是指向大模型的实现”
> 这一章主要内容：**大模型到底是怎么搭起来、怎么训练出来、又为什么会演化成今天这个样子。**
>
> 你可以先抓住一条主线：
>
> **Tokenizer 把文本切成 token → Embedding 把 token 变成向量 → Transformer 负责建模上下文 → 预训练把知识灌进去 → 对齐与微调把“会补全”变成“会配合”。**
>
>
> 返回 [知识库索引](/SYLLABUS)

---

## 2.0 这一章怎么学

- **如果你是第一次系统看模型层**：先按 `Transformer 基础 → 预训练与 Scaling → 对齐与微调` 这条主线看，先理解“大模型为什么成立”
- **如果你准备面试**：优先抓住 `Self-Attention`、`RoPE`、`GQA`、`MoE`、`LoRA`、`DPO`、`GRPO`
- **如果你更偏工程落地**：优先看 `KV Cache`、`Flash Attention`、`Tokenizer 效率`、`数据配比`、`ZeRO`
- **这章不建议死记硬背**：重点不是记住某个模型的技术名词，而是要理解它在解决什么问题，比如能更省显存、能更长上下文、更强推理
- **本章优先知识点**：`Attention`、`RoPE`、`KV Cache`、`MoE`、`Tokenizer`、`CLM`、`LoRA`、`DPO`

---

## 📂 模型层模块导航

> 模型层内容已经拆分为子目录 `02_models/` 管理，本文件作为索引导航

| # | 模块 | 文件 | 核心内容 | 重要度 |
|---|------|------|----------|--------|
| 2.1 | **Transformer 基础** 🔥🔥🔥 | [01_transformer_core.md](/modules/02_models/01_transformer_core.md) | Attention → FFN → 残差归一化 → RoPE → 架构分型 | 必学 |
| 2.2 | **Transformer 演进与效率** 🔥🔥 | [02_transformer_efficiency.md](/modules/02_models/02_transformer_efficiency.md) | KV Cache → GQA → Flash Attention → MoE → 长上下文 | 必学 |
| 2.3 | Tokenizer 与 Embedding 🔥 | [03_tokenizer_and_embedding.md](/modules/02_models/03_tokenizer_and_embedding.md) | 文本切分 → 向量表示 → 检索与语义表示 | 重要 |
| 2.4 | **预训练与 Scaling** 🔥🔥🔥 | [04_pretraining_and_scaling.md](/modules/02_models/04_pretraining_and_scaling.md) | CLM → 数据 → Scaling Law → 分布式训练 | 必学 |
| 2.5 | **对齐与微调** 🔥🔥🔥 | [05_alignment_and_finetuning.md](/modules/02_models/05_alignment_and_finetuning.md) | SFT → LoRA → RLHF → DPO → GRPO | 必学 |
| 2.6 | 大模型家族与选型视角 🔥 | [06_model_families.md](/modules/02_models/06_model_families.md) | 开闭源路线 → 架构风格 → 选型思路 | 重要 |

---

## 🗺️ 模型层主线关系

```text
文本
  ↓
Tokenizer
  ↓
Embedding
  ↓
Transformer
  ↓
预训练
  ↓
对齐 / 微调
  ↓
不同模型家族与产品形态
```

---

## 🎯 阅读建议

1. **先搞懂骨架**：为什么大模型几乎都绕不开 Transformer
2. **再搞懂训练**：为什么“下一个 token 预测”就能把知识学进去
3. **然后理解可用性**：为什么预训练模型还要做 SFT、偏好对齐和微调
4. **最后再看家族差异**：不同模型为什么会走出不同路线，本质上在权衡什么
