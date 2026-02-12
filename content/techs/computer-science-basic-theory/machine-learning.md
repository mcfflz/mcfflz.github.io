---
bookHidden: false
bookSearchExclude: false
title: 机器学习
weight: 111
params:
  math: true
---

# 机器学习 Machine Learning

## 概述

最初定义：Arthur Samuel (1959). Machine Learning: Field of study that gives computers the ability to learn without being explicitly programmed. 机器学习：赋予计算机无需明确编程即可具有学习能力的研究领域。

标准定义：Tom Mitchell (1998) Well-posed Learning Program: A computer program is said to learn from Experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E. 适定学习程序：如果一个计算机程序在任务 T 上的评价指标 P 随着经验 E 提升，那么我们就可以说这个程序在从经验 E 中学习（经验 E 代表任务 T 和评价指标 P）。

[适定]：源自数学中的“适定性问题”（如偏微分方程），指问题满足以下三个条件：存在性（Existence）：有解；唯一性（Uniqueness）：解唯一；稳定性（Stability）：解连续依赖于输入数据（微小扰动不会导致解剧烈变化）。

Google for Developer：从基本层面来说，机器学习是指训练一款名为模型的软件，以便做出有用的预测或根据数据生成内容。
模型是从数据中派生出来的数学关系，是人们研发模型想要发现的关系。

个人理解：模型求解的是一个 $f(x) = y$ 的问题，其中 $x$ 是已知信息，$y$ 是要解决的问题。
使用数学建模思路，将已知信息和问题量化为数学表示，建立数学模型，使用不同的数学工具来发现其中的数学关系。


## 名词术语

数据可以分为：

* 特征 features：数据的维度
* 标签 labels：数据要预测的结果

机器学习任务可以分为：

* 监督学习 Supervise Learning：输入同时有特征和标签数据，训练模型找出的特征和标签之间的关系。监督学习常见的模型包括：
  * 线性回归模型：预测数值
  * 逻辑回归模型：预测概率
  * 分类模型：基于逻辑回归模型，预测对象属于某个类别
  * 神经网络模型：预测数值或概率
* 非监督学习 Unsupervise Learning：输入仅有特征数据，训练模型找出特征数据中具有意义的模式。非监督学习没有关于特征数据的提示，需要推断自己的规则。非监督学习常见的模型包括：
  * 聚类模型：预测数据属于哪一类
  * PCA：
  * 异常检测模型：预测数据是否存在异常
* 强化学习 Reinforcement Learning：输入同时有特征和标签数据，根据环境中智能体执行的操作获得奖励或惩罚，从而进行预测。强化学习的目的是找到获得最多奖励的最佳策略。
* 生成式AI：根据用户输入生成内容，通常以“输入类型”到“输出类型”的形式写出：
  * 文本到文本
  * 文本到图像
  * 文本到视频
  * 文本到代码
  * 文本到语音
  * 图片到文本
  * 语音到文本
  * ……

损失函数：

* 损失函数（或称代价函数）衡量机器学习模型的效果
* 通过对不同的模型设置不同的损失函数，评价模型的学习效果


# 线性回归模型

## 线性回归模型简介

线性回归模型是监督学习模型

线性回归模型假设特征和标签数据之间的关系是线性的

[注意]：这里的线性是指模型参数是线性的，而不是说模型特征是线性的，特征可以是任意的线性或非线性组合

线性回归模型是最简单的数学模型

线性回归模型通过定义损失函数来衡量模型的效果，通过梯度下降法找到线性回归模型最佳的特征权重和偏差，使得损失函数最小


## 最简单的线性回归模型

输入：

* 样本数据：$(x^{(1)},y^{(1)}), (x^{(2)},y^{(2)}), \dots, (x^{(m)},y^{(m)})$

* 特征： $x^{(i)} \in \mathbb{R}^1$ ，标签： $y^{(i)} \in \mathbb{R}^1$ ，这里的 $\mathbb{R}^1$ 代表数据是一维的，后续不再重复说明


假设：

* 线性回归模型：$h_\theta(x^{(i)}) = \theta_0 + \theta_1 x^{(i)}$ ，其中 $\theta_0$ 被称为偏差 bias

* 模型参数：$\theta_0, \theta_1$ 

* 衡量模型效果的损失函数： $J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$ ，损失函数通过计算模型预测结果和实际结果（标签）的误差来衡量模型的效果

* 模型目标： $min\ J(\theta_0, \theta_1)$ 


计算模型：

* 设置初始化参数： $\theta_0 = 0, \theta_1 = 0$ ，线性回归模型一般设置初始化参数为 0，也可以设置为随机值

* 计算模型的损失值： $J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$ 
	* 其中，$h_\theta(x^{(i)}) = \theta_0 +  \theta_1x^{(i)}$ 

* 判断模型损失是否可以接受
	* 如是，则得到模型和模型参数
	* 如否，优化模型参数

* 计算模型参数的梯度，找到参数优化方向： $\theta_j := \theta_j - \alpha \cdot \frac{\partial J(\theta_0, \theta_1)}{\partial \theta_j}$ ，其中 $\alpha$ 是参数变更的幅度，也被称为学习率
	* 带入 $J(\theta_0, \theta_1), h_\theta(x^{(i)})$ 求得：
	* $\theta_0 := \theta_0 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})$ 
	* $\theta_1 := \theta_1 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$ 

* 更新参数，并重新计算模型的损失值

[注意1]：理想的学习率有助于模型在合理的迭代次数内收敛，需要根据实际问题来选择合适的学习率，包括也可以根据损失函数结果来动态更新学习率

[注意2]：需要同时更新 $\theta_0, \theta_1$ ，原因是：

* 梯度计算依赖所有参数的当前值，同步更新可以保证模型收敛。如果逐个更新参数，后续参数的更新会基于前一步更新后的值，可能导致损失值震荡或不收敛
* 固定参数等同于预先假设该特征不重要，模型将无法利用该特征的信息，可能导致模型欠拟合
* 特殊场景下，如果判断某个特征参数对于损失值收敛不产生作用，那么更倾向于剔除这个特征，而不是固定该特征的参数
* 可以使用以下 octave 代码简单验证为什么要同时更新参数

```octave
% 实际模型 y = 3x + 2
close all;clear all;clc;

X = [0;1;2;3;4;5];
y = 3 * X + 2;
X = [ones(length(X),1), X];
theta = [0;0];

function test1(X,y,theta,iters)
  % 不同时更新参数
  costh = zeros(1, iters);
  for i = 1:iters;
    costh(i) = (1/length(y)) * sum((X * theta - y).^2);
    if i > 1 && abs(costh(i) - costh(i-1))  < 0.000001 % 模型收敛要求
      costh(i+1:iters) = [];
      iters = i;
      break;
    end
    gradient = (1/length(y)) * X' * (X * theta -y);
    theta(2) = theta(2) - 0.1 * gradient(2); % 固定参数theta_0不变，仅更新theta_1
  end

  output(theta, costh, iters);
end

function test2(X,y,theta,iters)
  % 同时更新参数
  costh = zeros(1, iters);
  for i = 1:iters;
    costh(i) = (1/length(y)) * sum((X * theta - y).^2);
    if i > 1 && abs(costh(i) - costh(i-1)) < 0.000001 % 模型收敛要求
      costh(i+1:iters) = [];
      iters = i;
      break;
    end
    gradient = (1/length(y)) * X' * (X * theta -y);
    theta = theta - 0.1 * gradient; % 同时更新参数
  end

  output(theta, costh, iters);
end

function output(theta, costh, iters)
  % 输出结果并绘图
  printf("model y = %f + %f * x\n", theta(1), theta(2));
  printf("cost %f\n", costh(iters));

  figure;
  subplot(1,2,1); % 绘制损失曲线
  x = 1:1:iters;
  plot(x, costh, 'b-o', 'LineWidth', 0.8, 'MarkerSize', 1);
  hold on;
  % 在数据点旁添加标签
  text(1, costh(1), sprintf('%.2f', costh(1)), ...
    'HorizontalAlignment', 'right', ...  % 文本对齐方式
    'VerticalAlignment', 'bottom', ...   % 垂直对齐方式
    'FontSize', 16, ...
    'Color', 'red');

  text(iters, costh(iters), sprintf('%.2f', costh(iters)), ...
    'HorizontalAlignment', 'right', ...  % 文本对齐方式
    'VerticalAlignment', 'bottom', ...   % 垂直对齐方式
    'FontSize', 16, ...
    'Color', 'red');
  hold off;

  subplot(1,2,2); % 绘制预测曲线
  real = 2 + 3 * x;
  pred = theta(1) + theta(2) * x;
  plot(x, real, 'g-', 'LineWidth', 1, 'DisplayName', 'real line'); % 绿色实现表示实际曲线
  hold on;
  plot(x, pred, 'r--', 'LineWidth', 1, 'DisplayName', 'pred line'); % 红色虚线表示预测曲线
  legend('real line', 'pred line')
  hold off;
end

test1(X,y,theta,1000); % 模型并未拟合理想的函数
test2(X,y,theta,1000); % 模型输出结果符合预期
```

## 一般化的线性回归模型

最简单的线性回归模型用于解释原理。

在实际应用中，特征数据通常有非常多维度，例如预测天气可能要根据湿度、温度、气压、历史同期数据等，我们通常用矩阵来表示多维度的特征数据，即一般化的线性回归模型

输入：

* 样本数据：$(x^{(1)},y^{(1)}), (x^{(2)},y^{(2)}), \dots, (x^{(m)},y^{(m)})$ 

* 特征： $x^{(i)} \in \mathbb{R}^n$ ，即 $x^{(i)} = \left(
\begin{array}{c}
x_1^{(i)} \newline
x_2^{(i)} \newline
\vdots    \newline
x_n^{(i)} \newline
\end{array}
\right)$ ，表示特征 $x^{(i)}$ 是一个 $n$ 维的向量（Vector）

* 在实际的计算过程中，为了计算偏差方便，通常在特征中增加 $x^{(i)}_0 = 1$ ，即 $x^{(i)} = \left( \begin{array}{c}
x_0^{(i)} \newline
x_1^{(i)} \newline
x_2^{(i)} \newline
\vdots    \newline
x_n^{(i)} \newline
\end{array}
\right)$ ，此时 $x^{(i)} \in \mathbb{R}^{n+1}$ 。需要注意真实的特征只有 $n$ 个，第 $0$ 个特征是为了后续计算模型参数而增加的，后续直接简化描述

* 标签： $y^{(i)} \in \mathbb{R}^1$ 

* 样本数据可以表达为特征矩阵： $X = \left( \begin{array}{c}
{x^{(1)}}^T \newline
{x^{(2)}}^T \newline
\vdots      \newline
{x^{(m)}}^T \newline
\end{array} \right), \mathbb{R}^{m \times n+1}$ 和标签向量： $y = \left( \begin{array}{c}
y^{(1)} \newline
y^{(2)} \newline
\vdots  \newline
y^{(m)} \newline
\end{array} \right), \mathbb{R}^{m \times 1}$ ，其中 $\mathbb{R}^{m \times n}$ 代表矩阵的维度是 $m \times n$ 


假设：

* 线性回归模型：$h_\theta(x^{(i)}) = \theta_0x^{(i)}_0 + \theta_1x^{(i)}_1 + \theta_2x^{(i)}_2 + \dots + \theta_nx^{(i)}_n$ 

* 模型参数： $\theta = \left( \begin{array}{c}
\theta_0 \newline
\theta_1 \newline
\theta_2 \newline
\vdots   \newline
\theta_n \newline
\end{array} \right)$ ，$\theta$ 是一个 $n$ 维的向量

* 衡量模型效果的损失函数： $J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$ 

* 模型目标： $min \  J(\theta)$ 


计算模型：

* 设置初始化参数： $\theta =0$ ，即 $\theta_0 = 0, \theta_1 = 0, \dots, \theta_n = 0$ ，也可以设置为随机值

* 计算模型的损失值： $J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$ 
	* 其中，$h_\theta(x^{(i)}) = x^{(i)}_0 \cdot \theta_0 + x^{(i)}_1 \cdot \theta_1 + \cdots + x^{(i)}_n \cdot \theta_n$ 
	* 使用矩阵形式即为：  $J(\theta) = \frac{1}{2m} \sum(X\theta- y)$ 

* 判断模型损失是否可以接受
	* 如是，则得到模型和模型参数
	* 如否，优化模型参数

* 计算模型参数的梯度，找到参数优化方向： $\theta_j := \theta_j - \alpha \cdot \frac{\partial J(\theta)}{\partial \theta_j}$ ，其中 $\alpha$ 是参数变更的幅度，也被称为学习率
	* 带入 $J(\theta), h_\theta(x^{(i)})$ 求得：
	* $\theta_0 := \theta_0 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})$ 
	* $\theta_j := \theta_j - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$ 

* 计算梯度的公式可以化简为： $\frac{\partial J(\theta)}{\partial \theta_j} = \frac{1}{m} X^T (X\theta - y)$ 

* 更新参数，并重新计算模型的损失值


[可选]：推导梯度公式：

* 根据链式法则： $\frac{\partial J(\theta)}{\partial \theta_j} \newline
= \frac{\partial J(\theta)}{\partial h_\theta} \cdot \frac {\partial h_\theta}{\partial \theta_j} \newline
= \frac{1}{m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}_j$ 

*  $x^{(i)}_j$ 即为特征矩阵 $X$ 的第 $j$ 列（第 $j$ 个特征），因此用向量表示的梯度矩阵即为 $gradient(\theta) = \frac{1}{m} X^T (X\theta - y), gradient(\theta) \in \mathbb{R}^{n+1 \times 1}$ 


## 正规方程

对于线性回归模型，通过学习线性代数，可知正规方程（Normal equation）是求解参数 $\theta$ 更快的方式

正规方程： $\theta = (X^TX)^{-1}X^Ty$ ，可以说是最小二乘法的矩阵形式

缺陷：求解 $(X^TX)^{-1}$ 的算法复杂度是 $O(n^3)$ ，因此通常当特征 $n > 10000$ 时，正规方程的求解时间会超过梯度下降法。

```octave
function normalEquition(X, y, theta)
  theta = pinv(X' * X) * X' * y;
end
```

[可选]：推导正规方程：

* $J(\theta) = \frac{1}{2m} || X\theta - y ||^2$ ，其中：
	* 符号 $$||\ ||$$ 表示范数（Norm），在此处代表空间内向量的长度
	* 常数 $ \frac{1}{2m}$ 不影响极值点，因此可以忽略

* 展开多项式可得 $J(\theta) := || X\theta - y ||^2 = (X\theta - y)^T (X\theta - y) = θ^T X^T X \theta - 2y^T X \theta + y^T y$ 
	* 矩阵乘法的转置满足 $(AB)^T = B^TA^T, A \in \mathbb{R}^{m \times n}, B \in \mathbb{R}^{n \times p}$ ，因此有：
		* $(m \times n)(n \times p) = (m \times p)$ 
		* $((p \times n)(n \times m))^T = (p \times m)^T = (m \times p)$ 
		* 易得两者相等
		* 也可以将矩阵按照行列式展开的方式进行证明

* 计算偏导数 $\frac{\partial J(\theta)}{\partial \theta} = \frac{\partial}{\partial \theta} (θ^T X^T X \theta - 2y^T X \theta + y^T y) = 2\theta^T X^T X - 2y^T X$ 
	* $θ^T X^T X \theta$ 是一个二次型，结果是一个标量
		* 形如 $A^TBA$ 是一个二次型，其中 $B$ 是一个对称矩阵，也被称为二次型矩阵
		* $\frac{\partial}{\partial \theta} (\theta^T X^T X \theta) = d\theta^T X^T X \theta + \theta^T X^T X d\theta$ 
		* 因为 $X^TX$ 的对称性，因此 $d\theta^T X^T X \theta = \theta^T X^T X d\theta$ 
		* 即 $\frac{\partial}{\partial \theta} (\theta^T X^T X \theta) = 2\theta^T X^T X$ 

* 令导数 $2X^T X \theta - 2y^T X = 0 \Longrightarrow X^T X \theta = y^T X$ ，因此只要 $X^T X$ 的逆有解，就可以快速求解 $\theta = (X^T X)^{-1} y^T X$ 


## 损失函数选择

线性回归模型常见的损失函数有以下 4 种：

* L1 损失：$\sum |实际值-预测值|$
* MAE 平均绝对误差：$\frac{1}{m} \sum |实际值-预测值|$，使用MAE损失函数训练的模型距离大多数特征较近，距离离群值较远
* L2 损失：$\sum (实际值-预测值)^2$
* MSE 均方误差：$\frac{1}{2m} \sum (实际值-预测值)^2$，使用MSE损失函数训练的模型距离离群值更近

以上 4 种线性回归模型的损失函数都是凸函数，因此线性回归模型会收敛，可以使用梯度下降算法或正规方程计算模型的最优解

最常使用的损失函数是 MSE 


# 逻辑回归模型

逻辑回归模型是监督学习模型

逻辑回归模型假设特征和标签数据之间的关系是非线性的

[注意]：这里的非线性是指模型参数是非线性的，而不是说模型特征是非线性的，特征可以是任意的线性或非线性组合

逻辑回归模型通常用于解决分类问题，线性回归模型在分类问题上的表现并不是很好，因此需要做进一步的扩展

逻辑回归模型通过定义非线性函数来转换线性关系


## 最简单的分类模型

最简单的分类模型是二元分类模型

输入：

* 样本数据：$(x^{(1)},y^{(1)}), (x^{(2)},y^{(2)}), \dots, (x^{(m)},y^{(m)})$ 

* 特征： $x^{(i)} \in  \mathbb{R}^1$ ，标签： $y^{(i)} \in  \mathbb{R}^1$ 且 $y^{(i)} \in \{0, 1\}$


假设：

* 逻辑回归模型：$h_\theta(x^{(i)}) = g(\theta_0 + \theta_1 x^{(i)})$ ，其中 $0 \leq g(z) \leq 1$ 

* 使用 sigmoid 函数 $g(z) = \frac{1}{1+e^{-z}}$ 完成非线性关系转换，sigmoid 函数取值在 $(0, 1)$ 区间内。

* 模型参数： $\theta_0, \theta_1$ 

* 决策边界： $d$ 表示逻辑回归模型输出不同分类的边界值。例如当决策边界是 0.5 时，有：
	* 如果 $h_\theta(x^{(i)})  \geq 0.5$ ，那么模型输出为 1
	* 如果 $h_\theta(x^{(i)})  < 0.5$ ，那么模型输出为 0

* 衡量模型效果的损失函数： $J(\theta_0, \theta_1) =  \frac{1}{m}\sum_{i=1}^{m}\text{Cost}(h_\theta(x), y) = -\frac{1}{m} \sum_{i=1}^{m} (y^{(i)} log h_\theta(x^{(i)}) + (1-y^{(i)}) log(1 - h_\theta(x^{(i)})))$ 
	* 线性回归模型的损失函数 $J(\theta_0, \theta_1) = \frac{1}{2m}\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2$ 并不适用于逻辑回归模型，原因是：在引入 $h(x) = g(z) = \frac{1}{1+e^{-z}}$ 的情况下，损失函数会变成非凸函数，无法通过梯度下降找到全局最优解
	* 损失函数通过衡量预测值和实际值的误差来定义模型的损失，考虑到 sigmoid 函数特性和函数曲线，因此定义逻辑回归模型的损失 $\text{Cost}(h_\theta(x), y)  = \begin{cases}
	-\log(h_\theta(x)), & \text{if } y = 1 \newline
	-\log(1 - h_\theta(x)), & \text{if } y = 0
	\end{cases}$ ，组合即可得到上述的损失函数。新的损失函数具有很好的表现，其含义是当实际结果是 1/0，预测结果越接近 0/1，就具有越大的损失。可以通过观察函数曲线理解这一含义

* 模型目标： $min\  J(\theta_0, \theta_1)$ 


计算模型：

* 设置初始化参数： $\theta_0 = 0, \theta_1 = 0$ ，逻辑回归模型一般设置初始化参数为 0，也可以设置为随机值

* 计算模型的损失值： $J(\theta_0, \theta_1) = \frac{1}{m}\sum_{i=1}^{m}\text{Cost}(h_\theta(x), y) = -\frac{1}{m} \sum_{i=1}^{m} (y^{(i)} log h_\theta(x^{(i)}) + (1-y^{(i)}) log(1 - h_\theta(x^{(i)})))$ 
	* 其中，$h_\theta(x^{(i)}) = g(\theta_0 +  \theta_1x^{(i)})$ 

* 判断模型损失是否可以接受
	* 如是，则得到模型和模型参数
	* 如否，优化模型参数

* 计算模型参数的梯度，找到参数优化方向： $\theta_j := \theta_j - \alpha \cdot \frac{\partial J(\theta_0, \theta_1)}{\partial \theta_j}$ ，其中 $\alpha$ 是参数变更的幅度，也被称为学习率
	* 带入 $J(\theta_0, \theta_1), h_\theta(x^{(i)}), g(z)$ 求得：
	* $\theta_0 := \theta_0 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})$ 
	* $\theta_1 := \theta_1 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$ 

* 更新参数，并重新计算模型的损失值

[注意1]：sigmoid 函数 $g$ 求导为 $g(1 - g)$，推导过程

* $g = \frac{1}{1+e^{-z}}$ ，因此使用商求导公式 $g' = \frac{1'(1 + e^{-z}) - 1(1 + e^{-z})'}{(1 + e^{-z})^2} = \frac{e^{-z}}{(1+e^{-z})^2} = g(1-g)$

[注意2]：理论上可以使用其他函数代替 sigmoid 函数来完成非线性转换，但需要注意使用场景和函数特性


## 一般化的逻辑回归模型

用矩阵表示一般化的逻辑回归模型

输入：

* 样本数据：$(x^{(1)},y^{(1)}), (x^{(2)},y^{(2)}), \dots, (x^{(m)},y^{(m)})$ ，其中 $x^{(i)} \in \mathbb{R}^n, y^{(i)} \in \mathbb{R}^1$

* 特征： $x^{(i)} = \left( \begin{array}{c}
x_0^{(i)} \newline
x_1^{(i)} \newline
x_2^{(i)} \newline
\vdots   \newline
x_n^{(i)} \newline
\end{array} \right)$ ，其中 $x^{(i)}_0 = 1$ 

* 标签： $y^{(i)} \in \mathbb{R}^1$ 

* 样本数据可以表达为特征矩阵： $X = \left( \begin{array}{c}
{x^{(1)}}^T \newline
{x^{(2)}}^T \newline
\dots \newline
{x^{(m)}}^T \newline
\end{array} \right), \mathbb{R}^{m \times n+1}$ 和标签向量： $y = \left( \begin{array}{c}
y^{(1)} \newline
y^{(2)} \newline
\dots   \newline
y^{(m)} \newline
\end{array} \right), \mathbb{R}^{m \times 1}$ 


假设：

* 逻辑回归模型：$h_\theta(x^{(i)}) = g(\theta_0x^{(i)}_0 + \theta_1x^{(i)}_1 + \theta_2x^{(i)}_2 + \dots + \theta_nx^{(i)}_n)$ 

* 使用 sigmoid 函数 $g(z) = \frac{1}{1+e^{-z}}$ 完成非线性关系转换

* 模型参数： $\theta = \left( \begin{array}{c}
\theta_0 \newline
\theta_1 \newline
\theta_2 \newline
\vdots   \newline
\theta_n \newline
\end{array} \right) $ 

* 衡量模型效果的损失函数： $J(\theta) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$ 

* 模型目标： $min J(\theta)$ 


计算模型：

* 设置初始化参数： $\theta =0$ ，也可以设置为随机值

* 计算模型的损失值： $J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} (y log(h_\theta(x^{(i)})) + (1-y) log(1 - h_\theta(x^{(i)})))$ 
	* 其中，$h_\theta(x^{(i)}) = g(x^{(i)}_0 \cdot \theta_0 + x^{(i)}_1 \cdot \theta_1 + \cdots + x^{(i)}_n \cdot \theta_n) = \frac{1}{1+e^{-(x^{(i)}_0 \cdot \theta_0 + x^{(i)}_1 \cdot \theta_1 + \cdots + x^{(i)}_n \cdot \theta_n)}}$ 
	* 使用矩阵形式即为：  $J(\theta) = -\frac{1}{m} \sum (y \cdot g(X\theta) + (1 - y) \cdot (1 - g(X\theta)))$ 

* 判断模型损失是否可以接受
	* 如是，则得到模型和模型参数
	* 如否，优化模型参数

* 计算模型参数的梯度，找到参数优化方向： $\theta_j := \theta_j - \alpha \cdot \frac{\partial J(\theta)}{\partial \theta_j}$ 
	* 带入 $J(\theta), h_\theta(x^{(i)}), g(z)$ 求得：
	* $\theta_0 := \theta_0 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})$ 
	* $\theta_j := \theta_j - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$ 

* 计算梯度的公式可以化简为： $\frac{\partial J(\theta)}{\partial \theta_j} = \frac{1}{m} X^T (g(X\theta) - y)$ 

* 更新参数，并重新计算模型的损失值


[可选]：推导梯度公式：

* 根据链式法则： $\frac{\partial J(\theta)}{\partial \theta_j} \newline
= \frac{\partial J(\theta)}{\partial h_\theta} \cdot \frac {\partial h_\theta}{\partial z} \cdot \frac {\partial z}{\partial \theta_j} \newline
= -\frac{1}{m} \sum_{i=1}^m ( \frac{y^{(i)}}{h_\theta(x^{(i)})} -  \frac{1 - y^{(i)}}{1 - h_\theta(x^{(i)})} ) \cdot h_\theta(x^{(i)}) (1 - h_\theta(x^{(i)})) \cdot x^{(i)}_j \newline
= \frac{1}{m} \sum_{i=1}^m ( h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}_j $ 

*  $x^{(i)}_j$ 即为特征矩阵 $X$ 的第 $j$ 列（第 $j$ 个特征），因此用向量表示的梯度矩阵即为 $gradient(\theta) = \frac{1}{m} X^T (g(X\theta) - y), gradient(\theta) \in \mathbb{R}^{n+1 \times 1}$ 


## 损失函数

逻辑回归模型常见的损失函数有以下 2 种：

* 交叉熵损失函数：$-\sum y log(y') - (1-y) log(1-y')$ 
* 加权交叉熵损失函数：$-\sum w_1y log(y') - w_0 (1-y) log(1-y')$ ，对交叉熵函数的加权，适用于分布不均匀的样本


# 神经网络模型

神经网络模型是监督学习模型

线性回归模型和逻辑回归模型都能够通过特征组合的方式来表达复杂函数，但是这些特征组合需要人们精心设计，并且存在特征组合复杂度过高的问题。

那么是否有一种模型可以自动组合复杂的特征组合并解决问题？于是人们想到了人的大脑，一种完美的学习机器。科学家很早之前就想到可以仿照人的大脑设计一种机器学习算法，这就是神经网络模型

神经网络模型可以表示非常复杂的线性或非线性关系

神经网络模型通过激活函数来表示非线性关系，如果没有激活函数，那么模型表示的关系就是线性的

[注意]：这里的非线性是指模型的参数是线性或非线性的


## 通用近似定理

神经网络模型通过激活函数拟合任意连续的函数关系具有数学证明：

George Cybenko 最早在 1989 年提出并证明了通用近似定理（Universal Approximation Theorem）：假设特征空间为 $\mathbb{R}^n$，目标函数 $f$ 在 $\mathbb{R}^n$ 上是连续函数。若满足以下条件，则必定存在一个具有单隐藏层的前馈神经网络，使得该网络可以以任意精度（在任意紧集上）逼近 $f$：

1. 隐藏层激活函数 $\sigma$ 是非多项式的连续S型函数（Sigmoidal function），例如 Sigmoid 函数 $\sigma(x) = \frac{1}{1 + e^{-x}}$。
2. 隐藏层有足够多的神经元 $m$。
3. 网络权重和偏置可以自由调整。

Hornik 在 1991 年扩展了通用近似定理，激活函数只需要是连续且递增的函数，且定理不仅适用于单隐藏层网络，更深的网络（两层及以上）可以用更少的神经元逼近复杂函数

通用近似定理具有一定的限制条件：

* 逼近能力不等于泛化能力，模型仅在有限空间内逼近目标函数，在空间外的表现则是未知的
* 目标函数必须是连续函数，离散函数需要使用更多的数学手段进行处理


## 最简单的神经网络模型

以非线性问题举例：

输入：

* 样本数据：$(x^{(1)},y^{(1)}), (x^{(2)},y^{(2)}), \dots, (x^{(m)},y^{(m)})$ 

* 特征： $x^{(i)} \in  \mathbb{R}^2$ ，标签： $y^{(i)} \in  \mathbb{R}^1$ 


假设：

* 神经网络模型具有 1 个输入层，1 个隐藏层，1 个输出层，总计 3 层。隐藏层具有 2 个神经元和 1 个偏置 $a^1_0, a^1_1, a^1_2$ 

* 使用 sigmoid 函数 $g(z) = \frac{1}{1+e^{-z}}$ 完成非线性关系转换，sigmoid 函数取值在 $(0, 1)$ 区间内。

* 神经网络模型用图形表示即为： $\left( \begin{array}{c} 
a^{(1)}_0 = x^{(i)}_0 = 1 \newline
a^{(1)}_1 = x^{(i)}_1     \newline
a^{(1)}_2 = x^{(i)}_2     \newline
\end{array} \right) 
\Rightarrow 
\left( \begin{array}{c} 
a^{(2)}_0  = 1             \newline
a^{(2)}_1 = g( z^{(2)}_1 ) \newline
a^{(2)}_2 = g( z^{(2)}_2 ) \newline
\end{array} \right) 
\Rightarrow 
\left( \begin{array}{c} 
a^{(3)}_1 = h(x^{(i)}) = g( z^{(3)}_1 ) \newline
\end{array} \right) $ 
	* 其中$\begin{array}{c} 
z^{(2)}_1 = x^{(i)}_0 \theta^{(1)}_{1,0} + x^{(i)}_1 \theta^{(1)}_{1,1} + x^{(i)}_2 \theta^{(1)}_{1,2} \newline
z^{(2)}_2 = x^{(i)}_0 \theta^{(1)}_{2,0} + x^{(i)}_1 \theta^{(1)}_{2,1} + x^{(i)}_2 \theta^{(1)}_{2,2} \newline
z^{(3)}_1 = a^{(2)}_0 \theta^{(2)}_{1,0} + a^{(2)}_1 \theta^{(2)}_{1,1} + a^{(2)}_2 \theta^{(2)}_{1,2} \newline
\end{array} $ 

* 模型参数： $\theta^{(1)} = \left( \begin{array}{c} 
\theta^{(1)}_{1,0}, \theta^{(1)}_{1,1}, \theta^{(1)}_{1,2} \newline
\theta^{(1)}_{2,0}, \theta^{(1)}_{2,1}, \theta^{(1)}_{2,2} \newline
\end{array} \right), 
\theta^{(2)} = \left( \begin{array}{c} 
\theta^{(2)}_{1,0}, \theta^{(2)}_{1,1}, \theta^{(2)}_{1,2} \newline
\end{array} \right)$ 

* 衡量模型效果的损失函数： $J(\Theta) = -\frac{1}{m} \sum_{i=1}^{m} y^{(i)} log (h_{\Theta} (x^{(i)})) + (1 - y^{(i)}) log (1 - (h_{\Theta} (x^{(i)})))$ 

* 模型目标： $min J(\Theta)$ 


计算模型：

* 设置初始化参数 $\Theta}$ 是在区间 $(-\epsilon, \epsilon)$ 内的随机数，后续证明

* 计算隐藏层的输出： $a^{(2)}_1 = g(x^{(i)}_0 \theta^{(1)}_{1,0} + x^{(i)}_1 \theta^{(1)}_{1,1} + x^{(i)}_2 \theta^{(1)}_{1,2}), a^{(2)}_2 = g(x^{(i)}_0 \theta^{(1)}_{2,0} + x^{(i)}_1 \theta^{(1)}_{2,1} + x^{(i)}_2 \theta^{(1)}_{2,2})$

* 计算模型的损失值： $J(\Theta) = -\frac{1}{m} \sum_{i=1}^{m} y^{(i)} log (h_\Theta (x^{(i)})) + (1 - y^{(i)}) log (1 - (h_\Theta (x^{(i)})))$ 

* 判断模型损失是否可以接受
	* 如是，则得到模型和模型参数
	* 如否，优化模型参数

* 计算模型参数的梯度，找到参数优化方向： $\theta_j := \theta_j - \alpha \cdot \frac{\partial J(\Theta)}{\partial \theta_j}$ 
	* 带入 $J(\Theta), h_\theta(x^{(i)}), g(z)$ 求得：
	* $\theta^{(2)}_{1,0} := \theta^{(2)}_{1,0} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot a^{(2)}_0$ 
	* $\theta^{(2)}_{1,1} := \theta^{(2)}_{1,1} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot a^{(2)}_1$ 
	* $\theta^{(2)}_{1,2} := \theta^{(2)}_{1,2} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot a^{(2)}_2$ 
	* $\theta^{(1)}_{1,0} := \theta^{(2)}_{1,0} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot \theta^{(2)}_{1,1} \cdot a^{(1)}_0$ 
	* $\theta^{(1)}_{1,1} := \theta^{(2)}_{1,1} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot \theta^{(2)}_{1,1} \cdot a^{(1)}_1$ 
	* $\theta^{(1)}_{1,2} := \theta^{(2)}_{1,2} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot \theta^{(2)}_{1,1} \cdot a^{(1)}_2$ 
	* $\theta^{(1)}_{2,0} := \theta^{(2)}_{1,0} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot \theta^{(2)}_{1,2} \cdot a^{(1)}_0$ 
	* $\theta^{(1)}_{2,1} := \theta^{(2)}_{1,1} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot \theta^{(2)}_{1,2} \cdot a^{(1)}_1$ 
	* $\theta^{(1)}_{2,2} := \theta^{(2)}_{1,2} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot \theta^{(2)}_{1,2} \cdot a^{(1)}_2$ 

* 更新参数，并重新计算模型的损失值

[注意1]：在线性回归模型和逻辑回归模型中，我们通常将参数初始化为 0，但是这在神经网络模型中是行不通的。因为如果将所有的参数都初始化设置为 0，那么每一个隐藏层的每一个神经元输出和梯度都是相同的，无法优化模型

[注意2]：线性问题替换损失函数即可，例如 MSE 平方差

[注意3]：神经网络模型根据特征和参数计算模型结果的过程被称为正向传播，根据标签和预期值的差距计算梯度的过程被称为反向传播，从计算过程来看均是基于上一层网络的计算结果来计算下一层


## 矩阵形式表示一般化的神经网络模型

以非线性问题举例：

输入：

* 样本数据：$(x^{(1)},y^{(1)}), (x^{(2)},y^{(2)}), \dots, (x^{(m)},y^{(m)})$ ，其中 $y^{(i)} \in \mathbb{R}^n, y^{(i)} \in \mathbb{R}^k$ 

* 特征： $x^{(i)} = \left( \begin{array}{c}
x^{(i)}_0 \newline
x^{(i)}_1 \newline
x^{(i)}_2 \newline
\vdots \newline
x^{(i)}_n \newline
\end{array} \right)$ ，其中 $x^{(i)}_0 = 1$ 

* 标签： $y^{(i)} = \left( \begin{array}{c}
y^{(i)}_1 \newline
y^{(i)}_2 \newline
\vdots \newline
y^{(i)}_k \newline
\end{array} \right)$ 

* 样本数据可以表达为特征矩阵： $X = \left( \begin{array}{c}
{x^{(1)}} \newline
{x^{(2)}} \newline
\dots \newline
{x^{(m)}} \newline
\end{array} \right), \mathbb{R}^{m \times n+1}$ 和标签向量： $y = \left( \begin{array}{c}
{y^{(1)}}^T \newline
{y^{(2)}}^T \newline
\dots \newline
{y^{(m)}}^T \newline
\end{array} \right), \mathbb{R}^{m \times 1}$ 


假设：

* 神经网络模型共 $l$ 层，其中包括 1 个输入层，$l-2$ 个隐藏层，1 个输出层

* 每个隐藏层有 $j(l)$ 个神经元，和 1 个偏置。因此每一个隐藏层的输出可以使用 $a^{(l)}_0, a^{(l)}_1, \dots, a^{(l)}_{j(l)} $ 表示。下文叙述中常将 $j(l)$ 简化为 $j$
	* 每一个隐藏层具有任意的神经元数量，即 $j(l)$ 数量与 $l$ 有关
	* 每一个隐藏层的输出有： $ \begin{array}{c}
	a^{(l)}_0 = 1 \newline
	a^{(l)}_j = g( z^{(l)}_j ) = g( \theta^{(l-1)}_{(1,0)} a^{(l-1)}_0 + \theta^{(l-1)}_{(1,1)} a^{(l-1)}_1  + \dots + \theta^{(l-1)}_{(j,j_{l-1})} a^{(l-1)}_{j_{l-1}} ) \newline
	\end{array} $
	* $a^{(l)}_j$ 表示第 $l$ 层神经网络中，第 $j$ 个神经元的输出
	* $\theta^{(l-1)}_{j, j_{l-1}}$ 表示在计算第 $l$ 层神经网络的第 $j$ 个神经元时，第 $l-1$ 层神经网络的第 $j_{l-1}$ 个神经元的参数

* 使用 sigmoid 函数 $g(z) = \frac{1}{1+e^{-z}}$ 完成非线性关系转换

* 参数 $\Theta = \theta^{(1)}, \theta^{(2)}, \dots, \theta^{(l-1)}$ 是多个矩阵，每一个矩阵代表着计算神经网络下一层输出的参数，直到最后一层

* 每一层的参数： $\theta^{(l)} = \left( \begin{array}{c}
\theta^{(l)}_{1,0} & \theta^{(l)}_{1,1} & \dots & \theta^{(l)}_{1,j_{l-1}} \newline
\theta^{(l)}_{2,0} & \theta^{(l)}_{2,1} & \dots & \theta^{(l)}_{2,j_{l-1}} \newline
\vdots \newline
\theta^{(l)}_{j,0} & \theta^{(l)}_{j,1} & \dots & \theta^{(l)}_{j,j_{l-1}} \newline
\end{array} \right)$ 


计算模型：

* 设置初始化参数 $\Theta}$ 是在区间 $(-\epsilon, \epsilon)$ 内的随机数

* 计算隐藏层的输出： $a^{(l)}$ ，详见上文

* 计算模型的损失值： $J(\Theta) = -\frac{1}{m} \sum_{i=1}^{m} \sum_{p=1}^{k} y^{(i)}_p log (h_\Theta (x^{(i)})_p) + (1 - y^{(i)}_p) log (1 - (h_\Theta (x^{(i)}))_p)$ 

* 判断模型损失是否可以接受
	* 如是，则得到模型和模型参数
	* 如否，优化模型参数

* 计算模型参数的梯度，找到参数优化方向： $\theta_j := \theta_j - \alpha \cdot \frac{\partial J(\Theta)}{\partial \theta_j}$ 
	* 带入 $J(\Theta), h_\theta(x^{(i)}), g(z)$ 求得：
	* $\theta^{(l)}_{j_l,j_{l-1}} := \theta^{(l)}_{j_l,j_{l-1}} - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} \sum_{p=1}^{k} (h_\Theta (x^{(i)})_p - y^{(i)}_p) \cdot \theta^{(l+1)}_{j_l, j_{l-1}} \cdots \theta^{(l+1)}_{j_l, j_{l+1}} \cdot a^{(l)}_{j_l}$ 

* 更新参数，并重新计算模型的损失值


## 损失函数

回归问题的损失函数： $J(\Theta) = -\frac{1}{2m} 
\left[ 
\sum_{i=1}^{m} 
\sum_{k=1}^{K} (h_{\Theta} (x^{(i)}))_k - y^{(i)}_k)^2 
\right]
+ \frac{\lambda}{2m} 
\sum_{l=1}^{L-1}
\sum_{j=1}^{S_l}
\sum_{n=1}^{S_{l+1}} (\Theta^l_{(j,n)})^2 $ 

分类问题的损失函数： $J(\Theta) = -\frac{1}{m} 
\left[ 
\sum_{i=1}^{m} 
\sum_{k=1}^{K} y^{(i)}_k log (h_{\Theta} (x^{(i)})_k) + (1 - y^{(i)}_k) log (1 - (h_{\Theta} (x^{(i)}))_k) 
\right]
+ \frac{\lambda}{2m} 
\sum_{l=1}^{L-1}
\sum_{j=1}^{S_l}
\sum_{n=1}^{S_{l+1}} (\Theta^l_{(j,n)})^2 $ 

其中：
​	 $(h_\Theta(x^{(i)}))_k$ 代表神经网络模型的第 $k$ 个输出，$K$ 代表输出层的神经元数量。
​	 $l$ 代表神经网络模型当前的层数， $L$ 代表总层数。例如：输入层 $l = 1$ ，输出层 $l = L$ 。
​	 $S_l$ 代表神经网络模型当前层数的神经元数量。例如： $S_1 = n + 1, S_L = K$ 。

反向传播算法更新梯度：核心思想是通过链式法则从输出层到输入层逐层计算

$\frac{\partial J}{\partial \theta^{l}_{(j,n)}} = \frac{\partial J}{\partial a^{(L)}} · \frac{\partial a^{(L)}}{\partial z^{L}} · \dots · \frac{\partial z^{l}}{\partial \theta^{(l)}_{(j,n)}}$


## 激活函数

激活函数的特质：

* 在 $\mathbb{R}^n$ 内连续：连续保证可以处理任何输入数据
* 在 $\mathbb{R}^n$ 内可导：可导保证可以通过反向传播算法优化模型参数
* 非线性：非线性保证引入非线性
* 单调：不改变输入的特质
* 尽可能简单：有利于提高网络训练效率

常见的激活函数有：

* Sigmoid 函数： $\sigma = \frac{1}{1+e^{-y}}$ ，导数 $\sigma' = \sigma * (1 - \sigma)$ ，是非零均值函数，其导数是饱和函数，存在梯度消失问题
* tanh 函数： $\sigma = tanh(y) = \frac{e^{y}-e^{-y}}{e^{y}+e^{-y}}$ ，导数 $\sigma = 1 - \sigma^2$ ，零均值函数，其导数是饱和函数，存在梯度消失问题
* ReLU 函数：$f(x) = max(0, y)$ ，导数 $\sigma = 1(y>0), 0(y < 0)$，非饱和激活函数，不存在梯度消失问题，但存在梯度爆炸问题
* Para LeakReLU 函数：$f(x) = y (y>0), \alpha y(y<0)$ ，导数 $\sigma = 1(y>0), \alpha(y < 0)$，非饱和激活函数，不存在梯度消失问题，但存在梯度爆炸问题

梯度消失：随着层数的增加，求出的梯度的更新以指数形式衰减
梯度爆炸：随着层数的增加，求出的梯度的更新以指数形式增加

在神经网络模型中，如果不是在二元分类问题的输出层，否则不要使用 sigmoid 函数作为激活函数。tanh 函数在各方面的表现要优于 sigmoid 函数

softmax 函数： $p(y=j|\mathrm{x}) = \frac{exp(\mathrm{x})}{\sum exp(\mathrm{x})} = \frac{e^{(w_j^T\mathrm{x}+b_j)}}{\sum_{k \in K}e^{(w_k^T\mathrm{x}+b_k)}}$ 


# 支持向量机模型 SVM

支持向量机模型（SVM, support vector model）：相对于逻辑回归模型，简化了损失函数。

支持向量机（SVM）是一种强大的监督学习模型，主要用于分类任务，也可用于回归（即支持向量回归，SVR）。其核心思想是寻找最优分类超平面，最大化数据间隔，从而提升模型的泛化能力，因此又被称为大间距分类器


## 矩阵形式表示一般化的 SVM

输入：


$C \sum_{i=1}^{m} y^{(i)} cost_1(\theta^Tx^{(i)} + (1-y^{(i)}) cost_0(1 - \theta^Tx^{(i)}) + \frac{1}{2} \sum_{i=1}^{n} \theta^2$

$h_\theta(x) = \begin{equation}\begin{cases}
1, & if \ \theta^Tx^{(i)} \geq 0 \newline
0, & otherwise
\end{cases}
\end{equation}$

假设：

* 如果 $y = 1$ ，需要 $\theta^Tx \geq 1$ ，而不是 $\geq 0$ ；
* 如果 $y = 0$ ，需要 $\theta^Tx \leq -1$，而不是 $< 0$ 。

SVM 对异常数据会非常敏感。

核函数（Kernel）

高斯核函数（Gaussioan Kernel）

特征有非常多的组合可能性，那么如何组合特征？

假设使用 $f_1 \ f_2 \ f_3 \dots$ 来代表 $x^{(i)} = \left( \begin{array}{c} 
x^{(i)}_0 \newline
x^{(i)}_1 \newline
x^{(i)}_2 \newline
\dots \newline
x^{(i)}_n \newline
\end{array} \right)$ 的一种近似，那么在向量 $x^{(i)}$ 的空间内随机选择标记 $l^{(i)}$ 有：

$f_1 = similarity(x, l^{(i)}) = exp(-\frac{|| x - l^{(1)} ||^2}{2\sigma^2}) = exp(-\frac{\sum_{j=1}^n(x_j - (l^{(1)}_j))^2}{2\sigma^2})$ ，这就是高斯核函数

如果 $x \approx l^{(i)}$ ，
如果 $x$ 远离 $ l^{(i)}$ ，

$\sigma^2$ 是高斯核函数的参数。

核函数的选择必须满足莫塞尔定理

* 高斯核函数
* 线性核函数
* 多项式核函数
* 字符串核函数
* 卡方核函数
* 直方相交核函数


# K-Means 聚类算法

无监督学习算法。对特征分类。

输入：

* 特征数据： $x^{(1)}, x^{(2)}, \dots, x^{(m)}$ ，其中 $x^{(i)} \in \mathbb{R}^n$ 


假设：

* 聚类的数量： $K$ 

* 初始化聚类中心： $\mu_1, \mu_2, \dots, \mu_K$ 

* 损失函数： $J(c^{(1)}, c^{(2)}, \dots, c^{(m)}, \mu_1, \mu_2, \dots, \mu_k) = \frac{1}{m} \sum_{i=1}^{m} || x^{(i)} - \mu_{c^{(i)}} ||^2$


计算：

*	计算每个样本 $x^{(i)}$ 到聚类中心 $\mu_k$ 的距离 $c^{(i)}$ ，并将样本点按照距离最近的聚类中心分类为 $\mu_{c^{(i)}}$ ；

*	将聚类中心赋值为分类后的样本点均值

*	循环，直到聚类点不再变更


[注意1]：确定聚类中心暂时没有很好的方式，通常随机选择样本点作为初始的聚类中心。为了避免陷入局部最优解，通常随机初始化聚类中心多次，分别获得最优解后验证结果（通常 K < 10）

[注意2]：确定聚类的数量暂时没有很好的方式，通常是通过观察图像或者观察聚类算法的输出，手工调整。可以利用肘部法则：通过改变 K 的数量，比较损失函数的变化曲线。选择曲线变更较为明显的点


# 主成分分析 PCA 特征降维算法

无监督学习算法。主成分分析 PCA（Principal components analysis）对特征降维。

如果要将数据从 2D 降维到 1D，需要找到 1 个向量 $u^{1}$ ，使得数据投影到这个向量上的距离最小。

如果要将数据从 3D 降维到 2D，需要找到 2 个向量 $u^{1}, u^{2}$ ，使得数据投影到这个向量上的距离最小。

一般的，如果要将数据从 nD 降维到 kD，需要找到 k 个向量 $u^{1}, u^{2}, \dots, u^{k}$ ，使得数据投影到这些向量上的距离最小（投影误差）。

PCA 不是线性回归模型：PCA 要最小化投影距离，线性回归模型要最小化预测距离。

输入：

特征数据： $x^{(1)}, x^{(2)}, \dots, x^{(m)}$ 


数据处理：

均值标准化（$x_j - \mu_j$）、特征缩放（$\frac{x_j}{\sigma}$）


计算：

计算协方差 $\Sigma = \frac{1}{m} \sum_{i=1}^{n} (x^{(i)}) (x^{(i)})^T$ 

奇异值分解 $[U, S, V] = svd(\Sigma)$

获取矩阵 U 的前 k 列，计算 $z^{(i)} = U_{1:k} * x^{(i)}$ 

选择合适的维度 k，通常是使下面这个不等式成立的最小 k：

$\frac{ \frac{1}{m} \sum_{i=1}^{m} || x^{(i)} - x_{approx}^{(i)} ||^2 }
{\frac{1}{m} \sum_{i=1}^{m} || x^{(i)} ||^2} \leq 0.01 (1\%)$

也可以说是 99% 的方差被保留了，也可以选择 0.05 、0.1 这样的数值。

S 时一个对角阵，因此上述方程可以等于

$\frac{ \frac{1}{m} \sum_{i=1}^{m} || x^{(i)} - x_{approx}^{(i)} ||^2 }
{\frac{1}{m} \sum_{i=1}^{m} || x^{(i)} ||^2} = 
1 - \frac{ \sum_{i=1}^{k} S_{ii}} {\sum_{i=1}^{n} S_{ii}}$

也就是计算： $ \frac{ \sum_{i=1}^{k} S_{ii}} {\sum_{i=1}^{n} S_{ii}} \geq 0.99$ ，寻找最小的 k


PCA 也可以用来特征升维

$x_approx = u_reduce * z$ ，这样可以获得和原始数据相近似的数据。

不建议使用 PCA 去防止过拟合，这是错误使用。防止过拟合更推荐使用正则化参数。PCA 可能会损失原始特征的一些信息，而正则化不会。


# 异常检测算法

无监督学习。

异常检测算法运用了正态分布（高斯分布）： $x ~ N(\mu, \sigma^2)$ 。

正态分布的概率密度公式是 $P(x; \mu, \sigma^2) = \frac{1}{\sqrt{2\pi}\sigma} exp(- \frac{(x - \mu)^2}{2\sigma^2})$ .

## 高斯分布

输入：

特征数据： $x^{(1)}, x^{(2)}, \dots, x^{(m)}$ ，其中 $x^{(i)} \in \mathbb{R}^n$ 

处理：

假设样本分布 $p(x) = p(x_1; \mu_1, \sigma_1^2) p(x_2; \mu_2, \sigma_2^2) \dots p(x_n; \mu_n, \sigma_n^2) = \prod_{j=1}^{n} p(x_j; \mu_j, \sigma_j^2)$ 

计算：

$\mu_j = \frac{1}{m} \sum_{i=1}^{m} x^{(i)}_j$ 

$\sigma_j = \frac{1}{m} \sum_{i=1}^{m} (x^{(i)}_j - \mu_j)^2$ 

$p(x_j; mu_j, \sigma_j^2) =\frac{1}{\sqrt{2\pi}\sigma_j} exp(- \frac{(x_j - \mu_j)^2}{2\sigma_j^2}) $ 

$p(x) = \prod_{j=1}^{n} p(x_j; \mu_j, \sigma_j^2) $ 

验证：

$p(x) < \epsilon$ 


## 多元高斯分布

上面的算法考虑每一个特征的分布。现在考虑为所有特征的联合分布：

输入：

特征数据： $x^{(1)}, x^{(2)}, \dots, x^{(m)}$ ，每个样本有 $n$ 个特征

处理：

假设样本分布 $p(x) = p(x; \mu, \Sigma) = \frac{1}{(2\pi)^{\frac{n}{2}} |\epsilon|^{\frac{1}{2}}} exp(- \frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu))$ ，其中 $\mu \in \mathbb{R^n}, \ \Sigma \in \mathbb{R^{n \times n}}$

$\Sigma$ 是协方差矩阵。

计算：

$\mu = \frac{1}{m} \sum_{i=1}^{m} x^{(i)}$ 

$\Sgma = \frac{1}{m} \sum_{i=1}^{m} (x^{(i)} - \mu) (x^{(i)} - \mu)^T$ 

$p(x)$

验证：

$p(x) < \epsilon$ 

## 原始高斯模型和多元高斯模型的差异

原始高斯分布是多元高斯分布的一种特殊情况，当 $\Sigma = \left( \begin{array}{c}
\sigma_1^2 & 0 & \dots & 0 \newline
0 & \sigma_2^2 & \dots & 0 \newline
\vdots \newline
0 & 0 & \dots & \sigma_n^2 \newline
\end{array} \right)$ 时，多元高斯分布就是原始高斯分布。

原始高斯模型使用的更频繁，如果不需要考虑组合特征，那么选择原始高斯模型。

多元高斯模型可以自动考虑组合特征的问题。但是计算量大 $O(n^2)$ ，且需要 m > n（实践中一般需要 m > 10n）。

## 验证和测试

异常检测算法通常会使用带标签的数据进行验证和测试。

异常检测算法和监督学习的差异：

* 如果正样本和负样本的比例较为悬殊，那么建议选择异常检测算法。否则建议选择监督学习中的逻辑回归模型。
* 异常检测算法可以学习特征中的正样本范围，不在正样本范围内的可以认定为负样本。监督学习中可以从正样本和负样本中学习特征。


# 协同过滤算法

## 基于内容的推荐算法

基于用户和内容对象的交互历史，计算用户对未交互的内容的感兴趣程度，想用户推荐最感兴趣的内容。

假设能够获取到内容对象的特征，例如《指环王》这部电影的剧情得分 0.99，音乐得分是 0.95，动作得分 0.95，…… 。

输入：

$r(i, j)$ 代表用户 $j$ 是否对对内容 $i$ 的评分（0 或 1）；

$y^{(i, j)}$ 代表用户 $j$ 对内容 $i$ 的评分；

$\theta^{(j)}$ 代表要计算用户 $j$ 的参数；

$x^{(j)}$ 代表内容 $i$ 的特征数据；

假设：

用户 $j$ 对内容 $i$ 的评分预测为 $(\theta^{(j)})^T x^{(i)}$ 

单个用户的损失函数 $J(\theta^{(j)}) = \frac{1}{2m} \sum_{i=1}^{m} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 + \frac{1}{2m} \sum_{k=1}^{n} (\theta^{(j)}_k)^2, \ consider \ r(i,j) = 1$ 

考虑到 $m$ 是一个常数，因此对于单个用户来说可以省略。

推荐系统的损失函数 $J(\theta) = \frac{1}{2} \sum_{j=1}^{n_u} \sum_{i=1}^{m} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 
+ \frac{1}{2} \sum_{j=1}^{n_u} \sum_{k=1}^{n} (\theta^{(j)}_k)^2, \ consider \ r(i,j) = 1$ 

目标最小化 $J(\theta)$ 

计算：

通过梯度下降法可以计算参数。

## 基于用户兴趣的推荐算法

基于用户和内容对象的交互历史，计算用户对未交互的内容的感兴趣程度，想用户推荐最感兴趣的内容。

假设能够获取到用户的兴趣，例如用户 A 对爱情元素感兴趣，用户 B 对动作元素感兴趣，用户 C 对卡通动画画风感兴趣，……。

但是无法获得内容对象的特征。

输入：

$\theta^{(j)}$ 代表用户 $j$ 的参数；

$x^{(j)}$ 代表要计算内容 $i$ 的特征数据；

假设：

推荐系统的损失函数 $J(x) = \frac{1}{2} \sum_{i,j=1}^{m} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 
+ \frac{1}{2} \sum_{j=1}^{n_u} \sum_{k=1}^{n} (x_k)^2, \ consider \ r(i,j) = 1$ 

## 协同过滤算法

组合上述内容，可以得到一个最小化的损失函数目标：

$J(x, \theta) = \frac{1}{2} \sum_{j=1}^{n_u} \sum_{i=1}^{m} ((\theta^{(j)})^T x^{(i)} - y^{(i, j)})^2 
+ \frac{1}{2} \sum_{j=1}^{n_u} \sum_{k=1}^{n} (\theta^{(j)}_k)^2 
+ \frac{1}{2} \sum_{j=1}^{n_u} \sum_{k=1}^{n} (x_k)^2, \ consider \ r(i,j) = 1$

低秩矩阵分解


# 数据处理

数据是机器学习的基础，从业者往往需要花费更多的时间来评估、清理和转换数据，而不是构建模型。数据可以分为：

* 数值数据：连续或离散的整型或浮点型数据，是可累加的、可数的、有序的。例如：温度、重量、数量、……等等。
* 分类数据：具有一组特定的分类集合。例如：国家、城市、邮政编码、性别……等等。

## 特征缩放

将每一个特征缩放到一个近似于 [-1, 1] 的区间内，有助于模型更快的收敛。

例如：[0, 2]、[-3, 3]、[-1/3, 1/2] 等

均值归一化（Mean Normalization）：特征缩放中常用手段，将 $x_i$ 替换为 $x_i-\mu$ 使得特征的平均值为 0 。

更一般的形式是： $\frac{x_i-\mu}{s}$ ，其中 $\mu$ 是平均值，$s$ 是 $max-min$ 

## 数值数据处理

特征工程：对于数值数据，模型并不直接对原始数据执行操作，而是将原始数据提取和转换为特征向量。

常见的特征工程技术包括：

* 归一化：将数值转换到标准范围内。
* 分桶：将数值按区间分桶。

在创建特征向量前，需要研究数据：

* 数据可视化：在图表中直观地呈现数据，发现数据中隐藏的趋势或异常

* 统计评估：获取数据的统计信息，例如平均值、中位数、标准差、分界点

* 查找离群值：离群值是特征或标签中与大多数其他值相差甚远的值，常常会导致模型的训练出现问题。

  如果离群值是由于错误而导致的异常值，则通常做删除处理。

  如果离群值是合法的，则通常根据模型是否需要预测这些离群值，做保留或删除处理。

归一化技术主要可以分为以下几类：

* 线性缩放：将原始数据转换到某个标准范围内（通常是 0 到 1 区间内）。例如： $x' = (x - x_{min})/(x_{max} - x_{min})$ 。线性缩放适用于：数据上下限变化不大、离群值很少或没有、特征在范围内分布大致均匀。
* Z 分数缩放：将原始数据转换为与平均值之间的标准差数。例如：$x' = (x-\mu)/\sigma$ 。Z 分数缩放适用于：数据遵循或类似于正态分布。
* 对数缩放：将原始数据做对数处理。例如：$x' = ln(x)$  。对数缩放适用于：数据遵循或类似于幂律分布。
* 裁剪：将离群值限制到特定的最大（最小）值。例如：$如果x>x_{max}，则x'=max；如果x<x_{min}，则x'=min$ 。裁剪适用于：离群值对模型预测结果不重要。

分桶技术主要可以分为以下几类：

* 等宽分桶：每个分桶的特征区间大致相等。
* 等频分桶：每个分桶的样本数量大致相等。

在数据处理前，需要清洗数据：

* 省略的值：例如未登记的年龄
* 重复的值：例如服务器中相同的日志
* 超出范围的特征值：例如不小心输入了额外的数字
* 标签错误：例如一张橡树的图片被错标记为枫树

## 分类数据处理

当分类数据的维度（dimension）较低时，可以编码为词汇表（vocabulary），按照索引编号（index number）后转换为独热编码（one-hot encoding）。

当分类数据的维度较高时，可以使用嵌入（embedding）的方式，嵌入可以显著减少维度数量。

在独热编码中，一对一向量中只有 1 个元素的值为 1.0，其余所有元素的值均为 0.0。在多热编码（mutli-hot encoding），多个值可以为 1.0。

稀疏特征：稀疏特征的值主要为 0 或空。
稀疏表示法：稀疏表示法是指在稀疏矢量中存储 1.0 的位置。


## 合成特征与特征交叉

合成特征：对于数值数据，当特征与标签之间的关系是平方、立方或其他函数相关时，可以从现有特征中创建合成特征。

例如：假设某个场景下输入的特征数量为 2，训练线性回归模型 $y = b + w_1x_1 + w_2x_2$ 无法良好的拟合。分析数据发现特征间存在特定关系，因此假设 $x_3 = x_1^2,\ x_4 = x1*x2$ ，将线性回归模型转换为 $y = b + w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 = b + w_1x_1 + w_2x_2 + w_3x_1^2 + w_4x_1x_2$ 后重新训练模型。

对于上述假设，可以有更多的函数关系表示输入特征之间的关系，需要根据数据做具体分析。


特征交叉：对于分类数据，可以交叉两个或多个分类特征。

例如：分类 1 包含取值 A B C，分类 2 包含取值 a b c，这两个特征交叉（笛卡尔积）为 { Aa Ab Ac Ba Bb Bc Ca Cb Cc } ，其中每一项的值时基准特征值的乘积，因此特征交叉 Ba 的值为 (0, 1, 0)*(1, 0, 0) = (0, 0, 0, 1, 0, 0, 0, 0, 0)。


## 衡量数据集



## 嵌入

嵌入 embedding 通常是将一个离散的、高维的或符号化的对象（如单词、类别、用户、商品、图节点等）映射到一个连续的、相对低维的向量空间中的一个点（即一个向量），嵌入通常是降维过程


# 正则化

正则化的方式是在损失函数中增加对参数的惩罚，以获得更简化的参数

线性回归模型的正则化： 

梯度下降法增加正则化的损失函数： $J(\theta) = \frac{1}{2m}\sum_{1}^{m}(h_\theta(x^{(i)}) - y)^2 + \frac{1}{2m}\lambda\sum_{1}^{n}\theta_j^2$ 

梯度下降法增加正则化的梯度：

*  $\theta_{0} = \frac{1}{m}\sum_{1}^{m}(h_\theta(x^{(i)}) - y)x_0^{(i)}$ 
*  $\theta_{1 \dots m} = \frac{1}{m}\sum_{1}^{m}(h_\theta(x^{(i)}) - y)x_{j}^{(i)} + \frac{\lambda}{m}\theta_j$ 

正规方程增加正则化的求解：

* $\theta_{0} = (X^TX + \lambda \left( \begin{array}{c} 
0 & \dots \newline
\dots & 1 & \dots \newline
& \ddots \newline
\dots & \dots & 1 \newline
\end{array} \right) )^{-1} X^Ty$ 

在没有正则化之前，当样本数量 $m$ 小于特征数量 $n$ 时，$(X^TX)^{-1}$ 会无解。然而在正则化之后，正规方程一定会有解。

逻辑回归模型的正则化： 

梯度下降法增加正则化的损失函数： $J(\theta) = -\frac{1}{m}\sum_{1}^{m}(y^{(i)} log h_\theta(x^{(i)}) + (1-y) log (1 - h_\theta(x^{(i)}))) + \frac{1}{2m}\lambda\sum_{1}^{n}\theta_j^2$ 

梯度下降法增加正则化的梯度：
​	$\theta_{0} = \frac{1}{m}\sum_{1}^{m}(h_\theta(x^{(i)}) - y)x_0^{(i)}$ 
​	$\theta_{1 \dots m} = \frac{1}{m}\sum_{1}^{m}(h_\theta(x^{(i)}) - y)x_{j}^{(i)} + \frac{\lambda}{m}\theta_j$ 


# 机器学习模型评估

## 欠拟合和过拟合

机器学习出的模型不准确中通常代表着出现了以下两类问题：

* 欠拟合：模型无法很好地匹配训练集（损失很大），以至于几乎没有预测能力
* 过拟合：模型能够很好地匹配训练集（损失 ≈ 0），但是无法泛化到新的样本中（使用新的数据预测完全不可靠）

在遇到模型欠拟合或过拟合时，通常会采用以下几种方法：

* 使用更多的数据
* 增加特征数量/组合特征
* 减少特征数量
* 调高正则化参数
* 调低正则化参数
* 调整超参数

但是在选择使用这些方法之前，首先需要评估机器学习模型的性能：


## 评估模型选择

通过选择不同的特征、组合特征等方式，训练不同的模型

* 将数据拆分为训练集、交叉验证集和测试集，比例大约是 6:2:2 ，保证训练集数据分布的随机性
* 使用训练集训练模型，使用交叉验证集验证模型效果，使用测试集检验模型的泛化能力
* 神经网络模型通常首先选择 1 个隐藏层，较少的神经元数量，这样的计算量较小，然后再逐渐增加神经元数量和隐藏层数

按照不同的模型特征数量和损失值，绘制模型特征数量的损失曲线：

* 如果训练集和验证集（或测试集）的误差都比较大，那么是偏差较大，通常代表模型存在欠拟合问题。
* 如果训练集的误差比较小，验证集（或测试集）的误差比较大，那么是方差较大，通常代表模型存在过拟合问题。

## 评估正则化参数

首先在在不计算正则化损失的情况下，使用训练集数据训练模型。

然后在计算损失值时，按照不同的正则化参数计算正则化损失，绘制正则化参数的损失曲线：

验证集（或测试集）通常会在正则化参数较小和较大时的损失较大，而在适当时损失较小。

## 评估学习曲线：

绘制样本数的损失曲线：

* 如果训练集和验证集（或测试集）的误差随着样本数增大而相近，那么是偏差较大，通常代表模型存在欠拟合问题。
* 如果训练集和验证集（或测试集）的误差随着样本数增大而仍然存在较大的差距，那么是方差较大，通常代表模型存在过拟合问题。

增加样本数量对于高偏差问题没有帮助。
增加样本数量对于高方差问题有帮助。

## 二分类模型的评估指标

二元分类的结果可能有四种，可以通过混淆矩阵来表示：

|     | 实际正例 actually positive | 实际负例 actually negative |
| :-- | :--                      | :--                       |
| 预测为正例Predicted positive | **真正例 (TP, true positive)**：被正确分类为垃圾邮件的垃圾邮件。这些是系统自动发送到“垃圾邮件”文件夹的垃圾邮件。 | **假正例 (FP, false positive)**：非垃圾邮件被误分类为垃圾邮件。这些是最终进入“垃圾邮件”文件夹的正常电子邮件。 |
| 预测为负例Predicted negative | **假负例 (FN, false negative)**：垃圾邮件被错误分类为非垃圾邮件。这些是垃圾邮件过滤器未捕获的垃圾邮件，并已进入收件箱。 | **真负例 (TN, true negative)**：非垃圾邮件被正确分类为非垃圾邮件。 这些是直接发送到收件箱的正规电子邮件。 |

根据混淆矩阵，可以形成一些指标：

* 准确率：是指模型预测正确的比率（预测为正/负的样本中实际为正/负的比例）： $Accuracy = \frac{correct \ classfications}{total \ classifications} = \frac{TP+TN}{TP+TN+FP+FN}$，可以作为平衡数据集的模型训练指标。如果训练数据集不平衡，则需要考虑其他指标
* 召回率，或真实正预测率：是指所有实际正例中，预测正确为正例的比率： $Recall(or\ TPR) = \frac{correctly \ classified \ actual \ positives}{all \ actual \ positives} = \frac{TP}{TP+FN}$，在假负例比假正例开销更高时使用
* 假正预测率：是指所有实际负例中，预测错误为正例的比率： $FPR = \frac{incorrectly \ classified \ actual \ negatives}{all \ actual \ negatives} = \frac{FP}{FP+TN}$，在假正例比假负例开销更高时使用
* 精确率：是指所有预测正例中，实际正例的比率： $Precision = \frac{correctly \ classified \ actual \ positives}{everything \ classified \ as \ positive} = \frac{TP}{TP+FP}$，当正例预测的准确性非常重要时使用
* F1 得分：是召回率和精确率的一种调和平均数： $F1 = 2 * \frac{precision \ * \ recall}{precision \ + \ recall} = \frac{2*TP}{2*TP+FP+FN}$，当训练数据集不平衡时，该指标优于准确率

在平衡的数据集中，正例和负例标签的数量大致相同。如果一个标签比另一个标签更常见，则数据集可能不平衡

需要根据实际情况使用这些指标训练模型。

ROC 曲线（Receiver-operating characteristic curve，接收操作特征曲线）和 AUC 面积（Area under the curve，曲线下方面积）是分类模型在所有分类阈值上的可视化表示，用于评估模型在所有阈值下的效果。

ROC 曲线的绘制方式是在所有分类域值下计算 TPR 和 FPR 的值。完美模型会在某些域值下的 TPR 为 1.0，FPR 为 0.0，此时 AUC 为 1.0。
当 AUC 的取值越大，代表模型效果越好，但是也要考虑是否存在不平衡的样本数据的问题。
当 AUC 为 0.5 时，代表在这个域值下，二元分类器的表现和随机分类是一致的。

多元分类模型是二元分类模型的扩展。
如果每个数据只能分配到一个类，则可以将分类问题处理为多个二元分类问题。例如：首先建立第一个二元分类器对 A 和 B+C 进行分类，然后建立第二个二元分类器对 B 和 C 进行分类。

[注意]：二元分类模型的评估指标也可以扩展到其他模型中


## 多分类模型的评估指标

### 一、基于样本的指标

​准确率：​​

​定义：​​ 所有样本中被正确分类的比例。准确率 = (正确预测的样本数) / (总样本数)。
​优点：​​ 直观易懂，是整体分类效果的一个良好概括。
​缺点：​​ 在样本类别分布极度不平衡时，准确率会偏向多数类，不能很好地反映模型识别少数类的能力。
​计算：​​ 构建混淆矩阵后，对角线元素之和除以总元素数。



### 二、基于类别的指标（需要对每个类别分别计算）
需要为每个类别i计算：


TPᵢ: 实际是i且预测为i的数量。
FPᵢ: 预测为i但实际不是i的数量。
FNᵢ: 实际是i但预测不是i的数量。
TNᵢ: 实际不是i且预测不是i的数量（在多分类中计算较复杂，有时不显式计算）。


​精确率：​​

​定义（对类别i）:​​ 所有被模型预测为类别i的样本中，真正属于类别i的比例。Precisionᵢ = TPᵢ / (TPᵢ + FPᵢ)。
​含义：​​ 衡量模型预测类别i的可靠性。越高说明模型预测为i时，结果是i的可能性越大。



​召回率（或真正例率）：​​

​定义（对类别i）:​​ 所有真正属于类别i的样本中，被模型正确预测出来的比例。Recallᵢ = TPᵢ / (TPᵢ + FNᵢ)。
​含义：​​ 衡量模型找出类别i的能力。越高说明模型漏掉的i类样本越少。



​F1 分数：​​

​定义（对类别i）:​​ 精确率和召回率的调和平均值。F1ᵢ = 2 * (Precisionᵢ * Recallᵢ) / (Precisionᵢ + Recallᵢ)。
​含义：​​ 是综合考虑精确率和召回率的指标，在两者需要平衡时特别有用。当精确率和召回率都很高时，F1 才会高。



​特异度：​​

​定义（对类别i）:​​ 所有实际不属于类别i的样本中，被模型正确预测为不属于i的比例。Specificityᵢ = TNᵢ / (TNᵢ + FPᵢ)。
​含义：​​ 衡量模型识别“非i类”样本的能力。



​假正例率：​​

​定义（对类别i）:​​ 所有实际不属于类别i的样本中，被模型错误预测为属于i的比例。FPRᵢ = FPᵢ / (FPᵢ + TNᵢ)。
​含义：​​ 与特异度互补（FPRᵢ = 1 - Specificityᵢ）。



为了得到模型在所有类别上的综合性能评估，通常需要对基于类别的指标进行平均。常见的平均方法有：

​宏平均：​​

计算每个类别的指标（如 Precision, Recall, F1），然后直接取其算术平均值。
Macro-Precision = (Precision₁ + Precision₂ + ... + Precisionₙ) / num_classes
Macro-Recall = (Recall₁ + Recall₂ + ... + Recallₙ) / num_classes
Macro-F1 = (F1₁ + F1₂ + ... + F1ₙ) / num_classes
​特点：​​ 平等看待每个类，类别大小不平衡时，宏平均更能反映模型在小类上的性能。


​微平均：​​

先将所有类别的 TP, FP, FN (有时也包括 TN) 分别累加。
Micro-Precision = ΣTPᵢ / Σ(TPᵢ + FPᵢ) = ΣTPᵢ / (ΣTPᵢ + ΣFPᵢ)
Micro-Recall = ΣTPᵢ / Σ(TPᵢ + FNᵢ) = ΣTPᵢ / (ΣTPᵢ + ΣFNᵢ)
Micro-F1通常与Micro-Precision和Micro-Recall值相同（因为ΣFPᵢ = ΣFNᵢ）。
​特点：​​ 通过累加，相当于给每个样本平等权重。受大类影响更大，Micro-Precision = Micro-Recall = Micro-F1 = 准确率。


​加权平均：​​

计算每个类别的指标后，根据每个类别的样本数（或其他权重）进行加权平均。
Weighted-Precision = (w₁ * Precision₁ + w₂ * Precision₂ + ... + wₙ * Precisionₙ) / (w₁ + w₂ + ... + wₙ) (通常权重wᵢ取类别i的样本数)。
Weighted-Recall和Weighted-F1同理。
​特点：​​ 平衡宏平均和微平均的缺点，既考虑小类的性能，又考虑不同类别样本量的差异，​最常用的综合性指标之一。



### 三、其他重要指标


​混淆矩阵：​​

​定义：​​ N x N 矩阵（N 是类别数）。行代表真实类别，列代表预测类别。元素Cᵢⱼ表示真实为i类但被预测为j类的样本数。
​作用：​​ 是最基础、最详细的性能评估工具，直观展示了模型在每两个类别之间的识别错误情况（哪些类容易混淆）。所有计算类别的指标都基于此矩阵生成。



​Cohen's Kappa 系数：​​

​定义：​​ 在考虑数据集类别不平衡分布的前提下，量化分类器的性能比随机预测好多少。公式为：kappa = (p₀ - pₑ) / (1 - pₑ)，其中p₀是准确率（观察一致比例），pₑ是随机预测时的期望一致比例（根据类别边际分布计算）。
​含义：​​ 数值范围通常在 [-1, 1]（但更常见在 [0, 1]）。值越高越好：

0： 模型性能等同于随机猜测。
1： 模型完全正确。
<0： 模型表现比随机猜测还差（通常说明模型训练或数据有严重问题）。


​特点：​​ ​更能揭示模型性能本质，尤其是在处理不平衡数据集时，比单纯的准确率更能说明问题。



​ROC曲线和AUC（多分类扩展）：​​

​定义：​​ ROC曲线在二分类中是绘制 TPR(Recall) vs FPR 的曲线。对于多分类，有以下几种主要策略：

​One-vs-Rest (OvR):​​ 对每个类别i，将其视为正例，其他所有类视为反例，分别绘制一条ROC曲线，计算每个类别的AUC，然后取平均（宏平均或加权平均）。
​One-vs-One (OvO):​​ 对每两个不同的类别组合，将它们视为正反例，绘制一条ROC曲线，计算AUC，然后取所有组合结果的平均。


​AUC：​​ 表示对应ROC曲线下的面积。
​含义：​​ AUC衡量模型对各类别进行排序​（区分正反例）的能力，数值在 [0, 1] 之间，越接近1越好。AUC不受分类阈值影响，且对类别不平衡相对鲁棒。宏平均AUC(macro AUC)特别关注小类的性能。
​注意：​​ 多分类ROC/AUC的解释和计算比二分类更复杂，不同库的实现方式可能不同，报告结果时需要说明具体方法。



​对数损失：​​

​定义：​​ 也称交叉熵损失或多分类对数损失。直接衡量模型预测概率分布与真实分布之间的差异。公式为：Log Loss = - (1/N) * Σ(Σ yᵢⱼ * log(pᵢⱼ))其中N是样本数，yᵢⱼ是样本i在真实类别j上的指示变量（0或1），pᵢⱼ是模型预测样本i属于类别j的概率。
​含义：​​ 值越小越好，完美模型接近0。与仅关注最终类别标签的指标不同，对数损失评估的是预测概率的可靠性/置信度。它对预测错误的置信度高（即错判概率很大）施加了较大的惩罚。是训练中常用的损失函数。



​分类报告：​​

​定义：​​ 这是一个实用工具​（例如在scikit-learn中的classification_report），它汇总展示每个类别的精确率、召回率、F1分数以及支持度（该类别样本数），同时计算宏平均、加权平均、微平均（即准确率）等综合指标。
​作用：​​ 提供一站式、清晰的性能概览，方便比较各个类别的表现和综合指标。



### 四、如何选择指标？
选择哪项或哪几项指标取决于你的具体任务和关注点​：

​整体性能概览：​​ 起始点通常是准确率​（或等效的Micro-F1）、加权F1分数或Kappa系数。
​关注小类/类别平衡：​​ 如果识别少数类别很重要，看宏平均 F1 / Precision / Recall​ 或 ​Macro AUC。​混淆矩阵对识别错误模式至关重要。Kappa也是好指标。
​关注大类/整体效率：​​ 如果样本量大的类别更重要，看加权F1/Precision/Recall、准确率或Micro-F1。
​评估概率质量：​​ 如果预测概率的置信度很重要（例如推荐系统的排序、风险估计），用对数损失。
​评估排序能力（类别区分度）：​​ 如果需要评估模型对不同类别进行排序的能力，并且希望指标不受阈值和类别不平衡影响太大，看AUC​（需指明OvR宏平均或OvO）。
​详细错误分析：​​ 必须检查混淆矩阵。
​综合报告：​​ ​分类报告通常是首选，因为它在一个表里包含了大多数关键信息。

记住，通常不会只看单一指标，结合多个指标（例如 F1 加权平均 + 混淆矩阵 + Kappa 或 Macro AUC）才能对多分类模型的性能有一个全面且深入的理解，尤其在处理类别不平衡的数据时。

当然，不要忘记还需要对比模型的性能指标和人工的性能指标，对模型能否替代人工给出一个良好的结论。


# 如何构建大型的机器学习系统

1、机器学习 pipeline

将一个复杂的机器学习任务拆分到多个机器学习模块，分流程分步骤完成复杂任务
评估每个模块的改进对于整体模型的提升效果（上限分析）

2、构建特征

首先构建一个能够快速实现的算法，而不是设计一个复杂的系统。通过这个算法来检验数据。

* 学习曲线：通过学习曲线来检验，应该朝着哪个方向去构建特征
* 误差分析：通过分析误差数据，了解哪些问题出现的比较多，因此应该朝着哪个方向去构建特征

3、构建评估指标

* 精确率
* 精确率和召回率
* F1值

4、选择数据

如果特征中包含足够中的信息，能够构建模型，那么久不需要再寻找更多的数据。
否则需要找到更多的数据，提高特征中包含的信息。

考虑一个人类专家，在看到特征数据时，是否有自信来做出预测。


# 大规模数据集的机器学习

首先使用小样本量数据建模，然后评估学习曲线，如果随着样本量的增加，误差减小，那么可以增加样本量


## 随机梯度下降 Stochastic GD

为了解决大样本量下计算梯度困难的问题，可以使用随机梯度下降，每次只计算单一样本的梯度。


## 小样本梯度下降 Mini-batch GD

小样本梯度下降，每次使用全部样本中的一部分样本进行模型训练，直到使用全部样本。


## 在线学习

在线学习不采用固定的数据集，而是根据每一个输入来学习数据。对于大型网站来说，实时更新的数据会更有效。


## 并行计算

MapReduce 分拆计算任务到多个计算机。或者多个 CPU。


# Transformer 架构

编码器和解码器，对应的码是指字符编码。

字符编码有多种方式：

* 标记器 tokenizer：对每一个字符分配一个唯一的编码形成词汇表，例如：机-10，器-11，学-12，习-13，机器-14，学习-15。标记器表示的信息较为密集，且通过付出人工劳动，可以将含义相近的信息聚类在相近编码。
* 独热编码 tokenizer：对词汇表中的每一个字符分配一个向量 vector，例如：机-(1, 0, 0, 0, 0, 0)，器-(0, 1, 0, 0, 0, 0)，学-(0, 0, 1, 0, 0, 0)，习-(0, 0, 0, 1, 0, 0)，机器-(1, 1, 0, 0, 0, 0)，学习-(0, 0, 1, 1, 0, 0)。独热编码可以表示的信息是稀疏的


# 参考资料

[Machine Learning  | Google for Developers](https://developers.google.cn/machine-learning?hl=zh-cn)

[图灵1950论文《计算机器与智能(Computing Machinery and Intelligence)》全文译文 - 知乎](https://zhuanlan.zhihu.com/p/671028818)

[吴恩达机器学习]()

[对数损失函数的一点理解(怎么来的、与极大似然的关系) - 知乎](https://zhuanlan.zhihu.com/p/578769844)

[对数损失（Log Loss）详解（code） - 知乎](https://zhuanlan.zhihu.com/p/659617924)

[14 逻辑回归的本质及损失函数的推导、求解 - 知乎](https://zhuanlan.zhihu.com/p/103459570)

[如何通俗理解Word2Vec (23年修订版)-CSDN博客](https://blog.csdn.net/v_JULY_v/article/details/102708459)

[word2vec 中的数学原理详解（一）目录和前言_数学中vec-CSDN博客](https://blog.csdn.net/itplus/article/details/37969519)

[通用近似定理（Universal Approximation Theorem） - 知乎](https://zhuanlan.zhihu.com/p/10247926150)

[[深度学习之美05】神经网络最本质的理论基础是什么？ - 知乎](https://zhuanlan.zhihu.com/p/39334377)

[一起入门语言模型(Language Models) - 知乎](https://zhuanlan.zhihu.com/p/32292060)

[[5分钟深度学习\] #01 梯度下降算法_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1oY411N7Xz)
