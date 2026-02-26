# AGENTS.md 

--- 

## 1 通用规范

### 1.1 核心原则 

- **先理解，后动手**：修改代码前必须阅读相关上下文，理解现有架构

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

- 复杂度高的逻辑必须添加注释

- 所有公共函数必须有文档注释

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
    项目类型: [API 服务]
    主要语言: [Python]
    数据库: [MySQL]

### 2.2 目录结构 

    /
    ├── src/                 # 源代码
    ├── tests/               # 测试文件
    ├── docs/                # 文档
    └── scripts/             # 构建/部署脚本


### 2.3 常用命令 

    # 开发
    npm run dev              # 启动开发服务器
    npm run build            # 构建生产版本

    # 测试
    npm run test             # 运行所有测试
    npm run test:unit        # 运行单元测试
    npm run test:e2e         # 运行端到端测试

    # 代码质量
    npm run lint             # 运行 ESLint
    npm run format           # 运行 Prettier
    npm run typecheck        # TypeScript 类型检查

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

    // 1. 外部依赖
    import React from 'react';
    import { useState } from 'react';
 

    // 2. 内部模块 (绝对路径)
    import { UserService } from '@/services/user-service';
 

    // 3. 相对路径导入
    import { formatDate } from './utils';
 

    // 4. 类型导入
    import type { User } from '@/types';
 

#### 2.4.3 错误处理模式 

    // 推荐: 使用 Result 类型
    type Result<t, e="Error"> = 
      | { ok: true; value: T } 
      | { ok: false; error: E };
 

    // 或: 明确的 try-catch
    try {
      const result = await riskyOperation();
      return { ok: true, value: result };
    } catch (error) {
      logger.error('Operation failed', { error });
      return { ok: false, error: error as Error };
    }
 

### 2.5 测试规范 

- **测试文件命名**: *.test.ts 或 *.spec.ts 

- **测试文件位置**: 与源文件同目录或 __tests__ 子目录 

- **覆盖率目标**: 语句 80%，分支 70% 

- **必须测试**: 所有公共 API、边界条件、错误路径 

    describe('UserService', () => {
      describe('getUserById', () => {
        it('should return user when exists', async () => {
          // Arrange
          const userId = 'user-123';
          
          // Act
          const result = await userService.getUserById(userId);
          
          // Assert
          expect(result.ok).toBe(true);
          expect(result.value.id).toBe(userId);
        });
 
        it('should return error when user not found', async () => {
          // ...
        });
      });
    });
 

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

    # 必需的环境变量 (不要在代码中硬编码)
    DATABASE_URL=           # 数据库连接字符串
    API_KEY=                # 外部 API 密钥
    JWT_SECRET=             # JWT 签名密钥

    # 可选的环境变量
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