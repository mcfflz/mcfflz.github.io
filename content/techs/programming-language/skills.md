---
date: 2026-02-12T12:00:00+08:00
title: Skills
draft: false
# bookFlatSection: false        # 是否显示扁平章节（默认false）
# bookToc: true                 # 是否显示目录（默认true）
# bookHidden: false             # 是否在侧边栏列表中隐藏（默认false）
# bookCollapseSection: true     # 章节是否默认折叠（默认false）
# bookComments: false           # 是否启用评论（默认false）
# bookSearchExclude: true       # 是否从搜索结果中排除（默认false）
# params:                       # 自定义参数
#   maths: true                 # 数学公式支持
# weight: 1                     # 内容权重（排序用）
---

# Skills

## 参考资料

[Agent Skills Specification](https://agentskills.io/specification)

[github anthropics skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator)


## 目录结构

源文件结构：

```
skill-name/
├── SKILL.md              # 对 skills 的说明
├── references/           # 存放 skills 可以参考的资料
│   ├── patterns.md       # demo
│   └── advanced.md
├── assets/               # 存放 skills 输出结果可以使用的静态资源
│   ├── templates
│   ├── images
│   ├── data
│   └── examples
│       ├── example1.sh
│       └── example2.json
└── scripts/              # 存放 skills 可以执行的可执行脚本
    └── validate.sh
```


## SKILL.md 模板

SKILL.md 文件必须包含一段 YAML 前言，后面是 Markdown 内容。

### YAML 前言

```yaml
---
name: skill 的名称，和目录名 `skill-name` 保持一致
description: >- 
  描述 skill 的功能、适用场景。
  Agent 会根据技能描述和问题的相关性，决定是否激活技能。
license: 开源协议 Apache-2.0
compatibility: 描述兼容性，包括系统、环境、网络等。
metadata:
  author: mcfflz 元数据，可自定义
  version: 0.1.0
allowed-tools: 描述 skill 可以使用的工具
---
```

### SKILL 正文

正文按流程描述 Agent 需要完成的任务、最终输出结果。仅在 skill 被触发后加载。

参考 skill-creator，正文应当描述：

1. 专业化工作流程 - 针对特定领域的多步骤程序

2. 工具集成 - 处理特定文件格式或API的说明

3. 领域专业知识 - 公司特定知识、模式、业务逻辑

4. 捆绑资源 - 用于复杂和重复任务的脚本、参考资料和资产

对每条信息提出质疑：“真的需要这个解释吗？”以及“这段内容是否值得其 token 成本？”。
优先使用简洁示例而非冗长解释。

将 SKILL.md 正文保持在基本要素范围内，并保持在 500 行以内，以最大限度地减少上下文膨胀。接近此限制时，将内容拆分为单独的文件。

当将内容拆分到其他文件中时，从 SKILL.md 正文引用它们并清楚描述何时读取它们非常重要，以确保技能的读者知道它们的存在以及何时使用它们。

关键原则：​ 当一个技能支持多种变体、框架或选项时，只在 SKILL.md 正文中保留核心工作流程和选择指南。将特定于变体的详细信息（模式、示例、配置）移动到单独的参考资料文件中。

保持引用文件距离 SKILL.md 仅一层深度。所有引用文件都应直接从 SKILL.md 链接。

不要编写非常大 skill，使用工作流编排小的 skill 来完成复杂任务。


### 示例

```
---
name: your-skill-name
description: >-
  描述 skill 的功能、适用场景。
license: Apache-2.0
metadata:
  author: mcfflz
  version: 0.1.0
---

# [技能名称]

[这里可以放置更详细的技能介绍，补充说明技能的特性和优势。]

## 工作流程

### 1. 理解任务
- 仔细分析用户请求，明确核心目标、具体要求和任何约束条件。
- 明确输出结果的格式。
- 如有必要，向用户提问以澄清模糊或补充缺失的信息。

### 2. 执行操作
- 获取或准备必要资源，例如：读取特定文件、调用API、初始化工具等。
- 按照步骤和逻辑执行操作。

### 3. 生成输出
- 将最终结果组织成用户要求的格式。
- 确保输出准确、完整。

### 5. 检查输出结果
- 检查输出结果是否满足用户诉求。
- 如果结果不符合预期，分析问题，并向用户请求重新处理问题。

## 资源目录

本技能可能需要使用以下资源：

### 参考文件
- `references/` 目录下的文件。
- 当需要 xx 知识时，阅读 `` 文件。
- 当需要 xx 知识时，阅读 `` 文件。

### 脚本文件
- `scripts/` 目录下的文件。
- 当需要执行 xx 时，使用 `` 脚本。
- 当需要执行 xx 时，使用 `` 脚本。

### 静态文件
- `assets/` 目录下的文件。
- 当需要 xx 资源时，使用 `` 文件。
- 当需要 xx 资源时，使用 `` 文件。

*注意：这些资源仅在需要时按需加载，需要在正文中明确说明在何时使用。*

## 示例

### 示例1：基本用法
**用户输入**: [示例用户请求]
**技能响应**: [展示技能将如何回应和执行]

### 示例2：进阶用法  
**用户输入**: [更复杂的用户请求]
**技能响应**: [展示技能如何处理复杂场景]
```

