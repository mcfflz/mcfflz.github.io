---
date: 2026-02-12T12:00:00+08:00
title: Java ClassLoader
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

# ClassLoader

## 概述

java 类加载器。

java 程序源代码，并在内存中创建对应的 class 对象，这个过程称之为类的加载，整个过程如图所示：

```
src(*.java) -(javac 编译)->  dist(*.class)

dist --> 加载(loading) --> 验证(vertification) --> 准备(preparation) --> 解析(resolution) --> 初始化(initialization) --> jvm 内存堆区存储 --> jvm 内存栈区引用
```

