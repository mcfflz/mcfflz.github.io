---
date: 2026-02-12T12:00:00+08:00
title: Node.js
draft: false
# bookFlatSection: false        # 是否显示扁平章节（默认false）
# bookToc: true                 # 是否显示目录（默认true）
# bookHidden: false             # 是否在侧边栏列表中隐藏（默认false）
# bookCollapseSection: false    # 章节是否默认折叠（默认false）
# bookComments: false           # 是否启用评论（默认false）
# bookSearchExclude: false      # 是否从搜索结果中排除（默认false）
# params:                       # 自定义参数
#   maths: true                 # 数学公式支持
weight: 1                     # 内容权重（排序用）
---

# node 安装

[nodejs，zip压缩版安装与配置_焱的博客-CSDN博客](https://blog.csdn.net/jincheng_921/article/details/100109747)

[VSCode搭建VUE 开发环境 - sunny123456 - 博客园 (cnblogs.com)](https://www.cnblogs.com/sunny3158/p/14438325.html)



## node 下载

[Node.js (nodejs.org)](https://nodejs.org/zh-cn/)\

## node 路径配置

```bash
# 在 node 根目录下创建 node_global node_cache 文件夹
npm config set prefix "D:\DevTools\node.js-14.17.5\node_global"
npm config set cache "D:\DevTools\node.js-14.17.5\node_cache"
```

## node 环境变量

```bash
NODE_HOME=D:\DevTools\node.js-14.17.5
PAHT=%NODE_HOME%;%NODE_HOME%\node_global
```

## 设置阿里仓库

```bash
npm config set registry http://registry.npm.taobao.org/

# 恢复
# npm config set registry https://registry.npmjs.org/
```



# Vue-cli 脚手架下载

```bash
npm install @vue/cli -g
```

