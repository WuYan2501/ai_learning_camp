# Function Calling 和 ReAct 到底啥区别？—— 一场 Agent 技术面试实录

---

## 1. 这俩东西不是一回事？

**秋风**：小哈，你简历上写做过 Agent 项目，那我问你——Function Calling 和 ReAct，这俩有啥关系？

**小哈**：都可以让模型进行工具调用，但目的不一样

**秋风**：说的太笼统了，能具体说说吗。或者我换个问法——你觉得它们分别解决什么问题？

**小哈**：等等让我捋一下……Function Calling 是让模型输出结构化的 JSON，告诉我该调哪个函数、传什么参数。ReAct 目的是是让模型"先想再做"。

**秋风**：继续说，"先想再做"具体怎么理解？

**小哈**：ReAct 是 Reasoning + Acting，其实看英文大致就知道什么含义了，Reasoning是模型先输出一段思考内容来分析当前情况，然后再决定 Action。还有个重点，并不是简单的一次Reasoning + Acting，它会循环执行，中间还有个过程称为（Observation），直到最终问题解决结束。

**秋风**：ReAct说的不错，那说说Function Calling吧

**小哈**：Function Calling也是看明思意， 就是为了让模型能得到外部工具调用结果。例如询问天气，大模型返回格式化数据如下

**秋风**：那么它们之间有什么关系呢？

**小哈**：很明显，其实它两的核心并不一样，一个是结构化工具调用机制，一个则是推理+行动的决策框架。
所以它两其实是存在一定的协作关系的，在真实的 Agent 系统中，ReAct 负责思考和决策循环，而当 ReAct 在某一步决定"现在该调工具了"的时候，具体怎么调、参数怎么传、JSON 怎么组——靠的就是 Function Calling。打个比方：ReAct 是指挥官，Function Calling 是精锐士兵。指挥官下达命令，士兵精准执行。
![](https://files.mdnice.com/user/23907/783adebd-5db6-4389-ac46-55b5f9e62406.png)


---

## 2. 实际生产效果如何？

**秋风**：知道区别了，那实际业务上效果如何？

**小哈**：先说 Function Calling吧，效果好坏几乎完全取决于用的是什么模型。不过好在可控，通过链式提示词很容易掌控那些业务流程固定的业务

**秋风**：ReAct呢？

**小哈**：ReAct如果没用好，坑就比较多，我们遇到过：1. Token 消耗失控、2. 循环失控、3. 幻觉风险。导致实际使用时得加大量约束和校验，ReAct看起来厉害，实际使用真的得谨慎。

**秋风**：那在实际选型上，你们怎么决策的？

**小哈**：现在的原则是-**能用 Function Calling 解决的，绝不上 ReAct**。 Function Calling 快、省、确定性强，只有特别复杂的多步推理，灵活性非常高的业务场景，才用ReAct

---

## 3. 收尾：最近有什么新东西？

**秋风**：最后聊聊相关的最新进展吧。你说说你所了解的？

**小哈**：我知道Anthropic 搞了个 **PTC——Programmatic Tool Calling**（程序化工具调用），目的是让 Claude 在容器里用 Python 脚本之间将所有工具调完，避免了Tool Calling 每调一次工具，结果都要回传到模型上下文，节约上下文效果不错。

还有个 **Tool Search Tool**，工具库几千个的时候不用全塞进 Context，解决了"工具太多，Context 爆炸"的问题。

**秋风**：不错，基础扎实，经验也有，今天就到这儿。

**小哈**：谢谢秋风。

---

## 4. 总结

### 核心区别


![](https://files.mdnice.com/user/23907/b6a50836-9de6-4f5e-b46a-5eb75401cfa7.png)


### 选型原则

**一句话：能用 FC 解决的，绝不上 ReAct**


![](https://files.mdnice.com/user/23907/39be9a8e-f692-4596-a03f-945ce74cc58e.png)


### ReAct 踩坑清单

1. **Token 消耗失控**：每轮 Thought 都在烧钱，复杂任务轻松破万
2. **循环失控**：没设终止条件，模型能跑到天荒地老
3. **幻觉风险**：推理链越长，跑偏概率越高

### 最新进展（2025-2026）

- **PTC（Programmatic Tool Calling）**：Claude 在容器里用 Python 批量调工具，省 37% Token
- **Tool Search Tool**：工具库几千个不用全塞 Context，按需检索