---
date: 2026-02-12T12:00:00+08:00
title: Nginx
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

# nginx install

[nginx org](http://nginx.org/)

# nginx building

## ./configure

```bash
# 依赖 openssl pcre zlib 库的源码
tar zxvf /usr/local/src/pcre-8.45.tar.gz
cd /usr/local/src/pcre-8.45
./configure

tar zxvf /usr/local/src/openssl-1.1.1k.tar.gz
cd /usr/local/src/openssl-1.1.1k
./config
```



```bash
./configure --prefix=/home/admin/nginx-1.20.1 --error-log-path=/home/admin/logs/nginx/error.log --pid-path=/home/admin/etc/nginx/nginx.pid --lock-path=/home/admin/etc/nginx/nginx.lock --user=admin --with-http_ssl_module --with-pcre=/usr/local/src/pcre-8.45 --with-openssl=/usr/local/src/openssl-1.1.1k
```



```bash
Configuration summary
  + using PCRE library: /usr/local/src/pcre-8.45
  + using OpenSSL library: /usr/local/src/openssl-1.1.1k
  + using system zlib library

  nginx path prefix: "/home/admin/nginx-1.20.1"
  nginx binary file: "/home/admin/nginx-1.20.1/sbin/nginx"
  nginx modules path: "/home/admin/nginx-1.20.1/modules"
  nginx configuration prefix: "/home/admin/nginx-1.20.1/conf"
  nginx configuration file: "/home/admin/nginx-1.20.1/conf/nginx.conf"
  nginx pid file: "/home/admin/etc/nginx/nginx.pid"
  nginx error log file: "/home/admin/logs/nginx/error.log"
  nginx http access log file: "/home/admin/nginx-1.20.1/logs/access.log"
  nginx http client request body temporary files: "client_body_temp"
  nginx http proxy temporary files: "proxy_temp"
  nginx http fastcgi temporary files: "fastcgi_temp"
  nginx http uwsgi temporary files: "uwsgi_temp"
  nginx http scgi temporary files: "scgi_temp"
```

## make && make install

