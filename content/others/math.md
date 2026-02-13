---
date: 2026-02-12T12:00:00+08:00
title: Mathematical Reference
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

# 维纳过程

维纳过程是布朗运动的数学模型。

[维纳过程-概率论与数理统计- 人大经济论坛-经管百科 (pinggu.org)](http://wiki.pinggu.org/doc-view-29845.html)

[布朗运动、伊藤引理——细说Black-Scholes公式的前世今生（上篇） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/32664487)



## 布朗运动

https://www.bilibili.com/video/BV1tD4y197Sy

一维布朗运动

二维布朗运动



https://www.bilibili.com/video/BV1Cv411b7LW/



# 微分方程

https://www.bilibili.com/video/BV1Tr4y1w7Ef

和代数方程相比，方程中多了函数对自变量的各阶倒数，这样的方程叫做微分方程。

常微分方程（ordinary differential equation）和偏微分方程（partial differential equation）

常微分方程只存在一个自变量：
$$
F(x, f, \frac{dy}{dx},\cdots, \frac{d^ny}{dx^n}) = 0
$$
偏微分方程存在多个自变量：
$$
F(x1, x2, \cdots, x_m, f, \frac{\partial y}{\partial x_1}, \frac{\partial y}{\partial x_2},\cdots, \frac{\partial^ny}{\partial x_1^{\alpha_1}\partial x_2^{\alpha_2}\cdots\partial x_m^{\alpha_m}}) = 0

\\
记向量X=(x_1, x_2, \cdots, x_n),
\\ 则定义向量：
\alpha=(\alpha_1, \alpha_2, \cdots, \alpha_m), \\
\alpha的阶数
\abs{\alpha}=\alpha_1+ \alpha_2+ \cdots+ \alpha_m \\

可以定义如下记号：
D^{\alpha}_y = \frac{\partial^{\abs{\alpha}}y}{\partial x_1^{\alpha_1}\partial x_2^{\alpha_2}\cdots\partial x_m^{\alpha_m}}
$$


## 常微分方程

一阶/高阶、线性/非线性、通解（显式/隐式）/特解（初值条件）

## 偏微分方程

一阶/高阶、线性/非线性（半线性、拟线性、完全非线性）、齐次/非齐次

## 泰勒展开

一元函数的泰勒展开：
$$
f(x)=f(x_0)+\frac{f'(x_0)}{1!}(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)+o(x-x_0)^n
$$


多元函数的泰勒展开：
$$
\begin{align}
& f(x,y,\cdots,z)=f(x_0)+\cdots+f(z_0) \\

& +\frac{\partial f}{1!\partial x}(x_1-x_0)+\cdots+\frac{\partial f}{1!\partial z}(z_1-z_0) \\

& +\frac{\partial f^2}{2!\partial x^2}(x_1-x_0)^2+\frac{\partial f^2}{2!\partial x\partial y}(x_1-x_0)(y_1-y_0)+\cdots+\frac{\partial f^2}{2!\partial x\partial z}(x_1-x_0)(z_1-z_0)+\cdots+\frac{\partial f^2}{2!\partial z^2}(z_1-z_0)^2 \\

& +\cdots \\

& +\frac{\partial f^n}{n!\partial x^n}(x_1-x_0)^n+ \frac{\partial f^n}{n!\partial x^{n-1}\partial y}(x_1-x_0)^{n-1}(y_1-y_0)+ \cdots+ \frac{\partial f^n}{n!\partial x^{n-1}\partial z}(x_1-x_0)^{n-1}(z_1-z_0)+\cdots+\frac{\partial f^n}{n!\partial z^n}(z_1-z_0)^n
\end{align}
$$



# 随机过程
