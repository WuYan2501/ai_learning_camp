# ① 基础层：数学 / ML / DL

> 不需要死磕，但面试会问、debug 时会用到
>
> 返回 [知识库索引](../SYLLABUS.md)

---

## 1.1 必备数学

- **线性代数**
  - 矩阵乘法、转置、逆矩阵、特征值分解、SVD
  - *为什么重要*：Attention 本质是矩阵运算；SVD 是 LoRA 低秩分解的理论基础

- **概率统计**
  - 贝叶斯定理、条件概率、高斯分布、最大似然估计（MLE）、KL 散度
  - *为什么重要*：KL 散度是 RLHF/DPO 的核心约束项；MLE 是预训练目标的数学本质

- **微积分**
  - 梯度、偏导数、链式法则
  - *为什么重要*：反向传播 = 链式法则的工程实现；理解梯度消失/爆炸必须懂这个

- **信息论**
  - 熵、交叉熵、互信息、KL 散度
  - *为什么重要*：交叉熵损失函数的理论来源；理解为什么用 softmax + cross-entropy

- **最优化理论**
  - 凸优化基础、拉格朗日乘子法、KKT 条件
  - *为什么重要*：SVM 的数学基础；理解约束优化问题（如 PPO 的 clip 约束）

> 💡 **面试拷问**
> - SVD 分解在 LoRA 中扮演什么角色？为什么 LoRA 不直接做 SVD？⭐
> - KL 散度不对称意味着什么？KL(P||Q) 和 KL(Q||P) 的区别在 RLHF 中有什么影响？⭐
> - 为什么 Cross-Entropy 能衡量模型输出和真实分布的差距？它和 KL 散度的关系？⭐
> - 梯度消失和梯度爆炸的根本原因是什么？在 Transformer 中是怎么解决的？
> - 为什么 Softmax + Cross-Entropy 是标配？能不能用其他组合？

---

## 1.2 机器学习核心

- **监督学习算法**
  - 线性回归、逻辑回归、SVM、决策树、随机森林、XGBoost、LightGBM
  - *面试场景*：结构化数据任务仍然是这些；理解 Boosting vs Bagging 的本质差异

- **无监督学习**
  - K-Means、PCA、t-SNE、UMAP、DBSCAN、GMM
  - *为什么重要*：t-SNE/UMAP 用于 Embedding 可视化；PCA 是降维的经典方案

- **损失函数** ⭐
  - MSE（回归）、Cross-Entropy（分类/LM）、Focal Loss（类别不平衡）、Hinge Loss（SVM）
  - *核心问题*：为什么语言模型用 Cross-Entropy 而不是 MSE？（概率分布 vs 数值预测）

- **优化器** ⭐
  - SGD → Momentum → Adam → AdamW → LAMB → Lion
  - *核心问题*：Adam 为什么比 SGD 好？AdamW 和 Adam 的区别是什么（权重衰减的正确位置）？
  - *面试高频*：LLM 训练为什么用 AdamW 而不是 Adam？

- **正则化**
  - L1（稀疏）/ L2（权重衰减）/ Dropout / Early Stopping / Weight Decay
  - *核心问题*：L1 为什么产生稀疏解？Dropout 的训练/推理行为差异？

- **偏差-方差权衡（Bias-Variance Tradeoff）** ⭐
  - *核心思想*：模型复杂度增加 → 偏差降低但方差升高；过拟合 = 高方差，欠拟合 = 高偏差
  - *延伸*：大模型时代这个权衡如何变化？（参数量足够大时规律改变）

- **评估指标**
  - Accuracy / Precision / Recall / F1 / AUC-ROC（分类）
  - mAP（目标检测）/ BLEU / ROUGE（文本生成）/ NDCG（排序）
  - *核心问题*：为什么不能只看 Accuracy？（类别不平衡场景）

> 💡 **面试拷问**
> - XGBoost 和 Random Forest 的本质区别是什么？为什么 XGBoost 通常更好？⭐
> - 为什么 Adam 容易过拟合？AdamW 是怎么解决的？⭐
> - SGD 为什么在某些场景下泛化性比 Adam 更好？（flat minima vs sharp minima）⭐
> - Dropout 在训练和推理时的行为差异？为什么推理时要乘以 (1-p)？
> - 大模型时代，偏差-方差权衡还成立吗？双下降（Double Descent）现象是什么？⭐
> - L1 正则化为什么能产生稀疏解？从几何角度和梯度角度分别解释？
> - BLEU 和 ROUGE 的区别是什么？为什么 LLM 评估很少用它们了？
> - 什么是过拟合的本质？参数量远大于数据量的 LLM 为什么没有严重过拟合？⭐

---

## 1.3 深度学习基础

- **激活函数** ⭐
  - ReLU → GELU → SiLU / Swish → Mish
  - *核心问题*：ReLU 的 dying neuron 问题是什么？GELU 为什么比 ReLU 在 Transformer 中表现更好？
  - *延伸*：SwiGLU = Swish + GLU，是现代 LLM FFN 的标配（LLaMA/DeepSeek 都用）

- **反向传播与计算图**
  - *核心思想*：前向传播建图，反向传播沿图求梯度（链式法则）
  - *面试高频*：手推一个简单网络的反向传播

- **CNN 核心概念**
  - 卷积（局部感受野 + 权重共享）、池化、ResNet（残差连接解决梯度消失）
  - BatchNorm（训练稳定性）、DepthwiseSeparable Conv（轻量化）
  - *为什么重要*：ViT 之前的视觉主干；理解残差连接对后续理解 Transformer 很重要

- **RNN / LSTM / GRU**
  - *核心思想*：序列建模，隐状态传递历史信息
  - *核心问题*：为什么 RNN 有梯度消失？LSTM 的门控机制如何解决？
  - *历史地位*：Transformer 出现前的序列建模标准；理解它才能理解 Transformer 的革命性

- **归一化方法** ⭐ 🔥
  - **BatchNorm**：对 batch 维度归一化，依赖 batch size，训练/推理行为不同
  - **LayerNorm**：对单个样本的特征维度归一化，不依赖 batch，适合变长序列 📝
  - **RMSNorm**：LayerNorm 的简化版，去掉均值中心化，只做 RMS 缩放，速度更快
  - **GroupNorm**：介于 BN 和 LN 之间，按通道分组归一化
  - **InstanceNorm**：对每个样本每个通道独立归一化，常用于风格迁移
  - *核心问题*：为什么 LLM 选 LayerNorm 而不是 BatchNorm？（变长序列 + 分布式训练）📝
  - *核心问题*：为什么 LLaMA 用 RMSNorm 而不是 LayerNorm？（计算效率，效果相当）⭐
  - *核心问题*：Pre-Norm vs Post-Norm，哪个训练更稳定？（Pre-Norm 梯度更稳定，现代 LLM 标配）⭐

- **训练技巧**
  - **学习率调度**：Warmup（防止初期不稳定）→ Cosine Annealing（平滑衰减）→ OneCycleLR
    - *核心问题*：为什么 LLM 训练必须有 Warmup？（初期参数随机，梯度方差大）
  - **梯度裁剪（Gradient Clipping）**：防止梯度爆炸，LLM 训练标配（通常 clip=1.0）
  - **混合精度训练（AMP）** ⭐：FP16/BF16 前向 + FP32 参数更新，节省显存同时保持精度
    - *核心问题*：FP16 vs BF16 的区别？（BF16 动态范围更大，不容易溢出，LLM 首选）
  - **梯度累积**：小 batch 模拟大 batch，解决显存不足问题
  - **权重初始化**：Xavier（tanh）/ Kaiming（ReLU）/ Zero Init（残差分支）

> 💡 **面试拷问**
> - Transformer 为何选择 LayerNorm？—— 从 BatchNorm 的缺陷到 LN 的必然性 📝 ⭐
> - RMSNorm 去掉了均值中心化，为什么效果没有变差？⭐
> - Transformer中什么是归一化，为什么要归一化？
> - Transformer 中 Pre-Norm 和 Post-Norm 是什么？ 
> - Pre-Norm 训练更稳定，但 Post-Norm 理论上上限更高，怎么理解这个矛盾？⭐
> - GELU 的数学形式是什么？为什么它比 ReLU 在 Transformer 中表现更好？⭐
> - SwiGLU 的 "Gate" 在做什么？为什么门控线性单元比普通 FFN 效果好？⭐
> - Dying ReLU 问题是什么？LeakyReLU/PReLU 是怎么解决的？为什么 LLM 不用？
> - 残差连接的数学本质是什么？没有残差连接深层 Transformer 能训练吗？⭐
> - Warmup 的学习率是线性增长还是指数增长？为什么线性 Warmup 就够了？
> - Cosine Annealing 为什么比 StepLR 效果好？直觉上怎么理解？
> - BF16 比 FP16 动态范围大但精度低，为什么 LLM 训练反而更好？⭐
> - 梯度累积和直接用大 batch 在数学上完全等价吗？有什么细微差别？
> - Xavier 和 Kaiming 初始化的推导思路分别是什么？为什么激活函数不同要换初始化？
> - 混合精度训练中的 Loss Scaling 是什么？为什么 FP16 训练必须要它？⭐
> - 梯度裁剪的 max_norm 设为多少合适？设太小会怎样？⭐
