---
date: 2026-02-26T00:00:00+08:00
title: AI Coding Agent
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

# AI 编程智能体

## claude code

### 参考资料

无

### 安装

环境：tencentcloud Ubuntu Server 24.04 LTS 64bit

```bash
npm install -g @anthropic-ai/claude-code
```

### 配置文件

```bash
# ~/.claude/settings.json
# "env": {
#     "ANTHROPIC_AUTH_TOKEN": "sk-",
#     "ANTHROPIC_BASE_URL": "https://",
#     "ANTHROPIC_MODEL": "qwen3"
#   },
```

## opencode

### 参考资料

[Opencode docs](https://www.opencodecn.com/docs)

### 安装

```bash
# 使用官方提供的安装脚本
curl -fsSL https://opencode.ai/install | bash
# 也可以使用npm安装
npm install -g opencode-ai
```

### 配置文件

```bash
# `~/.config/opencode/opencode.json` - 全局配置
# 配置模型供应商
# "provider": {
#   "google": {
#     "name": "Google",
#     "npm": "@ai-sdk/google",
#     "options": {
#       "apiKey": "",
#       "baseURL": ""
#     },
#     "models": {
#       "gemini-3.1-pro-antigravity":{
#         "name": "Gemini-3.1-Pro-Preview"
#       }
#     }
#   }
# }

# 配置智能体
# "agent": {
#   "orchestrator": {
#     "description": "软件研发工程团队的 team leader",
#     "mode": "primary/subagent",
#     "file": "~/.opencode/agents/orchestrator.md"
# }

# `/.opencode/opencode.json` - 项目特定的配置
# 配置方式和全局配置内容相同
```

### opencode tui 常用命令

```bash
# 启动
opencode # 当前工作目录启动
opencode /path/to/project # 指定工作目录启动

# 文件引用
@packages/functions/src/api/index.ts 中的身份验证是如何处理的？

# Bash 命令
# 以 `!` 开头的消息会运行 shell 命令，命令的输出会作为工件结果添加到对话中
!ls -la

# 显示帮助对话框
/help

# init 创建或更新 `AGENTS.md` 文件。[了解更多](https://www.opencodecn.com/docs/rules)
/init

# 列出可用模型
/models

# 开始新对话
/new

# 列出并切换会话
/sessions

# 撤销对话中的最后一条消息。删除最近的用户消息、所有后续响应以及任何文件更改。
/undo

# 重做之前撤销的消息。仅在使用 `/undo` 后可用
/redo

# 仅在一个 session 下有效。分享当前对话
/share

# 仅在一个 session 下有效。取消分享当前对话
/unshare

# 仅在一个 session 下有效。压缩当前对话
/compact

# 退出
/exit
```

### opencode cli 常用命令

```bash
# 导出 session 
opencode export <session_id> > <file_name>
```


## codex

### 安装

```bash
# 使用 npm 安装
npm install -g @openai/codex
```
