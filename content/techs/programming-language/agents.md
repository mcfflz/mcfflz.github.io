# AGENTS.md

> AI 编码协作规范

本文档旨在为参与本代码生成项目的AI编码AGENT提供明确、可执行的指导。所有AGENT在开始任何工作前，必须阅读并遵守本文件中的规则。

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

- ❌ 修改配置文件（.env, CI/CD, 构建配置等）

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
    主要语言: [Python]
    数据库: [MySQL]
    部署方式：[docker compose]

### 2.2 运行环境

    硬件环境：4C 4GMem
    操作系统：Ubuntu 24.04 LTS

### 2.3 目录结构

    /
    ├── src/                  # 源代码
    ├── tests/                # 测试文件
    ├── docs/                 # 文档，包含 API 说明文档
    ├── scripts/              # 构建/部署脚本
    ├── docker-compose.yaml/  # docker compose 配置
    └── README.md/            # 项目说明


### 2.4 代码规范

#### 2.4.1 命名约定

  | 类型 | 风格 | 示例 |
  |------|------|------|
  | 文件名 | kebab-case | user-service.ts |
  | 组件名 | PascalCase | UserProfile.tsx |
  | 函数名 | camelCase | getUserById |
  | 常量名 | UPPER_SNAKE_CASE | MAX_RETRY_COUNT |
  | 类型/接口 | PascalCase | User 或 IUser |


#### 2.4.2 导入顺序

Python 导入顺序规范：

- 标准库模块（Python内置模块）

- 相关的第三方库模块

- 本地应用程序/库模块（使用绝对导入或相对导入）

- 每组导入之间用空行分隔

- 每个组内按字母顺序排序

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

# 3. 本地应用程序/模块导入（绝对或相对导入）
from app.models import User
from app.services.user_service import UserService
from .utils import format_date
from ..config import settings
```

#### 2.4.3 错误处理模式

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

### 2.4 测试规范

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

### 2.6 Git 提交规范

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

### 2.7 环境变量

所有配置项均以环境变量方式体现

示例环境变量： (不要在代码中硬编码)

    DATABASE_URL=           # 数据库连接字符串
    API_KEY=                # 外部 API 密钥
    JWT_SECRET=             # JWT 签名密钥
    LOG_LEVEL=info          # 日志级别: debug | info | warn | error
    ENABLE_CACHE=true       # 是否启用缓存


### 2.8 参考文档

- [项目 Wiki](./docs/wiki.md)

- [API 文档](./docs/api.md)

---

## 3 紧急联系

遇到以下情况时，**停止操作并询问人类**：

1. 涉及删除数据或数据库操作

2. 涉及安全敏感代码（认证、加密、权限）

3. 需要修改 CI/CD 配置

4. 任务描述模糊或存在多种理解

5. 发现现有代码有严重 bug（先报告，不要擅自修复）

--- 