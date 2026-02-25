---
name: web-search
description: >-
  通过指定的搜索引擎（如 Bing、Google、DuckDuckGo、Baidu 等）搜索关键词，获取搜索结果和网页内容，并将相关内容添加到对话上下文中。
license: Apache-2.0
metadata:
  author: mcfflz
  version: 1.0.0
---

# Web Search Skill

本技能用于执行网络搜索任务，获取实时信息并添加到上下文中，弥补模型知识的时间限制。

## 激活条件

当用户请求以下任一类任务时，本技能应被激活：
- "搜索 XXX 的最新资讯"
- "查找关于 XXX 的信息"
- "帮我搜索 XXX"
- "查询 XXX 的更新"
- 任何涉及需要实时信息或最新数据的查询

## 支持的搜索引擎

本技能支持以下搜索引擎（按优先级排序）：
1. **Bing** - 需要 Microsoft Azure 订阅和 API Key https://azure.microsoft.com/en-us/services/cognitive-services/bing-web-search-api/
2. **Google** - 需要 Custom Search API Key 和搜索引擎 ID https://developers.google.com/custom-search/v1/overview
3. **DuckDuckGo** - 无需 API Key，隐私友好，推荐默认使用 https://duckduckgo.com/
4. **Baidu** - 无需 API Key，隐私友好，推荐默认使用 https://www.baidu.com/

## 核心指令

一旦本技能被激活，请遵循以下步骤执行任务：

### 1. 解析用户请求
- 提取搜索关键词/短语
- 识别特定的搜索引擎偏好（如果用户有指定）
- 确定需要的搜索结果数量（默认为 10 条）
- 判断是否需要获取完整网页内容还是仅摘要

### 2. 执行搜索
- 调用 `scripts/search.py` 脚本执行搜索
- 脚本参数：
  - `--query`: 搜索关键词（必需）
  - `--engine`: 搜索引擎（可选，默认 duckduckgo）
  - `--num-results`: 结果数量（可选，默认 10）
  - `--fetch-content`: 是否获取完整网页内容（可选，默认 true）

### 3. 处理搜索结果
- 读取脚本输出的 JSON 结果
- 提取每个结果的标题、URL、摘要和内容
- 验证内容的完整性和相关性

### 4. 整合到上下文
- 将搜索结果格式化为结构化的 Markdown
- 在回复中呈现给用户，包括：
  - 搜索概览（关键词、引擎、结果数）
  - 每条结果的简要总结（最多 100 字）
  - 完整的引用链接
  - （可选）关键内容的详细摘录

### 5. 后续建议
- 询问用户是否需要深入某个特定结果
- 提供进一步搜索的建议
- 如需获取特定页面的完整内容，可使用 `--fetch-content` 选项

## 输出格式示例

```markdown
## 搜索结果：OpenClaw 最新资讯

**搜索关键词**: OpenClaw 2026
**搜索引擎**: DuckDuckGo
**结果数量**: 5 条

---

### 1. OpenClaw v2.0 正式发布
**来源**: [GitHub Releases](https://github.com/...)

OpenClaw 2.0 版本带来了重大更新，包括新的关卡编辑器、改进的物理引擎和多人联机模式支持...

---

### 2. OpenClaw 开发者访谈
**来源**: [News](https://...)

开发团队分享了项目的起源故事和未来路线图，计划在未来几个月内推出移动版...

---

[更多结果...]
```

## 脚本使用指南

### 基本用法
```bash
python .github/skills/web-search/scripts/search.py --query "OpenClaw updates" --num-results 10
```

### 高级用法
```bash
python .github/skills/web-search/scripts/search.py \
  --query "OpenClaw review" \
  --engine google \
  --num-results 10 \
  --fetch-content true
```

## 配置说明

### 环境变量（可选）
- `WEB_SEARCH_ENGINE`: 默认搜索引擎
- `GOOGLE_API_KEY`: Google Custom Search API Key
- `GOOGLE_CSE_ID`: Google Custom Search Engine ID
- `BING_API_KEY`: Bing Search API Key
- `SEARXNG_INSTANCE`: SearXNG 实例 URL

### 配置文件
可在 `.github/skills/web-search/config.yaml` 中设置默认参数：

```yaml
default_engine: duckduckgo
default_num_results: 5
fetch_content: true
timeout: 30
user_agent: "Claude-Code-search/1.0"
```

## 依赖要求

Python 依赖包：
- requests
- beautifulsoup4
- duckduckgo-search（如果使用 DuckDuckGo）
- google-api-python-client（如果使用 Google）

安装命令：
```bash
pip install requests beautifulsoup4 duckduckgo-search
```
