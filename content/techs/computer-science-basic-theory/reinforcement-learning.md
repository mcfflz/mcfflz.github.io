---
date: 2026-02-12T12:00:00+08:00
title: Reinforcement Learning
draft: false
# bookFlatSection: false        # 是否显示扁平章节（默认false）
# bookToc: true                 # 是否显示目录（默认true）
# bookHidden: false             # 是否在侧边栏列表中隐藏（默认false）
# bookCollapseSection: false    # 章节是否默认折叠（默认false）
# bookComments: false           # 是否启用评论（默认false）
# bookSearchExclude: false      # 是否从搜索结果中排除（默认false）
params:                       # 自定义参数
  maths: true                 # 数学公式支持
weight: 113                   # 内容权重（排序用）
---

# 强化学习 Reinforcement Learning

## 参考资料

Reinforcement Learning 2ed, Richard S. Sutton and Andrew G. Barto.pdf

Reinforcement Learning 2ed, 中文翻译.pdf


## 概述

强化学习（reinforcement learning，RL）讨论的问题是智能体（agent）怎么在复杂、不确定的环境（environment）下最大化它能获得的奖励。其核心思想非常直观：​​“通过试错来学习”​，就像训练宠物或教小孩走路一样。

在开始强化学习之前，首先对比强化学习和机器学习、深度学习的区别：
1. 机器学习主要基于统计学的方法，解决常规预测问题，例如明天的天气、下个月的销售额、明年的房价走势等。机器学习的常规方法是采集相关数据，组合不同的特征进行函数拟合。
2. 机器学习和深度学习的分界点，主要在于对神经网络模型的应用。在机器学习中，神经网络模型是一种特殊的模型，Google 研究员证明了，只需要足够的模型参数量，便可以在数据区间内拟合任意函数，而无需关注特征组合。
深度学习主要应用在视觉模型、语言模型、音频模型等复杂人工智能模型，解决计算机视觉和图像生成、自然语言理解和文本生成、音频解析和音频合成等复杂问题。在这个阶段，尤其是当 Transformer 架构出现后，模型训练很大程度上从模型架构问题变成了数据问题，只要有足够的高质量数据，便可以训练出良好的模型。
但是，在这个阶段，有监督学习的目标是拟合目标数据，基于高质量数据的深度学习结果依然存在瓶颈，即数据质量，人工标注的数据质量成为模型的上限。
3. 强化学习和深度学习没有明确的分界点，强化学习更像是训练神经网络的一种方法，但是由于其体系的特殊性，需要单独讨论。
强化学习提出了一种新的学习范式，将要求解的问题空间抽象为环境，定义状态空间、行为空间、状态转移函数、奖励函数等环境属性，将问题的解抽象为要训练的模型（或智能体），通过模型（或智能体）和环境的不断交互来训练模型。在此可以看出，强化学习要求模型能够主动探索和试错，这是深度学习过程所不具备的特性，由此可以突破数据质量的限制。

强化学习与监督学习​（有标签数据）和无监督学习​（无标签数据）并列，构成了机器学习的三大范式。


## 基础概念

Environment: 环境，代表所要求解的问题所面临的复杂的、不确定的特性。

Agent: 智能体，代表在环境中，能够与环境交互，通过不断试错来构建最优策略的主体。

State: 状态，代表环境当前的信息，用 $s$ 表示。

State space: 状态空间，代表环境可能存在状态集合，用 $S$ 表示。
在下文中，我们首先假设状态空间是有限的、离散的，即： $S = \{ s \}$ 。

Observation: 观测，代表 Agent 能够观测到的环境信息，用 $o$ 表示。
观测和状态的区别是：状态是对环境的完整描述，不会隐藏环境的信息。而观测是对状态的部分描述，可能会遗漏一些信息。
在下文中，我们假设环境是全部可观测的，即： $o = s$ 。

Observation space: 观测空间，代表观测可能存在的状态集合，用 $O$ 表示。
我们已经假设环境是全部可观测的，因此有 $O = S$ 。

Action space: 行为空间，代表环境在状态 $s$ 时 Agent 可以选择的行为，用 $A(s)$ 表示。Agent 的一切行为都发生在环境中，受到环境的约束。
在下文中，我们假设行为空间是有限的、离散的，即： $A(s) = \{ a \}$ 。

Action: 行为，代表 Agent 与环境的交互，用 $a$ 表示，行为会导致环境状态的改变。

Policy: 策略，代表 Agent 的行为策略。当 Agent 观测到 $o$ 时，在环境允许的行为空间 $A(s)$ 内选择行为 $a$ 的策略，用 $\pi$ 表示。
我们使用概率分布 $\pi(\cdots | s)$ 表示策略，代表在状态 $s$ 时选择的行为存在随机性。
如果策略是确定的，那么概率为 1，即 $\pi(a | s) = 1$ ，选择的行为是 $a$ 。

State transition: 环境状态转移，代表 Agent 选择行为后导致环境状态的变化，用 $s \overset\{ a \}{\longrightarrow} s'$ 表示。
我们使用概率分布 $p_s(\cdots | s, a)$ 表示环境状态转移，代表 Agent 在状态 $s$ 采取行为 $a$ 后，环境状态转移存在随机性。
如果环境状态转移是确定的，那么概率为 1，即 $p_s(s' | s, a) = 1$ ，所转移到的状态是 $s'$。

Reward: 奖励，代表 Agent 采取行为后，环境给予的奖励（或惩罚），用 $r$ 表示。
我们使用概率分布 $p_r(\cdots | s, a)$ 表示奖励，代表 Agent 在状态 $s$ 采取行为 $a$ 后，环境给予的奖励存在随机性。
如果奖励是确定的，那么概率为 1，即 $p_r(r | s, a) = 1$ ，所获取到的奖励是 $r$ 。

Trajectory: 轨迹，代表 Agent 和环境的交互从开始到结束的 State 和 Action 的记录，用 $\tau$ 表示。轨迹是时间序列数据，例如 ${S_0, A_1, S_1, A_2, S_2, \cdots}$ 。

Episode: 回合，代表具有最终状态（terminal state），有限步数的 trajectory。

Return: 回报，代表 Agent 和环境的交互从开始到结束所获得奖励的累计，用 $G$ 表示，有 $G = \sum_t R_t$ ，其中 $R_t$ 是时间序列数据。

Discount factor: 折扣因子 $\gamma$ ，我们希望在尽可能短的时间里面得到尽可能多的奖励，因此使用折扣因子来衡量未来奖励在当前时刻的价值。
按照金融业折现的方式理解。

Discounted Return: 折扣回报，使用折扣因子计算的回报，有 $G = R_1 + \gamma R_2 + \gamma^2 R_3 + \cdots$ 。
在下文中，我们使用折扣回报。
如果 $\gamma$ 接近于 0，那么未来获得的回报对于当前步骤来说价值会很小，策略会更加偏向于获取当前步骤的回报。
如果 $\gamma$ 接近于 1，那么未来获得的回报对于当前步骤来说价值会很大，策略会更加偏向于获取未来步骤的回报。


## 目标

强化学习的目标是：在给定的环境下，找到最优策略 policy，能够让 Agent 获得到最大的回报。

使用数学方式可以表述为：

在给定的环境下：

* 状态空间 State space: $S = \{ s \}$ 
* 行为空间 Action space: $A(s) = \{ a \}$ 
* 状态转移概率分布 State transition probability: $p_s(s' | s, a)$ 
* 奖励概率分布 Reward probability: $p_r(r | s, a)$ 

找到最优策略 policy：

* 策略概率分布 Policy: $\pi(a | s)$ 

能够让 Agent 获取到最大的回报：

* 期望回报 Expected return: $\mathbb{E}(R_1 + \gamma R_2 + \gamma^2 R_3 + \cdots)$ 


我们首先讨论环境信息已知的情况（有模型 model-base）。
在更复杂的情况下，环境信息是未知的（免模型 model-free），需要智能体通过探索来发现。探索需要时间，由此进一步收集数据同步改进策略（on-policy）和收集数据再改进策略（off-policy）。


## 关于奖励概率分布的说明

奖励的概率分布准确的描述是 $p_r(r | s, a, s')$ 。

奖励最根本的定义是，智能体在状态 $s$ 采取行为 $a$ 后，环境会转换到下一个状态 $s'$ ，​并且在此过程中产生一个奖励 $r$ 。奖励 $r$ 是一个随机变量，其分布取决于整个转换过程，即 $s$, $a$, 和 $s'$ 。

也可以使用联合分布写为 $p_r(s', r | s, a) = P_r(S_{t+1} = s', R_{t+1} = r | S_t = s, A_t = a)$ ，这个联合分布同时捕捉了状态转移和奖励发放的所有信息。

在很多理论中，为了简化分析，我们可以定义一个期望奖励函数​ $p_r(r | s, a)$ ，它是关于 $s$ 和 $a$ 的函数，在状态 $s$ 下执行动作 $a$ 后，所能获得的即时奖励的期望值 $\bar{r}$ ，这有助于化简公式。


## 马尔可夫过程 MP, Markov process

马尔可夫性质 Markov property: 
一个随机过程在给定当前状态及所有过去状态情况下，其未来状态的条件概率分布仅依赖于当前状态。也可以描述为，给定当前状态时，将来的状态与过去状态是条件独立的。
通俗来讲，在已知“现在”的条件下，“未来”与“过去”是相互独立的。


离散时间马尔可夫过程 Discrete-Time Markov process: 
对于一个索引集为离散时间 $T$ ，状态空间为 $S$ 的随机过程 $\{ X_t \}, t \in T$ ，它的任意随机变量序列 $X_0, X_1, \cdots, X_t$，其中下一个时刻的状态 $X_{t+1}$ 只取决于当前状态 $X_t$ ，我们就称这个随机过程为马尔可夫过程。
其数学表示为： $p(X_{t+1} | X_{t}) = p(X_{t+1} | X_{0}, X_{1}, \cdots, X_{t}), \forall t \in T$ 。
离散时间的马尔可夫过程也被称为马尔科夫链 Markov Chain，是最简单的马尔可夫过程。
在下文中，我们使用离散时间的马尔可夫过程，不讨论连续时间的马尔可夫过程。


我们假设环境具有马尔可夫性质，即：
* 状态转移概率分布具有马尔可夫性质： $p_s(s_{t+1} | s_0, a_1, \dots, s_t, a_{t+1}) = p_s(s_{t+1} | s_t, a_{t+1}), \forall t \in T$ 
* 奖励概率分布具有马尔可夫性质： $p_r(r_{t+1} | s_0, a_1, \dots, s_t, a_{t+1}) = p_r(r_{t+1} | s_t, a_{t+1}), \forall t \in T$ 

我们假设在 Agent 与环境的交互过程中，环境仅是根据当前信息和 Agent 的动作来给予反馈，和历史信息无关。
可以换一种方式理解，所有的历史信息都可以反映在环境的当前信息中。


# 状态价值 State value

我们的目标是在给定的外部环境下求解最优策略 $\pi$ ，我们通过回报 Return 来评价一个策略是“好”还是“坏”。
因此我们需要想办法衡量在给定初始状态 $s$ 下，policy $\pi$ 能够获得最大的回报 $G$ ，这就是 state value 。虽然我更希望能将它称为 policy value 。

根据基础概念，我们将一个单步的状态转移 State transition 及奖励 Reward 可以用如下方式来表示：

$$
S_t \overset{A_t}{\longrightarrow} R_{t+1}, S_{t+1}
$$

其中：

* $t, t+1$： 离散时间
* $S_t$： 环境在 $t$ 时刻的状态
* $A_t$： Agent 在观测到环境在 $t$ 时刻的状态 $S_t$ 后所采取的行为
* $R_{t+1}$： Agent 采取的行为 $A_t$ 后，环境给予的奖励
* $S_{t+1}$： Agent 采取的行为 $A_t$ 后，环境状态变更后的状态
* Agent 的 Action 遵循行为概率分布 $\pi(A_t = a | S_t = s)$ 
* Agent 获得的 Reward 遵循奖励概率分布 $p_r(R_{t+1} = r | S_t = s, A_t = a)$ 
* Environment 的 State transition 遵循状态转移概率分布 $p_s(S_{t+1} = s' | S_t = s, A_t = a)$ 

在这里需要特别注意数学符号：

$S$ 是状态空间， $\{ s \}$ 是状态空间内离散的状态， $S_t$ 是状态空间在离散时间 $t$ 的时间序列数据
$A$ 是行为空间， $\{ a \}$ 是行为空间内离散的状态， $A_t$ 是行为空间在离散时间 $t$ 的时间序列数据
$R$ 是奖励变量， $\{ r \}$ 是奖励值， $R_t$ 是奖励变量在离散时间 $t$ 的时间序列数据


将上述单步过程推广到一个 trajectory ，可以用如下方式来表示：

$$
S_t \overset{A_t}{\longrightarrow} R_{t+1}, S_{t+1} \overset{A_{t+1}}{\longrightarrow} R_{t+2}, S_{t+2} \overset{A_{t+2}}{\longrightarrow} R_{t+3}, S_{t+3}, \dots
$$

求 discounted return 有：

$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+2} + \dots
$$


有了上述的基础表示，我们可以定义状态价值 State value，也可以称为状态价值函数 state value function：

$$
v_{\pi}(s) = \mathbb{E}_{\pi}[G_t | S_t = s]
$$

即：状态价值 state value 是在给定策略 $\pi$ 和初始状态 $S_t = s$ 的情况下，期望获得的折扣回报 $\mathbb{E}_{\pi} [G_t | S_t = s]$ 。
我们的目标，是求解最大化 state value 的 $\pi$ 。

对这个函数需要有如下说明：

* 对于不同的初始状态 $s$ ，状态价值函数是不同的
* 对于不同的策略 $\pi$ ，状态价值函数是不同的


state value 能够衡量策略的“好坏”。
在给定初始状态 $s$ 的情况下，state value 可以表示哪一种策略 $\pi$ 可以得到更多的 return 。

state value 能够衡量状态的价值。
在给定策略 $\pi$ 的情况下，state value 可以表示从哪一种状态 $s$ 出发可以得到更多的 return 。

直观的解释：
state value 可以衡量在相同的策略下，哪一点出发更有优势。
state value 可以衡量在不同的策略下，哪一种策略更有优势。


State value 和 return 的区别在于，return 是单个 trajectory 的回报，而 state value 是执行多个 trajectory 所期望获得的回报。
如果从一个状态 $s$ 出发只有一条确定的 trajectory ，那么此时的 state value 和 return 就是相同的


# 贝尔曼公式 Bellman equation

## 公式推导

有了 state value ，还需要进一步的分析推导来求解。公式推导如下：

对于一个 discounted return 有：

$$
\begin{align}
G_t
& = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+2} + \dots \\
& = R_{t+1} + \gamma G_{t+1}
\end{align}
$$

那么对于 state value 有：

$$
\begin{align}
v_{\pi}(s)
& = \mathbb{E}[G_t | S_t = s] \\
& = \mathbb{E}[R_{t+1} + \gamma G_{t+1} | S_t = s] \\
& = \mathbb{E}[R_{t+1} | S_t = s] + \gamma \mathbb{E}[G_{t+1} | S_t = s] \\
\end{align}
$$

这一步可以理解为： state value 由两个部分组成：

* 第一部分： $\mathbb{E}[R_{t+1} | S_t = s]$ ，初始状态 $S_t = s$ 时，策略 $\pi$ 能够获得的即时奖励 $R_{t+1}$ 的期望
* 第二部分： $\gamma \mathbb{E}[G_{t+1} | S_t = s]$ ，初始状态 $S_t = s$ 时，策略 $\pi$ 能够获得的未来回报 $G_{t+1}$ 的折扣期望


分别分析两个部分：

第一部分：即时奖励

$$
\begin{align}
\mathbb{E}[R_{t+1} | S_t = s] 
& = \sum_a \pi(a | s) \mathbb{E}[R_{t+1} | S_t = s, A_t = a] \\
& = \sum_{a} \pi(a | s) \left( \sum_r p_r(r | s, a) \cdot r \right) \\
\end{align}
$$

解释说明：

* 状态为 $S_t = s$ 时所采取的行动概率分布是 $\pi(a | s)$ 
* 状态为 $S_t = s$ 且行动为 $A_t = a$ 时的奖励概率分布 $p_r(r | s, a) r$ 
* 状态为 $S_t = s$ 期望获得的奖励 $\mathbb{E}[R_{t+1} | S_t = s]$ 即为：状态为 $S_t = s$ 时所能采取的所有行动，对应能够获得的奖励的期望求和。
* 数学上的解释为应用全期望定律：对于两个离散的随机变量 $X, Y$ ，有 $E(X) = E(E(X | Y)) = \sum_y E(X | Y = y) \cdot p(Y = y)$ ，令 $X = R_{t+1}, Y = A_t$ ，且每一个概率和期望都额外条件于 $S_t = s$ ，代入公式即可求解。
* 更进一步的，可以理解为“条件版”的全期望定律：对于三个离散的随机变量 $X, Y, Z$ ，有 $E(X | Z = z) = E(E(X | Y, Z = z)) = \sum_y E(X | Y = y, Z = z) \cdot p(Y = y | Z = z)$ ，也就是在给定条件 $Z = z$ 嵌入在所有的条件概率中，全期望定律依然成立。


第二部分：未来回报

$$
\begin{align}
\mathbb{E}[G_{t+1} | S_t = s]
& = \sum_{s'} \mathbb{E}[G_{t+1} | S_{t+1} = s', S_t = s] p(s' | s) \\
& = \sum_{s'} \mathbb{E}[G_{t+1} | S_{t+1} = s'] p(s' | s) \\
& = \sum_{s'} v_{\pi}(s') p(s' | s) \\
& = \sum_{s'} v_{\pi}(s') \left ( \sum_a \pi(a | s) p_s(s' | s, a) \right ) \\
\end{align}
$$

说明：

* 为了计算状态 $s$ 的未来回报期望，我们需要考虑所有未来状态 $s'$ 下的回报
* 为此，我们需要考虑从 $s$ 出发，​所有可能到达的下一状态 $s'$ 的概率 $p(s' | s)$ 
* 根据 state value 的马尔可夫性质，“未来只依赖于初始状态，而与过去的历史无关”。我们知道了下一状态 $S_{t+1} = s$ ，那么从这一刻开始的所有未来回报 $G_{t+1}$ 的期望值，就只与这个新的状态 $s'$ 有关，而与 $s$ 无关。
* 展开状态转移概率 $p(s'|s)$ ，是状态 $s$ 下执行 Action 的策略 $\pi(a | s)$ 和状态转移概率 $p_s(s' | s, a)$ 
* 数学上的解释为应用全期望定律，在此不做展开。


因此，总结上述内容，这就是贝尔曼公式，的表达式为：
贝尔曼公式描述了不同 Environment State 的 state value 。

$$
\begin{align}
v_{\pi}(s)
& = \mathbb{E}[G_t | S_t = s] \\
& = \mathbb{E}[R_{t+1} | S_t = s] + \gamma \mathbb{E}[G_{t+1} | S_t = s] \\
& = \sum_a \pi(a | s) \left ( \sum_r p_r(r | s, a) r \right ) + \gamma \sum_{s'} v_{\pi}(s') \left ( \sum_a p_s(s' | s, a) \pi(a | s) \right ) \\
& = \sum_a \pi(a | s) \left [ \sum_r p_r(r | s, a) r + \gamma \sum_{s'} v_{\pi}(s') p_s(s' | s, a) \right ], \forall s \in S \\
\end{align}
$$

说明：

* 这里改变求和顺序具有一定的前提条件：求和符号 $\sum_{s'}$ 和 $\sum_a$ 作用于不同的变量，是独立的求和操作，且在实际强化学习问题中，状态空间和行为空间通常是有限的（或求和绝对收敛），因此我们可以交换求和顺序而不改变结果。
* 可以简单理解为求和交换律。
* 对于任意的 $s$ ，具有贝尔曼公式成立，因此可以求解 $v_{\pi}(s)$ 。
* 贝尔曼公式可以有另一种推导方式，即 $v_{\pi}(s) = \sum_a \pi(a | s) \left [ \mathbb{E}(G_t | S_t = s, A_t = a) \right ]$ ，由此继续推导。


贝尔曼公式的强大之处在于，它将一个复杂的大问题（从初始状态出发的长期回报）分解为立即的一步和后续的所有步骤这两个部分，是强化学习中“长远思考”的数学表述，为我们提供了一种递归地思考“价值”的方式。


## 矩阵-向量表示

由于贝尔曼公式对状态空间 $S$ 内的任意状态 $s$ 都有效，因此我们可以联立方程，建立贝尔曼公式的矩阵-向量表示。

首先对公式进行调整：

令：

* $r_{\pi}(s) = \sum_a \pi(a | s) \sum_r p_r(r | s, a) r$ 代表即时奖励期望
* $p_{\pi}(s' | s) = \sum_a \pi(a | s) p_s(s' | s, a)$ 代表状态转移概率矩阵

因此有：

$$
\begin{align}
v_{\pi}(s)
& = \sum_a \pi(a | s) \left ( \sum_r p_r(r | s, a) r \right ) + \gamma \sum_{s'} v_{\pi}(s') \left ( \sum_a p_s(s' | s, a) \pi(a | s) \right ) \\
& = r_{\pi}(s) + \gamma \sum_{s'} p_{\pi}(s' | s) v_{\pi}(s') \\
\end{align}
$$

假设：

* 状态空间 $S$ 中的状态可以表示为 $s_i (i = 1, 2, \dots, n)$ 

那么，对于任意状态 $s_i$ ，贝尔曼公式可以写为：

$$
v_{\pi}(s_i) = r_{\pi}(s_i) + \gamma \sum_{s_j} p_{\pi}(s_j | s_i) v_{\pi}(s_j)
$$

更进一步的，令：

* state value 的向量表示为 $v_{\pi} = \left [ v_{\pi}(s_1), v_{\pi}(s_2), \dots, v_{\pi}(s_n) \right ]^T, v_{\pi} \in \mathbb{R}^n$ 
* 即时奖励期望的向量表示为 $r_{\pi} = \left [ r_{\pi}(s_1), r_{\pi}(s_2), \dots, r_{\pi}(s_n) \right ]^T, r_{\pi} \in \mathbb{R}^n$ 
* 状态转移概率的矩阵表示为 $[P_{\pi}]_{ij} = \left [ p_{\pi}(s_j | s_i) \right ], P_{\pi} \in \mathbb{R}^{n \times n}$ 

因此贝尔曼公式的矩阵-向量形式可以表示为：

$$
v_{\pi} = r_{\pi} + \gamma P_{\pi} v_{\pi}
$$

使用代数形式表示会更容易理解：

$$
\begin{bmatrix}
v_{\pi}(s_1) \\
v_{\pi}(s_2) \\
\dots \\
v_{\pi}(s_n)
\end{bmatrix}

= 

\begin{bmatrix}
r_{\pi}(s_1) \\
r_{\pi}(s_2) \\
\dots \\
r_{\pi}(s_n)
\end{bmatrix}

+ 

\gamma 

\begin{bmatrix}
p_{\pi}(s_1 | s_1) & p_{\pi}(s_2 | s_1) & \dots & p_{\pi}(s_n | s_1) \\
p_{\pi}(s_1 | s_2) & p_{\pi}(s_2 | s_2) & \dots & p_{\pi}(s_n | s_2) \\
\vdots \\
p_{\pi}(s_1 | s_n) & p_{\pi}(s_2 | s_n) & \dots & p_{\pi}(s_n | s_n) \\
\end{bmatrix}

\cdot

\begin{bmatrix}
v_{\pi}(s_1) \\
v_{\pi}(s_2) \\
\dots \\
v_{\pi}(s_n)
\end{bmatrix}
$$


## 方程求解

贝尔曼方程的求解方式有两种：

第一种，求逆：

已知 $v_{\pi} = r_{\pi} + \gamma P_{\pi} v_{\pi}$ ，则 $v_{\pi} = (I - \gamma P_{\pi})^{-1} r_{\pi}$
这种方式最简单，但矩阵求逆的计算复杂度为 $O(n^3)$，当矩阵的维度较高时会难以求解。


第二种，值迭代 Value iteration ：

设置初始向量 $v_k$ （设为 0 或随机值） ，令 $v_{k+1} = r_{\pi} + \gamma P_{\pi} v_k$ ，当 $k$ 趋近于无穷时，$v_k$ 会收敛到 $v_{\pi}$ 。具体证明过程参考 赵世钰 视频介绍。


贝尔曼方程是 state value 的分析推导，求解出的 $v_{\pi}(s)$ 是在给定策略 $\pi$ 和初始状态 $s$ 时最能获得最大回报的折扣期望 discounted return ，有了贝尔曼方程的解，我们就可以衡量不同策略的“好坏”。
那么下一步的问题是如何找到最优策略？


## 动作价值 Action value

我们在此引入动作价值 action value 的概念。

已知状态价值 state value 是在给定策略 $\pi$ 和初始状态 $S_t = s$ 的情况下，期望获得的折扣回报 $v_{\pi}(s) = \mathbb{E}_{\pi} [G_t | S_t = s]$ 

令：动作价值 action value 是在给定策略 $\pi$ 和初始状态 $S_t = s$ 的情况下，采取动作 $A_t = a$ 时，期望获得的折扣回报 $q_{\pi}(s, a) = \mathbb{E}_{\pi}[G_t | S_t = s, A_t = a]$ 

因此有：

$$
\begin{align}
v_{\pi}(s)
& = \mathbb{E}[G_t | S_t = s] \\
& = \sum_a \pi(s, a) \mathbb{E}[G_t | S_t = s, A_t = a]\\
& = \sum_a \pi(a | s) q_{\pi}(s, a)
\end{align}
$$

由此可以看出，状态价值 state value 和动作价值 action value 是一体两面的，在给定的策略 $\pi$ 下，可以在知道任意一个值的情况下，求解出另外一个值。

此外，根据贝尔曼方程，我们也可以得到动作价值 action value 的另一种表达形式：

$$
q_{\pi}(s, a) = \sum_r p_r(r | s, a) r + \gamma \sum_{s'} p_s(s' | s, a) v_{\pi}(s')
$$


# 贝尔曼最优方程 Bellman optimality equation, BOE

## 最优策略 optimal policy 

首先，我们定义最优策略的概念：

对于两个策略 $\pi_1$ 和 $\pi_2$ ，如果有 $v_{\pi_1}(s) \ge v_{\pi_2}(s), \forall s \in S$ ，那么我们可以说 $\pi_1$ 的策略要优于 $\pi_2$ 。

更进一步的，如果一个策略 $\pi^*$ 有 $v_{\pi^*}(s) \ge v_{\pi}(s), \forall s \in S, \forall \pi$ ，那么我们可以说 $\pi^*$ 是最优策略。

最优策略也可以表达为 $v_{\pi^*}(s) = \max_{\pi} v_{\pi}(s), \pi^* = \arg \max_{\pi} v_{\pi}(s)$ 。
可以理解为，要求解最优策略，就是要找到能够最大化 state value 的策略。

而 state value 需要先给定策略 $\pi$ 才可以求解。

因此，我们需要回答以下问题：
* 最优策略是否存在？
* 最优策略是否是唯一的？
* 最优策略是随机的还是确定的？
* 如何得到最优策略？


在此，直接给出贝尔曼最优方程 BOE 的表达形式：

$$
\begin{align}
v_{\pi^*}(s)
& = \max_{\pi} \sum_a \pi(a | s) \left [ \sum_r p_r(r | s, a) r + \gamma \sum_{s'} p_s(s' | s, a) v(s') \right ], \forall s \in S \\
& = \max_{\pi} \sum_a \pi(a | s) q(s, a) , \forall s \in S \\
\end{align}
$$

使用矩阵-向量形式表示，可以写为：

$$
v = \max_{\pi}(r_{\pi} + \gamma P_{\pi} v)
$$


求解最优策略的公式推演较为复杂，在此，直接给出最优策略的定义：

最大的 state value $v^*(s)$ ：
$$
\begin{align}
v^*(s)
& = \max_{\pi} \sum_a \pi(a | s) q(s, a) \\
& = \max_{a \in A} q(s, a) \\
\end{align}
$$

贪婪最优策略 greedy optimal policy $\pi^*$ ：
$$
\pi^* = 
\left \{
\begin{matrix}
1, a = a^*(s) \\
0, a \neq a^*(s) \\
\end{matrix}
\right .
$$

最优行为 $a^*$ ：
$$
a^*(s) = \arg \max_a q^*(s, a)
$$

也就是，最大化 state value 需要找到最大化 action value 的 action 。
令一个策略 $\pi$ 在每一步都执行这个 action，那么就得到了最优策略 $\pi^*$ 。


由此，可以回答最初的问题：

* 最优策略是否存在？
  存在。
* 最优策略是否是唯一的？
  根据压缩映射定理 contraction mapping thorem，可以求解出最优的 state value 及对应的 policy 。
  其中的 optimal state value 是唯一的，但是 optimal policy 可能不唯一。
* 最优策略是否是随机的？或是确定的？
  确定的。
* 如何得到最优策略？
  通过迭代的方式可以求解最优策略。


## 最优策略的求解过程

根据贝尔曼最优方程：

$$
v = \max_{\pi}(r_{\pi} + \gamma P_{\pi} v)
$$

我们定义 $f(v) := \max_{\pi}(r_{\pi} + \gamma P_{\pi} v)$ ，我们需要求解 $f(v)$ 


## 巴拿赫不动点

fixed point: 

对于 $x \in X, f(x) \in X$ ，存在 $f(x) = x$ ，则称 $x$ 是不动点。


## 收缩映射定理 contraction mapping theorem

contraction mapping: 

对于函数 $f$ 有 $|| f(x_1) - f(x_2) || \leq \gamma || x_1 - x_2 ||, \gamma \in (0, 1), \forall x \in X$ ，则称函数 $f$ 是收缩函数 contractive function 

收缩映射定理：对于一个收缩函数 $f$，必定存在唯一的 fixed point $x^*$ ，且可以通过迭代的方式求解 $x_{k+1} = f(x_k)$ ，当 $k \to \infty$ 时, $x_k \to x^*$ ，迭代程指数收敛。

具体推理证明参见教材。


我们可以证明，贝尔曼最优方程是一个收缩函数，可以应用收缩映射定理。


## 最优策略的不变性 optimal policy invariance 

当 $r \to ar + b, a > 0$ 时，最优策略是不变的。


# 值迭代 value iteration 和策略迭代 policy iteration

## 基础概念

值迭代和策略迭代是两种求解贝尔曼最优策略的算法。


## 值迭代 value iteration

在介绍贝尔曼最优公式时，已经通过收缩映射定理 contraction mapping theorem 介绍了值迭代的方式，在此给出算法说明：

1. 初始化 $v_k$ ，设置为零向量或随机向量，维度是 $S$ 。
解释说明：初始化 $v_k$ 可以代表在初始化策略 $\pi_k$ 的情况下求解的 $[ v_k(s_i) ]^T$ 向量。
不需要关心初始策略，只需要随机指定的初始化的值，便可以更新策略。

2. 更新最优策略 PU, policy update ， $\pi_{k+1} = \arg \max_a r_{\pi_{k+1}} + \gamma P_{\pi_{k+1}} v_k $ 
解释说明：在随机指定初始策略和初始值的情况下，可以更新最优策略。

以上是向量的表示，用线性代数表示为：
$$
\pi_{k+1} =
\left \{
\begin{matrix}
1, a = a^*(s) \\
0, a \neq a^*(s) \\
\end{matrix}
\right .
,
$$

其中，
$$
\begin{align}
a^*(s) 
& = \arg \max_a q^*(s, a) \\
& = \arg \max_a \left ( \sum_r p_r(r | s, a) r + \gamma \sum_{s'} p_s(s' | s, a) v_k(s') \right ), \forall s in S \\
\end{align}
$$

使用向量化的表示即为 $\pi_{k+1} = \arg \max_a r_{\pi_{k+1}} + \gamma P_{\pi_{k+1}} v_k $ 
由于环境已经给出 $S$ ， $A$ ，$p_r(r | s, a)$ ， $r$ ， $\gamma$ 和 $p_s(s' | s, a)$ ，我们初始化了 $v_k$ ，因此可以求解出最优策略 $\pi_{k+1}$ 。

3. 更新值 VU, value update ， $v_{k+1} = r_{\pi_{k+1}} + \gamma P_{\pi_{k+1}} v_k $ ，由于 $\pi_{k+1}$ 采用贪婪策略（一定采取动作价值最大的行为），因此 $v_{k+1}(s) = \max_a q_k(s, a)$ ，同样的，可以使用线性代数方式理解。
解释说明：更新策略后，可以在新的策略下求解 state value 

4. 重复 2-3 的过程，直到 $| v_{k+1} - v_k | < \epsilon$ ，此时求解出的 $v_{k+1}$ 和 $\pi_{k+1}$ 就是 optimal state value 和 optimal policy 


使用伪代码方式理解上述求解过程：

```
已知：

* 状态空间 $S = {s}$ 
* 行为空间 $A = {a}$ 
* 奖励矩阵 $p_r = [s, a]$ ，值为奖励期望 $\bar{r}$ 
* 转移概率矩阵 $p_s = [s, a, s']$ ，值为概率
注意，在这里 $p_s$ 和 $p_r$ 代表矩阵，可以进行矩阵运算

假设：

* 初始向量 $v_k$ 

计算：
* 计算动作价值 $q_k = p_r + einsum("sas', s' -> sa", p_s, v_k)$ 。这里较难理解，需要仔细考虑 $p_r, p_s$ 
* 更新状态价值 $v_{k+1} = max(q_k, dim=a)$ 

直到 $|v_{k+1} - v_{k}| < \epsilon$ 时，停止上述计算。

最终的 $v_{k+1}$ 是 optimal state value ， $q_{k+1}$ 是 optimal action value 
最优策略 $\pi_{k+1} = argmax(q_{k+1}, dim=a)$ 
```

示例代码可以参考 RL_Value_Iteration.ipynb


## 策略迭代 policy iteration

策略迭代相对于值迭代来说，只是从初始化 state value 变成了初始化 policy 。在此给出算法说明：

1. 初始化 $\pi_k$ ，设置为零向量或随机向量，维度是 $s, a$ 。

2. 策略评估 PE, policy evaluation ，已知 $\pi_k$ 的情况下，可以求解 state value $v_{\pi_k} = r_{\pi_k} + \gamma P_{\pi_k} v_{\pi_k}$ 

3. 策略优化 PI, policy improvement ，在已知 $v_{\pi_k}$ 的情况下，可以优化策略 $\pi_{k+1} = \arg \max_{\pi} (r_{\pi} + \gamma P_{\pi} v_{\pi_k})$ 
解释说明：策略优化 $v{\pi_{k+1}} \geq v_{\pi_k}$ 且 $k \to \infty, v_{\pi_k} \to v^*$ ，具有严格的数学证明，在此省略。

4. 重复 2-3 的过程，直到 $\pi_k = \pi_{k+1}$ ，此时求解出的 $v_{k+1}$ 和 $\pi_{k+1}$ 就是 optimal state value 和 optimal policy 


使用伪代码方式理解上述求解过程：

```
已知：

* 状态空间 $S = {s}$ 
* 行为空间 $A = {a}$ 
* 转移概率矩阵 $p_s = [s, a, s']$ ，值为概率
* 奖励矩阵 $p_r = [s, a]$ ，值为奖励期望 $\bar{r}$ 
注意，在这里 $p_s$ 和 $p_r$ 代表矩阵，可以进行矩阵运算

假设：

* 初始策略矩阵 $\pi_k = [s, a]$ ，值为概率

计算：
* 计算 $r_{\pi_k} = (\pi_k \odot p_r) I_{|a|}$ ，其中 $I_{|a|}$ 是维度为 $a \times 1$ 的列向量，值全部为 1 
* 计算 $P_{\pi_k} = einsum('sa, sas -> ss', \pi_k, p_s)$ 
* 计算状态价值 $v_{\pi_k} = r_{\pi_k} + \gamma P_{\pi_k} v_{\pi_k}$ 。可以通过求逆法或迭代法计算（通常使用迭代法）。
  求逆法： $v_{\pi_k} = (I_{|s \times s|} - \gamma P_{\pi_k})^{-1} r_{\pi_k}$ 
  迭代法计算 $v_{\pi_k}^{i+1} = r_{\pi_k} + \gamma P_{\pi_k} v_{\pi_k}^i$ ，当 $i \to \infty$ 时， $v_{\pi_k}^i \to v_{\pi_k}^*$ 
* 计算动作价值 $q_k = p_r + einsum("sas', s' -> sa", p_s, v_{\pi_k})$ 
* 更新策略 $\pi_{k+1} = argmax(q_k, dim=a)$ 

直到 $\pi_k = \pi_{k+1}$ 时，停止上述计算。

最终的 $v_{k+1}$ 是 optimal state value ， $q_{k+1}$ 是 optimal action value 
最优策略 $\pi_{k+1} = argmax(q_{k+1}, dim=a)$ 
```


通过观察 policy iteration 可以发现，靠近目标的策略会被优先更新到最优，远离目标的策略会后被更新到最优。

示例代码可以参考 RL_Policy_Iteration.ipynb


## 截断策略迭代算法 truncated policy iteration

阶段迭代策略算法 truncated policy iteration 是 value iteration 和 policy iteration 的一般化推广。

观察 value iteration 和 policy iteration 可以发现：

value iteration:  $          v_0   \to \pi_1 \to v_1   \to \pi_2 \to \dots$ 
policy itetation: $\pi_0 \to v_0^* \to \pi_1 \to v_1^* \to \pi_2 \to \dots$ 

可以看到：
在 value iteration 中，实际上并没有去找在当前策略 $\pi$ 下最优的 state value ，只是进行不断的迭代更新，最终找到一个最大的 state value ，就是 optimal state value 。
而在 policy iteration 中，每一次都去找到策略 $\pi$ 下最优的 state value，然后再进行策略更新，最终找到一个最大的 state value ，就是 optimal state value 。

即使 value iteration 最开始的 $v_0$ 和 policy iteration 最开始的 $v_0^*$ 相同，后续的收敛方式也不一致。


在实际问题的求解过程中，我们很可能无法做到在每一次都找到策略 $\pi$ 下最优的 state value ，那么执行有限步数 $j$ 的 policy evaluation 的方式，就叫做 truncated policy iteration 。
可以看出，当 $j = 1$ 时，就是 value iteration ，当 $j \to \infty$ 时，就是 policy iteration 。


# 有模型 model-based 和免模型 model-free

环境信息包括：

* 状态空间 State space: $S = \{ s \}$ 
* 行为空间 Action space: $A(s) = \{ a \}$ 
* 状态转移概率分布 State transition probability: $p_s(s' | s, a)$ 
* 奖励概率分布 Reward probability: $p_r(r | s, a)$ 

如果我们知道环境信息，就可以认为这个环境是已知的，因为我们用这两个函数来描述环境，使用贝尔曼最优方程求解最优策略。
这种情况被称为有模型 model-based。

但是通常环境信息是未知的，我们不知道环境的状态转移概率分布和奖励概率分布，甚至是不知道环境的状态空间 $S$ 和行为空间 $A$ ，这种情况被称为免模型 model-free。
在这种情况下，我们无法直接求解贝尔曼方程，需要有其他的方法。


解释说明：
在这篇之前介绍的 value iteration ， policy iteration， truncated policy iteration 三个算法都是有模型算法，本质上是遍历访问整个环境的状态空间、行为空间、状态转移概率分布、奖励概率分布，使用动态规划的思想来获取贝尔曼方程的最优解。

而后续介绍的算法都将是免模型算法，算法无法访问整个环境的状态空间、行为空间、状态转移概率分布、奖励概率分布，只能通过与环境交互来获得有限的样本，探索环境并充分利用已有知识。


# 在线 on policy 和离线 off policy

on policy 是指
off policy 是指


# 蒙特卡洛模拟 MC, Monte Carlo Mean Estimation

在免模型的情况下，我们可以通过蒙特卡洛模拟的方式，通过对环境的采样，获得环境的状态转移概率分布和奖励概率分布。
潜在假设是环境的状态空间 $S$ 和行为空间 $A$ 是离散且有限的。

蒙特卡洛方法基于大数定律。

大数定律：

对于一个随机变量 $X$ ，假设 ${x_i}, i \to N$ 是 $N$ 次独立同分布采样的样本数据。令 $\bar{x} = \frac{1}{N} \sum_i^N x_i$ 是这 $N$ 个样本数据的平局值，那么有：

* $\mathbb{E}(\bar{x}) = \mathbb[X]$ 
* $Var[\bar{x}] = \frac{1}{N} Var[X]$ 

即： $\bar{x}$ 是对随机变量期望 $\mathbb{E}(X)$ 的无偏估计，且随着 $N$ 趋近于 $\infty$ ，其方差逐步趋近于 0 。


## 基本方法 MC basic

MC basic 基于 policy iteration 。

通过观察 policy iteration 可以看到，其过程主要分为两步：

* policy evaluate ： $v_{\pi_k} = r_{\pi_k} + \gamma P_{\pi_k} v_{\pi_k}$ 
* policy update: $\pi_{k+1} = \arg \max_{\pi} q_{\pi_k}(s, a)$ 

由于环境信息未知，即环境状态转移概率分布 $p_s(s' | s, a)$ 和奖励概率分布 $p_r(r | s, a)$ 未知，因而无法求解 $r_{\pi_k}$ 和 $P_{\pi_k}$ 。

转换视角来看，在给定策略 $\pi_k$ 时，我们可以通过大量的独立同分布的试验，可以采样到不同的轨迹 $\tau$ 的回报 $G_t$ （更准确的描述是回合 episode，因为采样存在有限步骤 episode step），通过计算期望，就得到了 $\mathbb{E}_{\pi_k}[G_t | S_t = s, A_t = a]$ ，也就是 $q_{\pi_k}(s, a)$ 。
因此，我们可以在没有 policy evaluate 的情况下，直接执行 policy update ，更新策略 $\pi_{k+1} = \arg \max_{\pi} q_{\pi_k}(s, a)$ 。
循环往复，我们就可以得到最优的策略 $\pi^*$ 。


采样步骤 episode step 是新加入的变量。通过观察可知，采样步骤 episode step 需要设置为从开始到目标的长度，这样可以从最开始的步骤就得到最优的 action value 。设置更短会影响更早的策略，设置更长不会更进一步改进最优策略。

MC basic 只是用来阐述强化学习下的蒙特卡洛模拟方法，适用场景很少。因为如果能够通过无限次的采样获取样本数据，那么就可以计算环境状态转移概率分布和奖励概率分布。

使用伪代码方式理解上述求解过程：

```
已知：

* 状态空间 $S = {s}$ 
* 行为空间 $A = {a}$ 

假设：

* 初始策略矩阵 $\pi_k = [s, a]$ ，值为概率

探索：

* 从每一个 $(s, a)$ 出发，收集策略 $\pi_k$ 下的多条轨迹

计算：
* 计算策略 $\pi_k$ 在每一个 $(s, a)$ 的回报的平均值 $q_k(s, a)$ ，作为动作价值函数的估计
* 更新策略 $\pi_{k+1} = argmax(q_k, dim=a)$ 

重复探索和计算动作，直到策略收敛

最终的 $q_{k+1}$ 是 optimal action value 
最优策略 $\pi_{k+1} = argmax(q_{k+1}, dim=a)$ 
```

示例代码参考 RL_MC_Basic.ipynb


## MC exploring starts

MC exploring stars 是对 MC basic 的一种改进，以更有效地利用数据，更高效地更新策略。

更有效地利用数据：

在 MC basic 中，假设一条采集到的完整的 episode ： $(s_1, a_1) \to (s_2, a_1) \to (s_1, a_1) \to (s_3, a_2) \to \infty$ 

可以看到，在采集到的一条 episode 中，可以分解为很对子轨迹，例如：

$(s_2, a_1) \to (s_1, a_1) \to (s_3, a_2) \to \infty$ 
$(s_1, a_1) \to (s_3, a_2) \to \infty$ 
$(s_3, a_2) \to \infty$ 
$\dots$ 

通过这种方式，可以减少需要采集的样本数量，更高效地使用数据。

在这里有两种策略：

* first-visit ：对于一条完整的 episode 中的 $(s, a)$ ，只使用第一次出现的作为一条 sub eposide 
* every-visit ：对于一条完整的 episode 中的 $(s, a)$ ，使用所有的 sub eposide 


更高效地更新策略：

在 MC basic 中，我们通过大量的独立同分布的试验，采样到不同的轨迹 $\tau$ 的回报 $G_t$ 计算期望得到 $q_{\pi_k}(s, a)$ 。

这样需要等待很长时间，收集轨迹数据 $\tau$ 。

我们也可以采集到一条 eposide 后，使用它作为 action value 的估计，更新策略，这样依然是有效的。
增加采集样本数量，确保每一个 $(s, a)$ 都有一条 eposide 能够经过，这有助于正确估计 $q(s,a)$ ，也有助于提高收敛效率。这也就是 exploring starts 的字面含义，探索所有的起点。
// TODO 证明


这两种算法可以叫做一般策略迭代算法 GPI, Generalized policy iteration 。
这是一种通用的算法框架，不需要精确地计算 state value 和 policy value ，通过不断地迭代，当误差足够小的情况下，就可以获得最优策略。


使用伪代码方式理解上述求解过程：
```
已知：

* 状态空间 $S = {s}$ 
* 行为空间 $A = {a}$ 

假设：

* 初始策略矩阵 $\pi_k = [s, a]$ ，值为概率

探索：

* 以策略 $\pi_k$ 在环境中探索，采集 $N$ 条长度为 $T$ 的轨迹数据 $\tau = [s, a]$ ，值为奖励 $r$ 。
  采集的数量 $N$ 是动态的，0 $(s, a)$ 。
  采集的步骤 $T$ 是动态的，需要确保能够从最远的 state 到达终点。

计算：

* 计算动作价值期望，得到 $q(s, a)$
  计算过程较为复杂，需要求解每一个 $(s, a)$ 行为的期望回报。当 $s$ 和 $a$ 较大时，构建矩阵运算会提高效率。
  一种计算方法示例：
  令 \tau[N][T] = (s, a, r), q[s][a] = (num, value)
  for i in range(N):
    for j in reversed(range(T)):
      s, a, r = \tau[i][j]
      num, value = q[s, a]
      num += 1
      value += r + \gamma * value
      q[s, a] = (num, value)
  q[s, a] = value / num
  q = tensor(q[s, a])
* 更新策略 $\pi_{k+1} = argmax(q(s, a), dim=a)$ 

重复探索和计算过程，直到策略 $\pi_{k+1} = \pi_{k}$ 。
```


## MC $\epsilon-$ Greedy

MC $\epsilon-$ Greedy 是对 MC exploring starts 的一种改进，可以称为 MC without exploring starts 。

首先明确 $\epsilon-$ Greedy policy ：

在求解贝尔曼最优方程时，我们实际上是使用 greedy policy 得到了 optimal policy 。
$\epsilon-$ greedy policy 就是对 greedy policy 增加了一个小的参数 $\epsilon \in [0, 1]$ ，使得策略并不总是贪婪的，能够具有一定的随机性质。

数学表示如下：

$$
\pi(a | s) = 
\left\{ 
\begin{array}{ll}
1 - \frac{\epsilon}{|A|} (|A| - 1), & \text{for the greedy action,} \\
\frac{\epsilon}{|A|}, & \text{for the other } |\mathcal{A}(s)| - 1 \text{ actions.} \\
\end{array} 
\right.
$$

当 $\epsilon = 0$ 时， $\epsilon-$ greedy policy 就是 greedy policy 。
当 $\epsilon = 1$ 时， $\epsilon-$ greedy policy 就没有一个最主要的选择，所有的 action 都具有相同的可能性。

选择使用 $\epsilon-$ greedy policy 最主要是为了平衡探索 exploration 和 利用 exploitation ：
* 探索 exploration ：在已知最大回报的策略的基础上，探索新的可能性，评估是否有更优的策略。
* 利用 exploitation ：利用已知最大回报的策略。
* 随着 $\epsilon$ 的增大，探索性会越来越强。


使用 MC $\epsilon-$ greedy policy 时，我们不需要使用 exploring starts ，使用多条 eposide 来覆盖所有的 $(s, a)$ 。可以只用一条 eposid 来覆盖所有的 $(s, a)$ 。

后续的算法求解步骤和 MC exploring starts 一致，最后求解出的策略是 optimal ε policy ，而不是 optimal policy 。
通过观察可知，当 $\epsilon$ 足够小时，求解出的 optimal ε policy 才是 optimal policy ，否则二者并不相同。


使用伪代码方式理解上述求解过程：
```
已知：

* 状态空间 $S = {s}$ 
* 行为空间 $A = {a}$ 

假设：

* 初始策略矩阵 $\pi_k = [s, a]$ ，值为概率

探索：

* 以策略 $\pi_k$ 在环境中探索，采集 1 条长度为 $T$ 的轨迹数据 $\tau = [s, a]$ ，值为奖励 $r$ 。
  采集的步骤 $T$ 需要确保能够覆盖所有的 $(s, a)$ 。

计算：

* 计算动作价值期望，得到 $q(s, a)$
  计算过程较为复杂，需要求解每一个 $(s, a)$ 行为的期望回报。当 $s$ 和 $a$ 较大时，构建矩阵运算会提高效率。
  一种计算方法示例：
  令 \tau[T] = (s, a, r), q[s][a] = (num, value)
  for i in range(N):
    s, a, r = \tau[i]
    num, value = q[s, a]
    num += 1
    value += r + \gamma * value
    q[s, a] = (num, value)
  q[s, a] = value / num
  q = tensor(q[s, a])
* 更新策略 $\pi_{k+1} = greedy(epsilon, q(s, a))$ 

重复探索和计算过程，直到策略 $\pi_{k+1} ≈ \pi_{k}$ 。
```


MC exploring starts 和 MC $epslion$-greedy 算法都是无模型算法，但是至少知晓环境的状态空间和行为空间，因此可以遍历整个环境。
后续我们将做进一步假设，我们将对环境一无所知，只能通过行为进行探索。


此外，还有可以使用优化的 MC $epslion$-greedy 算法：

```
探索：

* 以策略 $\pi_k$ 在环境中探索，以 $\epsilon$ 的概率选择随机行为，以 $1-\epsilon$ 的概率选择现有策略的最优行为

计算：

* 更新 action value 的 $Q(s, a)$ 
* 更细策略
```


# 上述几种算法的归纳总结

1. value iteration
思路是通过遍历 state action pair ，直接求解 optimal state value ，然后根据 optimal state value 直接获得 optimal policy 。

2. policy iteration
思路是先随机选择一个 policy ，然后求解这个 policy 下的 state value ，根据 state value 来更新 policy 。直到 policy 稳定的时候就是 optimal policy 。

3. truncated policy iteration
对 policy iteration 的一种改进。
在求解 policy 下的 state value 时，不需要特别精确，只需要从 state 出发，计算有限步数 reward 即可视为 state value 。

4. monte carlo basic
思路是先随机选择一个 policy ，然后从每一个 state action pair 出发，计算这个 policy 下的 return 作为 action value ，根据 action value 来更新 policy 。直到 policy 稳定的时候就是 optimal policy 。
每一个 state action pair 至少访问 1 次。
计算 action value 时，可以使用 first visit 或 every visit 策略。

5. monte carlo exploring starts
思路是先随机选择一个 policy ，然后从随机的 state action pair 出发，计算这个 policy 下的 return 作为 action value ，根据 action value 来更新 policy 。
计算 action value 时，可以使用 first visit 或 every visit 策略。

6. monte carlo $\epsilon$-greedy 
思路是先随机选择一个 policy ，然后从随机的 state 出发，计算这个 policy 下的 return 作为 action value ，根据 action value 来更新 policy 。
更新 policy 时根据 epsilon 概率来分配 best action 和 normal action 。

7. monte carlo $\epsilon$-greedy optimized
思路是先随机选择一个 policy ，然后从随机的 state 出发，计算这个 policy 下的 return 作为 action value ，根据 action value 来更新 policy 。
在 policy 下会有 $\epsilon$ 的概率选择随机动作（探索），$1-\epsilon$ 的概率选择 policy 下的 best action 。


总结：

value iteration, policy iteration, truncated policy iteration 这三者是 model-base 算法，必须在已知所有环境信息的情况下才可以使用。
计算效率， value iteration < policy iteration < truncated policy iteration 

monte carlo basic, exploring starts, $\epsilon$-greedy, $\epsilon$-greedy optimized 这四者是 model-free 算法，可以通过与环境交互来获取最优策略。
计算效率， basic > exploring starts > $\epsilon$-greedy = $\epsilon$-greedy optimized
通用性， basic < exploring starts < $\epsilon$-greedy = $\epsilon$-greedy optimized


# 随机近似理论 SA, Stochastic Approximation

## 计算平均数的渐进式算法

蒙特卡洛模拟在理论上可以逼近平均数，但是在实践过程中的效率太低，需要等待采样结果完成才能估计。
那么是否可以有一种渐进式算法，伴随着每一步的采样来进行估计，并且最终也能得到平均值的无偏估计？答案是可以。

假设 $e_k = \frac{1}{k} \sum_{i=1}^k x_i$ ，则 $e_{k+1} = \frac{1}{k+1} \sum_{i=1}^{k+1} x_i$ 
那么可以知道 $e_{k+1} = \frac{k}{k+1} e_k + \frac{x_{k+1}}{k+1} = e_k - \frac{1}{k+1} (e_k - x_{k+1})$ 

随着采样数量的增加，可以渐进式的估计平均值。


这个算法可以进一步推广为一般形式，将 $\frac{1}{k+1}$ 替换为 $a_k, a_k > 0$ ，得到 $e_{k+1} = e_k - a_k (e_k - x_{k+1})$ ，这样也可以逼近解。


## 罗宾斯-蒙罗算法 RM, Robbins-Monro 

随机近似理论 SA 代表一大类通过随机迭代的方式找到或逼近最优解的方法，这种方法甚至可以不知道要求解的目标方程。
RM 算法是 SA 领域的开创性算法。


假设有一个方程 $g: \mathbb{R} \to \mathbb{R}$ ，要求解 $g(w) = 0$ ，其中 $w \in \mathbb{R}$ 是要求解的变量。

那么求解 $w^*$ 的方式就是要求解 $g(w) = \nabla_w J(w) = 0$ 。

如果函数 $g$ 的表达式是已知的，那么直接求解即可。
如果函数 $g$ 的表达式是未知的，那么可以用 RM 算法求解。


RM 算法：

求解 $g(w) = 0$ 的解 $w^*$ ，有：

$$
w_{k+1} = w_k - a_k \tilde{g}(w_k, \eta_k), k = 1, 2, 3, \dots
$$

满足：

* $w_k$ 是对根 $w^*$ 的第 $k$ 次估计
* $\tilde{g}(w_k, \eta_k) = g(w_k) + \eta_k$ 是第 $k$ 次观测的结果，其中 $\eta_k$ 是观测过程中的噪音
* $a_k > 0$ 

在这个算法中，函数 $g$ 是一个黑盒，我们并不知道函数的表达式。
但是我们可以通过输入序列数据 $\{ w_k \}$ 以及观测到包含噪音的输出序列数据 $\tilde{g}(w_k, \eta_k)}$ ，估算函数的解 $w^*$ 。


RM 定理：

在 Robbins-Monro 算法中，若满足以下条件：
* $0 \leq c_1 \leq \nabla_w g(w) \leq c_2, \forall w$ 
* $\sum_{k=1}^{\infty} \alpha_k = \infty$ 且 $\sum_{k=1}^{\infty} \alpha_k^2 < \infty$ 
* $\mathbb{E}[\eta_k | \mathcal{H}_k] = 0$ 且 $\mathbb{E}[\eta_k^2 | \mathcal{H}_k] < \infty$ ，其中 $\mathcal{H}_k = {w_k, w_{k-1}, \dots, w_1}$ 

那么 $w_k$ 将以概率 1 (w.p.1) 收敛到根 $w^*$ ，满足 $g(w^*) = 0$ 


说明：

* $0 \leq c_1 \leq \nabla_w g(w)$ 要求函数 $g$ 是单调递增的，且存在 $g(w) = 0$ 的解
* $\nabla_w g(w) \leq c_2$ 要求函数 $g$ 是有界的，不会趋近于无穷
* $\sum_{k=1}^{\infty} \alpha_k^2 < \infty$ 要求步长 $\alpha_k \to 0$ ，步长平方和要收敛，保证噪声的影响不会累计到发散，从而使算法最终能稳定下来
* $\sum_{k=1}^{\infty} \alpha_k = \infty$ 要求步长（或称为学习率） $\alpha_k$ 不会是 0 ，步长之和要发散，保证迭代有足够的“能量”到达最优点，即使起点很远
* $\mathbb{E}[\eta_k | \mathcal{H}_k] = 0$ 要求噪声的期望为 0
* $\mathbb{E}[\eta_k^2 | \mathcal{H}_k] < \infty$ 要求噪声的方差是有界的，这意味着观测虽然不精确，但是无偏的


在实际应用中，通常会让 $\alpha_k$ 趋向于一个非常小的数，而不是随着采样数 $k$ 的增大趋近于 0，因为需要保证后续采样的数据能提供一定量的价值。


## 理解 RM 算法

已知：

* 随机变量 $X$ 的采样数据 $\{ x \}$

求解：

* 随机变量 $X$ 的期望值（均值） $w = E[X]$ 

RM 算法：

* 定义一个函数 $g(w) = w - E[X]$ ，其中 $w$ 是对随机变量 $X$ 期望值的估计，是变量， $E[X]$ 是随机变量 $X$ 的期望值，是常量，但未知。
  这个函数的意义是：估计的期望值 $w$ 与真实期望值 $E[X]$ 的差距。当且仅当估计值 $w$ 完全正确时，这个差距为零。
  这个函数满足 RM 算法中对于函数 $g$ 的要求：单调递增，且存在 $g(w) = 0$ 的解。

* 定义带噪声的观测函数 $\tilde{g}(w_k, \eta_k) = w_k - x_k$ 。
  因为我们无法计算 $g(w)$（它包含未知的 $E[X]$），所以必须用一个我们能获得的、带噪声的观测来替代它。
  既然我们能量测到样本 $x_k$ ，那么我们就定义噪声观测函数为 $w_k - x_k$ ，这个定义非常直观，因为 $x_k$ 是我们唯一能获得的数据。
  我们有了定义，但我们需要证明这个定义能满足 RM 算法的要求。 RM 算法要求观测噪声必须是无偏的，即 $\mathbb{E}[\tilde{g}(w_k, \eta_k)] = g(w_k)$ 
  证明如下：
  $\mathbb{E}[\tilde{g}(w_k, \eta_k)] = \mathbb{E}[w_k - x_k] = w_k - \mathbb{E}[x_k] = w_k - \mathbb{E}[X] = g(w_k)$
  我们定义的观测函数恰好满足 RM 算法的要求。
  同时：
  $$
  \begin{align}
    \tilde{g}(w_k, \eta_k) 
    & = w_k - x_k \\
    & = (w_k - E[X]) + (E[X] - x_k) \\
    & = g(w_k) + \eta_k \\
  \end{align}
  $$
  通过恒等式变形，我们定义的 $\tilde{g}(w_k, \eta_k) $ 恰好具有 $g(w_k) + \eta_k$ 的形式。

* 根据 RM 算法 $w_{k+1} = w_k - \alpha_k \tilde{g}(w_k, \eta_k) = w_k - \alpha_k (w_k - x_k)$ ，可以求解出 $g(w) = 0$ 的最优解 $w^*$ 


## 随机梯度下降 SGD, Stochastic Gradient Descent



## 随机梯度下降 SGD 和批量梯度下降 BGD、小批量梯度下降 MBGD 的关系



# 时序差分方法 TD, Temporal Difference

## 概述

在 MC 算法中，我们充分利用了每一条 episode 的数据。但是 MC 算法的缺陷在于，必须等到收集一条完整的 episode 后才能开始评估和优化策略。

TD 算法是对 MC 算法的进一步优化，不需要等待收集一条完整的 episode ，可以利用探索 episode 中的每一步 step 的信息，评估和优化策略。

TD 算法的假设如下：

已知：

* 环境空间 $S$ 
* 行为空间 $A$ 
* 初始策略 $\pi$ 

求解：

* 最优策略 $\pi^*$ 


## 基本方法 TD basic 

TD basic 算法：

假设：

* 可以采集策略 $\pi$ 下的 episode 数据 $(s_t, r_{t+1}, s_{t+1})$ 

计算：

$$
\begin{align}
& v_{t+1}(s_t) = v_t(s_t) - \alpha_t(s_t) \left [ v_t(s_t) - (r_{t+1} + \gamma v_t(s_{t+1})) \right ], s = s_t \\
& v_{t+1}(s) = v_t(s), \forall s \neq s_t
\end{align}
$$

解释说明：

* 在一条 episode 中， agent 在同一时刻 t 只能处在一个 state = $s_t$ ，此时可以对 state value 有一个估计 $v_t(s_t)$ 。
* 当到达 t+1 时刻时， agent 到达了一个新的 state = $s_{t=1}$ ， agent 同时获得环境给予的 reward $r_{t+1}$ 。此时可以对 state = $s_t$ 的 state value 做更进一步的估计，即为 $v_{t+1}(s_t)$ ，二者的差值是执行了 action = $a_{t+1}$ 后获得的 reward $r_{t+1}$ 和折扣因子 $\gamma$ 带来的。
* 第一个公式代表： $t+1$ 时刻对 state = $s_t$ 的 state value 估计 $v_{t+1}(s_t)$ ，等于 t 时刻对 state = $s_t$ 的 state value 估计 $v_t(s_t)$ ，减去一个差值。当这个差值不断收敛时，对 state value 的估计会越来越准确。
* 第二个公式代表：对估计值的优化仅限于 state = $s_t$ ，其他状态的 state value 估计值保持不变，不会随着一个 step 而优化。

时序差分法，是通过比较在时刻 t 的估计和在时刻 t+1 的估计来进行学习。这个“差分”或“误差”就发生在连续的时刻之间。


我们进一步解释 TD 算法中出现的差值：

* $r_{t+1} + \gamma v_t(s_{t+1})$ 可以理解为 TD target $\delta_t$ ，即根据 reward 和 gamma 对 $s_t$ 的 state value 的新的估计。
* $v_t(s_t) - \delta_t$ 可以理解为 TD current 和 TD target 之间存在的误差 TD error 。
* $\alpha_t$ 可以理解为 learning rate ，代表着对于 state = $s_t$ 的 state value 估计值 $v_{t+1}(s_t)$ 需要以一个小的学习率逐步改进，直到最后收敛。


这个算法和 RM 算法存在一定的相似性，可以从数学上证明 TD 算法的收敛性。以下是一个 RM 算法的例子：

已知：

* 随机变量 $X$ 的采样 $x$ 

求解：

* 随机变量 $X$ 的期望值（均值） $w = E[R + \gamma v(X)]$ 

RM 算法：

* 定义随机变量 $Y$ ，其中 $Y = R + \gamma v(X)$ 
* 定义 $g(w) = w - \mathbb{E}[Y]$ 
* 定义 $\tilde{g}(w_k, \eta_k) = w_k - y_k = w_k - (R + \gamma v(x_k))$ 
* 求解 $w_{k+1} = w_k - \alpha_k \tilde{g}(w_k, \eta_k) = w_k - \alpha_k (w_k - (R + \gamma v(x_k)))$ ，可以求解出 $g(w) = 0$ 的最优解 $w^*$ 


从数学的角度讲， TD 算法是在没有模型的情况下，求解 bellman equation 。

整体而言，TD 算法可以充分利用了每一个步骤的信息，在执行每一个步骤的同时更新 state value 。
这种思路也可以用于更新 state value 和 policy ，也就是下面要介绍的 Sarsa 相关算法


## Sarsa 算法 TD Sarsa

Sarsa 是 $s_t, a_t, r_{t+1}, s_{t+1}, a_{t+1}$ 的缩写。


TD Sarsa 算法：

假设：

* 可以采集策略 $\pi$ 下的 episode 数据 $(s_t, a_t, r_{t+1}, s_{t+1}, a_{t+1})$ 

计算：

$$
\begin{align}
& q_{t+1}(s_t, a_t) = q_t(s_t, a_t) - \alpha_t(s_t, a_t) \left [ q_t(s_t, a_t) - (r_{t+1} + \gamma q_t(s_{t+1}, a_{t+1})) \right ], (s, a) = (s_t, a_t) \\
& q_{t+1}(s, a) = q_t(s, a), \forall s \neq s_t
\end{align}
$$

解释说明：

* 从直观的理解上， TD sarsa 算法相比于 TD basic 而言仅仅是从对 state value 的估计修改为了对 action value 的估计。
* 


TD Expected Sarsa

计算：

$$
\begin{align}
& q_{t+1}(s_t, a_t) = q_t(s_t, a_t) - \alpha_t(s_t, a_t) \left [ q_t(s_t, a_t) - (r_{t+1} + \gamma \mathbb{E}[q_t(s_{t+1}, A)]) \right ], (s, a) = (s_t, a_t) \\
& q_{t+1}(s, a) = q_t(s, a), \forall s \neq s_t
\end{align}
$$

解释说明：

* 从直观的理解上， TD Expected sarsa 算法相比于 TD sarsa 而言仅仅是从 action value 的估计到 expected action value 。


TD n-step Sarsa

计算：

$$
\begin{align}
& q_{t+1}(s_t, a_t) = q_t(s_t, a_t) - \alpha_t(s_t, a_t) \left [ q_t(s_t, a_t) - (r_{t+1} + \gamma r_{t+2} + \dots + \gamma^{n-1} r_{t+n} + \gamma^{n} q_{t+n}) \right ], (s, a) = (s_t, a_t) \\
& q_{t+1}(s, a) = q_t(s, a), \forall s \neq s_t
\end{align}
$$



## Q-learning 算法，TD 算法计算 optimal action value

直接求解 optimal action



# 策略梯度 PG, Policy Gradient

## 公式推演

轨迹 $\tau_i = {s_0, a_0, s_1, a_1, \cdots, s_t, a_t}$ ，其中行为 $a_t = \pi(o_t, \theta)$ 
轨迹 $\tau_i$ 所获得的回报 $R(\tau) = {r_0, \cdots, r_t}$ 
轨迹 $\tau_i$ 概率 $P(\tau) = P(s_0) * P(a_1|s_0, \pi) * \cdots * P(a_t|s_0, a_0, \cdots, s_t, a_t, \pi)$ 
因此智能体 Agent 在环境 Environment 的 状态空间 S 和 行为空间 $\pi$ 的期望是 $E(R(\tau)) = \sum_{\tau} R(\tau) P_{\theta}(\tau)$ 

在这个问题中，只有 $\pi(\theta)$ 是变量。

求解期望的最大值，可以通过梯度上升的方法计算，因此首先计算梯度。

$$
\begin{align}
\nabla E(R(\tau))
& = \nabla \sum_{\tau} R(\tau) P_{\theta}(\tau) \\
& = \sum_{\tau} R(\tau) \nabla P_{\theta}(\tau) \\
& = \sum_{\tau} R(\tau) P_{\theta}(\tau) \frac{\nabla P_{\theta}(\tau)}{P_{\theta}(\tau)} \\
& = \sum_{\tau} R(\tau) P_{\theta}(\tau) \nabla log P_{\theta}(\tau) \\
& = \sum_{\tau} P_{\theta}(\tau) R(\tau) \nabla log P_{\theta}(\tau) \\
& = E_{\tau \sim P_{\theta}(\tau)} [ R(\tau) \nabla log P_{\theta}(\tau) ] \\
& \approx \frac{1}{N} \sum_{n=1}^{N} R(\tau^n) \nabla log P_{\theta}(\tau^n) \\
& = \frac{1}{N} \sum_{n=1}^{N} \sum_{t=1}^{T_n} R(\tau^n) \nabla log P_{\theta}(a^n_t | s^n_t) \\
\end{align}
$$
 
这里有几点需要澄清：
1、$\sum_{\tau} R(\tau) \nabla P_{\theta}(\tau)$ ：在这一步，从直觉上，策略参数 $\theta$ 决定了动作，动作影响了轨迹 $\tau$ ，而轨迹 $\tau$ 直接决定了最终获得的奖励 $R(\tau)$ 。从因果链上看， $\theta$ 确实通过 $\tau$ 间接影响了 $R(\tau)$ 。但在数学上计算梯度时，当我们把 $R(\tau)$ 当作一个函数写入期望回报的公式 $\sum_{\tau} R(\tau) P_{\theta}(\tau)$ 时，​​$R(\tau)$ 本身并不是参数 $\theta$ 的函数，我们并不需要对 $R(\tau)$ 求导。
我们可以这样理解这个公式：对于每一个固定的、已经发生的轨迹 $\tau$ ​，都对应着一个确定的、数值固定的奖励值 $R(\tau)$ ​。$\theta$ 的变化并不会改变一个已经发生的轨迹的奖励值，它只会改变这个轨迹在未来再次发生的概率 $P_{\theta}(\tau)$ 。
计算梯度 $\nabla E(R(\tau))$ 的过程，可以理解为在回答：“如果我把参数 $\theta$ 微微调整一下，那么我所有可能获得的期望回报​（即所有轨迹回报的平均值）会如何变化？”
·调整 $\theta$ 并不会改变过去某条特定轨迹 $\tau$ 的得分 $R(\tau)$ 。
·调整 $\theta$ 会改变未来采样到不同轨迹的概率分布。它会让一些高回报的轨迹变得更可能发生（增加 $P_{\theta}(\tau)$ ，同时让一些低回报的轨迹变得更不可能发生（减少 $P_{\theta}(\tau)$ ）。
因此，期望回报 \nabla E(R(\tau))​ 的变化，完全来自于概率分布 $P_{\theta}(\tau)$ 的变化。梯度计算只需要抓住这个变化的核心——即 $\nabla_{\theta} P_{\theta}(\tau)$ ——而不需要去关心 $R(\tau)$ 本身是如何变化的。

2、$\nabla f(x) = f(x) \nabla logf(x)$ ：这是微积分中的一个恒等式。
假设 $f(x)$ 是一个可微函数，且 $f(x) > 0$ （以便取对数）。我们考虑函数 $logf(x)$ 的梯度。
根据链式法则，对数函数的梯度为： $\nabla log f(x) = \frac{1}{f(x)} \nabla f(x)$ 。推导过程：$logf(x)$ 的导数是 $\frac{1}{f(x)} f'(x)$ ，对于梯度同理。
将上述等式两边同时乘以 f(x)，得到： $f(x) \nabla log f(x) = \nabla f(x)$ 。

3、$\approx \frac{1}{N} \sum_{n=1}^{N} R(\tau^n) \nabla log P_{\theta}(\tau^n)$ 这里应用了蒙特卡洛模拟的思想。用采样的方式，把每一个的值加起来，就可以得到梯度。

4、$\frac{1}{N} \sum_{n=1}^{N} \sum_{t=1}^{T_n} R(\tau^n) \nabla log P_{\theta}(a^n_t | s^n_t)$ ：这里的推导过程省略了一步。

对于 $P_{\theta}(\tau)$ 有 $P_{\theta}(\tau) = P(s_1)P_{\theta}(a_1 | s_1)P(s_2 | s_1, a_1)P_{\theta}(a_2 | s_2)\cdots$ 。其中 $P_{\theta}(a_t | s_t)$ 是 Agent 的策略 $\pi$ 的概率，而 $P(s_{t+1} | s_t, a_t)$ 是 Environment 的概率，它可能是固定的，也可能是有概率的。
将上述公式化简，即 $P_{\theta}(\tau) = P(s_1) \prod_{t=1}^{T} P_{\theta}(a_t | s_t) P(s_{t+1} | s_t, a_t)$ 。
由于 $P$ 和 $\theta$ 无关，因此在公式化简时只考虑 $P_{\theta}$ 。

5、$\frac{1}{N} \sum_{n=1}^{N} \sum_{t=1}^{T_n} R(\tau^n) \nabla log P_{\theta}(a^n_t | s^n_t)$ 。由于 log 函数是单调递增的，所以这个梯度函数的直观意义是：
·如果 $R(\tau)$ 是正的，那就增大所有状态为 $s_t$ 时，采取行为 $a_t$ 的概率
·如果 $R(\tau)$ 是负的，那就减小所有状态为 $s_t$ 时，采取行为 $a_t$ 的概率
·除了调整方向外，$R(\tau)$ 的大小还会影响调整幅度，是大幅度或是小幅度调整，但会被 $\sum_{t=1}^{T_n}$ 回合内求和，以及 $\frac{1}{N} \sum_{n=1}^{N}$ 多个回合平均

6、基线 baseline：在实际的训练过程中，通常会设置一个 baseline，这可以有两点解释：
·如果采样的 reward 总是正数（或负数），那么梯度会增加所有行为的概率，只是幅度有大有小，这样会导致模型收敛较慢。通过设置一个 baseline，使得模型可以区分“好”和“更好”的概念，不达到 baseline 的行为是“不够好”的，这可以加快模型收敛速度。也就是减少梯度的方差，使得训练结果更稳定。
·采样数量总是有限的，没有被采样的动作概率会下降。因此通过设置 baseline 可以设定一个强化学习目标。
使用数学表示即为： $\frac{1}{N} \sum_{n=1}^{N} \sum_{t=1}^{T_n} (R(\tau^n) - b) \nabla log P_{\theta}(a^n_t | s^n_t) \\$ 

7、Action 的价值评估：在一个能获得较大 Return 的 $\tau$ 中，可能不是所有的 Action 都是好的。评价一个 Action 的好坏，不能参考整个 $\tau$ 的 Return，而是计算这个 Action 执行以后得到的 Return，即假设之前获得 Reward 和执行这个 Action 没有关系（Action 只和观察到的 State 有关）。
因此将原来的整个 $\tau^n$ 的奖励的总和 $R(\tau^n)$ ，现在改成从某个时刻 $t$ 开始，这个动作是 $t$ 一直到游戏结束 $T_n$ 所有奖励的总和为 $\sum_{t'=t}^{T_n} r^n_{t'}$ 。

此外，在某一时刻，执行某一个 Action，会影响接下来所有的结果（有可能在某一时刻执行的动作，接下来得到的奖励都是这个动作的功劳），但在一般的情况下，时间拖得越长，该动作的影响力就越小。因此为了更好地评估当前 Action 对 Return 的影响，我们对 Return 设置时间价值的折扣因子 $\gamma \in [0, 1]$ （如果 $\gamma = 0$ ，这表示我们只关心即时奖励；如果 $\gamma = 1$ ，这表示未来奖励等同于即时奖励，类似于折现的概念）。
使用数学表示即为：$\sum_{t'=t}^{T_n} \gamma^{t'-t} r^n_{t'}$ 。


最后，我们获得了最终的公式：

$$
\begin{align}
\nabla E(R(\tau))
& = \frac{1}{N} \sum_{n=1}^{N} \sum_{t=1}^{T_n} (\sum_{t'=t}^{T_n} \gamma^{t'-t} r^n_{t'} - b) \nabla log P_{\theta}(a^n_t | s^n_t) \\
\end{align}
$$


## 价值函数

Action-Value Function: 动作价值函数，在 State $s$ 下，做出 Action $a$ ，期望获得的 Return $r$ ，用 $Q_{\theta}(s, a)$ 表示。
这个函数是 Environment 在 State 下对于 Action 提供 Reward 的期望函数，用于训练时的采样。

State-Value Function: 状态价值函数，在 State $s_t$ 下，期望获得的 Return $r_t$ ，用 $V_{\theta}(s)$ 表示。

Advantage Function: 优势函数，在 State $s$ 下，做出 Action $a$ ，比其他动作带来多少优势，用 $A_{\theta}(s, a) = Q_{\theta}(s, a) - V_{\theta}(s)$ 表示。


我们可以使用 $A_{\theta}(s_t, a_t)$ 代替 $\sum_{t'=t}^{T_n} \gamma^{t'-t} r^n_{t'} - b$ ，因此公式变为：

$$
\begin{align}
\nabla E(R(\tau))
& = \frac{1}{N} \sum_{n=1}^{N} \sum_{t=1}^{T_n} A_{\theta}(s_t, a_t) \nabla log P_{\theta}(a^n_t | s^n_t) \\
\end{align}
$$



## 直观理解

以伪代码形式进行直观理解。

```python
class env:
  # 创建环境
  def init():
    self.reset()

  # 重置环境
  def reset(self):
    self.state = ...
    return self.state

  # 环境受到 agent 行为的影响而发生改变状态，并给予 agent 对应的奖励
  def step(self, action):
    self.state = ...
    return self.state, reward


class agent():
  # 创建智能体
  def init():
    self.action_space = ...
    self.policy = ...

  # agent 观测环境
  def observe(state):
    ...
    return ob_state

  # agent 基于观测和策略产生行为
  def policy(ob_state):
    ...
    return action

  # 更新策略
  def update_policy():
    return self.policy

def main():
  env = env()
  agent = agent()
  trajectory = []
  for i in range(num_eposides):
    returns = 0
    for t in range(T):
      state = env.state
      ob_state = agent.observe(state)
      action = agent.policy(ob_state)
      next_state, reward = env.step(action)

      trajectory.extend((state, action, reward, next_state))
      returns += reward
```


# PPO, Proximal Policy Optimization

近端策略优化


# Q-learning 算法

Q-learning 是一种无模型强化学习算法，用于学习动作价作值函数（Q 函数，代表 action value function）。它通过智能体与环境的交互，学习在给定状态下选择最优动作的策略。

Q 函数​：Q(s, a) 表示在状态 s 下执行动作 a 的预期回报（累积奖励）。

Q-learning 的核心公式是： $Q(s, a) = Q(s, a) + \alpha [r + \gamma·max(Q(s', a')) - Q(s, a)]$ ，其中

* $\alpha$ 学习率
* $\gamma$ 折扣因子
* $r$ 即时奖励

用伪代码来表示 Q-learing 算法即为：

```
初始化 Q 表 Q(state_dims, action_dims)

for 每个训练轮次 (episode)：
    重置环境状态 s
    while 未达到终止状态 或 终止步数：
        # 动作选择（ε-贪婪策略）
        if random() < ε: 
            随机选择动作 a（探索）
        else:
            选择当前状态 s 下 Q 值最大的动作 a（利用）

        # 执行动作
        执行动作 a，观察奖励 r 和新状态 s'

        # 环境状态转移
        s ← s'

        # Q值更新
        Q(s,a) ← Q(s,a) + α[r + γ·max(Q(s',a')) - Q(s,a)]

    # 衰减探索率
    ε ← max(ε_min, ε × 衰减率)
```


Q-learning 算法可以用来处理离散状态和行为。我们使用一个2维网格世界导航的例子来理解 Q-learning 算法。

详细代码参考 RL_Q-learning.ipynb 中的 GridWorld2D


# DQN 算法

DQN 算法主要用来处理 Q-learning 无法处理的高纬度问题。

DQN 的核心公式是： $Q(s, a) = Q(s, a) + \alpha [r + \gamma·max(Q(s', a')) - Q(s, a)]$ ，其中

* $\alpha$ 学习率
* $\gamma$ 折扣因子
* $r$ 即时奖励

用伪代码来表示 DQN 算法即为：

```
初始化主 Q 网络 Q_θ(神经网络，输入 state_dims 维度数据，输出 action_dims 维度数据)
初始化目标 Q 网络 Q_θ'(神经网络，θ' = θ)

for 每个训练轮次 (episode)：
    重置环境状态 s
    while 未达到终止状态 或 终止步数：
        # 动作选择（ε-贪婪策略）
        if random() < ε: 
            随机选择动作 a（探索）
        else:
            选择当前状态 s 下 Q_θ 值最大的动作 a（利用）

        # 执行动作
        执行动作 a，观测奖励 r 和新状态 s'

        # 状态转移
        s ← s'

        # 存储经验
        将经验元组 (s, a, r, s', done) 存入回放缓冲区 D

        # Q值更新
        if D 中有足够的经验：
            从 D 中随机采样一批样本 (s_i, a_i, r_i, s'_i, done_i)
            
            for 每个样本
                if done_i:
                    y_i = r_i
                else:
                    y_i = r_i + γ * max_a' Q_θ'(s'_i, a')

            # 计算损失
            loss = MSE(Q_θ(s_i, a_i), y_i)

            使用反向传播更新 θ: θ ← θ - α * ∇θ loss
        if 达到更新频率:
            θ' ← θ  # 将主网络参数复制到目标网络

    # 衰减探索率
    ε ← max(ε_min, ε × 衰减率)
```


我们将2维网格世界导航的例子扩展为连续的状态来理解 DQN 算法。

需要注意的是，这只是一个简单的示例，用于理解强化学习的 DQN 算法。真实世界中存在各种客观的物理规律，通过实验可以编写更为精准的控制算法。

详细代码参考 RL_Deep_Q-Network.ipynb 中的 GridWorld2D



# 一些想法

## 自动驾驶

需要充足的特征数据来描述环境信息。

汽车周围的图像信息（前、后、左、右、上、下）
汽车当前的位置（x, y, z）
汽车当前的位置速度（dx, dy, dz）
汽车当前的加速度 a(+, -)
汽车当前的动力 p(+, -)
汽车当前的质量 m
汽车当前的轮胎磨损程度
……

需要充足的行为空间。

方向盘角度 （+180, -180）
方向盘速度 （+,-）
汽车动力 p(+, -)
汽车加速度 a(+, -)
手刹 （+,-）
手刹速度 （+,-）
……


