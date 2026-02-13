---
date: 2026-02-12T12:00:00+08:00
title: Java CLI
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

# javac

java 编译工具。

## javac

javac 命令基础用法

```java
// 示例一：编译当前目录下的 HelloWorld.java 文件
javac HelloWorld.java
// 示例二：编译 ./src/main/java/lesson1/ 目录下的 HelloWorld.java 文件
javac ./src/main/java/lesson1/HelloWorld.java
// 示例三：编译当前目录下的 *.java 文件
javac *.java
```



## javac -encoding utf8

java 编译使用 utf-8 字符集（Windows 默认使用 GBK 字符集）

```java
// 示例：使用 utf8 字符集编译 HelloWorld.java 文件
javac -encoding utf8 HelloWorld.java
```



## javac -d classpath

java 编译指定输入文件目录

```java
// 将当前目录下的 *.java 文件编译，并输出至上级目录的 classes 文件夹下
java HelloWorld.java -d ../classes
```



# java

java 命令执行工具

## java

java 命令基础用法

```java
// 示例一：编译当前目录下的 HelloWorld.java 文件
java HelloWorld
// 示例二：编译 ./src/main/java/lesson1/ 目录下的 HelloWorld.java 文件
java ./src/main/java/lesson1/HelloWorld
// 示例三：编译 ./src/main/java/lesson1/ 包下的 HelloWorld.java 文件，需要在包内声明 package
java src.main.java.lesson1.HelloWorld
```

