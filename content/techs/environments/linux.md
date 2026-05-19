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


## linux 常用命令

### 用户管理

```bash
# 查看完整用户信息（含UID/GID/家目录等）
cat /etc/passwd
getent passwd

# 查看当前用户信息
id
whoami

# 基础创建（默认家目录 /home/username）
sudo useradd username

# 高级参数组合
sudo useradd -m -d /custom/home -s /bin/zsh -u 1005 -g developers -G admins,devops username
# -m: 自动创建家目录
# -d: 指定自定义家目录路径
# -s: 设置登录 Shell
# -u: 指定 UID（需唯一且 >1000）
# -g: 主组（需提前存在）
# -G: 附加组（逗号分隔，不覆盖原有组）

# 修改用户名
sudo usermod -l newname oldname

# 修改用户家目录
sudo usermod -d /new/home/dir username

# 移动家目录内容到新位置
sudo usermod -d /new/home/dir -m username

# 修改UID
sudo usermod -u 2002 username

# 修改主组
sudo usermod -g new_primary_group username

# 删除用户（保留家目录）
# 注意：删除前需检查进程占用
ps -u username
sudo userdel username

# 删除用户（不保留家目录）
sudo userdel -r username

# 强制删除（即使用户已登录）
sudo userdel -f -r username
```

### 密码管理

```bash
# 用户自主修改密码
passwd

# 管理员重置密码
sudo passwd username

# 锁定账户（禁止登录）
sudo passwd -l username

# 解锁账户
sudo passwd -u username

# 删除用户密码（允许无密码登录）
sudo passwd -d username
```

### 用户组管理

用户组用于实现用户角色划分，便于权限管理

```bash
# 查看所有组
getent group
cat /etc/group

# 查看当前用户所属组
groups username
id username

# 查看特定组详情
getent group developers

# 创建新组（默认GID）
sudo groupadd developers

# 指定GID创建
sudo groupadd -g 1005 testers

# 重命名组
sudo groupmod -n dev_team developers

# 修改GID
sudo groupmod -g 2001 dev_team

# 设置组密码（慎用）
sudo groupmod -p password dev_team

# 删除空组
# 注意：无法删除作为主组的组
sudo groupdel testers 

# 添加用户到附加组
sudo usermod -aG dev_team alice

# 从组中移除用户
sudo gpasswd -d alice dev_team

# 设置组管理员
sudo gpasswd -A alice dev_team

# 批量添加用户到多个组
for GROUP in dev ops; do
  sudo usermod -aG $GROUP bob
done
```

### 硬盘挂载

```bash
# 查看硬盘信息（块存储）
lsblk -f

# fdisk 查看磁盘分区信息
fdisk -l

# mount 挂载文件系统
mount /dev/sda1 /home/thtf/file

# umount 卸载文件系统
umount /dev/sda1

# df 查看磁盘使用情况
df -l
```

### 磁盘空间

```bash
# 查看当前目录下所有文件和目录的总大小，*默认不匹配隐藏文件
du -sh *

# 查看指定路径下一级子目录的大小
du -h --max-depth=1 <directory>

# 交互式工具
ncdu
```

### 文件属性

[Linux 文件基本属性 | 菜鸟教程 (runoob.com)](https://www.runoob.com/linux/linux-file-attr-permission.html)



```bash
# 在 Linux 中第0个字符代表这个文件是目录、文件或链接文件等等。

# 当为 d 则是目录
# 当为 - 则是文件；
# 若是 l 则表示为链接文档(link file)；
# 若是 b 则表示为装置文件里面的可供储存的接口设备(可随机存取装置)；
# 若是 c 则表示为装置文件里面的串行端口设备，例如键盘、鼠标(一次性读取装置)。

# 在 Linux 中第1-9个字符代表这个文件的权限
# ugoa
# user：用户
# group：组
# others：其他
# all：全部
# 第1-3位确定所属用户（该文件的所有者,）拥有该文件的权限
# 第4-6位确定所属用户组（所有者的同组用户）拥有该文件的权限
# 第7-9位确定其他用户拥有该文件的权限。

# rwx
# r -- 4 readable
# w -- 2 writeable
# x -- 1 executable
# chmod u=rwx,g=rx,o=r filename 等价于 chmod 754 filename
# rwx存在依赖关系：
# 对所有文件，x依赖于r；
# 对目录文件，w依赖于x
# 对普通文件，w没有依赖
# 目录文件 r(4) rx(5) rwx(7)
# 普通文件 r(4) rw(6) rx(5) rwx(7)


# mkdir 创建目录
mkdir <directory>

# touch 创建文件
touch <filename>

# chown 更改文件所属用户和用户组
chown [OWNER][:[GROUP]] <filename>

# chgrp 更改文件所属用户组
chgrp <groupname> <filename>

#  chmod 更改文件权限
chmod [OPTION]... MODE <filename>...
```


### 文件查阅

```bash
# 查看文件内容
cat <filename>

# more 分页查看文件
more <filename>

# head 从文件头开始查阅
head <filename>

# tail 查看文件尾开始查阅
tail <filename>

# find 查找文件
find <directory> -name <filename>
```

### linux 中比较重要的文件

#### /etc/profile

此文件涉及系统的环境，即环境变量相关。这里修改会对所有用户起作用。/etc/profile会首先执行/etc/profile.d/目录下的所有*.sh文件

#### /etc/init.d/

init.d 目录中存放的是系统服务的管理（启动与停止）脚本。

### 网络管理命令

```bash
# ifconfig 查看ip
ifconfig

# lsof -i:port 查看端口是否开放
lsof -i:3306

# nc 设置网络路由
nc -lnvp 8080 # 监听 8080 端口

# curl 传输数据，默认将输出（如下载内容）打印到标准输出，通常需要配合 -o参数保存到文件。
curl www.baidu.com

# wget 获取文件，默认将文件直接下载并保存到当前目录。
wget www.baidu.com
```

### bash 快捷键

```bash
ctrl+u 删除命令行开始至光标处
ctrl+k 删除光标处至命令行结尾
ctrl+d 删除光标处的字符
ctrl+a 光标移动到最前面
ctrl+e 光标移动到最后面

ctrl+r 查找历史命令
```

### 内存管理

```bash
# 查看内存使用情况
free -h

# 查看内存占用前10的进程
ps aux --sort=-%mem | head -10
```

### 进程管理

```bash
# uname 查看操作系统信息
uname -a

# hostname 查看主机名
hostname

# ps 查看进程信息
# 查看系统所有进程的详细信息，这是最常用的命令
# a：显示所有用户的进程。
# u：以用户为主的格式显示。
# x：显示没有控制终端的进程（如后台服务）。
ps -aux

# 以完整格式列表显示所有进程，能清晰看到父进程ID（PPID）
# e：显示所有进程。
# f：显示完整格式列表。
ps -ef

# 显示进程层次关系
ps -ef --forest

# 查找特定进程
ps -aux | grep <name>


# top 查看进程信息
# 动态显示进程占用资源信息
top -hv | -bcEHiOSs1 -d secs -n max -u|U user -p pid(s) -o field -w [cols]

# env 查看环境变量
env
```

### 应用管理

```bash
# apt 是 Debian 和 Ubuntu 系统的包管理工具，用于安装、更新、删除软件包及管理依赖关系。
# 查看安装的软件包
apt list --installed

# 搜索包含关键词的包
apt search <keyword>

# 安装软件包
sudo apt install <package>            # 安装单个包
sudo apt install pkg1 pkg2            # 安装多个包
sudo apt install <package>=<version>  # 安装指定版本

# 卸载软件包
sudo apt remove <package>   # 保留配置文件
sudo apt purge <package>    # 彻底删除包及配置
sudo apt autoremove         # 清理不再需要的依赖

# 升级软件包
sudo apt update             # 更新软件仓库版本信息
apt list --upgradable       # 列出可以升级的软件包
sudo apt upgrade            # 保留旧配置升级
sudo apt full-upgrade       # 可能移除冲突包（推荐大版本升级时使用）

# 依赖关系
apt depends <package>         # 查看依赖树
sudo apt --fix-broken install # 修复依赖关系

# 清除缓存
sudo apt clean

# snap 是自包含的容器化软件包（.snap格式），集成应用程序及其所有依赖项，支持跨发行版运行
# snap 软件管理命令和 apt 命令相似，不做赘述
# snap 有一些高级命令

# aptitude 是提供图形化界面，可以更好地管理包
```

### 压缩/解压缩命令

```bash
# tar 压缩/解压文件
# 解压文件
tar -zxvf <filename>

# 压缩文件
tar -zcvf <filename> or <filepath>

# zip 压缩文件
zip [-options] [-b path] [-t mmddyyyy] [-n suffixes] [zipfile list] [-xi list]

# unzip 解压文件
unzip <filename>
```

### tmux 会话

tmux 命令核心用途是通过会话、窗口和窗格的分层管理，提升终端操作的效率和灵活性。主要应用场景：

1. 会话持久化，解决终端断开导致进程终止的问题，同一会话可被多个终端窗口或用户共享，实现协作开发或远程演示。
2. 多任务并行处理，创建多个独立窗口（Ctrl+b c），每个窗口可运行不同任务，通过快捷键（Ctrl+b n/p）快速切换。

```bash
# 启动命名会话
tmux new -s <session_name>

# 查看所有会话
tmux ls

# 重新连接会话
tmux attach -t <session_name>

# 从会话中分离（返回原终端）
前缀键 + D  # 按 Ctrl+B，松开，再按 D

# 重命名当前会话
前缀键 + $
```

### cron 定时任务

cron 的核心是一个长期运行在后台的**守护进程**，通常名为 `crond`。它的唯一职责就是“按时执行任务”。

工作流程

1. **启动与加载**：系统启动时，`crond` 被初始化（通过 systemd、init 等）。它会立即加载所有用户的 crontab 文件（来自 `/var/spool/cron/` 或 `/etc/cron.d/`）以及系统级的 `/etc/crontab` 文件到内存中。
2. **休眠与唤醒**：`crond` 随后进入休眠状态，但会设置一个“闹钟”，在**下一分钟开始时**唤醒自己。
3. **检查与执行**：每分钟被唤醒后，`crond` 会：
    *   检查内存中所有任务计划。
    *   将当前时间（年、月、日、周、时、分）与每个任务的“时间字段”进行匹配。
    *   将所有匹配到的任务，**立即**交给其指定的 shell（如 `/bin/sh`）去创建一个子进程执行。
    *   **重要**：任务执行是**并发**的，每分钟内匹配到的所有任务会同时启动，互不等待。
4. **记录日志**：`crond` 会将所有任务的执行行为（启动、完成）记录到系统日志（通常是 `/var/log/cron` 或 `journalctl -u cron`），这对于调试至关重要。
5. **循环**：完成后，再次计算到下一分钟的时间，进入休眠，等待下一次唤醒。

注意事项：

*  **环境变量**：`crond` 执行任务时，其环境变量**非常精简**，通常只包含最基本的环境（如 `PATH=/usr/bin:/bin`）。这与您登录 Shell 的丰富环境不同。因此，在 crontab 中执行的命令**必须使用绝对路径**，或者在脚本开头显式设置 `PATH` 等变量。
*  **执行上下文**：任务在**其所属用户**的身份下执行。例如，用户 `ubuntu` 的 cron 任务，会以 `ubuntu` 的权限运行，可以访问 `ubuntu` 有权访问的文件。


```bash
# 列出当前用户的所有cron任务
crontab -l

# 编辑当前用户的cron任务表
crontab -e

# 删除当前用户的cron任务表（慎用，会删除所有任务）
crontab -r

# linux crontab 表达式
* * * * * <script>
│ │ │ │ │
│ │ │ │ └── 星期几 (0-7, 0和7都表示周日)
│ │ │ └──── 月份 (1-12 或 JAN-DEC)
│ │ └────── 日期 (1-31)
│ └──────── 小时 (0-23)
└────────── 分钟 (0-59)

# 预定义宏，等价于表达式，可以替代使用
# `@reboot`：在系统启动后执行一次（不是“每次重启计划”，因为 crontab 只在启动时被读取）。
# `@yearly` / `@annually`：等同于 `0 0 1 1 *`（每年1月1日0点0分）。
# `@monthly`：等同于 `0 0 1 * *`（每月1号0点0分）。
# `@weekly`：等同于 `0 0 * * 0`（每周日0点0分）。
# `@daily` / `@midnight`：等同于 `0 0 * * *`（每天0点0分）。
# `@hourly`：等同于 `0 * * * *`（每小时0分）。
```

### 终端和终端模拟器

- **终端（Terminal）**：用户与计算机交互的**输入/输出界面**，分为**物理终端**（如早期电传打字机，已淘汰）和**虚拟终端**（如Linux的`/dev/tty1`~`tty6`，通过`Ctrl+Alt+F1`切换）。本质是内核提供的字符设备接口，负责传递用户输入并显示系统输出。

- **终端模拟器（Terminal Emulator）**：**软件程序**（如GNOME Terminal、Windows Terminal），模拟物理终端的行为，提供图形化界面、多标签、自定义主题等增强功能。依赖**伪终端（PTY）**与内核通信，是现代系统的主要交互方式。

- **TTY（Teletypewriter）**：**内核子系统**，管理终端设备的输入/输出。分为**物理TTY**（如串口终端`/dev/ttyS0`）和**虚拟TTY**（如`/dev/tty1`）。负责处理行规程（如回显、特殊字符映射，如`Ctrl+C`发送`SIGINT`）。

- **PTY（Pseudo Terminal）**：**用户态模拟的终端**，由**主设备（Master）**和**从设备（Slave）**组成（如`/dev/ptmx`为主设备，`/dev/pts/0`为从设备）。终端模拟器（如SSH客户端）通过主设备与内核通信，从设备连接Shell，实现远程登录、图形终端等功能。  

- **Shell**：用户与操作系统内核之间的**命令解释器**，负责解析用户输入的命令（如`ls -l`）并调用内核执行。常见类型包括Bash（Linux默认）、Zsh（增强交互）、PowerShell（Windows）。  

- **命令执行流程**：用户在终端模拟器输入命令→终端模拟器通过PTY将命令传递给Shell→Shell解析命令并调用内核→内核执行后将结果返回Shell→Shell将结果通过PTY传回终端模拟器显示。示例：用户输入 → 终端模拟器 → PTY 主设备 → TTY 驱动 → Shell → 内核执行 → Shell 输出 → TTY 驱动 → PTY 从设备 → 终端模拟器 → 屏幕显示。


