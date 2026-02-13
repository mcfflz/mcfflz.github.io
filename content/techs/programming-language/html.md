---
date: 2026-02-12T12:00:00+08:00
title: HTML
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

# 元素

## 区块元素

- 霸占一行，不能与其他任何元素并列。
- 能接受宽高，如果不设置宽度，那么宽度将默认变为父级的100%。
- 例如：

## 内联元素

- 与其他行内元素并排
- 不能设置宽高，默认的宽度就是文字的宽度

## 分类

在HTML的角度来讲，标签分为：

* 文本级标签：p , span , a , b , i , u , em
* 容器级标签：div , h系列 , li , dt ,dd

p：里面只能放文字和图片和表单元素，p里面不能放h和ul，也不能放p。

从CSS的角度讲，CSS的分类和上面的很像，就p不一样：

* 行内元素：除了p之外，所有的文本级标签，都是行内元素。p是个文本级标签，但是是个块级元素。
* 块级元素：所有的容器级标签，都是块级元素，以及p标签。

