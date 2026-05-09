---
date: 2026-05-06T12:00:00+08:00
title: AI Architecture
draft: false
# bookFlatSection: false        # 是否显示扁平章节（默认false）
# bookToc: true                 # 是否显示目录（默认true）
# bookHidden: false             # 是否在侧边栏列表中隐藏（默认false）
# bookCollapseSection: false    # 章节是否默认折叠（默认false）
# bookComments: false           # 是否启用评论（默认false）
# bookSearchExclude: false      # 是否从搜索结果中排除（默认false）
# params:                       # 自定义参数
#   maths: true                 # 数学公式支持
# weight: 1                     # 内容权重（排序用）
---

# AI 架构

## 算法与原理

### 词典 vocab 和分词器 tokenizer

vocab 是词典。

tokenizer 是根据词典将文本转换为 token，单个文字转换为 one-hot encoding。

### embedding

词嵌入，是一个升维的过程。可以直观的理解为，一个文字在不同维度有不同的含义。例如：苹果可以理解为水果，可以理解为手机，可以理解为公司，可以理解为诱惑等等。

同时也解决了 vocab 过大的问题，词表中的文字可以有几万、十几万甚至几十万。它们没有办法表示表达语义。

根据 one-hot encoding 经过 embedding 层（可以单独训练或和模型一起训练）后，转换为 vector 。

### position encoding

为了让模型能够识别到文本顺序，通过对 vector 增加 position encoding 来增加文本顺序，让模型能够学习到上下文关系。

### transformer

transformer 架构是当前 ai 领域事实上的架构标准。

在每一层 encoder 内计算 Q K V 矩阵，然后通过 attention 计算后（可以是一层注意力，也可以是 multi-head 多头注意力），经过一层全连接层 fnn 输出。经过残差连接后进入下一层 encoder 。

缩放点积注意力 scaled dot-product attention 是注意力机制的集大成者。

要知道 transformer 并不是突然出现的，在此之前经历过：RNN 循环神经网络、LSTM 长短期记忆网络 双向 LSTM 、GRU 门控制网络、Seq2Seq Encoder 和 Decoder 架构等。

```text
# 假设在推理阶段
# batch_size = 1, 省略
# vocab_size = 100000
# seq_len = 100
# hidden_size = 1024 （RNN、LSTM、GRU 等架构的 hidden_size 是包含了上文内容隐藏含义的隐层，而 transformer 架构的 hidden_size 更像是对 vocab 进行语义扩展的隐层，二者的概念存在较大差别）
# num_head = 8
# wq = (hidden_size, hidden_size)
# wk = (hidden_size, hidden_size)
# wv = (hidden_size, hidden_size)

input: (seq_len)
embedding: (seq_len, hidden_size)
q: (seq_len, hidden_size)
k: (seq_len, hidden_size)
v: (seq_len, hidden_size)

q_reshape: (num_head, seq_len, hidden_size/num_head)
k_reshape: (num_head, seq_len, hidden_size/num_head)
v_reshape: (num_head, seq_len, hidden_size/num_head)
q_reshape_i: q_reshape[i] = (seq_len, hidden_size/num_head)
k_reshape_i: k_reshape[i] = (seq_len, hidden_size/num_head)
v_reshape_i: v_reshape[i] = (seq_len, hidden_size/num_head)

attention: softmax((q_reshape_i @ k_reshape_i.T) / sqrt(hidden_size/num_head)) @ v_reshape_i = (seq_len, hidden_size/num_head)

encoder output: torch.cat([(seq_len, hidden_size/num_head), ...]) = (seq_len, hidden_size)
```

### attention

理解 transformer 需要对 attention 层进行进一步的分析。

假设输入：“今天天气很”。我们用 1 2 3 4 5 的位置表示，演示 attenton 层的计算过程：

embedding input + position encoding
今    e11   e12   e13   ...   e11024
天    e21   e22   e23   ...   e21024
天    e31   e32   e33   ...   e31024
气    e41   e42   e43   ...   e41024
很    e51   e52   e53   ...   e51024

假设没有多头，计算 qkv 矩阵为

q/k/v
今    q11   q12   q13   ...   q11024
天    q21   q22   q23   ...   q21024
天    q31   q32   q33   ...   q31024
气    q41   q42   q43   ...   q41024
很    q51   q52   q53   ...   q51024

q*k.T 计算之后会得到一个（seq_len， seq_len）维度的注意力权重矩阵 dot-product attention，表示的是两个文字在所有隐层维度（hidden_size）的注意力加总，就是点积注意力。

q*k.T 今    天    天    气    很
今    w11   mask  mask  mask  mask
天    w21   w22   mask  mask  mask
天    w31   w32   w33   mask  mask
气    w41   w42   w43   w44   mask
很    w51   w52   w53   w54   w55

其中 wmn = qm1*kn1 + qm2*kn2 + ... + qm1024*kn1024

为什么会有 mask，因为因果语言模型认为在计算注意力机制的时候， q 矩阵 query 是看不到后续信息的，也就是看不到要预测的信息，只能看到已经存在的信息。

然后是 sqrt(dk) 进行了缩放，softmax 进行了归一化。

最后计算 att*v 会得到注意力加和的结果，可以表示为：

o1 = (w11*v11 + mask*v21 + ... + mask*v51, w11*v12 + mask*v22 + ... + mask*v52, ..., w11*v11024 + mask*v21024 + ... + mask*v51024)
o2 = ...
o3 = ...
o4 = ...
o5 = (w51*v11 + w51*v21 + ... + w51*v51, w52*v12 + w52*v22 + ... + w52*v52, ..., w55*v11024 + w55*v21024 + ... + w55*v51024)

也就是计算注意力得分和 v 矩阵所有隐层维度的值。

### 自回归模型

自回归模型也叫做因果语言模型，是指根据前 n 个 token 预测第 n+1 个 token 的模型，然后基于前 n+1 个 token 预测第 n+2
 个 token，直至最后结束。

原因是，因果语言模型通过因果注意力掩码，确保每个位置的输出仅基于该位置及之前的输入（也就是 query 看不到之后的输入）。
在训练阶段：为了效率，总是进行并行计算，使用每个位置的输出同时去预测各自的下一个真实token，但其内在的因果约束与推理完全一致。
因此在推理阶段：在自回归生成时，我们将已生成的整个序列输入，并只使用最后一个位置的输出来预测下一个token，因为它是唯一蕴含了整个当前序列完整信息的向量。

### kv cache

自回归模型在推理过程中，因为只需要计算最后一个 token，因此不需要重复生成前序信息，过程中的 k 和 v 可以重复利用，演示如下：

第一次计算：
输入： [e1, e2, e3, e4, e5]
计算： [q1,k1,v1], [q2,k2,v2], [q3,k3,v3], [q4,k4,v4], [q5,k5,v5]
输出： [o1, o2, o3, o4, o5]
截取： [o5]

第二次计算：
无 kv cache（重复计算）：
输入： [e1, e2, e3, e4, e5, e6]
计算： [q1,k1,v1], [q2,k2,v2], [q3,k3,v3], [q4,k4,v4], [q5,k5,v5], [q6,k6,v6]  ← 全部重新计算
输出： [o1, o2, o3, o4, o5, o6]
截取： [o6]

有 kv cache（复用缓存）：
输入： [e6]  ← 只输入新token
计算： [q6,k6,v6]  ← 只计算新的 q k v
读取： [k1,v1], [k2,v2], [k3,v3], [k4,v4], [k5,v5]  ← 从缓存读取
输出： [o6]
截取： [o6]

可以看到在没有 kv cache 的情况下，会浪费计算资源，因此以空间换时间，可以减少提高模型推理速度。

### dense 和 moe

dense 架构是全连接/密集型架构。

moe 架构是混合专家的稀疏激活架构。其思想来源是 dense 架构的计算成本过高和部分层的计算贡献度较低。
moe 将庞大的神经网络切割成许多个小块的“专家”（experts）。当用户输入问题时，一个前置的“门控网络”（router）会快速判断这个问题属于哪些领域，然后只激活对应的 1-2 个“专家”进行计算，其他专家不参与。最后把这几个专家的计算结果汇总，作为最终输出。
这个 router 网络会和整个模型一起训练。

dense/moe 和 transformer 不是同一个维度的描述，transformer 既可以是 dense 架构，也可以是 moe 架构。transformer 架构中最主要的是缩放点积注意力机制。

### 显存计算

显存计算是模型训练和推理基础。

假设一个使用 4b 模型，参数使用 fp16 精度，加载模型需要的显存大约是：4b * 16bit ≈ 8GB 

训练时，因为优化器 + 数据（受到batch_size 和 seq_len 等因素影响） + 梯度 + 激活值等存储，4b 的模型大约需要 40 GB 的显存。

推理时，因为中间激活值 + kv cache 等影响，4b 的模型至少需要 8 GB 的显存。


## 模型训练

### 预训练 pre-training

通过海量的无标注数据进行模型预训练，目标是学会基础的文本规律，学习文本间的关联关系。

### 监督微调 sft

基于预训练模型，使用精心准备的数据进行监督微调。之所以是微调，是因为当前的模型参数量极大，全量训练的成本过高。

### 基于人类反馈强化学习 rlhf

拿同一个问题，让尚未经过 RLHF 的模型生成多个不同的回答。然后雇佣人类标注员，根据这些回答的帮助性、真实性、无害性进行打分和排序（比如选出最好的 A，最差的 D）。有了人类打分数据，就可以专门训练出一个小尺寸的“奖励模型”（RM）充当“裁判”，能自动预判大模型说出某句话，人类会有多喜欢。

然后基于强化学习算法，例如 PPO 或 DPO 微调大模型。

### 分布式训练技术

#### 模型并行 model parallelism

随着模型尺寸的增大，没有 GPU 能够放得下这个模型，此时需要将模型拆分到多张 GPU 上，可以有流水线并行和张量并行两种方案。

流水线并行 pipeline 是将模型的层数分拆，例如前 2 层由 GPU 1 来执行，后 2 层由 GPU 2 来执行。

张量并行 tensor 是将模型的计算矩阵分拆，例如前 W/2 矩阵由 GPU 1 来执行，后 W/2 矩阵由 GPU 2 来执行，GPU 3 来汇总运算结果。

#### 数据并行 data parallelism

把一个大 batch 的数据切成 2 份（每张 GPU 拿 1/2），然后用自己那份数据跑一遍模型，算出 Loss，然后汇总平均后，再反向计算。

#### ZeRO (Zero Redundancy Optimizer)

zero 是微软提供的超大尺寸模型训练方法，PyTorch 官方对应的实现叫 FSDP。

### 微调

prompt 方案：修改模型输入

adapter 方案：在模型中插入层

修改方案：修改模型参数。最典型的 lora ，低秩矩阵近似


## 模型推理

### 量化

模型原始是 fp16 尺寸，可以使用 int8 来量化，显存减半。


## 模型应用

### 提示词工程 prompt

对用户的输入增加提示词，补充上下文，来引导大模型输出符合用于预期的结果。

prompt 不是“提问技巧”，而是一门将自然语言转化为确定性系统指令的工程学。

当前也有 dspy 等框架支持迭代评估和优化 prompt。

### 检索增强生成 rag

模型在没有见过相关知识时，如果没有足够的上下文，可能幻觉会比较严重。

通过提供外挂的知识库，可以在询问大模型的时候提供额外的信息。

基本操作包括：文本切割、向量数据库、向量检索等

### agent

LLM 到 agent 的关键变化不是“回答更像人”，而是“能够把回答转化为行动”。

Agent = LLM (核心大脑) + Memory (记忆系统) + Planning (规划调度) + Tools (工具执行)，完成感知->思考->行动循环 ReAct。

架构师箴言（Architect's Rule of Thumb）： "Agent = 概率性的大脑 + 确定性的工具"。永远不要让 LLM 去做精确的数学计算或直接修改底层数据库表。正确的做法是让 LLM（Agent）负责意图理解与规划调度，而将具体的业务逻辑封装为确定性的 API 工具供其调用。

Agent 几乎可以应用于所有需要智能化的场景，是增强人类能力，不是替代人类。

#### mcp 和 function calling

mcp（model content protocol） 模型上下文协议，给大模型工具调用提供了标准协议。

function calling 是指模型调用外部工具的能力。
agent 在给 llm 输入的信息中，包含了可以调用的工具，当 llm 识别到需要调用外部工具时，将返回给 agent 执行工具，然后 agent 将工具返回给 llm，llm 继续下一步判断。

#### skill

skill 本质上是渐进上下文披露机制，为了保护有限的模型上下文，将需要加载的信息在需要使用的时候再加载。


## 框架

### 训练框架

pytorch, tensorflow, jax, deepspeed 等。

早期是 tensorflow ，后来是 pytorch 成为了事实上的标准，最新的还有 jax 和 deepspeed 提高训练效率。

### 推理服务框架

fastchat, llama-cpp 等。

### 推理加速框架

vllm, deepspeed-fastgen 等

### 压缩框架

bitsandbytes 等

### 微调框架

peft

### agent 框架


### 向量数据库


## 参考资料

[从零开始学 Agent](https://haozhe-xing.github.io/agent_learning/zh/part1.html)

[大模型技术栈](https://www.bilibili.com/video/BV1jj411H7vG/)
