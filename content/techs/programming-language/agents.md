# AGENTS.md

本文档为AI编码提供指导规范。所有Agent在开始工作前，必须阅读并遵守本文件中的规则。

---

## 1 通用规范

### 1.1 核心原则

- **先理解后动手**：修改前必须阅读相关上下文
- **最小变更**：只改必须改的，不做"顺手优化"
- **保持一致**：遵循现有命名、格式、架构风格
- **测试验证**：修改后运行相关测试

### 1.2 禁止行为

- ❌ 删除或重命名现有的公共 API
- ❌ 引入新依赖（除非明确要求）
- ❌ 在未被要求的文件中进行更改
- ❌ 使用 `any` 类型绕过类型检查
- ❌ 忽略或跳过测试用例

### 1.3 代码质量要求

- 单个函数不超过 50 行
- 复杂度高的逻辑必须添加注释
- 所有公共函数必须有文档
- 错误处理必须明确，不吞异常
- 日志输出要有意义，便于调试
- 注释、文档和说明使用中文

---

## 2 项目概述

- **名称**: 电商平台订单服务
- **类型**: API 后台服务
- **技术栈**: Python 3.10, FastAPI, SQLAlchemy, MySQL 8.0, Redis 7.0, Celery
- **部署**: Docker Compose

项目详细信息请阅读 [README.md](./README.md)

### 2.1 运行环境

开发环境：Ubuntu server 24.04 LTS, 4C/4G Mem/30G Disk
系统用户：ubuntu
预装命令：docker、docker compose、python3、pip3

### 2.2 目录结构

```
├── src/app/
│   ├── main.py           # FastAPI入口
│   ├── api/v1/           # API路由（auth, order, payment...）
│   ├── core/             # 配置、异常、日志、数据库
│   ├── models/           # SQLAlchemy模型
│   ├── schemas/          # Pydantic模型
│   ├── services/         # 业务逻辑
│   ├── tasks/            # Celery异步任务
│   └── utils/            # 工具函数
├── tests/
│   ├── unit/             # 单元测试（SQLite+FakeRedis）
│   └── integration/      # 集成测试（MySQL+Redis）
├── alembic/              # 数据库迁移
└── scripts/              # 启动脚本
```

### 2.3 命名规范

| 类型 | 风格 | 示例 |
|------|------|------|
| 模块/文件 | snake_case | `order_service.py` |
| 类名 | PascalCase | `OrderService` |
| 函数/变量 | snake_case | `get_order_by_id` |
| 常量 | UPPER_SNAKE_CASE | `DEFAULT_PAGE_SIZE` |

### 2.4 导入顺序

```python
# 1. 标准库
import json
from typing import List

# 2. 第三方库
from fastapi import FastAPI
from sqlalchemy.orm import Session

# 3. 本地模块（绝对导入）
from src.app.core.exceptions import BusinessException
from src.app.services.order_service import OrderService
```

---

## 3 开发规范

### 3.1 代码质量

- 函数不超过50行
- 复杂逻辑添加**中文**注释
- 公共函数必须有**中文**文档
- 错误处理明确，不吞异常

### 3.2 错误处理

```python
from src.app.core.exceptions import BusinessException, ErrorCode

try:
    # 业务逻辑
    pass
except BusinessException:
    db.rollback()
    raise
except SQLAlchemyError as e:
    db.rollback()
    logger.error(f"Error: {e}", exc_info=True)
    raise BusinessException(
        ErrorCode.DATABASE_ERROR, message="操作失败", cause=e
    )
```

**错误码范围**：
- 0000-0999: 通用错误
- 1000-1999: 认证与用户
- 2000-2999: 订单与商品
- 3000-3999: 支付

### 3.3 API规范

- URL使用名词复数：`/api/v1/orders`
- HTTP方法语义：GET查询、POST创建、PUT全量更新、PATCH部分更新、DELETE删除
- 统一响应格式：
  ```json
  {
    "code": 200,
    "message": "success",
    "data": {...},
    "timestamp": "2024-01-01T00:00:00Z"
  }
  ```

### 3.4 数据库规范

- 引擎：InnoDB
- 字符集：utf8mb4
- 禁止SELECT *，明确列出字段
- 敏感数据加密存储
- 使用参数化查询防SQL注入

---

## 4 测试规范

**单元测试**：使用SQLite内存数据库+FakeRedis，完全隔离

**集成测试**：使用真实MySQL+Redis，事务自动回滚

```bash
# 运行单元测试
./scripts/run_unit_tests.sh

# 运行集成测试
./scripts/run_integration_tests.sh

# 覆盖率报告
coverage run --source=src/app -m pytest tests/
```

**覆盖率目标**：语句覆盖率≥80%，分支覆盖率≥70%

---

## 5 Git规范

```
<type>(<scope>): <subject>

类型：
- feat: 新功能
- fix: 修复bug
- docs: 文档更新
- style: 代码格式
- refactor: 重构
- test: 测试相关
- chore: 构建/工具

示例：
feat(order): add order cancellation API
fix(auth): handle expired token
```

---

## 6 环境变量

所有配置使用环境变量，禁止硬编码。

```bash
DATABASE_URL=mysql+pymysql://user:pass@db:3306/dbname?charset=utf8mb4
REDIS_URL=redis://redis:6379/0
JWT_SECRET=your-secret-key
MASTER_KEY=encryption-key
```

---

## 7 参考文档

- [README.md](README.md) - 项目说明与启动指南
- [TESTING.md](TESTING.md) - 测试指南
- [DATA_PERSISTENCE.md](DATA_PERSISTENCE.md) - 数据持久化方案

---

## 8 紧急联系

**遇到以下情况时，停止操作并询问人类：**

1. 涉及删除数据或数据库操作
2. 涉及安全敏感代码（认证、加密、权限）
3. 需要修改CI/CD配置
4. 任务描述模糊或存在多种理解
5. 发现现有代码有严重bug（先报告，不要擅自修复）

---
