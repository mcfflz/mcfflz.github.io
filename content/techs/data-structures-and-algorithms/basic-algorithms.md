---
date: 2026-02-12T12:00:00+08:00
title: Basic Algorithms
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

# 基础算法

## 思路

使用伪代码描述基础算法的实现思路，并任选一种语言实现。

复杂算法单独介绍。


## 排列组合算法

排列组合算法实质上是递归问题。

题目1：假设有 m 个小球中，一次性取出 n 个小球（m>=n），枚举所有的可能性。

```java
假设 m = [1,2,3,4,5]
假设 n = 3
则可以有以下 10 种可能：
[] -- [1] -- [1,2] -- [1,2,3]
[] -- [1] -- [1,2] -- [1,2,4]
[] -- [1] -- [1,2] -- [1,2,5]
[] -- [1] -- [1,3] -- [1,3,4]
[] -- [1] -- [1,3] -- [1,3,5]
[] -- [1] -- [1,4] -- [1,4,5]
[] -- [2] -- [2,3] -- [2,3,4]
[] -- [2] -- [2,3] -- [2,3,5]
[] -- [2] -- [2,4] -- [2,4,5]
[] -- [3] -- [3,4] -- [3,4,5]
寻找规律，发现为递归：
每次都按照小球的顺序，从中选取一个小球，加入到结果集中来；
退出条件为，当结果集的大小 = n 时。

public class Combination {
	List<Stack<Integer>> res = new ArrayList<>();
    Stack<Integer> stack = new Stack<>();
    int m;
    int n;
    
    public void combine(int m, int n) {
        int[] used = new int[m];
        helper(0);
    }
    
    public void helper(int start) {
        if (stack.size() == n) {
            res.add(stack);
            return;
        }
        for (int i = start; i <= m; i++) {
            if (stack.contains(i)) {
                continue;
            }
            stack.add(i);
            helper(start + 1);
            stack.pop();
        }
    }
    public static void main(String[] args) {
        combine(m, n);
    }
}
```



题目2：假设有 m 个小球中，按顺序取出 n 个小球（m>=n），枚举所有的可能性（当 m = n 时，也称全排列问题）。

```java
假设 m = [1,2,3]
假设 n = 3
则可以有以下 6 种可能性：
[] -- [1] -- [1,2] -- [1,2,3]
[] -- [1] -- [1,3] -- [1,3,2]
[] -- [2] -- [2,1] -- [2,1,3]
[] -- [2] -- [2,3] -- [2,3,1]
[] -- [3] -- [3,1] -- [3,1,2]
[] -- [3] -- [3,2] -- [3,2,1]


```

$$
C^n_{m} = \begin{cases}
\frac{A^n_{m}}{n!} = \frac{m!}{n!(m-n)!}
\\
\\
C^{m-n}_{m}
\\
\\
C^{n}_{m-1} + C^{n-1}_{m-1}
\end{cases}
$$

