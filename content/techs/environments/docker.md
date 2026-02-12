# Docker Install

Ubuntu

## storage drivers

Docker Engine on Ubuntu supports `overlay2`, `aufs` and `btrfs` storage drivers.

Docker Engine uses the `overlay2` storage driver by default. If you need to use `aufs` instead, you need to configure it manually. See [use the AUFS storage driver](https://docs.docker.com/storage/storagedriver/aufs-driver/)

docker 有两个非常重要的概念，分别是镜像（image）与容器（container）。镜像和容器本质上都是一个文件系统，它们唯一的不同，就是镜像是只读的，而容器是可读可写的。

## Installation methods

You can install Docker Engine in different ways, depending on your needs:

- Most users [set up Docker’s repositories](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) and install from them, for ease of installation and upgrade tasks. This is the recommended approach.

    ```bash
    apt-get update
    
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    apt-get update
    apt-get install docker-ce docker-ce-cli containerd.io
    
    apt-cache madison docker-ce
    
    VERSION_STRING=????;sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io
    ```

- Some users download the DEB package and [install it manually](https://docs.docker.com/engine/install/ubuntu/#install-from-a-package) and manage upgrades completely manually. This is useful in situations such as installing Docker on air-gapped systems with no access to the internet.

- In testing and development environments, some users choose to use automated [convenience scripts](https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script) to install Docker.

## docker run hello-world

```bash
root@iZ2ze49dgr09ifxfj9lirgZ:~# docker run hello-world
Unable to find image 'hello-world:latest' locally

latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:975f4b14f326b05db86e16de00144f9c12257553bba9484fed41f9b6f2257800
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Manage Docker as a non-root user

The Docker daemon binds to a Unix socket instead of a TCP port. By default that Unix socket is owned by the user `root` and other users can only access it using `sudo`. The Docker daemon always runs as the `root` user.

If you don’t want to preface the `docker` command with `sudo`, create a Unix group called `docker` and add users to it. When the Docker daemon starts, it creates a Unix socket accessible by members of the `docker` group.

[Post-installation steps for Linux | Docker Documentation](https://docs.docker.com/engine/install/linux-postinstall/)

# Docker 更换国内镜像源

1. 查找并编辑配置文件
2. 重启 docker 服务，注意：会停止运行中的 docker 镜像
3. 使用 docker info 查看 docker 的镜像源是否变更

```bash
# 如果没有文件，直接新建
vim /etc/docker/daemon.json
```

```json
# 编辑内容，镜像可以更换为任意国内镜像源
{
 "registry-mirrors" : [
   "https://docker.mirrors.ustc.edu.cn/",
   "https://mirror.ccs.tencentyun.com",
   "https://hub-mirror.c.163.com/",
   "http://registry.docker-cn.com"
 ],
 "insecure-registries" : [
   "registry.docker-cn.com",
   "docker.mirrors.ustc.edu.cn"
 ],
 "debug" : true,
 "experimental" : true
}
```

```bash
systemctl restart docker.service
docker info
```



# Docker 相关概念

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

