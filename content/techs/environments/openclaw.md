---
date: 2026-02-12T12:00:00+08:00
title: OpenClaw
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

# OpenClaw

## 安装

```bash
# 下载安装 Node.js
# 到官方网站 https://nodejs.org/en/download 查找稳定版本
curl -O https://nodejs.org/dist/v24.13.1/node-v24.13.1-linux-x64.tar.xz
tar -xJvf node-v24.13.1-linux-x64.tar.xz
# 添加环境变量
vi ~/.bashrc
export PATH=$:PATH/home/ubuntu/openclaw/node-v24.13.1-linux-x64/bin

# 下载安装 OpenClaw
# https://docs.openclaw.ai/start/getting-started
curl -fsSL https://openclaw.ai/install.sh | bash
# 阅读安全协议 Security
# 安装模式 Onboarding mode 默认端口 18789
# 选择模型提供商 Model/auth provider
# 过滤模型提供商 Filter models by provider
# 默认模型 Default model
# 选择渠道 Channel status
# 选择技能 Skills status
# 一堆选项...
# 选择技能 Hook
```