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

# Node.js

## 参考资料

[关于 Node.js](https://nodejs.org/zh-cn/about)

## 概述

Node.js 不是一个 JavaScript 框架，而是一个 JavaScript 运行时环境。它让 JavaScript 可以脱离浏览器运行在服务器端，执行各种后端任务。

Node.js 具有以下优势：

1. **统一技术栈**：前后端都可以使用 JavaScript，减少语言切换成本
2. **高性能**：V8 引擎优化良好，非阻塞 I/O 处理大量并发请求
3. **丰富的生态**：npm 是世界上最大的开源库生态系统
4. **社区活跃**：大量开源项目和解决方案
5. **适合实时应用**：WebSocket 和事件驱动模型非常适合聊天、协作等实时应用

## 安装

```bash
# 查找需要的版本 https://nodejs.org/zh-cn/download 执行命令
# 也可以直接下载压缩文件后配置环境变量
# 我们选择配置环境变量的方式，这样更能掌握环境
# 在 PATH 下添加目录即可
export PATH=$PATH:/home/ubuntu/node-v24.13.1-linux-x64/bin

# 验证安装情况
node --version
npm --version

# Windows 环境下会出现 powershell 不支持执行未知 .ps 文件
# 查询执行策略
Get-ExecutionPolicy
# 更新执行策略为可执行本地文件
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# 更换为国内镜像
npm config set registry https://mirrors.cloud.tencent.com/npm/
```

## 第一个 Node.js 程序

创建一个名为 `hello.js` 的文件，输入以下代码：

```javascript
// 输出 "Hello, World!" 到控制台
console.log("Hello, Node.js!");
```

在终端运行该文件：

```bash
node hello.js
```

你应该会看到输出："Hello, Node.js!"

## npm 包管理器

npm 是 Node.js 的包管理器，可以管理项目依赖。

### 初始化项目

```bash
# 初始化新项目
npm init

# 快速初始化（使用默认值）
npm init -y
```

这会创建一个 `package.json` 文件，记录项目信息和依赖。

### 安装包

```bash
# 安装本地环境依赖
npm install <package-name>

# 安装指定版本
npm install <package-name>@<version>

# 全局安装包
npm install -g <package-name>

# 安装开发环境依赖
npm install --save-dev nodemon
```

### 更新包

```bash
# 查看所有可更新的包（本地）
npm outdated

# 查看可更新的全局包
npm outdated -g

# 更新单个包到最新版本
npm update <package-name>

# 更新所有本地包到最新版本（遵循package.json中的版本范围）
npm update

# 更新所有全局包到最新版本
npm update -g

# 更新包到最新主要版本（可能包含破坏性变更）
# 先安装npm-check-updates工具
npm install -g npm-check-updates

# 检查哪些包可以更新（不实际更新）
ncu

# 更新package.json中的版本号
ncu -u

# 然后运行安装
npm install
```

### 卸载包

```bash
# 查看已安装包的详细信息
npm list <package-name>

# 卸载包
npm uninstall <package-name>

# 卸载全局包
npm uninstall -g <package-name>
```

### 版本管理

```bash
# 查看包的版本信息
npm view <package-name> versions

# 查看包的最新版本
npm view <package-name> version

# 在package.json中固定版本
# 使用精确版本号（不自动更新）
"dependencies": {
  "express": "4.18.2"
}

# 使用语义化版本控制
"dependencies": {
  "express": "^4.18.2",  # 允许更新补丁和次要版本
  "lodash": "~4.17.21"   # 只允许更新补丁版本
}
```


### 配置管理

```bash
# 查看所有配置项（包括默认值）
npm config list

# 查看全局配置
npm config list -g

# 获取某个特定配置项的值
npm config get <key>
# 示例：获取当前注册表地址
npm config get registry

# 设置一个配置项
npm config set <key> <value>

# 删除一个配置项
npm config delete <key>

# 将配置恢复为默认值
npm config delete <key> -g

# 设置全局配置项
npm config set <key> <value> -g
# 示例：设置全局安装路径
npm config set prefix ~/.npm-global -g

# 在项目中编辑本地.npmrc文件
npm config edit

# 编辑全局npmrc文件
npm config edit -g

# 设置包安装时的认证令牌（常用于私有仓库）
npm config set //<registry-domain>/:_authToken <your-token>
```

### 其他命令

```bash
# 查看包的文档
npm docs <package-name>

# 查看包的仓库地址
npm repo <package-name>
```
