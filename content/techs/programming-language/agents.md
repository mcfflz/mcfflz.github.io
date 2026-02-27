# AGENTS.md

> AI 编码协作规范

本文档旨在为参与本项目的AI编码AGENT提供明确、可执行的指导。所有AGENT在开始任何工作前，必须阅读并遵守本文件中的规则。

---

## 1 通用规范

### 1.1 核心原则

- **先理解，后动手**：修改代码前必须阅读相关上下文，充分理解现有架构

- **最小变更**：只改必须改的，不做"顺手优化"

- **保持一致**：严格遵循项目现有的命名、格式、架构风格

- **测试验证**：每次修改后运行相关测试，确保不破坏现有功能

### 1.2 禁止行为

- ❌ 删除或重命名现有的公共 API

- ❌ 引入新依赖（除非明确要求）

- ❌ 在未被要求的文件中进行更改

- ❌ 使用 `any` 类型绕过类型检查

- ❌ 忽略或跳过测试用例

### 1.3 代码质量要求

- 单个函数不超过 50 行

- 复杂度高的逻辑必须添加注释，注释使用中文

- 所有公共函数必须有文档，文档使用中文

- 错误处理必须明确，不吞异常

- 日志输出要有意义，便于调试

### 1.4. 协作流程

1. **确认理解**：复述任务要点，确保理解正确

2. **说明方案**：修改前简要说明计划

3. **分步执行**：大改动拆分成小步骤

4. **验证结果**：修改后运行测试并报告结果

5. **承认局限**：遇到不确定的问题，主动询问而非猜测

---

## 2 项目特定规范

### 2.1 项目概述

    项目名称: [电商平台订单服务]
    项目类型: [API 后台服务]
    技术栈选择：
      - Python: 3.10.x 
      - MySQL:  ≥ 8.0.x
    部署方式：[Docker compose]

### 2.2 运行环境

    开发测试环境：
    - 硬件环境：4C / 4G Mem / 30G Disk
    - 操作系统：Ubuntu server 24.04 LTS
    - 预装命令：docker、python3、pip3

### 2.3 目录结构

    /
    ├── src/                  # 源代码
    ├── tests/                # 测试文件
    ├── docs/                 # 文档，包含 API 说明文档
    ├── scripts/              # 构建脚本
    ├── docker-compose.yaml   # docker compose 配置
    └── README.md/            # 项目说明

### 2.4 编码规范

核心原则：保持一致性，优先遵循PEP 8

#### 2.4.1 命名约定

  | 类型 | 风格 | 示例 |
  |------|------|------|
  | 模块/文件名 | snake_case | `user_service.py` |
  | 类名 | PascalCase | `UserProfile` |
  | 函数/方法名 | snake_case | `get_user_by_id` |
  | 变量名 | snake_case | `user_list` |
  | 常量名 | UPPER_SNAKE_CASE | `MAX_RETRY_COUNT`, `DEFAULT_PAGE_SIZE` |
  | 私有成员 | _single_leading_underscore | `_internal_cache` |

#### 2.4.2 导入顺序

Python 导入顺序规范：

- 标准库模块（Python内置模块）

- 第三方库模块

- 本地应用程序/库模块（使用绝对导入）

- 每组导入之间用空行分隔

- 在同一组内，先写 import ...语句，再写 from ... import ...语句，并分别按字母顺序排序。

示例：

```python
# 1. 标准库导入
import os
import sys
from typing import List, Dict, Optional

# 2. 第三方库导入
import pandas as pd
import numpy as np
from fastapi import FastAPI
from sqlalchemy import create_engine

# 3. 本地应用程序/模块导入（使用绝对导入）
from app.models import User
from app.services.user_service import UserService
```

#### 2.4.3 异常处理模式

明确异常类型，不用裸except

所有的业务异常和系统异常统一定义错误码和错误描述

错误码定义遵循统一规范，便于快速定位异常位置

```python
from typing import Optional, Any
from enum import IntEnum
from dataclasses import dataclass

# 1. 统一定义错误码枚举
class ErrorCode(IntEnum):
    """应用错误码枚举"""
    # 通用错误 (0-999)
    SUCCESS = 0
    UNKNOWN_ERROR = 1
    VALIDATION_ERROR = 2
    RESOURCE_NOT_FOUND = 3
    PERMISSION_DENIED = 4
    NETWORK_ERROR = 5
    DATABASE_ERROR = 6
    
    # 业务域错误码可按模块分段定义，例如：
    # 用户模块 (1000-1999)
    USER_NOT_FOUND = 1001
    USER_ALREADY_EXISTS = 1002
    INVALID_CREDENTIALS = 1003
    
    # 订单模块 (2000-2999)
    ORDER_CREATE_FAILED = 2001
    INSUFFICIENT_BALANCE = 2002
    
    # ... 其他模块

# 2. 错误码与默认消息的映射（可选，用于国际化或默认消息）
ERROR_MESSAGES = {
    ErrorCode.SUCCESS: "成功",
    ErrorCode.UNKNOWN_ERROR: "未知系统错误",
    ErrorCode.VALIDATION_ERROR: "请求参数验证失败",
    ErrorCode.USER_NOT_FOUND: "用户不存在",
    ErrorCode.USER_ALREADY_EXISTS: "用户已存在",
    # ... 其他错误消息
}

# 3. 带错误码的自定义异常基类
class CodedException(Exception):
    """带错误码的应用异常基类"""
    
    def __init__(self, 
                 code: ErrorCode, 
                 message: Optional[str] = None,
                 details: Optional[Any] = None,
                 cause: Optional[Exception] = None):
        """
        初始化
        :param code: 错误码枚举值
        :param message: 可覆盖的错误消息，为None时使用默认消息
        :param details: 错误详情，可用于传递额外调试信息
        :param cause: 引发此异常的原始异常
        """
        self.code = code
        self.message = message or ERROR_MESSAGES.get(code, "未知错误")
        self.details = details
        self.cause = cause
        super().__init__(self.message)
    
    def to_dict(self) -> dict:
        """将异常转换为字典，便于序列化（如API响应）"""
        return {
            "code": self.code.value,
            "message": self.message,
            "details": self.details,
        }
    
    def __str__(self) -> str:
        """字符串表示，包含错误码和消息"""
        return f"[{self.code.name}] {self.message}"

# 4. 具体的业务异常类
class ValidationException(CodedException):
    """请求参数验证失败异常"""
    def __init__(self, 
                 message: Optional[str] = None,
                 details: Optional[Any] = None,
                 cause: Optional[Exception] = None):
        super().__init__(
            code=ErrorCode.VALIDATION_ERROR,
            message=message,
            details=details,
            cause=cause
        )

class UserNotFoundException(CodedException):
    """用户不存在异常"""
    def __init__(self, 
                 user_id: Optional[str] = None,
                 cause: Optional[Exception] = None):
        details = {"user_id": user_id} if user_id else None
        super().__init__(
            code=ErrorCode.USER_NOT_FOUND,
            details=details,
            cause=cause
        )

class BusinessException(CodedException):
    """通用业务异常，可使用任意错误码"""
    pass

# 5. 使用示例
def create_user(user_data: dict) -> dict:
    """
    创建用户
    :param user_data: 用户数据
    :return: 创建成功的用户信息
    :raises: ValidationException, UserNotFoundException
    """
    # 示例1: 参数验证失败，抛出带错误码的验证异常
    if not user_data.get("username"):
        raise ValidationException(
            message="用户名不能为空",
            details={"field": "username", "value": user_data.get("username")}
        )
    
    # 示例2: 检查用户是否已存在
    existing_user = find_user_by_username(user_data["username"])
    if existing_user:
        raise BusinessException(
            code=ErrorCode.USER_ALREADY_EXISTS,
            details={"username": user_data["username"]}
        )
    
    # 示例3: 模拟数据库操作异常
    try:
        user_id = save_to_database(user_data)
        return {"id": user_id, **user_data}
    except ConnectionError as e:
        # 包装底层异常，保留错误链
        raise BusinessException(
            code=ErrorCode.DATABASE_ERROR,
            message="数据库连接失败",
            cause=e
        )

def handle_user_request(user_data: dict):
    """处理用户请求，展示完整的错误处理流程"""
    try:
        result = create_user(user_data)
        return {
            "success": True,
            "code": ErrorCode.SUCCESS.value,
            "data": result
        }
    except CodedException as e:
        # 记录日志（包含错误码）
        logger.error(f"业务处理失败: {e.code.name}", 
                    extra={"error_code": e.code.value, "details": e.details})
        
        # 返回结构化错误信息（适用于API）
        return {
            "success": False,
            "code": e.code.value,
            "message": e.message,
            "details": e.details
        }
    except Exception as e:
        # 捕获未预期的异常
        logger.exception("未预期的系统错误")
        return {
            "success": False,
            "code": ErrorCode.UNKNOWN_ERROR.value,
            "message": "系统内部错误"
        }

# 6. 工具函数：根据错误码获取异常实例
def get_exception_by_code(code: ErrorCode, **kwargs) -> CodedException:
    """
    根据错误码获取对应的异常实例
    :param code: 错误码
    :param kwargs: 传递给异常构造函数的参数
    :return: 异常实例
    """
    # 可以建立错误码到异常类的映射
    exception_map = {
        ErrorCode.VALIDATION_ERROR: ValidationException,
        ErrorCode.USER_NOT_FOUND: UserNotFoundException,
        # ... 其他映射
    }
    
    exception_class = exception_map.get(code, BusinessException)
    return exception_class(code=code, **kwargs)

# 使用工具函数
def validate_input(input_data: dict):
    if not input_data:
        error = get_exception_by_code(
            code=ErrorCode.VALIDATION_ERROR,
            message="输入数据不能为空"
        )
        raise error
```

### 2.5 API设计规范

### 2.4.1 核心原则

- **RESTful 架构**：以资源为中心，使用标准HTTP方法表达操作意图

- **无状态性**：每个请求包含所有必要信息，服务器不存储客户端状态

- **一致性**：统一的URI命名、HTTP方法使用、响应格式和状态码

### 2.4.2 URL 设计规范

#### 2.4.2.1 资源命名

- 使用**名词复数**形式，如 `/orders` 而非 `/order`

- 使用**小写字母+连字符**分隔，如 `/user-orders`

- 层级不超过3层，避免过度嵌套

- 示例：
  ```
  ✅ 正确：GET /api/v1/orders
  ❌ 错误：GET /api/getOrders
  ```

#### 2.4.2.2 版本控制

- 在URL路径中体现版本：`/api/v1/orders`

- 同时支持请求头版本标识：`Accept: application/vnd.example.v1+json`

#### 2.4.2.3 资源关系表达

- **强关联用子资源**：例如`/users/{userId}/orders`（获取用户的订单）

- **独立查询用过滤**：例如`/orders?userId={userId}`（通过查询参数过滤）

- **批量操作**：例如`POST /orders/batch`（批量创建订单）

### 2.4.3 HTTP 方法使用规范

  | 方法 | 操作语义 | 适用场景 | 示例 |
  |------|----------|----------|------|
  | GET | 查询/获取资源 | 读取数据，无副作用 | `GET /api/v1/orders` |
  | POST | 创建资源 | 新增数据，有副作用 | `POST /api/v1/orders` |
  | PUT | 全量更新资源 | 替换整个资源，需传全字段 | `PUT /api/v1/orders/{id}` |
  | PATCH | 部分更新资源 | 仅更新指定字段 | `PATCH /api/v1/orders/{id}` |
  | DELETE | 删除资源 | 删除指定资源 | `DELETE /api/v1/orders/{id}` |

### 2.4.4 请求与响应规范

#### 2.4.4.1 请求参数

- **路径参数**：标识资源层次，如 `/orders/{orderId}`

- **查询参数**：用于筛选、排序、分页
  - 分页：`?page=1&size=20`
  - 排序：`?sort=created_at,desc`
  - 过滤：`?status=pending&start_date=2024-01-01`

#### 2.4.4.2 响应格式

示例：

**成功响应格式**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "items": [...],
    "total": 100,
    "page": 1,
    "size": 20
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

**异常响应格式**：
```json
{
  "code": 40001,
  "message": "参数验证失败",
  "details": {
    "field": "amount",
    "error": "金额必须大于0"
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

#### 2.4.4.3 HTTP 状态码使用

| 状态码 | 含义 | 适用场景 |
|--------|------|----------|
| 200 OK | 成功 | 一般查询成功 |
| 201 Created | 创建成功 | 资源创建成功 |
| 204 No Content | 成功无内容 | 删除成功 |
| 400 Bad Request | 客户端错误 | 参数验证失败 |
| 401 Unauthorized | 未认证 | 缺少或无效token |
| 403 Forbidden | 无权限 | 权限不足 |
| 404 Not Found | 资源不存在 | 请求的资源不存在 |
| 429 Too Many Requests | 请求过多 | 限流触发 |
| 500 Internal Server Error | 服务器错误 | 未捕获的异常 |

### 2.4.5 安全规范

- **HTTPS**：所有API必须使用HTTPS传输

- **认证授权**：使用JWT token进行用户认证和权限控制

- **请求签名**：支付等敏感接口使用HMAC签名验证

- **限流防护**：实现API限流，防止恶意请求

- **敏感数据脱敏**：响应中脱敏手机号、身份证等敏感信息


### 2.5 日志规范

日志应当符合格式标准，便于快速排查问题

注意：日志中的身份证号等敏感信息应当脱敏，密码等安全信息不应当就。

#### 2.5.1 JSON日志格式标准

示例：
```json
{
  "timestamp": "2024-01-01T12:00:00.000Z",
  "level": "INFO",
  "logger": "order_service",
  "message": "订单创建成功",
  "trace_id": "abc123xyz",
  "span_id": "def456",
  "service_name": "order-service",
  "environment": "production",
  "request_id": "req_123456",
  "user_id": "u12345",
  "details": {
    "order_id": "ORD202401010001",
    "amount": 299.99,
    "items_count": 3
  },
  "duration_ms": 150,
  "exception": null
}
```

#### 2.5.2 必选字段说明

| 字段 | 类型 | 说明 | 必选 |
|------|------|------|------|
| timestamp | string | ISO 8601格式时间戳 | 是 |
| level | string | 日志级别 | 是 |
| message | string | 日志消息 | 是 |
| logger | string | 日志记录器名称 | 是 |
| service_name | string | 服务名称 | 是 |
| environment | string | 环境标识 | 是 |
| trace_id | string | 分布式追踪ID | 是 |
| request_id | string | 请求唯一ID | 是 |

#### 2.5.3 业务上下文字段

| 字段 | 说明 | 适用场景 |
|------|------|----------|
| user_id | 用户ID | 用户相关操作 |
| order_id | 订单ID | 订单相关操作 |
| payment_id | 支付ID | 支付相关操作 |
| api_path | API路径 | API请求日志 |
| http_method | HTTP方法 | API请求日志 |
| status_code | HTTP状态码 | API响应日志 |
| client_ip | 客户端IP | 访问日志 |
| user_agent | 用户代理 | 访问日志 |


### 2.5.4 日志性能优化

1. **异步写入**：使用异步日志处理器避免阻塞主线程

2. **批量写入**：配置日志批量写入，减少IO次数

3. **日志轮转**：按大小和时间轮转，避免单文件过大

4. **日志分级存储**：不同级别日志存储到不同位置

### 2.6 数据库与ORM规范

#### 2.6.1 引擎与字符集

- **存储引擎**：统一使用InnoDB，支持事务和行级锁

- **字符集**：统一使用utf8mb4，支持完整Unicode和表情符号

- **排序规则**：`utf8mb4_general_ci`（不区分大小写）

#### 2.6.2 表设计原则

1. **单表数据量控制**：建议500万行以内，超过需考虑分表

2. **字段数量控制**：单表字段数建议不超过50个

3. **禁止预留字段**：不使用`future_use1`等预留字段

4. **冷热数据分离**：历史数据归档到历史表

5. **禁止存储二进制文件**：图片、文件等存储路径，不存数据库

#### 2.6.3 命名规范

| 对象类型 | 命名规范 | 示例 |
|----------|----------|------|
| 数据库 | 小写+下划线，见名知义 | `order_db` |
| 表名 | 小写+下划线，复数形式 | `orders`, `order_items` |
| 字段名 | 小写+下划线 | `user_id`, `created_at` |
| 主键 | `id`（bigint unsigned auto_increment） | `id` |
| 外键 | `关联表名_字段名` | `user_id`, `order_id` |
| 索引 | `idx_字段名[_字段名...]` | `idx_user_status` |
| 唯一索引 | `uk_字段名[_字段名...]` | `uk_order_no` |

#### 2.6.4 数据类型选择

| 字段类型 | 推荐类型 | 说明 | 示例 |
|----------|----------|------|------|
| 整数 | 根据范围选择最小类型 | TINYINT(1字节)到BIGINT(8字节) | `status TINYINT UNSIGNED` |
| 字符串 | VARCHAR(长度) | 按实际需要设置长度 | `username VARCHAR(50)` |
| 文本 | 避免使用TEXT/BLOB | 大文本单独建表 | 报文等大文本单独存储 |
| 金额 | DECIMAL(M,N) | 精确浮点数 | `amount DECIMAL(10,2)` |
| 时间 | DATETIME/TIMESTAMP | 按需选择 | `created_at DATETIME` |
| 布尔 | TINYINT(1) | 0/1表示真假 | `is_deleted TINYINT(1)` |
| 枚举 | 避免ENUM过长 | 选项超20个改用关联表 | `status ENUM('pending','paid')` |

#### 2.6.5 字段约束

1. **NOT NULL**：尽可能定义字段为NOT NULL，提高查询性能

2. **默认值**：合理设置默认值，如`created_at DEFAULT CURRENT_TIMESTAMP`

3. **无符号**：非负数使用UNSIGNED，扩大存储范围

4. **注释**：所有字段必须添加COMMENT说明

#### 2.6.6 索引设计规范

1. **主键索引**：每张InnoDB表必须有主键，建议自增ID

2. **索引数量**：单表索引不超过5个

3. **索引字段数**：联合索引字段不超过5个

4. **前缀索引**：字符串索引长度不超过8个字符

#### 2.6.7 必须建立索引的场景

1. **主键和外键**：自动创建

2. **WHERE条件字段**：频繁作为查询条件的字段

3. **JOIN关联字段**：多表连接的关联列

4. **ORDER BY/GROUP BY字段**：排序和分组字段

5. **DISTINCT字段**：去重字段

#### 2.6.8 SQL开发规范

1. **禁止SELECT ***：明确列出所需字段
   ```sql
   -- ❌ 错误
   SELECT * FROM orders WHERE user_id = 123;
   
   -- ✅ 正确
   SELECT id, order_no, amount, status FROM orders WHERE user_id = 123;
   ```
2. **避免大事务**：事务内操作行数不超过1000行

4. **批量操作分批进行**：超过100万行的操作分批执行

5. **使用JOIN替代子查询**：JOIN性能通常优于子查询

6. **避免过多JOIN**：单条SQL的JOIN表不超过3个

7. **联合索引必须从最左列开始使用**

#### 2.6.8 数据库安全规范

1. **禁止明文存储密码**：使用哈希加盐存储

2. **最小权限原则**：应用使用只读/只写账号

3. **SQL注入防护**：使用参数化查询或ORM

4. **敏感数据加密**：身份证、手机号等字段加密存储

5. **审计日志**：记录所有数据变更操作

### 2.7 测试规范

Python 测试最佳实践：

- 每个测试应该独立，不依赖其他测试的执行顺序

- 使用夹具（fixtures）管理测试资源和状态

- 遵循 Arrange-Act-Assert 模式

- 为错误路径和边界条件编写测试

- 使用参数化测试减少重复代码

- 集成测试应该与外部依赖隔离（使用mock）

```python
# 1. 测试文件命名规范
#    - 测试文件：test_*.py 或 *_test.py
#    - 测试类：Test*（如果使用unittest）
#    - 测试方法：test_*

# 2. 测试文件位置
#    - tests/ 目录下
#    - 推荐结构：
#        project/
#        ├── src/
#        │   └── app.py
#        └── tests/
#            ├── test_app.py
#            └── conftest.py

# 3. pytest 测试示例
import pytest
from app.services.user_service import UserService

class TestUserService:
    """用户服务测试类"""
    
    @pytest.fixture
    def user_service(self):
        """测试夹具：创建UserService实例"""
        return UserService()
    
    def test_create_user_success(self, user_service):
        """测试成功创建用户"""
        # 准备
        user_data = {"username": "testuser", "email": "test@example.com"}
        
        # 执行
        result = user_service.create_user(user_data)
        
        # 断言
        assert result.success is True
        assert result.data.username == "testuser"
        assert "id" in result.data.__dict__
    
    def test_create_user_duplicate(self, user_service):
        """测试创建重复用户（边界条件）"""
        # 准备
        user_data = {"username": "existing", "email": "existing@example.com"}
        user_service.create_user(user_data)  # 先创建
        
        # 执行 & 断言
        with pytest.raises(ValidationError) as exc_info:
            user_service.create_user(user_data)
        
        assert "已存在" in str(exc_info.value)
    
    @pytest.mark.parametrize("invalid_email", [
        "invalid",
        "invalid@",
        "@example.com",
        ""
    ])
    def test_create_user_invalid_email(self, user_service, invalid_email):
        """参数化测试：各种无效邮箱格式"""
        user_data = {"username": "test", "email": invalid_email}
        
        with pytest.raises(ValidationError):
            user_service.create_user(user_data)
    
    def test_get_user_not_found(self, user_service):
        """测试错误路径：用户不存在"""
        result = user_service.get_user(99999)  # 不存在的ID
        
        assert result.success is False
        assert "未找到" in result.message

# 4. 异步测试示例（如使用FastAPI）
@pytest.mark.asyncio
async def test_async_operation():
    """测试异步操作"""
    result = await async_function()
    assert result == expected_value

# 5. 测试覆盖率配置（pyproject.toml 或 setup.cfg）
"""
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]

[tool.coverage.run]
source = ["src"]
omit = ["*/tests/*", "*/migrations/*"]

[tool.coverage.report]
fail_under = 80
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise AssertionError",
    "raise NotImplementedError"
]
"""

# 覆盖率目标建议：
# - 语句覆盖率：80% 以上
# - 分支覆盖率：70% 以上
# - 必须测试：所有公共API、边界条件、错误处理路径
```

### 2.8 Git 提交规范

    <type>(<scope>): <subject>

    类型 (type):
    - feat:     新功能
    - fix:      修复 bug
    - docs:     文档更新
    - style:    代码格式 (不影响功能)
    - refactor: 重构
    - test:     测试相关
    - chore:    构建/工具相关

    示例:
    feat(auth): add OAuth2 login support
    fix(api): handle null response from user endpoint
    docs(readme): update installation instructions

### 2.9 环境变量

所有配置项均以环境变量方式体现

敏感信息（密码、密钥、内网IP），必须使用环境变量

示例环境变量： (不要在代码中硬编码)

    DATABASE_URL=           # 数据库连接字符串
    API_KEY=                # 外部 API 密钥
    JWT_SECRET=             # JWT 签名密钥
    LOG_LEVEL=info          # 日志级别: debug | info | warn | error
    ENABLE_CACHE=true       # 是否启用缓存

### 2.10 参考文档

- [项目 Wiki](./docs/wiki.md)

- [API 文档](./docs/api.md)

- [项目介绍](README.md)

---

## 3 部署要求

使用 README.md：

- 一行启动命令：docker-compose up --build

- 查看服务访问地址（如 http://localhost:8000）

- 直接用复制的 curl 命令验证核心功能的步骤

- 包含预置的测试账号信息

---

## 4 紧急联系

遇到以下情况时，**停止操作并询问人类**：

1. 涉及删除数据或数据库操作

2. 涉及安全敏感代码（认证、加密、权限）

3. 需要修改 CI/CD 配置

4. 任务描述模糊或存在多种理解

5. 发现现有代码有严重 bug（先报告，不要擅自修复）

--- 