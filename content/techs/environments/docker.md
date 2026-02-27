---
date: 2026-02-12T12:00:00+08:00
title: Docker
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

# Docker

## 参考资料

[docker ubuntu install](https://docs.docker.com/engine/install/ubuntu/#install-from-a-package)

## 概述

Docker 是一个应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的 Linux 机器上。容器是完全使用沙箱机制，相互之间不会有任何接口。

Docker 解决了"代码在我机器上能跑起来"的问题，通过容器化技术确保应用在不同环境中具有一致的行为。Docker 主要有三个核心概念：

- **镜像（Image）**：Docker 镜像是一个特殊的文件系统，除了提供容器运行时必需的程序、库、资源、配置等文件外，还包含了一些为运行时准备的一些配置参数。镜像是只读的。
- **容器（Container）**：容器是从镜像创建的运行实例。它可以被启动、开始、停止、删除。每个容器都是相互隔离的、保证安全的平台。
- **仓库（Repository）**：仓库是集中存放镜像文件的场所。Docker Hub 是官方提供的公共仓库，用户可以上传自己的镜像，也可以下载他人分享的镜像。

```sequence
title: docker engine
participant remote machine\nregistry\n（远程仓库） as a
participant local machine\nimages\n（本地镜像） as b
participant local machine\ncontainers\n（容器） as c

note over a: repositories
b->a: docker search images
a->b: docker pull images
b->b: docker images
b->c: docker run image
```

## 安装

环境：tencentcloud Ubuntu Server 24.04 LTS 64bit

```bash
# 参考 docker 官方安装指南 https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
# 更新系统命令并安装依赖
sudo apt update
sudo apt install ca-certificates curl

# 创建密钥目录并下载 Docker GPG 密钥
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# 添加 Docker APT 仓库并更新软件源
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF
sudo apt update

# 安装 docker 核心组件
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 启动 docker 服务
sudo systemctl status docker

# 更换镜像源
sudo mkdir -p /etc/docker
sudo vim /etc/docker/daemon.json
{
  "registry-mirrors": [
    "https://mirror.ccs.tencentyun.com"
  ]
}
sudo systemctl daemon-reload
sudo docker info | grep "Registry Mirrors" -A 3
sudo systemctl restart docker

# 验证
sudo docker run hello-world
```

## docker cli 常用命令

### 镜像相关命令

- `docker images` - 列出本地所有镜像
- `docker search <keyword>` - 在 Docker Hub 搜索镜像
- `docker pull <image>` - 从仓库拉取镜像
- `docker push <image>` - 推送镜像到仓库
- `docker rmi <image>` - 删除本地镜像
- `docker build -t <name> .` - 使用当前目录下的 Dockerfile 构建镜像

### 容器相关命令

- `docker ps` - 列出正在运行的容器
- `docker ps -a` - 列出所有容器（包括已停止的）
- `docker run <image>` - 运行容器
- `docker start <container>` - 启动已停止的容器
- `docker stop <container>` - 停止运行中的容器
- `docker restart <container>` - 重启容器
- `docker rm <container>` - 删除容器
- `docker exec -it <container> /bin/bash` - 进入容器执行命令

### 其他常用命令

- `docker logs <container>` - 查看容器日志
- `docker stats` - 查看容器资源使用情况
- `docker inspect <container>` - 查看容器详细信息
- `docker volume` - 管理数据卷
- `docker network` - 管理网络
- `docker system prune` - 清理未使用的数据（镜像、容器、网络、数据卷）

### docker run 常用参数

- `-d` - 后台运行容器
- `-it` - 交互式运行容器
- `-p <host_port>:<container_port>` - 端口映射
- `-v <host_path>:<container_path>` - 数据卷挂载
- `-e KEY=VALUE` - 设置环境变量
- `--name <name>` - 指定容器名称
- `--rm` - 容器退出时自动删除

## docker 网络

Docker 网络管理思路来自于虚拟机，把虚拟机中管理网络的思想移植过来，对于构建在虚拟机上的公有云来说，网络安全和高效是非常重要的。

### Docker 网络驱动类型

- **bridge（网桥模式）**：默认网络驱动，容器通过 docker0 虚拟网桥连接，每个容器有独立的 IP
- **host（主机模式）**：容器直接使用主机网络，没有独立的 IP，性能更好但隔离性差
- **none（无网络）**：容器有独立的 Network Namespace，但不进行任何网络配置
- **container（容器共享）**：新创建的容器与一个已存在的容器共享同一个 Network Namespace
- **overlay（覆盖网络）**：用于 Docker Swarm 跨主机通信
- **macvlan**：为容器分配 MAC 地址，使容器看起来像物理设备

### 网络操作命令

```bash
# 列出所有网络
docker network ls

# 创建自定义网络
docker network create my-network

# 查看网络详情
docker network inspect my-network

# 容器连接到网络
docker network connect my-network <container>

# 容器断开网络
docker network disconnect my-network <container>

# 删除网络
docker network rm my-network
```

### 使用示例

```bash
# 使用自定义 bridge 网络运行容器
docker run --name web --network my-network -p 8080:80 nginx
docker run --name app --network my-network my-app

# 使用 host 网络（容器没有独立 IP，直接使用主机端口）
docker run --network host nginx

# 容器共享网络（新容器与已存在容器共享 network namespace）
docker run --network container:existing-container alpine
```

## Dockerfile

Dockerfile 是一个用来构建 Docker 镜像的文本文件，包含了一系列构建镜像所需的指令。

### 常用指令

| 指令 | 说明 |
|------|------|
| `FROM` | 指定基础镜像 |
| `RUN` | 执行命令（构建时） |
| `CMD` | 容器启动时执行的命令（可被覆盖） |
| `ENTRYPOINT` | 容器启动时执行的命令（不可被覆盖） |
| `COPY` | 复制文件到镜像 |
| `ADD` | 复制文件（支持 URL 和解压） |
| `WORKDIR` | 设置工作目录 |
| `ENV` | 设置环境变量 |
| `ARG` | 设置构建参数 |
| `EXPOSE` | 暴露端口 |
| `VOLUME` | 创建数据卷挂载点 |
| `USER` | 指定运行用户 |
| `HEALTHCHECK` | 健康检查配置 |
| `LABEL` | 添加元数据 |

### Dockerfile 示例

```dockerfile
# 指定基础镜像
FROM ubuntu:22.04

# 设置 maintainer 标签
LABEL maintainer="your.email@example.com"

# 设置环境变量
ENV DEBIAN_FRONTEND=noninteractive
ENV APP_HOME=/app

# 设置工作目录
WORKDIR $APP_HOME

# 复制文件（支持通配符）
COPY requirements.txt .

# 执行命令（每行创建一个新层，建议合并 RUN 指令）
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip3 install -r requirements.txt && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 复制应用代码
COPY . .

# 创建非 root 用户并切换
RUN useradd -m appuser
USER appuser

# 暴露端口
EXPOSE 8000

# 健康检查
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# 容器启动命令（可被 docker run 后面的参数覆盖）
CMD ["python3", "app.py"]
```

### 构建命令

```bash
# 基本构建
docker build -t my-image .

# 指定 Dockerfile 路径
docker build -f Dockerfile.prod -t my-image:prod .

# 使用构建参数
docker build --build-arg NODE_ENV=production -t my-image .

# 使用 BuildKit（更快的构建速度）
DOCKER_BUILDKIT=1 docker build -t my-image .
```

## docker-compose.yaml

Docker Compose 允许使用 YAML 文件来定义和管理多容器应用。

### 常用配置项

```yaml
version: '3.8'

services:
  web:
    # 使用已有镜像
    image: nginx:alpine
    # 或从 Dockerfile 构建
    build:
      context: .
      dockerfile: Dockerfile.prod
      args:
        - NODE_ENV=production

    # 容器名称
    container_name: my-web-container

    # 端口映射
    ports:
      - "80:80"
      - "443:443"

    # 环境变量
    environment:
      - NODE_ENV=production
      - API_KEY=${API_KEY}
    # 或使用 env_file
    env_file:
      - .env

    # 数据卷挂载
    volumes:
      - ./html:/usr/share/nginx/html
      - /var/log/nginx:/var/log/nginx
    # 或命名数据卷
    # volumes:
    #   - data-volume:/data

    # 网络配置
    networks:
      - frontend
      - backend

    # 依赖关系
    depends_on:
      - app
      - db

    # 重启策略
    restart: unless-stopped

    # 资源限制
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M

    # 健康检查
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 3

  app:
    build: ./app
    networks:
      - backend
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5

# 定义命名数据卷
volumes:
  postgres_data:
  data-volume:

# 定义网络
networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge
    internal: true  # 内部网络，不连接外网
```

### Compose 常用命令

```bash
# 启动服务（后台运行）
docker-compose up -d

# 启动并重建容器
docker-compose up -d --build

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs
docker-compose logs -f app  # 跟踪特定服务日志

# 停止服务
docker-compose stop

# 停止并删除容器、网络（保留数据卷）
docker-compose down

# 停止并删除容器、网络和数据卷
docker-compose down -v

# 重启服务
docker-compose restart

# 进入服务容器
docker-compose exec app /bin/bash

# 构建/重建服务
docker-compose build
docker-compose build --no-cache  # 不使用缓存
```

## Docker 实践示例

### 示例 1：运行 Nginx 服务器

```bash
# 拉取 Nginx 镜像
docker pull nginx

# 运行 Nginx 容器，将主机 8080 端口映射到容器 80 端口
docker run --name my-nginx -p 8080:80 -d nginx

# 查看运行中的容器
docker ps

# 浏览器访问 http://localhost:8080 即可看到 Nginx 默认页面

# 停止并删除容器
docker stop my-nginx
docker rm my-nginx
```

### 示例 2：运行 MySQL 数据库

```bash
# 拉取 MySQL 镜像
docker pull mysql:8.0

# 运行 MySQL 容器（持久化存储）
docker run --name mysql-container \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=testdb \
  -p 3306:3306 \
  -v mysql-data:/var/lib/mysql \
  -d mysql:8.0

# 进入 MySQL 容器
docker exec -it mysql-container mysql -u root -p

# 停止 MySQL 容器
docker stop mysql-container
```

### 示例 3：运行 Redis 缓存

```bash
# 拉取并运行 Redis
docker run --name my-redis -p 6379:6379 -d redis

# 连接到 Redis
docker exec -it my-redis redis-cli

# 设置和获取值
SET mykey "Hello Docker"
GET mykey

# 停止并删除 Redis 容器
docker stop my-redis
docker rm my-redis
```

### 示例 4：使用 Dockerfile 构建自定义镜像

创建一个简单的 Node.js 应用示例：

1. 创建项目目录和文件：

```bash
mkdir my-node-app
cd my-node-app
touch app.js
touch package.json
touch Dockerfile
```

2. 编写 `package.json`：

```json
{
  "name": "my-node-app",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^4.18.0"
  }
}
```

3. 编写 `app.js`：

```javascript
const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Hello Docker!');
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

4. 创建 `Dockerfile`：

```dockerfile
# 使用官方 Node.js 运行时作为基础镜像
FROM node:18-alpine

# 设置工作目录
WORKDIR /app

# 复制 package*.json 到工作目录
COPY package*.json ./

# 安装依赖
RUN npm install

# 复制应用源代码到工作目录
COPY . .

# 暴露端口
EXPOSE 3000

# 定义启动命令
CMD [ "npm", "start" ]
```

5. 构建并运行：

```bash
# 构建镜像
docker build -t my-node-app .

# 运行容器
docker run --name my-node-container -p 3000:3000 -d my-node-app

# 访问应用
curl http://localhost:3000
```

### 示例 5：使用 Docker Compose

Docker Compose 允许使用 YAML 文件来定义多容器应用。

1. 创建 `docker-compose.yml`：

```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - app

  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development

  db:
    image: postgres:13
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

2. 运行多容器应用：

```bash
# 启动服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 停止服务
docker-compose down
```

## Docker 最佳实践

### 镜像优化

1. **使用合适的基镜像**：选择更小的基镜像如 Alpine Linux 可以显著减小最终镜像的大小
2. **多阶段构建**：在构建过程中使用多个 FROM 指令，只将必要的文件复制到最后的镜像中
3. **合并 RUN 指令**：减少镜像层的数量，提高构建效率
4. **清理缓存和临时文件**：在同一个 RUN 指令中安装包并清理缓存

### 安全性

1. **避免使用 root 用户**：使用 USER 指令切换到非 root 用户运行应用
2. **使用 .dockerignore**：排除不必要的文件，如敏感配置文件或开发工具
3. **扫描镜像漏洞**：定期扫描镜像中的安全漏洞
4. **限制容器资源**：使用 --memory 和 --cpu-quota 限制容器资源使用

### 性能优化

1. **合理使用数据卷**：对于频繁读写的数据，使用数据卷而不是绑定挂载
2. **使用 Docker BuildKit**：启用 BuildKit 可以提高构建速度和缓存效率
3. **容器健康检查**：使用 HEALTHCHECK 指令检查容器内应用的健康状态


