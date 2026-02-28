---
date: 2026-02-26T00:00:00+08:00
title: Opencode
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

# Opencode

## 参考资料

[Opencode docs](https://www.opencodecn.com/docs)

## 概述

OpenCode是一个开源的编程助手工具，专注于提供智能化的代码生成、补全和分析功能。能够帮助开发者提高编程效率，通过自然语言描述生成相应代码，或对现有代码进行优化建议。

## 安装

环境：tencentcloud Ubuntu Server 24.04 LTS 64bit

```bash
# 使用官方提供的安装脚本
curl -fsSL https://opencode.ai/install | bash
# 也可以使用npm安装
npm install -g opencode-ai
```

## 配置文件

- `~/.config/opencode/opencode.json` - 全局配置，通常在这里配置模型供应商

- `opencode.json` - 项目特定的配置

## opencode tui 常用命令

OpenCode 提供了一个终端用户界面（TUI），可以通过以下命令启动：

```bash
# 当前工作目录
opencode
# 或者指定工作目录
opencode /path/to/project
```

TUI 提供了直观的终端界面，用于在项目中与 LLM 协作。

### 文件引用

可以在消息中使用 `@` 引用文件。

```
@packages/functions/src/api/index.ts 中的身份验证是如何处理的？
```

文件内容会自动添加到对话中。

### Bash 命令

以 `!` 开头的消息会运行 shell 命令。
```
!ls -la
```

命令的输出会作为工件结果添加到对话中。

### 斜杠命令

在使用 OpenCode TUI 时，可以输入 `/` 后跟命令名称来快速执行操作。以下是常用的斜杠命令：

#### help
显示帮助对话框。
```
/help
```

#### init
创建或更新 `AGENTS.md` 文件。[了解更多](https://www.opencodecn.com/docs/rules)。
```
/init
```

#### models
列出可用模型。
```
/models
```

#### new
开始新对话。别名：`/clear`
```
/new
```

#### sessions
列出并切换会话。别名：`/resume`、`/continue`
```
/sessions
```

#### undo
撤销对话中的最后一条消息。删除最近的用户消息、所有后续响应以及任何文件更改。
> 提示：所做的任何文件更改也会被还原。
在内部，这使用 Git 来管理文件更改。所以你的项目**需要是一个 Git 仓库**。
```
/undo
```

#### redo
重做之前撤销的消息。仅在使用 `/undo` 后可用。
> 提示：任何文件更改也将被恢复。
在内部，这使用 Git 来管理文件更改。所以你的项目**需要是一个 Git 仓库**。
```
/redo
```

#### exit
退出 OpenCode。别名：`/quit`、`/q`
```
/exit
```

#### share
仅在一个 session 下有效。分享当前对话。
```
/share
```

#### unshare
仅在一个 session 下有效。取消分享当前对话。
```
/unshare
```

#### compact
仅在一个 session 下有效。压缩当前对话。别名：`/summarize`
```
/compact
```

## opencode cli 常用命令

```bash
# 导出 session 
opencode export session_id > file_name

```