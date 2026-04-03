---
date: 2026-02-12T12:00:00+08:00
title: Windows Commands
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


# Windows

## 查看用户和用户组

```shell
# 查看所有用户
net user

# 查看所有用户组
net localgroup

# 查看用户账户信息
wmic useraccount list brief
```


## 删除服务

注册表目录 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`

删除对应的服务名


## 清理 windows 菜单

当前用户菜单文件 `%APPDATA%\Microsoft\Windows\Start Menu\Programs`

所有用户菜单文件 `C:\ProgramData\Microsoft\Windows\Start Menu\Programs`

## 设置 powershell 终端

```powershell
# 查看所有配置文件地址
# 使用 CurrentUserAllHosts 或 CurrentUserCurrentHost

$PROFILE | Select-Object *

# 如果目录和文件不存在，则创建目录和文件
if (-not (Test-Path $parentDir)) { New-Item -ItemType Directory -Path $parentDir -Force }
New-Item -Path $PROFILE -ItemType File -Force
Test-Path $PROFILE

# 编辑文件
notepad $PROFILE

# 保证和服务端的终端一致
# 在 linux 服务器执行 echo $TERM
$Env:TERM = "xterm-256color"
```