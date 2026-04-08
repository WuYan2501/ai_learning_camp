
---

## 1. 用案例说明和 ReAct 的区别

**秋风**：小哈，上次我们聊了 ReAct，今天接着问一个类似的ai技术问题——Plan-and-Execute。说说你对它的理解吧

**小哈**：我理解就事这个是先做计划再分步骤执行

**秋风**：说的太笼统了，这样，我们今天换种思路，全程用实战模拟来说清这个事如何？
具体场景就是订机票："帮我订一张下周三去上海的机票，要最便宜的"。
用 ReAct 和 Plan-and-Execute 分别会怎么处理？

**小哈**：好，我想想……

用 **ReAct** ，大致流程是这样的：
- 第一轮：Thought "需要查航班" → Action 调航班API → Observation 拿到航班列表
- 第二轮：Thought "要找最便宜的" → Action 比价 → Observation 找到最低价
- 第三轮：Thought "现在可以下单了" → Action 下单 → 完成

重点就是每一步都要让模型来 Thought ，也就是“边想边做”。

**秋风**：好，继续说

**小哈**：Plan-and-Execute 则会先一次性把整个计划先列出来，如下

```
Plan：
1. 查询下周三飞上海的所有航班
2. 按价格排序，筛选最便宜的
3. 确认航班信息，执行下单
```

这个重点就是把计划提前构思好，然后在执行，也就是“先想后做”

**秋风**：还可以，你来画个对比图说明一下吧

**小哈**：好的

![](https://files.mdnice.com/user/23907/0a0dba8a-3a59-4db1-9b04-debf340bf42e.png)

**小哈**：还有一个核心要点，“边想边做”想较于“先想后做”明显会更加节约token.


---

## 2. 核心架构

**秋风**：基本理解不错，我们深入一点聊聊 Plan-and-Execute 的核心架构。

**小哈**：Plan-and-Execute有三个核心组件，分别是**Planner**、**Executor**、**Replanner**。

还是那个例子来说明吧——"订下周三去上海最便宜的机票"：

**Planner（规划器）** 负责将任务拆分成计划：
```
输入：用户请求
输出：["查航班", "比价筛选", "下单"]
```

**Executor（执行器）** 负责执行：
```
执行 "查航班" → 调用航班API → 返回结果
执行 "比价筛选" → 排序比较 → 返回最低价航班
执行 "下单" → 调用订票API → 返回订单号
```

**秋风**：不错，逻辑很清晰，继续说说吧

**小哈**：**Replanner（重规划器）** 负责"中途纠偏"。

比如执行器执行到"下单"这步时，发现最便宜的机票卖完了，那怎么办呢？Replanner 就派上了用场，重新再出一个计划，例如

```
原计划：["查航班", "比价筛选", "下单"]
                              ↑ 失败！该批次机票卖完了

Replanner 调整后：
["查询备选航班", "重新比价", "下单"]
```

所谓“计划赶不上变化”说的就是这个问题，不过很明显 Plan-and-Execute 并没有我们想的这么死板
核心结构图如下

![](https://files.mdnice.com/user/23907/4360c8b4-1ab6-40d6-ab75-bd3a25e7ad8d.png)

---

## 3. 现场手撕

**秋风**：用代码把整个流程串起来吧，伪代码形式就行

**小哈**：没问题。我先实现一个核心循环框架：

```python
def plan_and_execute(user_request):
    # "订下周三去上海最便宜的机票"
    
    # Step 1: Planner 生成计划
    plan = planner.generate(user_request)
    # plan = ["查航班", "比价筛选", "下单"]
    
    results = []
    
    while plan:
        task = plan.pop(0)
        
        # Step 2: Executor 执行当前任务
        result = executor.run(task)
        results.append((task, result))
        
        # Step 3: Replanner 检查是否需要调整
        if result.failed:
            plan = replanner.adjust(
                goal=user_request,
                done=results,
                remaining=plan
            )
    
    return summarize(results)
```

**小哈**：实际执行过程说明如下

```python
# === 订机票完整执行过程 ===

user_request = "订下周三去上海最便宜的机票"

# -------- Planner 阶段 --------
plan = ["查航班", "比价筛选", "下单"]

# -------- Executor 阶段 --------
# 第一步
task_1 = "查航班"
result_1 = executor.run(task_1)
# ✅ 成功，返回: [MU5101 ¥580, CA1234 ¥620, FM9102 ¥550]

# 第二步  
task_2 = "比价筛选"
result_2 = executor.run(task_2)
# ✅ 成功，返回: FM9102 ¥550 是最便宜的

# 第三步
task_3 = "下单"
result_3 = executor.run(task_3)
# ❌ 失败！FM9102 航班已售罄

# -------- Replanner 介入 --------
# 输入：goal="订最便宜的机票", done=[查航班✅, 比价✅, 下单❌]
# 分析：最便宜的卖完了，需要换一个

new_plan = replanner.adjust(...)
# new_plan = ["选择次便宜航班MU5101", "重新下单"]

# -------- 继续执行调整后的计划 --------
task_4 = "选择次便宜航班MU5101"
result_4 = executor.run(task_4)  # ✅ 成功

task_5 = "重新下单"
result_5 = executor.run(task_5)  # ✅ 成功，订单号: ORD20260302

# -------- 最终输出 --------
# "已为您预订 MU5101 航班，票价 ¥580，订单号 ORD20260302"
```
---

## 4. 常见问题

**秋风**：Plan-and-Execute 实际使用时有遇到什么问题吗？

**小哈**：有，我总结了几个常见问题：

### 问题一：Plan的计划粒度把握不好

一种是拆太粗，执行器不知道具体干啥：
```
❌ 计划：["处理机票"]  // 太模糊
```

一种则是拆太细，计划列表太长，上下文可能丢失：
```
❌ 计划：["打开浏览器", "输入网址", "点击搜索框", "输入出发地"...]  // 太碎
```

> 想将计划粒度拆好，也不是一件容易的事，避免文章太长影响观看，此处就不展开了，如有兴趣，则留言：**Plan-and-Execute 拆分粒度**，我会专门出一期分析，关注我AI方向不迷路

### 问题二：Replanner 越补越乱

这说的就是，如果执行器在某一步失败了，Replanner 可能会生成一堆补救步骤，重复执行后依旧错误，再次生成补救步骤……这就形成了死循环。

解决办法也很简单：**设置重试次数**，超过就降级处理，伪代码如下
```python
MAX_REPLAN_TIMES = 3
if replan_count > MAX_REPLAN_TIMES:
    return "无法完成，请人工处理"
```

### 问题三：规划阶段耗时过长

复杂任务的计划可能很长，Planner 推理时间久，用户等得不耐烦。

解决办法：**先返回计划，让用户知道在干嘛**，或者流式输出计划步骤。

**秋风**：总结三个问题就是粒度适中、重试有限、反馈及时。

**小哈**：对，总结得比我好。

**秋风**：不错，今天就到这儿。

**小哈**：谢谢秋风。

---

## 5. 总结


![](https://files.mdnice.com/user/23907/0d10fba3-5b64-4a49-8edd-fe9b95a5cc79.png)

![](https://files.mdnice.com/user/23907/046d384d-5094-481b-b199-167f3d48ce91.png)
