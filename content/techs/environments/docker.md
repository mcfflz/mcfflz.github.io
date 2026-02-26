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
weight: 1                     # 内容权重（排序用）
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

## 核心概念详解

### 镜像与容器的关系

Docker 遵循"构建一次，到处运行"的原则。镜像和容器本质上都是一个文件系统，它们唯一的不同，就是镜像（image）是只读的，而容器（container）是可读可写的。

- 镜像就像一个模板，包含了运行应用所需的一切
- 容器是镜像的运行时实例，多个容器可以从同一个镜像启动

### 存储驱动

Docker Engine 支持多种存储驱动，如 `overlay2`、`aufs` 和 `btrfs`。默认使用 `overlay2` 存储驱动，它提供了更好的性能和稳定性。

### 网络

Docker 网络管理借鉴了虚拟机网络管理思想，为容器提供网络连接功能。Docker 支持多种网络模式：
- Bridge（桥接）：默认模式，容器通过网桥连接
- Host（主机）：容器直接使用宿主机网络
- None：无网络连接

### 数据卷（Volume）

数据卷用于实现数据持久化，使数据在容器生命周期之外得到保留。数据卷可以在容器间共享和重用，对数据卷的修改会直接生效，且更新数据卷不影响镜像。


## Docker 常用命令

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

### Docker Run 常用参数

- `-d` - 后台运行容器
- `-it` - 交互式运行容器
- `-p <host_port>:<container_port>` - 端口映射
- `-v <host_path>:<container_path>` - 数据卷挂载
- `-e KEY=VALUE` - 设置环境变量
- `--name <name>` - 指定容器名称
- `--rm` - 容器退出时自动删除

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

Docker Compose 允许你使用 YAML 文件来定义多容器应用。

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

## 总结

Docker 提供了一种轻量级、可移植的容器化解决方案，能够简化应用的开发、部署和管理。通过使用 Docker，你可以：

- 确保开发、测试和生产环境的一致性
- 快速部署和扩展应用
- 节省服务器资源
- 简化应用的打包和分发

掌握 Docker 的基本概念和命令是现代软件开发的重要技能。通过实践上述示例，您可以快速上手 Docker 并在实际项目中应用这些知识。


## 本地镜像

docker 本地镜像

## docker 网络

docker 网络管理思路来自于虚拟机，把虚拟机中管理网络的思想移植过来，对于构建在虚拟机上的公有云来说，网络安全和高效是非常重要的。



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

# Docker Container Status

```sequence
participant Up as u
participant Exited as e

u->e: docker stop
e->u: docker start
```

# Docker Volume

```sequence
participant local machine as l
participant container as c
note over l,c: volume share
l->c: docker run -v localVolumePath:containerPath:rwo
```



# Docker Command-Line

基础 docker 命令

## docker info

查看 docker 信息

```bash
Usage:  docker info [OPTIONS]

Display system-wide information

Options:
  -f, --format string   Format the output using the given Go template
```

## docker search

在 docker 远程仓库搜索镜像

```bash
Usage:  docker search [OPTIONS] TERM

Search the Docker Hub for images

Options:
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print search using a Go template
      --limit int       Max number of search results (default 25)
      --no-trunc        Don't truncate output
```

## docker pull

从 docker 远程仓库拉取镜像

```bash
Usage:  docker pull [OPTIONS] NAME[:TAG|@DIGEST]

Pull an image or a repository from a registry

Options:
  -a, --all-tags                Download all tagged images in the repository
      --disable-content-trust   Skip image verification (default true)
      --platform string         Set platform if server is multi-platform
                                capable
  -q, --quiet                   Suppress verbose output
```

## docker images

列出本地仓库的 docker 镜像

```bash
Usage:  docker images [OPTIONS] [REPOSITORY[:TAG]]

List images

Options:
  -a, --all             Show all images (default hides intermediate images)
      --digests         Show digests
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print images using a Go template
      --no-trunc        Don't truncate output
  -q, --quiet           Only show image IDs
```

## docker tag

创建一个镜像副本，以新的 repository 和 tag 命名

```bash
Usage:  docker tag SOURCE_IMAGE[:TAG] TARGET_IMAGE[:TAG]

Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
```

## docker volume

查看 docker 存储卷信息

```bash
Usage:  docker volume COMMAND

Manage volumes

Commands:
  create      Create a volume
  inspect     Display detailed information on one or more volumes
  ls          List volumes
  prune       Remove all unused local volumes
  rm          Remove one or more volumes
```

## docker rmi

从本地仓库中删除 docker 镜像

```bash
Usage:  docker rmi [OPTIONS] IMAGE [IMAGE...]

Remove one or more images

Options:
  -f, --force      Force removal of the image
      --no-prune   Do not delete untagged parents
```

## docker run

利用 docker 镜像，启动一个 docker 容器

```bash
Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container

Options:
  ...
  -d, --detach                         Run container in background and print container ID
  -e, --env list                       Set environment variables
  -p, --publish list                   Publish a container's port(s) to the host
  -v, --volume list                    Bind mount a volume
```

## docker exec

进入 docker 容器，启动某个命令

```bash
Usage:  docker exec [OPTIONS] CONTAINER COMMAND [ARG...]

Run a command in a running container

Options:
  -d, --detach               Detached mode: run command in the background
      --detach-keys string   Override the key sequence for detaching a
                             container
  -e, --env list             Set environment variables
      --env-file list        Read in a file of environment variables
  -i, --interactive          Keep STDIN open even if not attached
      --privileged           Give extended privileges to the command
  -t, --tty                  Allocate a pseudo-TTY
  -u, --user string          Username or UID (format:
                             <name|uid>[:<group|gid>])
  -w, --workdir string       Working directory inside the container
```

## docker stop

停止运行中的 docker 容器

```bash
Usage:  docker stop [OPTIONS] CONTAINER [CONTAINER...]

Stop one or more running containers

Options:
  -t, --time int   Seconds to wait for stop before killing it (default 10)
```

## docker start

启动停止运行的 docker 容器

```bash
Usage:  docker start [OPTIONS] CONTAINER [CONTAINER...]

Start one or more stopped containers

Options:
  -a, --attach               Attach STDOUT/STDERR and forward signals
      --detach-keys string   Override the key sequence for detaching a
                             container
  -i, --interactive          Attach container's STDIN
```

## docker restart

重启停止运行的 docker 镜像

```bash
Usage:  docker restart [OPTIONS] CONTAINER [CONTAINER...]

Restart one or more containers

Options:
  -t, --time int   Seconds to wait for stop before killing the container
                   (default 10)
```

## docker rm

删除运行中的 docker 容器

```bash
Usage:  docker rm [OPTIONS] CONTAINER [CONTAINER...]

Remove one or more containers

Options:
  -f, --force     Force the removal of a running container (uses SIGKILL)
  -l, --link      Remove the specified link
  -v, --volumes   Remove anonymous volumes associated with the container
```

## docker build

使用 Dockerfile 构建 docker 镜像

```bash
Usage:  docker build [OPTIONS] PATH | URL | -

Build an image from a Dockerfile

Options:
  -f, --file string             Name of the Dockerfile (Default is 'PATH/Dockerfile')
  -t, --tag list                Name and optionally a tag in the 'name:tag' format
```

## docker network

组建和管理 docker 网络

```bash
Usage:  docker network COMMAND

Manage networks

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks
```

# Docker-Compose Command-Line

从 dockerfile 中建立镜像

```bash
apt install docker-compose
```



# Docker 实例

## Nginx

```bash
# 创建一个 nginx 实例
docker run --name nginxname -p 80:80 -d nginx
# 进入容器
docker exec -it nginx /bin/bash
```

## MySQL

```bash
docker pull mysql
# 创建一个 mysql 实例
# 方式 1.不持久化存储
docker run --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
# 方式 2.持久化存储
docker run --name mysql -p 3306:3306 -v /root/mysql/data:/var/lib/mysql -v /root/mysql/logs:/logs -e MYSQL_ROOT_PASSWORD=root -d mysql:latest

# 进入 mysql 容器，登录
docker exec -it mysql bash
mysql -u root -p
```

## PostgreSQL

```bash
docker pull postgres
docker run --name postgresql -v /root/postgresql/data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=root -d postgres:latest

docker exec -it postgresql bash
psql -U postgres

docker start postgresql
docker stop postgresql
docker rm postgresql

docker start pgadmin
docker stop pgadmin
```

## Redis

```bash
# 创建一个 redis 实例
docker run -itd --name redis -p 6379:6379 redis

# 进入 redis 容器
docker exec -it redis redis-cli
# set key value
# get key
```

## WordPress

```bash
# 在 mysql 创建 wordpress 用户，并设置授权
mysql -u root -p
CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'wordpress';
CREATE DATABASE wordpress charset utf8;
GRANT ALL ON wordpress.* TO 'wordpress'@'localhost';

# 启动 wordpress
docker run --name wordpress -p 80:80 -d wordpress -e WORDPRESS_DB_HOST=localhost WORDPRESS_DB_USER=wordpress WORDPRESS_DB_PASSWORD=wordpress WORDPRESS_DB_NAME=wrodpress WORDPRESS_TABLE_PREFIX=TB_
```

## Hadoop

```bash
# 单机版镜像，开发试用
docker pull sequenceiq/hadoop-docker

docker run -it sequenceiq/hadoop-docker:latest /etc/bootstrap.sh -bash --privileged=true
# 50070 Hadoop Namenode UI端口
# 50075 Hadoop Datanode UI端口
# 8088 Yarn任务监控端口
docker run -it -p 50070:50070 -p 8088:8088 -p 50075:50075 sequenceiq/hadoop-docker:latest /etc/bootstrap.sh -bash --privileged=true

# Starting sshd:                                             [  OK  ]
# Starting namenodes on [d27ab660f78c]
# d27ab660f78c: starting namenode, logging to /usr/local/hadoop/logs/hadoop-root-namenode-d27ab660f78c.out
# localhost: starting datanode, logging to /usr/local/hadoop/logs/hadoop-root-datanode-d27ab660f78c.out
# Starting secondary namenodes [0.0.0.0]
# 0.0.0.0: starting secondarynamenode, logging to /usr/local/hadoop/logs/hadoop-root-secondarynamenode-d27ab660f78c.out
# starting yarn daemons
# starting resourcemanager, logging to /usr/local/hadoop/logs/yarn--resourcemanager-d27ab660f78c.out
# localhost: starting nodemanager, logging to /usr/local/hadoop/logs/yarn-root-nodemanager-d27ab660f78c.out

cd /usr/local/hadoop/sbin
./start-all.sh
./mr-jobhistory-daemon.sh start historyserver

# 回到Hadoop主目录cd /usr/local/hadoop，运行示例程序。
# 这个示例程序的功能是将 input 文件夹中的所有文件作为输入，筛选当中符合正则表达式 dfs[a-z.]+ 的单词并统计出现的次数，最后输出结果到 output 文件夹中。
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.0.jar grep input output 'dfs[a-b.]+'

# 查看输出结果
bin/hdfs dfs -cat output/*
```

## ElasticSearch

```bash
docker pull elasticsearch:latest

docker run -it elasticsearch
```

## Kibana

```bash
```



## LogStash

## Kafka



# DockerFile

## Nginx

```dockerfile
web:
  image: nginx
  volumes:
   - ./templates:/etc/nginx/templates
  ports:
   - "8080:80"
  environment:
   - NGINX_HOST=foobar.com
   - NGINX_PORT=80
```

