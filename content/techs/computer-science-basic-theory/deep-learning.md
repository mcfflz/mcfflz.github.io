---
date: 2026-02-12T12:00:00+08:00
title: Deep Learning
draft: false
# bookFlatSection: false        # 是否显示扁平章节（默认false）
# bookToc: true                 # 是否显示目录（默认true）
# bookHidden: false             # 是否在侧边栏列表中隐藏（默认false）
# bookCollapseSection: false    # 章节是否默认折叠（默认false）
# bookComments: false           # 是否启用评论（默认false）
# bookSearchExclude: false      # 是否从搜索结果中排除（默认false）
params:                       # 自定义参数
  maths: true                 # 数学公式支持
weight: 112                   # 内容权重（排序用）
---


# 深度学习 Deep Learning

深度学习用于训练神经网络模型。



## 逻辑回归模型假设

model： $\hat{y} = \sigma (w^Tx + b), \sigma(z) = \frac{1}{1+e^{-z}}$ 

loss function： $\mathcal{L}(\hat{y}^{(i)}, y^{(i)}) = -(y^{(i)} log(\hat{y}^{(i)}) + (1 - y^{(i)}) log(1 - \hat{y}^{(i)}))$ 

cost function：$J(w,b) = \frac{1}{m} \sum_{i=1}^{m} \mathcal{L}(\hat{y}^{(i)}, y^{(i)}) =  -\frac{1}{m} \sum_{i=1}^{m} (y^{(i)} log(\hat{y}^{(i)}) + (1 - y^{(i)}) log(1 - \hat{y}^{(i)}))$ 

gradient descent：$\frac{\partial J(w,b)}{\partial w}$ 

update paras： $w := w - \alpha \frac{\partial J(w,b)}{\partial w}$ 



## 神经网络模型假设

神经网络模型是一个通用性很强的说法，具体到模型层面，这是一个多层感知机模型（MLP）。

输入：

* 样本数据： $(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), \cdots, (x^{(m)}, y^{(m)})$ 。
* 特征 $x \in \mathbb{R}^{n_x}$ ，标签 $y \in \mathbb{R}^k$ 。
* 模型输出： $\hat{y}$ 。
* 神经网络模型的层数 $l$ ，取值从 $0 - L$ 。当 $l = 0$ 时，代表输入特征，当 $l = L$ 时，代表模型输出。
* 神经网络模型第 $l$ 层神经元的数量 $n^{[l]}$ 。因此有 $n^{[0]} = n_x$ ，$n^{[L]} = k$ 。
* 神经网络模型第 $l$ 层神经元的非线性输出 $a^{[l]}$ 和 激活函数 $g^{[l]}$ 。因此有 $a^{[l] (i)} = x^{(i)}, a^{[L] (j)} = \hat{y}^{(j)}$ 。
* 非线性输出等于激活函数处理后的线性输出 $a^{[l]} = g^{[l]}(z^{[l]})$ 。
* 神经网络模型第 $l$ 层神经元的参数 $W^{[l]}$ 和偏置 $b^{[l]}$ 。


向前传播计算（均为向量）：

* 输入 $a^{[l-1]}$ 。
* 参数 $W^{[l]}$ 和偏置 $b^{[l]}$ 。
* 计算 $z^{[l]} = W^{[l]} \cdot a^{[l-1]} + b^{[l]}$ 。
* 计算 $a^{[l]} = g^{[l]} (z^{[l]})$ 。
* 直到 $l = L$ 结束。

反向传播计算（均为向量）：

* 计算 $da^{[l]}$ 。
* 计算 $dz^{[l]} = da^{[l]} \cdot g'$ 。
* 计算 $dW^{[l]} = \frac{1}{m} dz^{[l]} \cdot a^{[l-1]}$ 。
* 计算 $db^{[l]} = \frac{1}{m} dz^{[l]}$ 。
* 计算 $da^{[l-1]} = {W^{[l]}}^T \cdot dz^{[l]}$ 。
* 计算 $dz^{[l-1]}$ ，……
* 直到 $l = 1$ 结束。

使用计算图和链式法则来表示这一过程：
```
a[0] -> z[1] -> a[1] -> z[2] -> a[2] -> ··· -> a[l-1] -> z[l] -> a[l]
w[1]            w[2]            w[3]           w[l]
b[1]            b[2]            b[3]           b[l]

即：
z[1] = w[1]·a[0] + b[1]
a[1] = g(z[1])
z[2] = w[2]·a[1] + b[2]
a[2] = g(z[2])
···
z[l-1] = w[l-1]·a[l-2] + b[1-1]
a[l-1] = g(z[l-1])
z[l] = w[l]·a[l-1] + b[1]
a[l] = g(z[l])

因此：
da[l] = dJ = -y/a[l] + (1-y)/(1-a[l])
dz[l] = da[l]·g'
dw[l] = dz[l]·a[l-1]
db[l] = dz[l]
da[l-1] = dz[l]·w[l-1]
dz[l-1] = da[l-1]·g'
dw[l-1] = dz[l-1]·a[l-2]
db[l-1] = dz[l-1]
···
da[2] = dz[3]·w[2]
dz[2] = da[2]·g'
dw[2] = dz[2]·a[1]
db[2] = dz[2]
da[1] = dz[2]·w[1]
dz[1] = da[1]·g'
dw[1] = dz[1]·a[0]
db[1] = dz[1]
```

各数组维度：
```
layer_dims:
n[0] -> n[1] -> n[2] -> ··· ->  n[l] -> ···  -> n[L-1] -> n[L]

a[l-1]: n[l-1] × m
W[l]: n[l] × n[l-1]
b[l]: n[l] × 1
z[l]: n[l] × m

da[l]: n[l] × m
dz[l]: n[l] × m
dw[l]: n[l] × n[l-1] = dz · a[l-1].T
db[l]: n[l] × 1 = np.sum(dz, axis=1, keepdims=True)
```

使用 python 中的 numpy 的向量化计算（利用 CPU 或 GPU 的 SIMD, single instruction multiple data 单指令多数据流技术），可以极大地提高计算效率。

```python
import numpy as np
import time

a = np.random.randn(1000000)
b = np.random.randn(1000000)

st = time.time()
c = np.dot(a,b)
ed = time.time()
print("vector: " + str(1000 * (ed-st)) + " ms")

c = 0
st = time.time()
for i in range(1000000):
    c += a[i] * b[i]
ed = time.time()
print("for loop: " + str(1000 * (ed - st)) + " ms")

# vector: 1.6088485717773438 ms
# for loop: 1135.8444690704346 ms
```


使用 python 中的 numpy 实现神经网络中的向前传播和反向传播的示例（不适用TensorFlow、PyTorch等框架）：

```python
import numpy as np

# vector Z
def sigmoid(Z):
	return 1 / (1 + np.exp(-Z))

# vector Z
def sigmoid_derivative(Z):
	S = sigmoid(Z)
	return S * (1 - S)

# vector Z
def relu(Z):
	return np.maximum(0, Z)

# vector Z
def relu_derivative(Z):
	return (Z > 0).astype(float)

# 参数初始化
# list layer_dims
def initialize_parameters(layer_dims):
	parameters = {}
	L = len(layer_dims) - 1  # 神经网络层数，不算输入层
	for l in range(1, L+1):  # w1,b1,w2,b2,...,wL,bL
		parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1]) * 0.01  # 这里可以根据选择的激活函数替换为对应的参数初始化函数
		parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))
	return parameters

# 前向传播
# vector X, dict parameters
def forward_propagation(layer_dims, X, parameters):
	caches = {}
	A = X
	L = len(layer_dims) - 1  # 神经网络层数
	caches['A0'] = A

	# [1,L-1]层使用ReLU函数
	for l in range(1, L):
		A_prev = A
		W = parameters['W' + str(l)]
		b = parameters['b' + str(l)]
		Z = np.dot(W, A_prev) + b
		A = relu(Z)
		caches['Z' + str(l)] = Z
		caches['A' + str(l)] = A

	# [L]层使用Sigmoid函数
	W = parameters['W' + str(L)]
	b = parameters['b' + str(L)]
	Z = np.dot(W, A) + b
	Y_pred = sigmoid(Z)
	caches['Z' + str(L)] = Z
	caches['A' + str(L)] = Y_pred

	return Y_pred, caches

# 计算损失
# vector Y_pred, vector Y
def compute_cost(Y_pred, Y):
	m = Y.shape[1]
	cost = - (1/m) * np.sum(Y * np.log(Y_pred) + (1-Y) * np.log(1-Y_pred))
	return np.squeeze(cost)

# 反向传播
# dict parameters, list caches, vector X, vector Y
def backward_propagation(layer_dims, parameters, caches, X, Y):
	grads = {}
	L = len(layer_dims) - 1  # 神经网络层数
	m = X.shape[1]

	# 输出层梯度
	Y_pred = caches['A' + str(L)]
	A_prev = caches['A' + str(L-1)]
	dZ = Y_pred - Y
	dW = (1/m) * np.dot(dZ, A_prev.T)  # dW(l) = dZ(l) · A(l-1).T / m
	db = (1/m) * np.sum(dZ, axis=1, keepdims=True)  # db(l) = dZ(l) / m
	grads['dW' + str(L)] = dW
	grads['db' + str(L)] = db

	# 隐藏层梯度
	for l in reversed(range(1, L)):
		Z = caches['Z' + str(l)]  # Z(l)
		A_prev = caches['A' + str(l-1)]  # A(l-1)
		dZ = np.dot(parameters['W' + str(l+1)].T, dZ) * relu_derivative(Z)  # dZ(l) = W(l+1) · dZ(l+1) * g'(Z(l))
		dW = (1/m) * np.dot(dZ, A_prev.T)
		db = (1/m) * np.sum(dZ, axis=1, keepdims=True)
		grads['dW' + str(l)] = dW
		grads['db' + str(l)] = db

	return grads

# 参数更新
# dict parameters, dict grads, float learning_rate
def update_parameters(layer_dims, parameters, grads, learning_rate):
	L = len(layer_dims) - 1  # 神经网络层数
	for l in range(1, L+1):  # w1,b1,w2,b2,...,wL,bL
		parameters['W' + str(l)] -= learning_rate * grads['dW' + str(l)]
		parameters['b' + str(l)] -= learning_rate * grads['db' + str(l)]
	return parameters

# 训练模型
# vector X, vector Y, list layer_dims, float learning_rate, int num_iterations
def train_model(X, Y, layer_dims, learning_rate=0.01, num_iterations=1000):
	parameters = initialize_parameters(layer_dims)
	for i in range(num_iterations):
		# 前向传播
		Y_pred, caches = forward_propagation(layer_dims, X, parameters)
		# 计算损失
		cost = compute_cost(Y_pred, Y)
		# 反向传播
		grads = backward_propagation(layer_dims, parameters, caches, X, Y)
		# 更新参数
		parameters = update_parameters(layer_dims, parameters, grads, learning_rate)
		# 打印损失
		if i % 100 == 0:
			print(f"Cost after iteration {i}: {cost}")
	return parameters

# 模型预测函数
def predict(X, parameters, layer_dims):
	Y_pred, _ = forward_propagation(layer_dims, X, parameters)
	predictions = (Y_pred > 0.5).astype(int)
	return predictions

# 评估模型准确率
def evaluate_accuracy(X, Y, parameters, layer_dims):
	predictions = predict(X, parameters, layer_dims)
	accuracy = np.mean(predictions == Y) * 100
	return accuracy

# 测试
# 生成样本数据（XOR问题）
np.random.seed(1)
X = np.array([[0, 0, 1, 1], [0, 1, 0, 1]])
Y = np.array([[0, 1, 1, 0]])
# 网络结构：输入层2，隐藏层4，隐藏层6，输出层1
layer_dims = [2, 4, 1]
# 训练模型
parameters = train_model(X, Y, layer_dims, learning_rate=0.1, num_iterations=10000)

accuracy = evaluate_accuracy(X, Y, parameters, layer_dims)  # 输出：100.0
print(accuracy)
```


# 正则化

## 偏差和方差

通过误差判断机器学习问题：

* 高偏差：训练集误差高，验证集误差高，欠拟合
* 高方差：训练集误差低，验证集误差高，过拟合
* 高方差，高偏差：训练集误差高，验证集误差更高，同时存在欠拟合和过拟合问题
* 低偏差，低方差：训练集误差低，验证集误差低，良好的模型

首先解决高偏差问题，保证模型可以拟合训练集。可以通过调整模型选择，增加模型层数或神经元数量，增加模型训练次数等方式
其次解决高方差问题，保证模型不要过拟合。可以通过获取更多的数据、调整正则化参数等方式，也可以调整模型选择


## L1正则化

对于一般的逻辑回归模型，损失函数增加 L1 正则化：$J(w, b) = \frac{1}{m} \sum_{i=1}^{m} \mathcal{L}(\hat{y}^{(i)}, y^{(i)}) + \frac{\lambda}{2m} | w |_1$ 

如果使用 L1 正则化，$w$ 最终会是稀疏的，即参数中会有很多 0 。


## L2正则化

对于一般的逻辑回归模型，损失函数增加 L2 正则化： $J(w, b) = \frac{1}{m} \sum_{i=1}^{m} \mathcal{L}(\hat{y}^{(i)}, y^{(i)}) + \frac{\lambda}{2m} || w ||_2^2$ 

$|| w ||_2$ 被称为向量 $w$ 的欧几里得范数，其定义是向量中所有元素的平方求和。即 $|| w ||_2^2 = \sum_{j=1}^{n_x} w_j^2 = w^T·w $ 。

在 L2 正则化中可以增加 $b$ 的范数，但通常不增加，因为参数 $w$ 的维度要比 $b$ 更丰富，已经可以表达对参数的惩罚。

深度学习中常见使用 L2 正则化。

神经网络模型损失函数增加 L2 正则化： $J(w^{[1]}, b^{[1]}, \cdots, w^{[L]}, b^{[L]}) = \frac{1}{m} \sum_{i=1}^{m} \mathcal{L}(\hat{y}^{(i)}, y^{(i)}) + \frac{\lambda}{2m} \sum_{l=1}^{L} || w^{[l]} ||_F^2$ 

$|| w^{[l]} ||_F^2$ 被称为矩阵 $w$ 的佛罗贝尼乌斯范数（线性代数中的定义），其定义是矩阵中所有元素的平方求和。即 $|| w^{[l]} ||_F^2 = \sum_{i=1}^{n[l-1]} \sum_{j=1}^{n[l]} {w^{[l]}_{i,j}}^2$ 。


## Dropout正则化

Dropout 正则化是通过随机失活神经元来防止过拟合，有多种变体：

* 标准正则化：以概率 p 随机将神经元的输出设置为零
* Inverted Dropout：训练时对保留的神经元进行缩放（乘以 $\frac{1}{1-p}$ ），以保证激活值的期望，测试时不使用 Dropout
* Spatial Dropout：随机丢弃整个特征图

```python
import numpy as np

Ax = np.array([[1,1,1,1],[1,1,1,1],[1,1,1,1]])  # 3x4
px = 0.8  # 80%的概率保留，输出缩放时直接除以此概率p即可。或者以20%的概率随机丢弃输出，输出缩放时需要除以1-p
Dx = np.random.rand(Ax.shape[0], Ax.shape[1]) < px
Ax = Ax * Dx / px
```

在实际操作中，可以对神经网络中的不同层使用不同的 Dropout 概率，以防止某些层过拟合。


## 提前停止（早停法）

通过观察训练集和验证集的损失函数曲线（横轴是训练次数，纵轴是损失值），在一个合适的地方停止，即找到了训练集和验证集较为合适的模型参数，这也可以视为一种正则化方法，可以防止模型的过拟合。


# 机器学习中的问题处理

## 模型训练时长与归一化输入

归一化输入的核心目标是将不同量纲的特征缩放到统一范围，可以加速模型收敛，解决训练时长和学习率的问题。

使用归一化输入时，训练集、验证集和测试集必须使用相同的归一化方式和参数。

归一化输入主要有两种方式：

* Z-Score 标准化（高斯分布归一化）：将所有数据转换为均值为 0，标准差为 1 的分布。
* Min-Max缩放（线性映射）：将数据压缩到指定的区间。

```python
def zscore(X):  # 二维 X
	mu = X.mean(axis=0)  # 按特征计算均值
	sigma = X.std(axis=0)  # 按特征计算标准差
	X_score = (X - mu) / sigma
	return X_score

def minmax(X):  # 二维 X
	X_min = X.min(axis=0)  # 按特征计算最小值
	X_max = X.max(axis=0)  # 按特征计算最大值
	X_minmax = (X - X_min) / (X_max - X_min)
	return X_minmax
	
def normalize_nd(data, axis=None, eps=1e-8):
	"""
	支持任意维度的归一化函数

	参数：
	data : numpy.ndarray
		输入数据（支持任意维度）
	axis : int/tuple of ints, optional
		归一化计算的轴（默认全部特征维度）
	eps : float
		防止除零的小常数

	返回：
	normalized_data : numpy.ndarray
		归一化后的数据
	mean : numpy.ndarray
		计算得到的均值
	std : numpy.ndarray
		计算得到的标准差
	"""
	# 计算均值和标准差
	mean = np.mean(data, axis=axis, keepdims=True)
	std = np.std(data, axis=axis, keepdims=True) + eps

	# 执行归一化
	normalized = (data - mean) / std

	return normalized, mean.squeeze(), std.squeeze()

# 测试数据
X = np.array([[1,2,3,4],[5,6,7,8],[10,11,12,13],[14,15,16,17]])
X.shape
zscore(X)
minmax(X)

# 测试数据
Z = np.array([[[1,1,1,1],[2,2,2,2],[3,3,3,3]],[[4,4,4,4],[5,5,5,5],[6,6,6,6]]])
Z.shape
normalize_nd(Z)
```


## 梯度消失、梯度爆炸与随机初始化

深层神经网络会面临梯度消失或梯度爆炸问题。以一个简化的数学模型来表示：

假设：

* 每一层的参数 $W$ 是固定值 1.5 （或 0.5），偏置 $b$ 为零
* 激活函数 $g(z) = z$ 是线性的

那么模型预测值 $\hat{y} = W^{[L]} · W^{[L-1]} \cdots W^{[2]} · W^{[1]} · X$ 

显然，当神经网络模型的层数 $L$ 足够大时（模型足够深时），模型输出将会爆炸或消失（$1.5^L$ 或 $0.5^L$）

随机初始化可以缓解这一问题。


## 损失不下降与梯度检验

反向传播代码错误可能导致模型训练失败，计算数值梯度与解析梯度是否一致，可以验证是否存在此类问题。


# 梯度下降法的优化

## 带动量的梯度下降算法

带动量的梯度下降法运用的是一种加权平均的思想，即累计过去的梯度，用于计算当前的梯度。带动量的梯度下降算法的表现通常要优于不带动量的梯度下降算法，可以更快实现模型收敛。

数学公式如下：

* 初始化 $VdW = 0, VdW \in \mathbb{R}^{(n[l], n[l-1])}; Vdb = 0, Vdb \in \mathbb{R}^{(n[l],1)}$ ，即 $VdW, Vdb$ 的维度和 $W, dW, b, db$ 的维度一致
* 更新动量 $VdW = \beta VdW + (1 - \beta) dW, Vdb = \beta Vdb + (1 - \beta) db$ 
* 更新参数 $W = W - \alpha VdW, b = b - \alpha Vdb$ 

示例代码如下：

```python
import numpy as np

# 初始化梯度动量
def initialize_momentum(layer_dims):
	momentum = {}
	L = len(layer_dims) - 1  # 神经网络层数，不算输入层
	for l in range(1, L+1):  # Vdw1,Vdb1,Vdw2,Vdb2,...,VdwL,VdbL
		momentum['VdW' + str(l)] = np.zeros((layer_dims[l], layer_dims[l-1]))
		momentum['Vdb' + str(l)] = np.zeros((layer_dims[l], 1))
	return momentum

# 更新梯度动量
def update_momentum(layer_dims, momentum, beta, grads):
	L = len(layer_dims) - 1  # 神经网络层数，不算输入层
	for l in range(1, L+1):  # Vdw1,Vdb1,Vdw2,Vdb2,...,VdwL,VdbL
		momentum['VdW' + str(l)] = beta * momentum['VdW' + str(l)] + (1-beta) * grads['dW' + str(l)]
		momentum['Vdb' + str(l)] = beta * momentum['Vdb' + str(l)] + (1-beta) * grads['db' + str(l)]
	return momentum

# 更新参数
def update_parameters(layer_dims, parameters, momentum, learning_rate):
	L = len(layer_dims) - 1  # 神经网络层数
	for l in range(1, L+1):  # w1,b1,w2,b2,...,wL,bL
		parameters['W' + str(l)] -= learning_rate * momentum['VdW' + str(l)]
		parameters['b' + str(l)] -= learning_rate * momentum['Vdb' + str(l)]
	return parameters

beta = 0.9  # 动量参数通常设置为0.9
```


## 均方根传播算法 RMSprop

均方根传播算法 RMSprop (Root Mean Square Propagation) 是另一种加速模型收敛的算法，其思路是抑制梯度大的的参数梯度更新，增大梯度小的参数梯度更新。

数学公式如下：

* 初始化 $SdW = 0, SdW \in \mathbb{R}^{(n[l], n[l-1])}; Sdb = 0, Sdb \in \mathbb{R}^{(n[l],1)}$ ，即 $SdW, Sdb$ 的维度和 $W, dW, b, db$ 的维度一致
* 更新动量 $SdW = \beta SdW + (1 - \beta) dW^2, Sdb = \beta Vdb + (1 - \beta) db^2$ 
* 更新参数 $W = W - \alpha \frac{dW}{\sqrt{SdW}}, b = b - \alpha \frac{db}{\sqrt {Sdb}}$ 

示例代码如下：

```python
import numpy as np

# 初始化RMSprop动量
def initialize_RMSprop(layer_dims):
	RMSprop = {}
	L = len(layer_dims) - 1  # 神经网络层数，不算输入层
	for l in range(1, L+1):  # Sdw1,Sdb1,Sdw2,Sdb2,...,SdwL,SdbL
		RMSprop['SdW' + str(l)] = np.zeros((layer_dims[l], layer_dims[l-1]))
		RMSprop['Sdb' + str(l)] = np.zeros((layer_dims[l], 1))
	return RMSprop

# 更新RMSprop动量
def update_RMSprop(layer_dims, RMSprop, beta, grads):
	L = len(layer_dims) - 1  # 神经网络层数，不算输入层
	for l in range(1, L+1):  # Vdw1,Vdb1,Vdw2,Vdb2,...,VdwL,VdbL
		RMSprop['SdW' + str(l)] = beta * RMSprop['SdW' + str(l)] + (1-beta) * np.square(grads['dW' + str(l)])
		RMSprop['Sdb' + str(l)] = beta * RMSprop['Sdb' + str(l)] + (1-beta) * np.square(grads['db' + str(l)])
	return RMSprop

# 更新参数
def update_parameters(layer_dims, parameters, grads, RMSprop, learning_rate):
	L = len(layer_dims) - 1  # 神经网络层数
	epsilon = 1e-8
	for l in range(1, L+1):  # w1,b1,w2,b2,...,wL,bL
		parameters['W' + str(l)] -= learning_rate * grads['dW' + str(l)] / (np.sqrt(RMSprop['SdW' + str(l)]) + epsilon)
		parameters['b' + str(l)] -= learning_rate * grads['db' + str(l)] / (np.sqrt(RMSprop['Sdb' + str(l)]) + epsilon)
	return parameters

beta = 0.9  # 动量参数通常设置为0.9
```


## 自适应矩估计算法 Adam

自适应矩估计算法 Adam (Adaptive moment estimation) 是将动量法和 RMSprop 结合在一起的方法。

数学公式如下：

* 初始化 $VdW = 0; Vdb = 0; SdW = 0; Sdb = 0$ ，其中 $VdW, Vdb, SdW, Sdb$ 的维度和 $W, dW, b, db$ 的维度一致
* 更新动量 $VdW = \beta_1 VdW + (1 - \beta_1) dW, Vdb = \beta_1 Vdb + (1 - \beta_1) db$ 
* 更新动量 $SdW = \beta_2 SdW + (1 - \beta_2) dW^2, Sdb = \beta_2 Vdb + (1 - \beta_2) db^2$ 
* 偏差矫正 $VdW^{corrected} = VdW / (1 - \beta_1^{\{t\}}), Vdb^{corrected} = Vdb / (1 - \beta_1^{\{t\}})$ 
* 偏差矫正 $SdW^{corrected} = SdW / (1 - \beta_2^{\{t\}}), Sdb^{corrected} = Sdb / (1 - \beta_2^{\{t\}})$ 
* 更新参数 $W = W - \alpha \frac{VdW^{corrected}}{\sqrt{SdW^{corrected} + \epsilon}}, b = b - \alpha \frac{Vdb^{corrected}}{\sqrt{Sdb^{corrected} + \epsilon}}$ 
* 通常 $\beta_1 = 0.9, \beta_2 = 0.999, \epsilon = 1e^{-8}$
* 更新参数 $W = W - \alpha \frac{dW}{\sqrt{SdW}}, b = b - \alpha \frac{db}{\sqrt {Sdb}}$ 

示例代码如下：

```python
# 初始化adam
def initialize_adam(layer_dims):
	adam = {}
	L = len(layer_dims) - 1  # 神经网络层数，不算输入层
	for l in range(1, L+1):
		adam['VdW' + str(l)] = np.zeros((layer_dims[l], layer_dims[l-1]))
		adam['Vdb' + str(l)] = np.zeros((layer_dims[l], 1))
		adam['SdW' + str(l)] = np.zeros((layer_dims[l], layer_dims[l-1]))
		adam['Sdb' + str(l)] = np.zeros((layer_dims[l], 1))
	return adam

# 更新adam
def update_adam(layer_dims, adam, beta1, beta2, grads):
	L = len(layer_dims) - 1  # 神经网络层数，不算输入层
	for l in range(1, L+1):
		adam['VdW' + str(l)] = beta * adam['VdW' + str(l)] + (1-beta) * grads['dW' + str(l)]
		adam['Vdb' + str(l)] = beta * adam['Vdb' + str(l)] + (1-beta) * grads['db' + str(l)]
		adam['SdW' + str(l)] = beta * adam['SdW' + str(l)] + (1-beta) * np.square(grads['dW' + str(l)])
		adam['Sdb' + str(l)] = beta * adam['Sdb' + str(l)] + (1-beta) * np.square(grads['db' + str(l)])
	return adam

# 动量修正
def correct_adam(layer_dims, adam, beta1, beta2, t):
	adam_corr = {}
	L = len(layer_dims) - 1  # 神经网络层数，不算输入层
	for l in range(1, L+1):
		adam_corr['VdW' + str(l)] = adam['VdW' + str(l)] / (1 - beta1 ** t)
		adam_corr['Vdb' + str(l)] = adam['Vdb' + str(l)] / (1 - beta1 ** t)
		adam_corr['SdW' + str(l)] = adam['SdW' + str(l)] / (1 - beta2 ** t)
		adam_corr['Sdb' + str(l)] = adam['Sdb' + str(l)] / (1 - beta2 ** t)
	return adam_corr

# 更新参数
def update_parameters(layer_dims, parameters, adam_corr, learning_rate):
	L = len(layer_dims) - 1  # 神经网络层数
	epsilon = 1e-8
	for l in range(1, L+1):  # w1,b1,w2,b2,...,wL,bL
		parameters['W' + str(l)] -= learning_rate * adam_corr['VdW' + str(l)] / (np.sqrt(adam_corr['SdW' + str(l)]) + epsilon)
		parameters['b' + str(l)] -= learning_rate * adam_corr['Sdb' + str(l)] / (np.sqrt(adam_corr['Sdb' + str(l)]) + epsilon)
	return parameters

beta1 = 0.9
beta2 = 0.999
```


## 学习率衰减

学习率衰减可以加快模型收敛。

数学公式如下：

* 随循环次数衰减的学习率 $\alpha = \frac{1}{1 + \text{decay rate } * \text{ epoch num}}$ 
* 随循环次数指数衰减的学习率 $\alpha = 0.95 ^ {epoch num} · \alpha_0$ 
* 随循环次数衰减的学习率 $\alpha = \frac{k}{\sqrt{epoch num}} · \alpha_0$ 
* 离散衰减的学习率 $\alpha = k, epoch-num < ti$ 

示例代码如下：

```python
alpha = 1 / (1 + 0.05 * i)
```


# 批量归一化 Batch Norm

对神经网络模型隐藏层的输出执行批量归一化有助于模型的快速收敛。即： $z^{[l]} -> \tilde{z}^{[l]} -> a^{[l]}$ 这是更常见的版本，也有归一化 $a^{[l]}$ 的版本。执行输出的批量归一化需要同时更新正向传播和反向传播算法。

数学公式如下：

* 计算隐藏层输出的平均值： $\mu = \frac{1}{m} \sum_{i=1}^{m} z^{(i)}$ 
* 计算隐藏层输出的方差： $\sigma^2 = \frac{1}{m} \sum_{i=1}^{m} (z^{(i)} - \mu)^2$ 
* 对隐藏层输入进行归一化处理： $z_{norm}^{(i)} = \frac{z^{(i)} - \mu}{\sqrt{\sigma^2 + \epsilon}}$ 
* 对归一化后的隐藏层进行灵活调整： $\tilde{z}^{(i)} = \gamma · z_{norm}^{(i)} + \beta$ ，其中 $\gamma, \beta$ 是可以学习的参数

示例代码如下：

```python
def batch_normalization(x, gamma=1.0, beta=0.0, eps=1e-8, axis=0):
	"""
	批量归一化操作

	参数:
		x : 输入数据，形状为任意维度数组，如 (batch_size, features) 或 (batch, channel, H, W)
		gamma : 缩放参数，默认为1.0
		beta : 偏移参数，默认为0.0
		eps : 防除零常数，默认为1e-5
		axis : 归一化的轴（默认为0，即对每个特征独立归一化）

	返回:
		归一化后的数据，形状与x相同
	"""
	# 计算均值和方差
	mu = np.mean(x, axis=axis, keepdims=True)  # 保持维度以支持广播
	var = np.var(x, axis=axis, keepdims=True)

	# 标准化
	x_normalized = (x - mu) / np.sqrt(var + eps)

	# 缩放和偏移（gamma和beta需与x_normalized兼容）
	out = gamma * x_normalized + beta
	return out
```

批量归一化操作不是正则化操作，但是对正则化有少量作用。



# Softmax 回归

softmax 回归是对二元逻辑回归的拓展，支持对多个类别进行分类。即在输出层不使用激活函数，而是使用 softmax 函数将多个输出总和概率归一到 1。

数学公式如下：

* 令 $t_i = e^{z^{[L]}}$ ，输出经过 softmax 函数转换： $a^{[L]} = \frac{t_i}{\sum_{j=1}^{n[L]} t_i}$ 

示例代码如下：

```python
def softmax(x):
	exp_Z = np.exp(Z)
	sum_exp_Z = np.sum(exp_Z, axis=0, keepdims=True)
	return exp_Z / sum_exp_Z
```

在输出层使用 softmax 函数时，反向传播算法需要同步更新。


# 与人类的表现做比较

通过比较机器学习模型和人的表现，可以知道机器学习模型的效果。

在某些领域，例如图像识别，人的表现已经接近于贝叶斯最优误差。因此在这些领域中，如果模型的误差已经接近于人的表现，那么可以代表模型已经相当优秀。具体取决于模型应用的领域。

人的表现也可以划分具体的人群。在某些情况下，可以将模型与专家的表现相对比，在另一些情况下，可以将模型与普通人的表现相对比。具体取决于模型的应用场景。

随着模型的表现接近或超过人类的表现，模型的训练会越发困难。这可能是因为对数据的观测。


# 神经网络模型中的超参数

超参数包括：

* 神经网络模型层数 $L$ 
* 隐藏层的神经元数量 $n^{[l]}$ 
* 隐藏层的激活函数 $g^{[l]}$ 
* 输出层的激活函数 $g^{[L]}$ 
* 学习率 $\alpha$ 
* 小样本数量 $mini-batch \ size \ t$ 
* 学习率衰减 $decay-rate$ 
* 迭代次数 $iterations$ 
* 梯度下降优化参数 $\beta_1 = 0.9, \beta_2 = 0.999, \epsilon = 1e^{-8}$ 
* ……


选择超参数的方式：

* 在可行空间内随机采样，而非均匀采样
* 由粗到细


## 评估和调整超参数以提高机器学习性能

训练模型通常需要两步：

* 拟合训练集
* 拟合验证集/测试集

在拟合训练集时，主要解决高偏差问题（欠拟合）：

* 比较训练集误差和人类的水平，判断机器学习模型的效果
* 增加更多的训练数据
* 调整优化算法
* 调整神经网络模型结构


在拟合验证集/测试集时，主要解决高方差问题（过拟合）：

* 比较训练集和验证集/测试集的误差，判断是否存在过拟合问题
* 增加正则化
* 调整神经网络模型结构


有时候手工进行误差分析会很有帮助。


# 多任务学习

在具备以下场景时，可以尝试使用同一个神经网络模型同时进行多个任务的学习。

* 猜测多个任务具有相似的底层特征，即底层特征可以互相有帮助。
* 通常，多个任务具有相同的训练数据量。
* 通常，应用于大规模神经网络的训练。


# 迁移学习

在具备以下场景时，可以尝试使用迁移学习。即应用已经调试好的模型，修改模型最后的输出层或最后的几层，来适配新的任务。

* 任务 A 和任务 B 具有相同的输入。
* 任务 A 的训练数据量比任务 B 的训练数据量多。
* 猜测任务 A 的低层特征对与任务 B 有帮助。


迁移学习可以具体分为 3 个层次：

* 固定已有权重，新增和重新训练一层输出层，适用于数据量较小的场景，消耗资源少
* 固定已有权重，新增和重新训练多层输出层，适用于数据量中等的场景，消耗资源一般
* 使用已有权重作为初始参数，重新训练整个模型，适用于数据量较多的场景，消耗资源多


# 数据扩充

图像数据扩充方式：

* 特定区域随机裁剪
* 旋转
* 颜色偏移
* 




# 端到端深度学习

在具备以下场景时，可以尝试使用直接从原始输入到最终输出的端到端深度学习，而无需分解和建立中间任务。

* 原始输入到最终输出具有足够多的数据量，而中间任务缺少足够的数据量。

这样的模型由于缺少人工设计，可能会有较好的表现，也可能会表现的不如人类。


# 视觉模型-卷积神经网络CNN

计算机视觉问题包括：

* 物体识别
* 物体检测
* 图片风格转换

图像在计算机中使用像素点来存储，8位存储的图像中每个像素点的取值是 0-255 的数字（如果是16位存储则是0-65535）。

训练计算机视觉模型的主要问题是特征数量太多。图片的基本组成是像素，800 万像素的摄像头拍摄的照片大约是 3200 * 2400 像素，即输入特征大约有 800 万个。这种情况下构建的神经网络模型参数非常多，计算需要消耗大量的资源。

因此人们设计了卷积神经网络，通过构建过滤器（卷积核），使用卷积计算识别图像中的特征。通过识别图像特征，解决图像识别、图像转换等问题。

卷积神经网络的几个基本概念：

* 过滤器（卷积核） filter
* 填充 padding
* 步长 stride


## 过滤器（卷积核）与卷积计算

过滤器（卷积核）：大小为 $f \times f$ 的矩阵。过滤器是卷积神经网络要训练的模型参数。

卷积计算：逐个计算输入矩阵上与卷积核相同大小的矩阵，和过滤器（卷积核）逐元素乘法后再求和，作为输出矩阵的元素。假设输入图像的大小是 $n \times n$ ，则计算输出的图像是 $n-f+1 \times n-f+1$ 

卷积计算形象化的理解：用一个小型“过滤器”在输入矩阵上滑动，每一步将过滤器与对应区域的数据逐元素相乘后再求和，生成新的特征值。这一过程像“扫描”图像，通过不同过滤器提取边缘、纹理等局部特征。

常见的卷积核大小是 3 × 3，但也会存在 5 × 5 或 7 × 7 大小的卷积核。卷积核的维度通常为奇数，几乎没有偶数。

数学表示如下：

$\left[ \begin{matrix}
n_{11} & n_{12} & n_{13} & \cdots & n_{1y} \\
n_{21} & n_{22} & n_{23} & \cdots & n_{2y} \\
n_{31} & n_{32} & n_{33} & \cdots & n_{3y} \\
\vdots \\
n_{x1} & n_{x2} & n_{x3} & \cdots & n_{xy} \\
\end{matrix} \right]
\times
\left[ \begin{matrix}
w_{11} & w_{12} & w_{13} \\
w_{21} & w_{22} & w_{23} \\
w_{31} & w_{32} & w_{33} \\
\end{matrix} \right]
= 
\left[ \begin{matrix}
\sum_{i=1}^3 \sum_{j=1}^3 n_{ij}*w_{ij} & \cdots \\
\vdots \\
\end{matrix} \right]$ 


常见的初始化卷积核例如：

* 垂直卷积核： $\left[ \begin{matrix} 
1 & 0 & -1 \\
1 & 0 & -1 \\
1 & 0 & -1 \\
\end{matrix} \right]$ 
* 水平卷积核： $\left[ \begin{matrix} 
1 & 1 & 1 \\
0 & 0 & 0 \\
-1 & -1 & -1 \\
\end{matrix} \right]$ 
* sobel filter ： $\left[ \begin{matrix} 
1 & 0 & -1 \\
2 & 0 & -2 \\
1 & 0 & -1 \\
\end{matrix} \right]$ 
* schar filter： $\left[ \begin{matrix} 
3 & 0 & -3 \\
10 & 0 & -10 \\
3 & 0 & -3 \\
\end{matrix} \right]$ 


## 填充

卷积计算后的矩阵大小为 $n-f+1 \times n-f+1$ 。可以看到，当 $f > 1$ 时，经过卷积计算后图片会缩小（丢弃了边缘信息）。为了使图片的输入和输出的信息一致，人们可以对输入图片进行一定的填充（扩展）。

填充：在输入图像的边缘填充$2p$ 的大小，填充的数据取值为 0。

因此，假设输入图像的大小是 $n \times n$ ，经过填充后图像的大小变为 $n+2p \times n+2p$ 。卷积核大小 $f \times f$ ，则经过卷积计算后输出的图像大小是 $n+2p-f+1 \times n+2p-f+1$ 。

填充是一种可选项，对此有两种术语：

* 有效卷积：不经过填充，卷积计算过程中所有信息都是有效的。
* 相同卷积：经过填充后，输出图像的大小和输入图像的大小相同，即 $p = \frac{f-1}{2}$ 。在计算机视觉中，$f$ 通常是奇数。


## 步长

步长：卷积计算时可以选择计算的间隔，即步长。

假设卷积计算的步长为 $s$ ，输入图像的大小是 $n \times n$ ，在输入图像的边缘填充 $2p$ 的大小，卷积核大小是 $f \times f$ ，则计算输出图像的大小是 $\frac{n+2p-f}{s}+1 \times \frac{n+2p-f}{s}+1$ 。

特别的，如果最后一步超过了输入矩阵的边界，则丢弃计算结果。即输出图像的大小是 $(\lfloor \frac{n+2p-f}{s}+1 \rfloor \times \lfloor \frac{n+2p-f}{s}+1) \rfloor$ 。

在有步长的卷积计算中，为了使输入和输出具有相同的维度，在确定输入图像的大小 $n$ 和卷积核的大小 $f$ 的情况下，需要使 $p = \frac{(n-1)s-n+f}{2}$ 。


## 多维卷积

图像通常使用多个通道定义，每个通道存储图像某一个维度的信息。例如RGB图像有3个通道，定义红绿蓝。

在卷积计算中，为了识别图像特征，需要定义多维度的卷积核，其维度与输入图像的维度相同。

多维度的卷积计算和二维的卷积计算一致，都是在输入矩阵中逐一取和卷积核大小相同的矩阵，和卷积核逐元素相乘后再求和，生成输出矩阵。

假设输入图像的大小是 $n_H \times n_W \times C$ ，填充为 0，步长为 1，卷积核大小 $f \times f \times C$ ，则计算输出的图像是 $n_H+2p-f+1 \times n_W+2p-f+1$ 。


## 卷积神经网络的分层

卷积神经网络通常由三层组成：卷积层、池化层、全连接层。


## 卷积层

卷积层执行卷积计算，用于提取图片的特征。

输入：

* 第 $l$ 层的输入图像的大小为 $n_H^{[l]} \times n_W^{[l]} \times n_C^{[l]}$ 。
* 输入图像的填充大小为 $p^{[l]}$ 。
* 步长的大小为 $s^{[l]}$ 。
* 过滤器的大小为 $f^{[l]} \times f^{[l]} \times n_C^{[l]}$ 。
* 过滤器的数量小为 $n^{[l]}$ 。

计算：

* 逐个过滤器执行卷积计算

输出：

* 第 $l+1$ 层的输入图像的大小为 $n_H^{[l+1]} \times n_W^{[l+1]} \times n_C^{[l+1]}$ ，其中 $n_C^{[l]} = n^{[l]}$ 。

过滤器中的数据即为参数，参数量级为 $f^{[l]} \times f^{[l]} \times n_C^{[l]} \times n^{[l]}$ 。


## 池化层

池化层对卷积计算进行降维，直觉上的意义在于提取最有可能的特征/平均特征。

池化层的计算和卷积计算相类似，在输入矩阵中逐一计算和池化核（池化窗口）大小的矩阵，但不是逐元素相乘再求和，而是求最大值/平均值。

输入：

* 第 $l$ 层的输入图像的大小为 $n_H^{[l]} \times n_W^{[l]} \times n_C^{[l]}$ 。
* 池化层大小 $f \times f$ 。
* 池化层步长 $s$ 。
* 池化层通常没有填充 $p$ ，如果有的话加入计算即可。

计算：

* 最大化池 max pool：取最大值
* 平均化池 avg pool：取平均值

输出：

* 第 $l$ 层的输出图像的大小为 $\frac{n_H^{[l]}+f-1}{s} \times \frac{n_W^{[l]}+f-1}{s} \times n_C^{[l]}$ 。


## 全连接层

全连接层用于计算卷积神经网络的输出。它是一个简单的神经网络，并常在输出层使用 softmax 函数识别出图像的分类。


## 经典的卷积神经网络

LeNet-5 模型

* input: 32×32×1
* filter 1: f = 5, s = 1, p = 0, n = 6; -> 28×28×6
* avg pool 1: f = 2, s = 2; -> 14×14×6
* filter 2: f = 5, s = 1, p = 0, n = 16; -> 10×10×16
* avg pool 2: f = 2, s = 2; -> 5×5×16
* FC 3: n = 120; -> 120
* FC 4: n = 84; -> 84
* output 5: n = 10; -> 10


Alex 模型

* input: 227×227×3
* filter 1: f = 11, s = 4, p = 0, n = 96; -> 55×55×96
* max pool 1: f = 3, s = 2; -> 27×27×96
* filter 2: f = 5, s = 1, p = 2, n = 256; -> 27×27×256
* max pool 2: f = 3, s = 2; -> 13×13×256
* filter 3: f = 3, s = 1, p = 1, n = 384; -> 13×13×384
* filter 4: f = 3, s = 1, p = 1, n = 384; -> 13×13×384
* filter 5: f = 3, s = 1, p = 1, n = 256; -> 13×13×256
* max pool 5: f = 3, s = 2; -> 6×6×256
* FC 6: n = 4096; -> 4096
* FC 7: n = 4096; -> 4096
* output 8: n = 1000; -> 1000


VGG-16 模型

* input: 224×224×1
* filter 1: f = 3, s = 1, p = 1, n = 64; -> 224×224×64
* filter 2: f = 3, s = 1, p = 1, n = 64; -> 224×224×64
* max pool 2: f = 2, s = 2; -> 112×112×64
* filter 3: f = 3, s = 1, p = 1, n = 128; -> 112×112×128
* filter 4: f = 3, s = 1, p = 1, n = 128; -> 112×112×128
* max pool 4: f = 2, s = 2; -> 56×56×128
* filter 5: f = 3, s = 1, p = 1, n = 256; -> 56×56×256
* filter 6: f = 3, s = 1, p = 1, n = 256; -> 56×56×256
* filter 7: f = 3, s = 1, p = 1, n = 256; -> 56×56×256
* max pool 7: f = 2, s = 2; -> 28×28×256
* filter 8: f = 3, s = 1, p = 1, n = 512; -> 28×28×512
* filter 9: f = 3, s = 1, p = 1, n = 512; -> 28×28×512
* filter 10: f = 3, s = 1, p = 1, n = 512; -> 28×28×512
* max pool 10: f = 2, s = 2; -> 14×14×512
* filter 11: f = 3, s = 1, p = 1, n = 512; -> 14×14×512
* filter 12: f = 3, s = 1, p = 1, n = 512; -> 14×14×512
* filter 13: f = 3, s = 1, p = 1, n = 512; -> 14×14×512
* max pool 13: f = 2, s = 2; -> 7×7×512
* FC 14: n = 4096; -> 4096
* FC 15: n = 4096; -> 4096
* output 16: n = 1000; -> 1000


## 残差网络模型

Residual Networks (ResNet) 在计算下一层 $l+1$ 的输出时，不仅使用当层 $l$ 的输入，还使用前一层 $l-1$ 的输入。这里把前一层 $l-1$ 的输入视为残差（保留下来的特征）。

输入：

* 第 $l-1$ 层的输入 $a^{[l-1]}$ 
* 第 $l$ 层的输入 $a^{[l]}$ 
* 第 $l+1$ 层的参数 $W^{[l]}$ 和偏置 $b^{[l]}$ 

计算：

* $z^{[l+1]} = W^{[l+1]} · a^{[l]} + b^{[l+1]}$ 
* $a^{[l+1]} = g(z^{[l+1]} + a^{[l-1]})$ 

输出：

* $a^{[l+1]}$ 

通常在每两层之间使用残差网络，不会连续使用。

也可以选择将输入数据作为残差，用于每一层的处理。


## Inception网络模型（GoogleNet）

Inception 网络支持设定多个卷积核和池化核，同时验证多个特征。

输入：

* 输入图像的大小为 $n_H \times n_W \times n_C$ 。
* 卷积核 1 的大小 $f_1 \times f_1 \times n_C$ ，填充 $2p_1$，步长 $s_1$ ，卷积核 1 数量 $n_1$ 
* 卷积核 2 的大小 $f_2 \times f_2 \times n_C$ ，填充 $2p_2$，步长 $s_2$ ，卷积核 2 数量 $n_2$ 
* ……
* 池化核 1 的大小 $pf_1 \times pf_1$ ，填充 $2pp_1$，步长 $ps_2$ 
* 池化核 2 的大小 $pf_2 \times pf_2$ ，填充 $2pp_2$，步长 $ps_2$ 
* ……

计算：

* 保证输入图像和输出图像具有相同的大小

输出：

* 卷积核 1 的输出： $n_H  \times n_W \times n_1$ 。
* 卷积核 2 的输出： $n_H  \times n_W \times n_2$ 。
* ……
* 池化核 1 的输出： $n_H  \times n_W \times n_C$ 。
* 池化核 2 的输出： $n_H  \times n_W \times n_C$ 。
* ……
* 组合上述输出，作为 Inception 层的输出 $n_H  \times n_W \times (n_1 + n_2 + \cdots + n_C + n_C + \cdots)$ 。


在 Inception 网络中，计算量通常会特别巨大。

为了避免这个问题，通常可以使用 $n$ 个 $1 \times 1 \times n_C$ 卷积核，对输入图像进行降维，再进行最终的输出。

举例如下：

* 原始计算：
	* 输入矩阵 28 × 28 × 192，32 个卷积核 5 × 5 × 192，输出矩阵 28 × 28 × 32。
	* 计算量大约是 28 * 28 * 32 * 5 * 5 * 192 = 1.2亿。
	* 理解这一过程：一次卷积计算的计算量是 5 * 5 * 192，计算后的输出矩阵是 28 * 28 * 32，因此计算量大约是28 * 28 * 32 * 5 * 5 * 192
* 使用 $1 \times 1$ 矩阵降维：
	* 输入矩阵 28 × 28 × 192，16 个卷积核 1 × 1 × 192，输出矩阵 28 × 28 × 16。
	* 输入矩阵 28 × 28 × 16，32 个卷积核 5 × 5 × 16，输出矩阵 28 × 28 × 32。
	* 计算量大约是 28 * 28 * 16 * 1 * 1 * 192 + 28 * 28 * 32 * 5 * 5 * 16 = 0.12亿。
* 通过使用 $1 \times 1$ 矩阵降维，可以极大地压缩计算量，这通常是一种很好的选择。

Inception 网络就是通过 Inception 模块聚合而来。


## 卷积神经网络的代码实现

```python



```


## 目标定位

识别目标定位，输出：

* 是否检测到目标
* 目标中心点位横坐标 bx
* 目标中心点位纵坐标 by
* 目标宽度 bw
* 目标高度 bh

扩展地，如果不仅要识别一目标，可以扩展到多个目标（例如道路物体检测），或者目标的多个点位（例如车辆的各个部位）


## 卷积实现滑动窗口检测

## YOLO 算法


# 序列模型

## 统计工具

* 当前数据跟之前观察到的数据相关
* 在时间 $t$ 观察到 $x_t$，那么得到 $T$ 个不独立的随机变量 $(x_1, x_2, \dots, x_T) \sim p(\mathrm{x})$ 
* 使用条件概率展开 $p(a, b) = p(a)p(b|a) = p(b)p(a|b)$ 

那么有：

* $p(\mathrm{x}) = p(x_1) · p(x_2 | x_1) · p(x_3 | x_1, x_2) \dots p(x_T | x_1, x_2, \cdots, x_{T-1})$ 
* $p(\mathrm{x}) = p(x_T) · p(x_{T-1} | x_T) · p(x_{T-2} | x_{T-1}, x_{T}) \dots p(x_1 | x_2, x_3, \dots, x_T)$ 

## 自回归模型

序列模型对条件概率建模（自回归模型）：

* $p(x_t | x_1, \dots, x_{t-1}) = p(x_t | f(x_1, \dots, x_{t-1}))$ 


## 马尔可夫假设

假设当前数据只跟 $\tau$ 个过去数据点相关：

* $p(x_t | x_1, \dots, x_{t-1}) \approx p(x_t | x_{t-\tau}, \dots, x_{t-1}) = p(x_t | f(x_{t-\tau}, \dots, x_{t-1}))$ 


理解：
在马尔科夫假设中，未来只与当下有关，而与过去无关。
当下是存在的。
当下的信息包含着过去。


## 潜变量模型

使用潜变量 $h_t$ 来表示过去信息 $h_t = f(x1, \dots, x_{t-1})$ ，因此 $x_t = p(x_t | h_t)$

隐变量和潜变量的区别：

* 隐变量hidden variable：真实存在，只是暂时没有观察到
* 潜变量latent variable：不能直接观察到，但是可以通过其他变量推断存在

在深度学习领域，这两个概念没有差异，可以互换使用。


理解：
使用高纬度+高精度的数学向量来表示信息。


## 潜变量自回归模型

使用潜变量 $h_t$ 来表示过去信息 $h_t = f(x1, \dots, x_{t-1})$ ，并且当前信息 $x_t = p(x_t | h_t, x_{t-1})$ 


# 序列模型-循环神经网络RNN

## 模型假设

循环神经网络使用潜变量自回归模型假设：每一层的输出不仅与自身的输入有关，还与之前的输入和输出有关。

用数学公式表示：

* 隐藏状态 $h_t = \sigma_h(W_{hh} \cdot h_{t-1} + W_{hx} \cdot x_{t-1} + b_h)$ ，第 $t$ 层的隐藏状态和第 $t-1$ 层的隐藏状态和输入有关
* 输出 $o_t = \sigma_o(W_{ho} \cdot h_t + b_o)$ ，第 $t$ 层的输出和第 $t$ 层的隐藏状态有关

![image-20250521164010017](./深度学习.assets/image-20250521164010017.png)

![image-20250625144511047](./深度学习.assets/image-20250625144511047.png)


## 模型评估

衡量一个语言模型的好坏可以用平均交叉熵 $\pi = \frac{1}{n} \sum_{i=1}{n} - log p(x_t | x_{t-1}, \dots)$ 。

历史原因 NLP 使用困惑度（perplexity） $exp(\pi)$ 来衡量。


## 前向传播

* $h_0 = 0$ 
* $z_t = x_{t-1} \cdot w_{xh} + h_{t-1} \cdot w_{hh} + b_{h}$ 
* $h_t = tanh(z_t)$ 
* $o_t = h_t \cdot w_{ho} + b_o$ 
* $\hat{y_t} = softmax(o_t)$ 


## 反向传播

* 定义损失函数 $L = \sum_{t=1}^T L_t$ ，其中 $L_t = -y_t\top \cdot log \hat{y_t}$ 
* 计算 $\frac{\partial L}{\partial o_t} = \hat{y_t} - y_t$ 。【注意】：此处链式法则推导较为复杂，直接使用结论，推导过程参考下图。
* 计算 $ dw_ho = \frac{\partial L}{\partial o_t} \cdot \frac{\partial o_t}{\partial w_ho} = (\hat{y_t} - y_t) \cdot h_t$
* 计算 $ db_ho = \frac{\partial L}{\partial o_t} \cdot \frac{\partial o_t}{\partial b_ho} = \hat{y_t} - y_t$
* 计算 $ dw_xhh = \frac{\partial L}{\partial o_t} \cdot \frac{\partial o_t}{\partial h_t} \cdot \frac{\partial h_t}{\partial z_t} \cdot \frac{\partial z_t}{\partial w_{xhh}}$ 。【注意】：此处链式法则推导较为复杂，推导过程参考下图。
* 计算 $ dw_xh $ 和 $ db_xh $ 的过程同上，不做展开。

[RNN的反向传播推导与numpy实现 - 知乎](https://zhuanlan.zhihu.com/p/371849556)


![image-20250630152708559](./深度学习.assets/image-20250630152708559.png)

![image-20250630153414910](./深度学习.assets/image-20250630153414910.png)

## 演示代码

参考 ML_RNN.ipynb

从训练过程和训练结果来看，RNN 只是单纯记住了信息。


# 序列模型-长短期记忆网络LSTM


## 模型假设

长短期记忆网络在 RNN 的基础上，增加了记忆单元、候选记忆单元、三个门：遗忘门、输入门、输出门。

* 候选记忆单元：当前输入对记忆的影响
* 输入门：决定候选记忆单元生成的记忆单元
* 遗忘门：遗忘历史记忆的程度
* 记忆单元：当前的记忆
* 输出门：当前记忆对输出的影响

用数学公式表示：

* 候选记忆单元 $\tilde{c}_t = tanh(w_{xc} \cdot x_t + w_{hc} \cdot h_{t-1} + b_c)$ 

* 遗忘门 $f_t = sigmoid(w_{xf} \cdot x_t + w_{hf} \cdot h_{t-1} + b_f)$ 
* 输入门 $i_t = sigmoid(w_{xi} \cdot x_t + w_{hi} \cdot h_{t-1} + b_i)$ 
* 记忆单元 $c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t $ 

* 输出门 $o_t = sigmoid(w_{xo} \cdot x_t + w_{ho} \cdot h_{t-1} + b_o)$ 
* 隐藏状态 $h_t = o_t \odot tanh(c_t)$ 


## 前向传播

* $h_0 = 0$ 
* $c_0 = 0$ 
* $f_t = sigmoid(w_{xf} \cdot x_{t-1} + w_{hf} \cdot h_{t-1} + b_f)$ 
* $i_t = sigmoid(w_{xi} \cdot x_{t-1} + w_{hi} \cdot h_{t-1} + b_i)$ 
* $o_t = sigmoid(w_{xo} \cdot x_{t-1} + w_{ho} \cdot h_{t-1} + b_o)$ 
* $\tilde{c}_t = tanh(w_{xc} \cdot x_{t-1} + w_{hc} \cdot h_{t-1} + b_c)$ 
* $c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$ 
* $h_t = o_t \odot tanh(c_t)$ 
* $\hat{y}_t = softmax(w_{hy} \cdot h_t + b_y)$ 


## 反向传播

* 定义损失函数 $L = \sum_{t=1}^T L_t$ ，其中 $L_t = -y_t\top \cdot log \hat{y_t}$ 
* 计算 $\frac{\partial L}{\partial h_t}$

从后一个时间步传递的梯度
```python
dh_next = dh_{t+1}
dm_next = dm_{t+1}
```


当前时间步梯度计算
```python
dy_t = y_h - y
dw_hy = dy_t @ dh_next.T
db_y = dy_t

dh_t = (w_hy^T @ dy_t) + dh_next  # 输出层梯度 + 来自后续时刻的梯度
do_t = dh_t * np.tanh(m_t)        # 输出门梯度
d_o_raw = do_t * o_t * (1 - o_t)  # sigmoid反向传播

d_tanh_mt = dh_t * o_t            # tanh(m_t)的梯度
dm_t = d_tanh_mt * (1 - np.tanh(m_t)**2) + dm_next  # 记忆单元总梯度

df_t = dm_t * m_{t-1}             # 遗忘门梯度
d_f_raw = df_t * f_t * (1 - f_t)  # sigmoid反向传播

di_t = dm_t * m_tilde_t           # 输入门梯度
d_i_raw = di_t * i_t * (1 - i_t)  # sigmoid反向传播

dm_tilde_t = dm_t * i_t           # 候选记忆单元梯度
d_m_tilde_raw = dm_tilde_t * (1 - m_tilde_t**2)     # tanh反向传播
```


参数梯度（累加）
```python
dw_xo += d_o_raw @ x_t.T
dw_ho += d_o_raw @ h_{t-1}.T
db_o += d_o_raw

dw_xi += d_i_raw @ x_t.T
dw_hi += d_i_raw @ h_{t-1}.T
db_i += d_i_raw

dw_xf += d_f_raw @ x_t.T
dw_hf += d_f_raw @ h_{t-1}.T
db_f += d_f_raw

dw_xm += d_m_tilde_raw @ x_t.T
dw_hm += d_m_tilde_raw @ h_{t-1}.T
db_m += d_m_tilde_raw
```


传递给前一时间步的梯度
```python
dh_prev = (w_hf^T @ d_f_raw) + (w_hi^T @ d_i_raw) + (w_ho^T @ d_o_raw) + (w_hm^T @ d_m_tilde_raw)
dm_prev = f_t * dm_t  # 遗忘门作用
```

![image-20250707180317325](./深度学习.assets/image-20250707180317325.png)


# 序列模型-Transformer

## 注意力机制

注意力机制的核心思想是让模型能够动态地关注输入中与当前任务最相关的部分。本质是计算相关性。

心理学上讲，动物需要在复杂环境下有效关注值得注意的点（随意线索和不随意线索）。

以下简述注意力机制的历史：


### 非参注意力池化层

* 给定已观测的统计数据 $(x_i, y_i), i = 1, \dots, n$ ，预测新的数据 $x_{n+1}, y_{n+1}$ 
* 最简单的方案是平均池化： $f(x) = \frac{1}{n} \sum_i y_i$ 
* 更好的方案是1960s提出的Nadaraya-Watson核回归，通过核函数对输入数据进行加权平均后，预测输出值： $f(x) = \sum_{i=1}^n \frac{K(x-x_i)}{\sum_{j=1}^n K(x-x_j)} y_i$ 。其中的 $K(u)$ 是核函数。
* 非参模型的优势是无需训练模型参数，只要找到合适的模型，就可以做预测

Nadaraya-Watson核回归举例：

* 假设使用高斯核 $k(u) = \frac{1}{\sqrt{2\pi}} exp(- \frac{u^2}{2})$ 
* 那么 $f(x) = \sum_{i=1}^n \frac{exp(-\frac{1}{2}(x-x_i)^2)}{\sum_{j=1}^n exp(-\frac{1}{2}(x-x_j)^2)} y_i = \sum_{i=1}^n softmax(-\frac{1}{2} (x-x_i)^2) y_i$ 。
* 这个函数可以理解为，预测一个新的值，是它和所有已观测到的样本之间的距离的函数，同时做了一定的柔和化处理

示例代码参考 ML_Attention.ipynb


### 带参注意力池化层

Nadaraya-Watson核回归举例：

* $f(x) = \sum_{i=1}^n softmax(-\frac{1}{2} ((x-x_i)w)^2) y_i$ ，这里的 $w$ 是可以学习的参数。

示例代码参考 ML_Attention.ipynb


### 注意力权重和注意力分数

一般的，注意力机制可以写作 $f(x) = \sum_i \alpha(x, x_i) y_i$ 。这里的 $\alpha(x, x_i)$ 就是注意力权重，注意力权重之和等于 1。

以Nadaraya-Watson核回归举例：函数 $f(x) = \sum_i \alpha(x, x_i) y_i = \sum_{i=1}^n softmax(-\frac{1}{2} (x-x_i)^2) y_i$ ，这里的 $-\frac{1}{2} (x-x_i)^2$ 就是注意力分数，经过 softmax 函数计算之后就是注意力权重。

更一般的（拓展到高维度）

假设 query $q \in \mathbb{R}^q$ ， $m$ 对 key-value $(k_1, v_1), \dots, (k_m, v_m)$ ，这里的 $k_i \in \mathbb{R}^k, v_i \in \mathbb{R}^v$ 。

那么注意力池化层：

$f(q,(k_1,v_1),\dots,(k_m,v_m)) = \sum_{i=1}^{m} \alpha(q,k_i)v_i$ 

其中 $\alpha(q, k_i) = softmax(a(q, k_i)) = \frac{exp(a(q, k_i))}{\sum_{j=1}^{m} exp(a(q, k_j))}$ ，这里的 $a(q, k_i)$ 就是注意力分数。

注意力分数是 query 和 key 的相似度，注意力权重是对注意力分数做 softmax 的结果。

因此，主要的问题是 $a$ 函数的设计。以下是两种常见的注意力分数计算：

1、Additive Attention：将 query 和 key 合并起来进入一个隐藏层大小为 h 输出大小为 1 的单隐藏层 MLP。

* 可学习参数 $W_k \in \mathbb{R}^{h \times k}, W_q \in \mathbb{R}^{h \times q}, W_v \in \mathbb{R}^{h}$ 
* $a(k, q) = W_v^T tanh(W_k k + W_q q)$ 

2、Scaled Dot-Product Attention：将 query 和 key 做点积运算（或缩放点积运算）

* 如果 query 和 key 都是同样的长度 $q,k \in \mathbb{R}^d$ ，那么可以 $a(q,k_i) = \langle q,k_i \rangle / \sqrt{d}$ 
* 向量化版本
* $Q \in \mathbb{R}^{n \times d}, K \in \mathbb{R}^{m \times d},V \in \mathbb{R}^{m \times v}$ ，其含义是：有 $n$ 个 $d$ 维的 query，有 $m$ 个 $d$ 维的 key 和 $v$ 维的value
* 注意力分数： $a(Q, K) = QK^T/\sqrt{d} \in \mathbb{R}^{n \times m}$ 
* 注意力池化： $f = softmax(a(Q, K))V \in \mathbb{R}^{n \times v}$ 

示例代码参考 ML_Attention.ipynb


为什么用相似度来表示注意力分数？
一个直观的例子，企业招聘员工的薪资水平，不能是来源于所有员工薪资的平均值，而需要参考相关员工的薪资水平。



关于注意力机制的历史，可参考：

![image-20250714144003293](D:\codes\study-notes\深度学习.assets\image-20250714144003293-1752475208797-1.png)


### 自注意力

给定输入序列 $x_1, \cdots, x_t, x_i \in \mathbb{R}^d$ ，

自注意力池化层将 $x_i$ 当作 query, key, value 来对序列抽取特征得到 $y_1, \cdots, y_t$ 。

这里的 $y_i = f(x_i, (x_1, x_1), \cdots, (x_t, x_t)) \in \mathbb{R}^d$ 。

和 CNN/RNN 不同，自注意力并没有记录位置信息，因此通常会通过位置编码将位置信息注入到输入里。

Transformer 架构的位置信息编码（第 i 行，第 2j 列和第 2j+1 列）：

假设长度为 $n$ 的输入序列 $X \in \mathbb{R}^{n \times d}$ ，那么使用位置编码矩阵 $P \in \mathbb{R}^{n \times d}$ 的 $X+P$ 作为自编码输入。其中有 $P_{i, 2j} = sin(\frac{i}{10000^{2j/d}}), P_{i, 2j+1} = cos(\frac{i}{10000^{2j/d}})$ 

$i$ 表示编码数据在序列中的位置，取值从 $0$ 到 $n$ 。
$j$ 表示编码数据维度的一半，取值从 $0$ 到 $d/2$ ，也就是 $2j$ 和 $2j+1$ 的取值从 $0$ 到 $d$ 。
$d$ 表示编码数据的维度。


示例代码参考 ML_Attention.ipynb


### 多头注意力



### Transformer 架构

transformer 是一个纯使用注意力的 encoder-decoder 架构。





# 预训练

预训练的思想来源于计算机视觉 CV 领域。

研究人员发现，在 CNN 模型中，越浅的层学到的特征越通用（横竖撇捺），越深的层学到的特征和具体任务的关联性越强（人脸-人脸轮廓、汽车-汽车轮廓）。对于任务 A 有一个已经训练好的模型，那么在对模型参数进行冻结或微调后，便可以在另一个相似的任务 B 中同样表现良好。

冻结：浅层参数不变。
微调：浅层参数会跟着任务 B 训练而改变。

具体来说，任务 B 对应的模型 B 的参数不再是随机初始化的，而是通过任务 A 进行预先训练得到模型 A，然后利用模型 A 的参数对模型 B 进行初始化，再通过任务 B 的数据对模型 B 进行训练。注：模型 B 的参数是随机初始化的。

也可以称为迁移学习。

在图像领域取得成功后，预训练的思想扩展到文本领域，同样取得了不错的效果。


# 高效微调（PEFT parameters effective fine tuning）

## LoRA

LoRA的数学原理
对于预训练权重矩阵 $W ∈ ℝ^{d×k}$ ，LoRA将其更新表示为：
ΔW = BA
其中：

B ∈ ℝ^{d×r}
A ∈ ℝ^{r×k}
r ≪ min(d,k) 是低秩维度

前向传播变为：
h = Wx + ΔWx = Wx + BAx


# Scaling Law 缩放定律

OpenAI 提出的 ​Scaling Laws（尺度定律）​​ ，主要指其团队在 2020 年发表的论文 Scaling Laws for Neural Language Models中揭示的核心规律。该研究基于大量实验（涵盖从百万参数到百亿参数的模型），系统地量化了模型规模、数据集大小、计算量和模型性能（损失）之间的关系，​开创了大语言模型（LLM）系统性缩放研究的先河，对后续模型发展产生了深远影响。

核心发现：性能可预测地随规模提升​

• ​关键结论：​​ 语言模型的测试损失 (L) 以可预测的幂律方式随着三个关键资源的增加而下降：
•​ 模型参数量 (N)​​
•​ 数据集大小 (D)​​
• ​训练计算量 (C)​​ （通常以训练期间消耗的 FLOPs 衡量）

这为大规模训练模型提供了理论依据和预测工具​：投入更多计算/数据/参数，就能知道模型性能大概能提升多少。



性能损失 (L) 的近似公式：​​

• 损失 L可以近似表示为：L ≈ k / (N^α * D^β * C^γ) + L0（其中 k, α, β, γ, L0是常数，通过拟合实验数据得出）

•​ 论文中最重要的经验幂律关系之一：​​L ≈ 0.06 / N^{0.034} + 0.18 / D^{0.28} + ...(该形式经过简化，只为说明幂律关系，非完整精确公式)。

• ​意义：​​ 损失随着 N、D、C的增加按照幂律下降，但存在一个不可逾越的极限 L0


# Chinchilla Scaling Law 奇努卡/龙猫缩放定律

DeepMind 在 2022 年提出的奇努卡缩放定律，颠覆了之前主流的大语言模型缩放思路。它指出，单纯地增加模型的大小（参数数量）并不是最优策略，而应该平衡模型的大小和训练数据量的大小，才能达到最佳的“计算效率最优”状态。

1.​数据量与模型大小需成比例：​​ 为了在给定的计算资源下（即训练花费的 FLOPs），让模型达到最佳性能（最低的损失），训练数据量（以Token数量衡量）和模型参数量需要按一定比例缩放。

2.​关键比例 ≈ 20:1：​​ 研究中发现，一个简单有效的经验法则是：​为模型中的每个参数提供大约 20 个训练 Token。

• 示例：一个拥有 700 亿参数（70B）的模型（如奇努卡模型本身），应该在大约 ​1.4 万亿 Token（1.4T）​​ 的数据上训练（70B * 20 = 1.4T）。


重要意义与影响：​​

1.​数据至关重要：​​ 证明了高质量、海量训练数据在构建高性能大语言模型中，其重要性至少与模型架构和参数规模同等重要。
2.​小模型 + 大数据 > 大模型 + 小数据：​​ 对于固定的计算资源，遵循奇努卡定律训练出的更小模型，其性能可以远超不遵循该定律训练的、参数量大得多但数据不足的模型。
3.​效率提升：​​ 使得在达到顶尖性能的同时，​训练成本更低​（更有效地利用计算资源），​推理成本更低​（部署运行更小的模型）。
4.​引领发展潮流：​​ 直接影响了后续模型的开发。例如，Meta 著名的 ​LLaMA​ 系列模型就高度遵循了该定律，实现了极高的性价比并开源发布。像 GPT-4 这样的顶级模型，也必然在训练中融合了对模型大小和数据量进行更优平衡的原则。
5.​推动普及：​​ 一定程度上降低了训练顶尖模型的门槛，不再需要追求极端的千亿规模参数（但对海量高质量数据的需求依然很高）。


# 附录

## python 广播

当计算矩阵 $A = m \times n$ 矩阵和矩阵 $B = 1 \times n$ 的矩阵时，python 会自动复制矩阵 $B$ 的行直至扩展到 $m \times n$ 

当计算矩阵 $A = m \times n$ 矩阵和矩阵 $C = m \times 1$ 的矩阵时，python 会自动复制矩阵 $C$ 的列直至扩 请   展到 $m \times n$ 


## 贝叶斯最优误差

贝叶斯最优误差（Bayes Optimal Error）是模型在理论上能达到的最优误差。

贝叶斯统计，在先验概率的基础上，结合观测数据，计算后验概率。

贝叶斯公式非常简单： $P(A|X) = \frac{P(X|A) \cdot P(A)}{P(X)}$ 。其中：

* $P(A)$ 被称为先验概率。
* $P(X|A)$ 被称为基于观测数据的似然函数，即对数据观测。
* $P(X)$ 被称为边缘分布，即数据的总体概率。
* $P(A|X)$ 被称为后验概率。

古典概率和贝叶斯概率在哲学上的解释：

* 古典概率理论：观测事件发生的频率，当观测的次数足够多时（样本足够大），事件发生的频率就是事件发生的概率。
* 贝叶斯概率理论：通过经验或历史数据设定先验概率，然后基于观测数据计算后验概率，修正先验概率。


## 蒙特卡洛模拟

蒙特卡洛模拟在数学上有明确的定义：蒙特卡洛积分是一种通过随机抽样来估算积分值的方法。

对于积分： $I = \int_a^b f(x) dx$ ，它可以被解释为函数 $f(x)$ 在区间 $[a, b]$ 上的期望值。通过从 $[a, b]$ 上均匀抽样出点 $x_i$ ，并计算 $f(x_i)$ 的平均值，再乘以区间长度 $(b-a)$ ，即可得到积分的近似值：$I \approx (b−a) \cdot \frac{1}{N} \sum_{i=1}^{N} f(x_i)$ 

除此之外，在广义上，蒙特卡洛方法是一种​通过重复随机采样，利用统计规律来求解确定性或随机性的问题。​​


面对一个复杂问题，尤其是包含不确定性的问题，通过构建概率模型并进行大量独立重复的随机实验，将结果的统计特性（如平均值）作为问题的近似解。​​ 

具体方法是：首先明确问题中的随机性和不确定性，然后从预先定义的概率分布中生成随机样本，进行大量的独立实验并计算实验结果，对实验结果进行统计分析，计算平均值，即可以近似地得到目标的期望值。


## 对神经网络的理解

神经网络的直观理解就是使用计算机模仿人类大脑的思考过程进行计算。

然而剖析神经网络来看，它的每一步都是对数字的计算过程，神经网络为什么能达到如此惊人的效果？目前看仍然是不可解释的。

人类至今无法解释人类的思考和决策过程，因此可能人类也并没有理解创造出的神经网络到底是什么，为什么会有这样的作用。

直观的理解也许是最接近的理解，模仿人类大脑的思考过程。


## 对语言模型的理解

《数学之美》
数学、文字和自然语言一样，都是信息的载体，它们之间有着天然的联系。语言和数学的产生都是为了同一个目的——记录和传播信息。

任何一种语言都是一种编码的方式，而语言的语法规则是编解码算法。我们把一个要表达的意思，通过某种语言的一句话表达出来，就是用这种语言的编码方式，对头脑中的信息做了一次编码，编码的结果就是一串文字。而如果对方懂得这门语言，他就可以用这门语言的解码方式获得说话人要表达的信息。

今人考古破解古人的文字，本质上是因为我们面对的是同一个自然世界，信息是相近的。可以使用相近的上下文，就可以理解古人的文字，和想要表达的信息。

文字只是信息的载体，而非信息本身。那么不用文字，而用其他的载体是否可以存储同样意义的信息呢？这个答案是肯定的。

计算机能否处理自然语言？答案是肯定的。只要能够处理语言的编解码规则，那么计算机就可以处理自然语言。

因此，语言模型最早的应用领域是在语音识别（识别语音编码信息，判断哪个单词序列出现的可能性最高）和机器翻译（从一个语法规则转换到另一个语法规则），也包括实体识别、文本分类等。

从语法模型到统计语言模型，而统计语言模型中的神经网络模型最终突破了图灵假设，达到了较高的智能程度。


## 对词嵌入的理解

计算机表示文字（词汇表征 word representation）有两种方式：

* one-hot encoding representation：独热编码表示
* distributed representation：分布式表示，word embedding 词嵌入

早期的语言模型，例如 n-gram，使用的是 one-hot encoding ，主要不足体现在：

* 词汇量大，要表示所有词汇所需的编码过长，编码的维度太高
* 离散表示
* 无法表示词语之间的相关性

分布式表示可以使用 word2vec，其思想是：文本中距离越近的词语相似度越高。

用来压缩文本向量的维度。

word embedding 参数是使用大量文本语料训练出来的，识别了语料中的实体，并基于语料训练得到实体所具有的在不同维度的信息。



CBOW（Continuous Bag-of-Words）算法：使用上下文词预测中心词，目标是最大化中心词的对数概率 $max \sum_t log p(w_t | w_{t-k}, \dots, w_{t+k})$ ，其中， $w_t$ 是中心词， $w_{t \pm k}$ 是上下文词。 $p(w_t | w_{t-k}, \dots, w_{t+k}) = \frac{exp(\mathrm{v}_{w_t}^T · \bar{\mathrm{h}})}{\sum_{i=1}^V exp(\mathrm{v}_i^T · \bar{\mathrm{h}})}$ 。

skip-gram 算法：使用中心词预测上下文词，目标是最大化上下文词的对数概率 $max \sum_t \sum_{-k \le c \le k, c \neq 0} log p(w_{t+c} | w_t)$ 。 $p(w_{t+c} | w_t) = \frac{exp(\mathrm{v}_{w_{t+c}}^T · \mathrm{v}_{w_t})}{\sum_{i=1}^V exp(\mathrm{v}_i^T · \mathrm{v}_{w_t})}$ 。

```python
text1 = "天青色等烟雨，而我在等你。炊烟袅袅升起，隔江千万里。"
text2 = "good good study, day day up."

# 简单处理分词和创建词表
punc = ",.，。"
punc_translator = str.maketrans("", "", punc)
words1 = list(text1.translate(punc_translator))
words2 = text2.translate(punc_translator).split()
words = []
words.extend(words1)
words.extend(words2)
vocab = set(words)

# tokenizer
word_to_idx = {word: i for i, word in enumerate(vocab)}
idx_to_word = {i: word for i, word in enumerate(vocab)}

def encoder(words: list) -> list:
    tokenized_words = []
    for i in range(len(words)):
        tokenized_words.append(word_to_idx.get(words[i]))
    return tokenized_words

def decoder(tokenized_words: list) -> list:
    words = []
    for i in range(len(tokenized_words)):
        words.append(idx_to_word.get(tokenized_words[i]))
    return words

# 准备训练数据
embedding_dim = 8
window_size = 2
data_cbow = []
data_skip_gram = []

# cbow 训练数据，使用上下文词预测中心词
def get_cbow_data(words: list) -> list:
    data = []
    for i in range(window_size, len(words)-window_size):
        # 获取上下文单词
        content = []
        for j in range(i - window_size, i + window_size + 1):
            if j != i:
                content.append(words[j])
        target = words[i]
        data.append((content, target))
    return data

# skip-gram 训练数据，使用中心词预测上下文词
def get_skip_gram_data(words: list) -> list:
    data = []
    for i in range(window_size, len(words)-window_size):
        content = words[i]
        target = []
        for j in range(i - window_size, i + window_size + 1):
            if j != i:
                target.append(words[j])
        data.append((content, target))
    return data

```

从实际效果来看， word2vec 既是算法，也是模型。


## 对 softmax 函数的理解

softmax 函数使用指数能够在保持顺序的同时放大差异。

![image-20250627103847458](./深度学习.assets/image-20250627103847458.png)

softmax 函数特质：

1. 处理负值方便。
2. 突出最大值，抑制最小值。
3. 连续可导，且梯度计算非常高效。

使用 softmax 函数没有什么直观理解上的意义，主要是为了计算方便。

