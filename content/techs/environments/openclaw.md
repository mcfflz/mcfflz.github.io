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

## 参考资料

- [openclaw](https://docs.openclaw.ai/)

## 安装

环境：tencentcloud Ubuntu Server 24.04 LTS 64bit

```bash
# 下载安装 Node.js
# 先到官方网站 https://nodejs.org/en/download 获取稳定版本和下载链接
curl -O https://nodejs.org/dist/v24.13.1/node-v24.13.1-linux-x64.tar.xz
tar -xJvf node-v24.13.1-linux-x64.tar.xz

# 添加环境变量
vi ~/.bashrc
export PATH=$PATH:/home/ubuntu/node-v24.13.1-linux-x64/bin
source ~/.bashrc

# 验证安装情况
node --version
npm --version
# 更换为国内镜像
npm config set registry https://mirrors.cloud.tencent.com/npm/

# 下载安装 OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash
# 初始化配置并启动为守护进程
openclaw onboard --install-daemon
# 检查服务状态
openclaw gateway status
# 启动 web 仪表板
openclaw dashboard
```

## 访问方式

### 远程服务器访问 dashboard
```bash
# 本地终端执行 SSH 隧道转发
ssh -N -L 18789:127.0.0.1:18789 ubuntu@xxx.xxx.xxx.xxx
# 本地浏览器访问
http://127.0.0.1:18789/
```

### 本地直接访问
```bash
openclaw tui
```

## OpenClaw 架构

```mermaid
graph TB
    %% === 用户与接入层 ===
    User[用户/开发者] --> Channels[消息渠道<br/>Telegram/WhatsApp/API]
    User --> TUI[终端用户界面<br/>TUI]
    User --> Dashboard[系统仪表板<br/>Dashboard]

    %% === 控制中枢：网关 ===
    Channels --> Gateway[网关 Gateway<br/>中央调度/会话管理/消息路由]
    TUI --> Gateway
    Dashboard --> Gateway

    %% === 核心：智能体 (包含内部组件) ===
    subgraph "智能体 Agent"
        direction LR
        A_Core[代理核心<br/>任务规划与协调] --> A_Memory[记忆系统]
        A_Core --> A_Skills[技能执行器]

        A_Memory --> M1[短期记忆<br/>会话上下文]
        A_Memory --> M2[长期记忆<br/>MEMORY.md]
        A_Memory --> M3[向量记忆<br/>语义检索SQLite向量库]

        A_Skills --> S1[Shell命令]
        A_Skills --> S2[文件操作]
        A_Skills --> S3[网络请求]
        A_Skills --> S_More[...更多插件]
    end

    %% === 外部服务 ===
    BaseModel[基础模型服务<br/>Claude API / GPT / Ollama...]
    Tools[外部API<br/>邮件服务器/Github...]

    %% === 主要数据流向 ===
    Gateway --> A_Core

    A_Core --> BaseModel
    BaseModel --> A_Core
    A_Skills --> Tools
    Tools --> A_Skills
    
    A_Core --> Gateway

    %% === 样式定义 ===
    classDef user fill:#f9f,stroke:#333,stroke-width:2px
    classDef access fill:#ccf,stroke:#333,stroke-width:2px
    classDef control fill:#dda0dd,stroke:#333,stroke-width:2px
    classDef agent fill:#ffa07a,stroke:#333,stroke-width:3px
    classDef external fill:#98fb98,stroke:#333,stroke-width:2px
    
    class User user
    class Channels,TUI,Dashboard access
    class Gateway control
    class A_Core,A_Memory,A_Skills,M1,M2,M3,S1,S2,S3,S_More agent
    class BaseModel,Tools external
```

OpenClaw 架构主要包括：

- **TUI (Terminal UI)**: 终端界面，适合快速操作
- **Dashboard/Web界面**: 提供图形化管理界面
- **Channels**: 多种接入渠道，支持不同交互方式
- **Gateway**: 网关，所有交互的唯一出入口，处理请求分发和路由
- **Agent**: 智能体，核心系统功能
- **Skills**: 技能，Agent可以使用的工具
- **Memory**: 记忆，Agent可以从长期记忆、每日笔记和当前会话中获取上下文
- **Models**: 模型，Agent调用模型来规划任务和执行


## 核心配置文件

```bash
vi ~/.openclaw/openclaw.json
```


## 常用 openclaw 命令行工具

### 配置管理
```bash
# 查看当前配置
openclaw config show

# 设置配置项
openclaw config set <key> <value>

# 重置配置
openclaw config reset

# 导出配置
openclaw config export > backup-config.json

# 导入配置
openclaw config import < backup-config.json
```

### 服务管理
```bash
# 检查网关状态
openclaw gateway status

# 启动网关服务
openclaw gateway start

# 停止网关服务
openclaw gateway stop

# 重启网关服务
openclaw gateway restart

# 查看网关日志
openclaw gateway logs
```

### 模型管理
```bash
# 列出所有可用模型
openclaw models list

# 查看当前默认模型
openclaw models current

# 设置默认模型
openclaw models set <model-name>

# 测试模型连接
openclaw models test <model-name>
```

### 技能管理
```bash
# 列出所有技能
openclaw skills list

# 安装技能
openclaw skills install <skill-name>

# 更新技能
openclaw skills update <skill-name>

# 卸载技能
openclaw skills uninstall <skill-name>

# 查看技能详情
openclaw skills show <skill-name>

# 启用技能
openclaw skills enable <skill-name>

# 禁用技能
openclaw skills disable <skill-name>
```


### 通道管理
```bash
# 列出所有通道
openclaw channels list

# 查看通道状态
openclaw channels status <channel-name>

# 启用通道
openclaw channels enable <channel-name>

# 禁用通道
openclaw channels disable <channel-name>
```

## 个人理解

openclaw 最大的意义在于让个人能够编辑 agent ，帮助完成一些简单的工作。

openclaw 的架构也可以支持一些多 agent 的复杂应用。

