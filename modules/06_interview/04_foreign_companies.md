# 6.4 外企 / 海外厂公开面经整理

> 外企 / 海外厂的公开中文面经相对分散，很多内容会混着 `面经 / 题单 / 攻略 / 英文经验帖` 一起出现
>
> 所以这页更适合你把握：**这些公司更看重哪类问题、表达方式和思考方式有什么区别**
>
> 返回 [面试区索引](/modules/06_interview) | [高频题库总表](01_high_frequency_question_bank.md) | [知识库索引](/SYLLABUS)

---

## 🌍 外企常见共同点

- **英文表达要更清晰**：结论先行，别绕
- **更看重指标量化**：最好能说清楚 `latency / cost / quality / impact`
- **ML + System Design + Behavioral** 往往会混着考
- **论文 / 实验设计** 比纯八股更常见

---

## 4.1 Microsoft

### 公开面经线索

| 线索 | 平台 | 备注 |
|------|------|------|
| `微软上海C+AI 产品面经` | 牛客 | C+AI 方向比较明确 |
| `上海微软实习C+AI面经` | 牛客 | 实习流程 |
| `微软C+AI一二三面面经` | 牛客 | 多轮复盘 |
| `微软上海C+AI暑实面经` | 牛客 | 偏实习与产品结合 |

### 高频知识点

`AI 产品系统设计` `实验设计` `英文表达` `指标量化`

### 代表题目

| 题目 | 更像在考什么 | 对应通用题库 |
|------|--------------|--------------|
| Design an AI copilot for enterprise users. What metrics will you track? | 系统设计 + 指标体系 | `#170` `#182` |
| Why is final-answer accuracy not enough for evaluating an agent? | 过程评测思维 | `#130` `#170` |
| Tell me about an AI feature you shipped and what trade-off you made. | 行为面 + 技术取舍 | `#176` `#182` |

---

## 4.2 Google

### 公开面经线索

| 线索 | 平台 | 备注 |
|------|------|------|
| `Google人工智能面试·真·题(附参考答案+攻略)` | 公开文章 | 更像题单整理 |
| `研究型AI面经 | 来自一位Reddit网友谷歌面试经验分享` | CSDN | 偏研究型视角 |

### 高频知识点

`基础 ML / DL` `实验设计` `研究思维` `论文理解` `推理链条`

### 代表题目

| 题目 | 更像在考什么 | 对应通用题库 |
|------|--------------|--------------|
| If a model looks strong offline but weak online, how will you debug it? | 实验设计与因果拆解 | `#93` `#170` |
| Why might larger models fail to keep scaling in practice? | Scaling Law 的边界 | `#67` `#68` |
| Compare long-context prompting with retrieval-based systems. | 对比与取舍能力 | `#95` `#96` |

---

## 4.3 Amazon

### 公开面经线索

| 线索 | 平台 | 备注 |
|------|------|------|
| `这份AI算法岗面经很干货:亚马逊分享实战经验` | 公开文章 | 更偏经验整理 |
| `这份AI算法岗面经很干货:亚马逊工程师分享实战经验` | 腾讯云 / 澎湃系公开文章 | 侧重岗位经验 |
| `Day One Careers | 亚马逊面试备考与AI辅导` | 公开站点 | 偏流程与准备建议 |

### 高频知识点

`ML 系统设计` `领导力故事` `成本意识` `用户体验和 SLA`

### 代表题目

| 题目 | 更像在考什么 | 对应通用题库 |
|------|--------------|--------------|
| Design a scalable LLM-powered support system for millions of users. | 大规模系统设计 | `#175` `#182` |
| How would you reduce serving cost without hurting user experience too much? | 成本与体验平衡 | `#151` `#176` |
| Tell me about a time your ML/AI approach failed and what you changed. | 行为面 + 复盘 | `#93` `#133` |

---

## 4.4 Meta

### 公开面经线索

| 线索 | 平台 | 备注 |
|------|------|------|
| `转码选手的寻找暑期实习之路(2)-MetaAPP AI面试` | 牛客 | 更接近真实流程帖 |
| `Meta允许编程面试使用AI助手` | 公开新闻 / 讨论 | 说明工具使用话题已经进入流程讨论 |
| `面试Meta可以用AI了` | 公开文章 | 更偏制度与趋势 |

### 高频知识点

`Coding + AI 工具协作` `系统设计` `安全边界` `效率与正确性`

### 代表题目

| 题目 | 更像在考什么 | 对应通用题库 |
|------|--------------|--------------|
| If coding interviews allow AI tools, what new risks appear? | 工具依赖、正确性、安全 | `#136` `#134` |
| How would you evaluate an AI coding assistant beyond pass rate? | 过程评测、回归集、修复质量 | `#132` `#170` |
| When should a coding agent ask for human confirmation? | 权限和不可逆操作 | `#130` `#134` |

---

## ✍️ 外企准备建议

- **准备英文版一页总结**：项目背景、目标、指标、trade-off、结果
- **把“为什么这样设计”讲清楚**：不是只讲“我用了什么”
- **多练口语版系统设计**：尤其是 LLM 服务、RAG、Agent、评测
