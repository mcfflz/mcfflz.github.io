---
date: 2026-02-12T12:00:00+08:00
title: Linux Commands
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

# linux 基础

## 参考资料

[文件系统层次结构标准](https://people.ubuntu.com/~happyaron/docs/FHS.zh_CN.pdf)

[FHS](https://github.com/GrandKai/Filesystem-Hierarchy-Standard/blob/master/fhs-3.0.pdf)

[linux 教程](https://www.runoob.com/linux/linux-tutorial.html)

[linux 命令大全](https://www.runoob.com/linux/linux-command-manual.html)


## linux 目录结构

linux 操作系统的目录结构是一个层次化的树状结构，所有文件都在根目录 `/` 下。

它遵循文件系统层次结构标准（FHS），主要设计思想是将系统文件、配置文件、用户文件和运行时的文件分开存放，便于管理和维护。

和 windows 不同，linux 目录没有 C、D、E 等盘符。

linux 核心目录及简要介绍：

| 目录 | 主要用途 |
| :--- | :--- |
| `/` | 根目录，整个文件系统的起点。根文件系统的内容必须足以启动、还原、恢复和/或修复系统。 |
| `/bin` | 基础命令二进制文件。存放所有用户（包括普通用户和系统管理员）在单用户模式或紧急恢复时都必需的基础命令。例如：`ls`, `cp`, `bash`, `cat` 等。这里的命令是系统运行的根本，通常为静态链接，不依赖于 `/usr` 目录。 |
| `/boot` | 引导加载程序静态文件。存放启动 linux 系统所需的核心文件。例如：内核镜像 `vmlinuz`、初始内存磁盘镜像 `initrd.img`，以及引导加载程序（如 GRUB）的配置文件。 |
| `/dev` | 设备文件。包含了所有的设备文件。在 linux 中，“一切皆文件”，硬件设备（如硬盘 `/dev/sda`、终端 `/dev/tty`、随机数生成器 `/dev/random`）以特殊文件的形式存在于此。 |
| `/etc` | 主机特定系统配置。存放这台主机系统的全局配置文件（文本文件）。例如：用户密码文件 `/etc/passwd`、网络配置 `/etc/network/`、软件包管理配置等。不应存放二进制可执行文件。 |
| `/lib` & `lib64` | 必要共享库和内核模块。为 `/bin` 和 `/sbin` 中的二进制程序提供必要的共享库和内核模块。类似于 Windows 的 `System32` 目录。没有这些库，`/bin` 和 `/sbin` 下的很多命令将无法运行。 |
| `/media` | 可移动媒体挂载点。系统自动挂载可移动媒体（如 U 盘、光盘、SD 卡）的标准位置。例如：插入 U 盘后，通常会自动挂载到 `/media/username/USB_NAME` 这样的路径下。 |
| `/mnt` | 临时文件系统挂载点。临时手动挂载文件系统的通用目录。root 用户可以在这里挂载硬盘分区、网络共享（NFS）等，用于临时的操作或测试。 |
| `/opt` | 附加应用软件包。用于安装独立的、第三方的、大型应用程序。通常，一个软件的所有文件（二进制、库、资源）都集中在这个软件自己的子目录里。例如：`/opt/google/chrome/`。 |
| `/run` | 运行进程相关数据。存放自系统本次启动以来的运行时数据。例如：进程的 PID 文件、用户登录信息、服务锁文件等。这是一个临时文件系统，重启后内容会清空。 |
| `/sbin` | 必要系统二进制文件。存放系统管理所必需的命令。通常只有 root 用户才有权限执行。例如：`fdisk`（磁盘分区）、`ifconfig`（网络配置）、`init`（初始化进程）等。 |
| `/srv` | 系统服务数据。存放本系统对外提供服务所产生的数据。例如，一个 Web 服务器可以将其网站文件放在 `/srv/www/`，FTP 服务器的文件放在 `/srv/ftp/`。有助于将服务数据与系统本身的配置（`/etc`）和可变数据（`/var`）清晰分离。 |
| `/tmp` | 临时文件。供所有用户和程序存放临时文件。系统可能配置为在重启时或定期清理此目录。 |
| `/usr` | 二级层次。这是系统中最庞大、最重要的目录之一，可以视作一个只读的、可共享的、独立的次级文件系统。它包含了所有用户的应用程序、库、文档等。例如：`/usr/bin`: 绝大多数用户命令，`/usr/lib`: 应用程序的共享库。在系统正常启动后，它应该是只读的。其内部结构本身也是一个完整的层次。 |
| `/var` | 可变数据。存放经常变化的数据。如系统日志（`/var/log`）、邮件队列（`/var/mail`）、打印任务缓存（`/var/spool`）、数据库文件、网站的动态内容等。 |

| `/home` | 普通用户目录，每个普通用户都有一个以用户名命名的子目录（如 `/home/ubuntu`），用于存放个人文件。 |
| `/root` | root 用户目录，仅 root 用户使用。 |
| `/proc` | 进程与内核信息，一个虚拟文件系统，提供关于系统进程和内核参数的实时信息。 |

这种结构将静态的命令、动态的数据、用户的文件、系统的配置清晰地分离。对于普通用户，最常接触的是 `/home` 下的个人目录和 `/usr` 下的应用程序；而系统管理员则需要关注 `/etc`, `/var/log` 等目录。


## linux 用户与用户组

### /etc/group

[Linux /etc/group文件解析（超详细） (biancheng.net)](http://c.biancheng.net/view/841.html)

```bash
# 组名：密码：GID：该用户组中的用户列表
# 示例如下
root:x:0:
daemon:x:1:
...
admin:x:1000:
```

### /etc/passwd

[Linux /etc/passwd内容解释（超详细） (biancheng.net)](http://c.biancheng.net/view/839.html)

```bash
# 用户名：密码：UID（用户ID）：GID（组ID）：描述性信息：主目录：默认Shell
# 示例如下
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
admin:x:1000:1000::/home/admin:/bin/bash
```

### /etc/shadow

[Linux /etc/shadow（影子文件）内容解析（超详细） (biancheng.net)](http://c.biancheng.net/view/840.html)

```bash
# 用户名：加密密码：最后一次修改时间：最小修改时间间隔：密码有效期：密码需要变更前的警告天数：密码过期后的宽限时间：账号失效时间：保留字段
# 示例如下
root:$6$O7sgR5mfuCpFKbe1$VUUzqM/IvDBlqV3CGHV3/FG3mfWw2ngYQFR39wrQVLayoW75ATUf95gq8aJB4xGtAEDtjsxm68.o3veEz5msn.:18841:0:99999:7:::
# aliyunServer:Psbc@123456
daemon:*:18375:0:99999:7:::
...
admin:$6$o4Ui0hCtBUTUw16g$00PXoA4/uN00VFkmp3bnVbBIrqyBp0IaFlLS/ECIPEYgUIlpMY37cEeN1pGXfWmp7QgUth9mWk8g4dwv4d16h/:18846:0:99999:7:::
# aliyunServer:admin1234
```

### /etc/gshadow

[Linux /etc/gshadow文件内容解析 (biancheng.net)](http://c.biancheng.net/view/842.html)

```bash
# 组名：加密密码：组管理员：组附加用户列表
# 示例如下
root:*::
daemon:*::
...
admin:!::
```

### 创建用户组

[Linux groupadd命令：添加用户组 (biancheng.net)](http://c.biancheng.net/view/856.html)

```bash
groupadd [options] group
options:
	-p --password
	-r --system
```

### 创建用户

[Linux useradd命令详解：添加新的系统用户 (biancheng.net)](http://c.biancheng.net/view/844.html)

```bash
useradd [options]
options:
	-b --base-dir
	-d --home-dir
	-g --gid
	-G --groups
	-p --password
	-r --system
	-s --shell
```

### 修改用户密码

```bash
passwd [options] username
options:
	-l --lock
	-u --unlock

# 有sudo权限可以设置root密码
sudo passwd root
```

# linux 硬盘挂载

## lsblk 查看硬盘信息（块存储）

```bash
lsblk -f
```

## fdisk 查看磁盘分区信息

```bash
fdisk -l
```

## mount 挂载文件系统

挂载文件系统到某个目录下，使得能够文件系统能够访问该磁盘。

```bash
mount /dev/sda1 /home/thtf/file
```

## umount 卸载文件系统

```bash
umount /dev/sda1
```

## df 查看磁盘使用情况

```bash
df -l
```

## /etc/fstab 挂载配置文件

```bash

```

# linux 文件操作

## 文件属性

[Linux 文件基本属性 | 菜鸟教程 (runoob.com)](https://www.runoob.com/linux/linux-file-attr-permission.html)

### 文件类型

```bash
在 Linux 中第一个字符代表这个文件是目录、文件或链接文件等等。

当为 d 则是目录
当为 - 则是文件；
若是 l 则表示为链接文档(link file)；
若是 b 则表示为装置文件里面的可供储存的接口设备(可随机存取装置)；
若是 c 则表示为装置文件里面的串行端口设备，例如键盘、鼠标(一次性读取装置)。
```

### ugoa

```bash
user：用户
group：组
others：其他
all：全部
第1-3位确定所属用户（该文件的所有者,）拥有该文件的权限
第4-6位确定所属用户组（所有者的同组用户）拥有该文件的权限
第7-9位确定其他用户拥有该文件的权限。
```

### rwx

```bash
r -- 4 readable
w -- 2 writeable
x -- 1 executable
# chmod u=rwx,g=rx,o=r filename 等价于 chmod 754 filename
# rwx存在依赖关系：
# 对所有文件，x依赖于r；
# 对目录文件，w依赖于x
# 对普通文件，w没有依赖
目录文件 r(4) rx(5) rwx(7)
普通文件 r(4) rw(6) rx(5) rwx(7)
```

## mkdir 创建目录

```bash
# mkdir - make directories
mkdir [OPTION]... DIRECTORY...
```

## touch 创建文件

```bash
# touch - change file timestamps
touch [OPTION]... FILE...
```

## chown 更改文件所属用户和用户组

```bash
# chown - change file owner and group
chown [OPTION]... [OWNER][:[GROUP]] FILE...
chown [OPTION]... --reference=RFILE FILE...

chmod thtf filename
```

## chgrp 更改文件所属用户组

```bash
# chgrp - change group ownership
chgrp [OPTION]... GROUP FILE...
chgrp [OPTION]... --reference=RFILE FILE...
```

##  chmod 更改文件权限

```bash
# chmod - change file mode bits
chmod [OPTION]... MODE[,MODE]... FILE...
chmod [OPTION]... OCTAL-MODE FILE...
chmod [OPTION]... --reference=RFILE FILE...
```

## ln 链接

```bash
# ln 
ln [OPTION]... [-T] TARGET LINK_NAME
  or:  ln [OPTION]... TARGET
  or:  ln [OPTION]... TARGET... DIRECTORY
  or:  ln [OPTION]... -t DIRECTORY TARGET...

```



# linux 中比较重要的文件

## /etc/profile

此文件涉及系统的环境，即环境变量相关。这里修改会对所有用户起作用。/etc/profile会首先执行/etc/profile.d/目录下的所有*.sh文件

## /etc/init.d/

init.d 目录中存放的是系统服务的管理（启动与停止）脚本。





# linux 网络

## ifconfig 查看ip

```bash
ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.25.18.32  netmask 255.255.192.0  broadcast 172.25.63.255
        inet6 fe80::216:3eff:fe34:d9a4  prefixlen 64  scopeid 0x20<link>
        ether 00:16:3e:34:d9:a4  txqueuelen 1000  (Ethernet)
        RX packets 883830  bytes 1239691155 (1.2 GB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 503995  bytes 41476128 (41.4 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 8279  bytes 658587 (658.5 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 8279  bytes 658587 (658.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## lsof -i:port 查看端口是否开放

```bash
lsof -i:3306

COMMAND   PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
mysqld  15656 admin   25u  IPv6 285819      0t0  TCP *:mysql (LISTEN)
```

## nc 设置网络路由

```bash
# 监听 8080 端口
nc -lnvp 8080
```

## curl 执行 URL 命令

```bash
# 访问页面
curl www.baidu.com
```



# 遇到过的问题

## /etc/profile 文件错误导致命令无法使用

[Linux下修复修改profile文件导致命令不用可的解决方法_an7800666的博客-CSDN博客](https://blog.csdn.net/an7800666/article/details/101476361)

在配置环境变量时，修改了/etc/profile 文件，然后source /etc/profile

由于一个配置错误，导致一些系统命令没法使用了

```
 ll
-bash: ls: command not found
```

 

用下面方法可以修复

命令行 输入;

export PATH=/usr/bin:/usr/sbin:/bin:/sbin:/usr/X11R6/bin

然后 vi /etc/profile，纠正错误配置，然后source /etc/profile即可



# linux bash 快捷键

```bash
ctrl+u 删除命令行开始至光标处
ctrl+k 删除光标处至命令行结尾
ctrl+d 删除光标处的字符
ctrl+a 光标移动到最前面
ctrl+e 光标移动到最后面

ctrl+r 查找历史命令
```

# linux 操作系统常用命令

## uname 查看操作系统信息

```bash
# 查看操作系统信息
uname -a
```

## hostname 查看主机名

```bash
hostname
```

## ps 查看进程信息

```bash
# 显示当前进程占用资源的快照
ps -a            - 列出所有运行中/激活进程
ps -ef | grep     - 列出需要进程
ps -aux          - 显示进程信息，包括无终端的（x）和针对用户（u）的进程：如USER, PID, %CPU, %MEM等
```

## top 查看进程信息

```bash
# 动态显示进程占用资源信息
top -hv | -bcEHiOSs1 -d secs -n max -u|U user -p pid(s) -o field -w [cols]
```

## ifconfig 查看网络信息

```bash
# 查看设备的网络信息 ip mac
ifconfig
```

## env 查看环境变量

```bash
env
```



# linux 文件常用命令

## touch 创建文件

```bash
touch filename
```

## file 查看文件类型

```bash
file [OPTION...] <file>...
```

## cat 查看文件内容

```bash
# 查看文件内容
cat filename
```

## more 分页查看文件

```bash
# 按照屏幕分页查看文件内容
# A file perusal filter for CRT viewing.
# CRT: connection remote terminator
more [options] <file>...
```

## head 从文件头开始查阅

```bash
# 查看文件前十行内容

head [OPTION]... [FILE]...
```

## tail 查看文件尾开始查阅

```bash
# 查看文件后十行内容

tail [OPTION]... [FILE]...
```

## xargs 参数转换

```bash
# 将多行参数转换为单行参数

find / -name "filename" | xargs grep "keywords"

# 将单行参数转换为多行参数

cat filename | xargs -n3
```

## tar 压缩/解压文件

```bash
# 解压文件
tar -zxvf filename

# 压缩文件
tar -zcvf filename or filepath

```

## zip 压缩文件

```bash
zip [-options] [-b path] [-t mmddyyyy] [-n suffixes] [zipfile list] [-xi list]
```

## unzip 解压文件

```bash
unzip filename
```



# linux 网络通讯常用命令

## wget 网络通讯

```bash
# GNU Wget is a free software package for retrieving files using HTTP, HTTPS, FTP and FTPS, the most widely used Internet protocols.
# It is a non-interactive commandline tool, so it may easily be called from scripts, cron jobs, terminals without X-Windows support, etc.

wget [OPTION]... [URL]...
```



## curl 文件传输下载

```bash
# command line tool and library for transferring data with URLs (since 1998)
# curl 是常用的命令行工具，用来请求服务器，与服务器之间传输数据。

curl [options...] <url>
```



# linux 安全常用命令

## gpg 加密

```bash
# Supported algorithms:
# Pubkey: RSA, ELG, DSA, ECDH, ECDSA, EDDSA
# Cipher: IDEA, 3DES, CAST5, BLOWFISH, AES, AES192, AES256, TWOFISH,
#         CAMELLIA128, CAMELLIA192, CAMELLIA256
# Hash: SHA1, RIPEMD160, SHA256, SHA384, SHA512, SHA224
# Compression: Uncompressed, ZIP, ZLIB, BZIP2

gpg [options] [files]
```

```bash
root@iZ2ze49dgr09ifxfj9lirgZ:~# gpg --gen-key
gpg (GnuPG) 2.2.19; Copyright (C) 2019 Free Software Foundation, Inc.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

gpg: directory '/root/.gnupg' created
gpg: keybox '/root/.gnupg/pubring.kbx' created
Note: Use "gpg --full-generate-key" for a full featured key generation dialog.

GnuPG needs to construct a user ID to identify your key.

Real name: testkey
Email address: test@mail.com
You selected this USER-ID:
    "testkey <test@mail.com>"

Change (N)ame, (E)mail, or (O)kay/(Q)uit? o
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: /root/.gnupg/trustdb.gpg: trustdb created
gpg: key C00C9AFCA7D9017D marked as ultimately trusted
gpg: directory '/root/.gnupg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/root/.gnupg/openpgp-revocs.d/8406B61A034AECDA03443297C00C9AFCA7D9017D.rev'
public and secret key created and signed.

pub   rsa3072 2022-01-20 [SC] [expires: 2024-01-20]
      8406B61A034AECDA03443297C00C9AFCA7D9017D
uid                      testkey <test@mail.com>
sub   rsa3072 2022-01-20 [E] [expires: 2024-01-20]

```



# linux make 编译工具

makefile 是一个编辑工具，能让编译过程更加轻松，编译器是 gcc 和 g++。

makefile 可以看做是脚本语言。

# linux jdk 安装

[Linux安装jdk8及环境变量配置 - 简书 (jianshu.com)](https://www.jianshu.com/p/f000e05f3512)

```bash
# 配置环境变量
vi /etc/profile

export JAVA_HOME=/usr/local/jdk-16.0.2
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export PATH=$PATH:$JAVA_HOME/bin
```

```bash
# 环境变量生效
source /etc/profile
```

# linux maven 安装

[linux安装maven - 惊涛随笔 - 博客园 (cnblogs.com)](https://www.cnblogs.com/jtnote/p/9982185.html)



```bash
# 配置环境变量
vi /etc/profile

export MAVEN_HOME=/opt/apache-maven-3.5.4
export PATH=$MAVEN_HOME/bin:$PATH
```

```bash
# 环境变量生效
source /etc/profile
```

```bash
# 更改maven配置

# 本地仓库
<localRepository>/usr/local/maven/local_repository</localRepository>

# 镜像源
<mirror>
    <id>aliyunmaven</id>
    <mirrorOf>*</mirrorOf>
    <name>阿里云公共仓库</name>
    <url>https://maven.aliyun.com/repository/public</url>
</mirror>
```

# linux rocketmq 安装

```bash
# 解压


```

