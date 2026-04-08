---

一台MacBook，一个下午，我把Qwen3.5训练成了自己的AI分类员

---

"微调大模型"-SFT篇章

这篇文章就是我的完整实战记录，从0跑通、踩了一堆坑、最后成功训练**的全过程。

---

### 先说结论：为什么选Qwen3.5 + Mac？

**1. Qwen3.5-2B 是目前最适合本地微调的开源模型之一**

2B参数量，模型权重只有4.3GB。放在Mac或者个人Windows电脑基本都能尝试，不需要量化就能跑。Qwen3.5也是目前千问最新发布的一系列模型

**2. Apple Silicon的MPS加速，比CPU快5-10倍**

M系列芯片的GPU虽然比不上A100，但跑2B模型完全够用。实测每个训练step大约15秒，1个epoch跑完大约半小时。

**3. LoRA让"微调"变得平民化**

不需要训练全部参数。LoRA只训练不到1%的参数，显存占用低，电脑能扛得住。

> 一句话总结：**Qwen3.5-2B + LoRA + Mac MPS = 低门槛也能玩大模型微调。**

---

### 业务场景：微调解决什么问题？

业务场景是**POI（兴趣点）分类**——给一个地点名称，判断它属于什么类型。分类微调比较简单，数据有固定答案，用来上手操练非常合适

比如：
- "翡翠花园-3号楼" → **楼栋**
- "深圳宝创宝马4S店" → **4S店**
- "肯德基(北京南站店)" → **室内子**（火车站内部的子POI）
- "张记烧烤" → **其它**

当前做实验就用4个分类就行：**楼栋、4S店、室内子、其它**。

---

### 第一步：造数据——用规则给大模型当老师

构建训练大模型的模版，我才用的是系统提示词+用户输入+最后的输出为模型，部分代码如下

数据生成的核心逻辑：

```python
# 用规则引擎自动打标签，构造SFT训练样本
for poi in pois:
    category = classify_by_name(poi["name"])
    sample = {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"名称：{name}"},
            {"role": "assistant", "content": f"<answer>{category}</answer>"},
        ]
    }
```

输出格式用`<answer>`标签包裹，让模型的输出结构化，方便程序解析。

有个细节值是训练时绕不开的，数据要均衡，也就是**少数类的过采样**问题。比如一开始4S店在数据中只有9条，室内子142条，而"其它"有1300多条。如果直接训练，模型预测会严重偏向多数类。

解决办法其实很直观，将少量case的数据多补充一点就行，方式很多，我强烈推荐大模型来帮你构造数据。我的做法就是对少数类做了大模型采样，让大模型根据少量数据的特点自主生成，最后保证每个分类至少150条。

最终生成了**1638条训练数据 + 182条验证数据**。

---

### 第二步：环境搭建——坑比代码多

**坑1：Qwen3.5太新，老版本transformers不认识**

解决方案——必须用transformers的开发版：

```bash
python3 -m venv venv && source venv/bin/activate

# 开发版transformers（支持Qwen3.5）
pip install git+https://github.com/huggingface/transformers.git
pip install torch trl peft datasets accelerate
```

> 经验：**太新的模型往往不适合生产，新模型出来的头几个月，要用开发版的transformers。**

**坑2：国内下载HuggingFace模型卡死**

必须用镜像源，而且要禁用xet协议（它不走镜像）：

```python
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "0"
os.environ["HF_HUB_DISABLE_XET"] = "1"
```
---

### 第三步：Mac上的特殊处理

Mac的MPS有几个坑：

```python
# 坑1：不能用bfloat16，但可以用float16
bf16 = False
fp16 = True  # MPS支持fp16

# 坑2：不能用pin_memory
dataloader_pin_memory = False

# 坑3：显存管理——GPU和CPU共享内存
os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"
```

核心必懂训练参数如下：

| 参数 | 值 | 说明                       |
|------|------|--------------------------|
| 模型 | Qwen3.5-2B | 最新开源模型                   |
| LoRA r / alpha | 16 / 32 | 低秩适配参数，r越小训练越快、r越大拟合能力越强 |
| Batch Size | 2 × 8累积 | 等效batch=16               |
| 学习率 | 5e-5 | 偏保守，防过拟合                 |
| Epochs | 1 | 数据量不大，1轮足够               |
| 最大序列长度 | 256 | POI名称不长                  |
| 精度 | float16 | MPS兼容且高效                 |

---

### 第四步：开跑！

```bash
python3 train_poi_classifier.py
```

这套代码还包含评自动估，训练完成后会自动验证数据。

训练好后的模型，可以直接加载，也是交互式的方式，例如下面，输入POI名称，就按训练规格返回分类。
这种微调在业务中落地其实很合适，专注于某个场景，响应也非常快，也不需要每次都调整提示词等：

```bash
python3 inference_poi_classifier.py

📍 POI名称> 星巴克(首都机场T2店)
   ➡️  分类结果: 【室内子】

📍 POI名称> 万科城市花园-A栋
   ➡️  分类结果: 【楼栋】
```

---

### 整体架构

需要代码的话，留言关注获取，无广无推

```
├── poi_classifier_data_gen.py   # 数据生成（规则引擎 + SFT样本构造）
├── train_poi_classifier.py      # 训练 + 评估
├── inference_poi_classifier.py  # 交互式推理
├── data/
│   ├── *.csv                    # 原始业务数据
│   └── poi_classify/
│       ├── classify_train.json  # 训练集
│       └── classify_val.json    # 验证集
└── output/
    └── poi_classifier/
        └── final/               # LoRA adapter（训练产物）
```

---

### 写在最后

整个过程花了一个下午：环境搭建踩坑1小时，下载模型20分钟，训练挂着就行，调试半小时。总成本：**0元**。

这件事给我最大的感触是：**大模型微调的门槛，真的已经低到不可思议了。**

两年前，微调一个7B模型需要4张A100。一年前，QLoRA让单卡成为可能。现在，一台笔记本电脑就能跑通全流程。

如果你也有类似的分类、抽取、判断类业务需求，强烈建议试试：

> **小模型（2B-7B）+ LoRA + 领域数据 = 低成本、高精度的专属AI**

比调用API便宜，比写规则灵活，比训练大模型省钱。

---

**如果这篇文章对你有帮助，点个赞让更多人看到。有问题评论区见！**
