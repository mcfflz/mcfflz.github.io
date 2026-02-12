# linux 目录结构

linux 所有文件都在根目录 / 下。和 windows 不同，没有 C、D、E 等盘符

## /usr

### /usr/local 本地目录

## /mnt

硬盘挂载目录

# linux 用户与用户组

## /etc/group

[Linux /etc/group文件解析（超详细） (biancheng.net)](http://c.biancheng.net/view/841.html)

```bash
# 组名：密码：GID：该用户组中的用户列表
# 示例如下
root:x:0:
daemon:x:1:
...
admin:x:1000:
```

## /etc/passwd

[Linux /etc/passwd内容解释（超详细） (biancheng.net)](http://c.biancheng.net/view/839.html)

```bash
# 用户名：密码：UID（用户ID）：GID（组ID）：描述性信息：主目录：默认Shell
# 示例如下
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
...
admin:x:1000:1000::/home/admin:/bin/bash
```

## /etc/shadow

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

## /etc/gshadow

[Linux /etc/gshadow文件内容解析 (biancheng.net)](http://c.biancheng.net/view/842.html)

```bash
# 组名：加密密码：组管理员：组附加用户列表
# 示例如下
root:*::
daemon:*::
...
admin:!::
```

## 创建用户组

[Linux groupadd命令：添加用户组 (biancheng.net)](http://c.biancheng.net/view/856.html)

```bash
groupadd [options] group
options:
	-p --password
	-r --system
```

## 创建用户

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

## 修改用户密码

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

