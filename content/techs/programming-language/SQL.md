---
date: 2026-02-12T12:00:00+08:00
title: SQL
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

# SQL (sequel)

## 参考资料

[数据库系统概论（第5版）.pdf]()

[A First Course in Database Systems 3rd, 中文翻译.pdf]()

[postgresql sql-commands](https://www.postgresql.org/docs/18/sql-commands.html)

[hive language manual](https://hive.apache.org/docs/latest/language/languagemanual/)


## 基本概念


### 数据库管理系统 Database Management system, DBMS

数据库管理系统是一个能有效建立和维护大量数据的强大工具，并且能安全地长期保存这些数据。

数据库管理系统是位于用户和操作系统之间的一层数据管理软件。它的主要功能包括：

1. 提供数据定义语言（Data Definition Language, DDL），用户可以使用它定义数据库中的数据对象的组成和结构。

2. 提供数据操纵语言（Data Manipulation Language, DML），用户可以使用它操纵数据库中的数据对象。

3. 分类组织、存储和管理各种数据。

4. 具有持久性，在面对各种故障、错误时，数据库的恢复能够保证数据的一致性。

5. 控制多个用户对数据的同时存取，不允许一个用户的操作影响另一个用户（独立性 isolation），也不允许对数据的不完整操作（原子性 atomicity）


事务：

正确实现的事务通常应满足以下“ACID性质”：

* A, atomicity 表示“原子性”，事务的操作要么全部被执行，要么全部不被执行。

* I, isolation 表示“独立性”，每个事务必须如同没有其他事务在同时执行一样被执行。

* D, durability 表示“持久性”，一旦事务已经完成，则该事务对数据库的影响就永远不会丢失。

* C, consistency 表示“一致性”。事务能保持数据库的一致性，保持所有预定义的规则和约束。


### 数据模型 Data Model

数据模型是对现实世界数据特征的抽象，可以划分为两个层次：概念模型、逻辑模型和物理模型。

主要的逻辑模型包括：

* 层次模型 hierarchical model
  层次模型和网状模型统称为格式化模型。
  层次模型是最早出现的数据模型，数据组织成清晰的树形结构，接近于文件系统按层次存放数据。
  层次模型的主要问题是显示世界中很多联系是非层次性的，不适合用层次模型表示。

* 网状模型 network model
  网状模型的相较于层次模型有一定扩展，允许一个节点有多个父节点，形成网状结构，能够更直接的描述现实世界。
  网状模型的主要问题是结构比较复杂，不易于管理和掌握。

* 关系模型 relational model
  关系模型是一种基于关系（二维表）的数据模型，它易于管理和使用。
  关系模型的主要问题是查询效率不如格式化模型，需要 DBMS 对用户的数据库操作请求进行优化。

* 面向对象模型 object oriented data model
  面向对象模型和面向对象程序设计方法结合，按照对象存储数据。

* 对象关系模型 object relational data model
  对象关系模型是关系模型和面向对象模型的结合，同时支持关系型数据管理和面向对象型数据。

* 半结构化数据模型 semistrucure data model
  数据具有一定的结构，但模式信息不固定或与数据本身混合存储，例如 XML、RDF、JSON、JPG、WAV 等。

这些数据模型中最常用的是关系模型，也就是关系型数据库。


### 数据库 Database, DB

本质上讲，数据库就是信息的集合。

在应用层面，一个数据库管理系统 DBMS 可以创建和管理多个独立的数据库 database。


### 数据表

数据表是数据逻辑组织的核心结构，是数据库中用于表示实体集及其属性的二维逻辑结构，由记录（行）和字段（列）构成，每张表定义一种实体（如“客户信息”）或一个事件（如“交易流水”）的数据格式。


### SQL

SQL, Structured Query Language，结构化查询语言，是关系数据库系统的标准查询语言。最新的标准是 SQL-99。

深入了解可以参考：

[SQL-99 Complete, Really](https://sql-99.readthedocs.io/en/latest/index.html)

[ISO/IEC 9075 Information technology — Database languages SQL]()


### 常见的数据库

常见的关系型数据库：Mysql、Postgresql、Oracle、Hadoop + Hive 等

常见的非关系型数据库：Redis、MongoDB、HBase、ClickHouse 等


## SQL 编写顺序

虽然 DBMS 不同，但是 SQL 的编写遵循一定的规范。

```sql
WITH <temp_table_name> AS (
    ...                                     --定义临时表
)
SELECT [DISTINCT] <column_name> AS <alias>  --查询列
FROM <table_name>                           --查询表
JOIN <table_name> ON <expression>           --关联表和关联条件
WHERE <expression>                          --查询条件
GROUP BY <colum_name>                       --分组列
HAVING <expression>                         --分组过滤条件
ORDER BY <column_name> [ASC|DESC]           --排序列
LIMIT <row_number>                          --限制返回的记录数或对结果进行分页
UNION
<select_statement>                          --聚合多个查询结果
```

这样一条语句可以处理绝大多数的日常数据查询。

## SQL 表达式

| 类型 | 用途 | 运算符 |
| :-- | :-- | :-- |
| 1. 一元表达式 | 元素选择 | `.` |
| 1. 关系表达式 | 条件筛选 | `=`, `>`, `<`, `>=`, `<=`, `!=` 或 `<>` <br> `LIKE`, `REGEXP`(正则表达式) |
| 2. 算术表达式 | 数值计算 | `+`, `-`, `*`, `/`, `%` (取模), `DIV`(取余), `&`, `^`(位运算) |
| 3. 逻辑表达式 | 多条件组合判断 | `AND`, `OR`, `NOT` <br> `IN (...)`, `BETWEEN ... AND ...` <br> `IS NULL`, `IS NOT NULL`, `IS TRUE/FALSE`, `IS NOT TRUE/FALSE` <br> `CASE ... WHEN ... THEN ... END` |


## SQL 逻辑执行顺序

不同的数据库系统在 SQL 的优化上有差异，但在逻辑执行顺序大致沿用了相同的设计思路。

```
 1. FROM 和 JOIN：定位数据源，确定从哪些表中检索数据
 2. ON：按连接条件筛选
 3. JOIN：执行连接操作
 4. WHERE：行级过滤
 5. GROUP BY：数据分组
 6. HAVING：组级过滤
 7. SELECT：选择输出的列并计算表达式
 8. DISTINCT：去重
 9. ORDER BY：排序
10. LIMIT/OFFSET：限制返回的记录数或对结果进行分页
```

## SQL 连接查询的笛卡尔积

在多表查询的连接查询（join）中，存在笛卡尔积运算，因此需要谨慎考虑 SQL 的编写条件。

以下举例说明：

假设存在两张表 $X(A, B) 和 $Y(B, C, D)$，经过笛卡尔积运算后的结果 $X \times Y(A, X.B, Y.B, C, D)$ 数据如下：

{{% columns ratio="1:4:8"%}}
- $X(A, B)$
  | A | B |
  |:-:|:-:|
  | 1 | 2 |
  | 3 | 4 |

- $Y(B, C, D)$
  | B | C | D |
  |:-:|:-:|:-:|
  | 2 | 5 | 6 |
  | 4 | 7 | 8 |
  | 9 | 10| 11|

- $X \times Y(A, X.B, Y.B, C, D)$
  | B |X.B|Y.B| C | D |
  |:-:|:-:|:-:|:-:|:-:|
  | 1 | 2 | 2 | 5 | 6 |
  | 1 | 2 | 4 | 7 | 8 |
  | 1 | 2 | 9 | 10| 11|
  | 3 | 4 | 2 | 5 | 6 |
  | 3 | 4 | 4 | 7 | 8 |
  | 3 | 4 | 9 | 10| 11|
{{% /columns %}}

在执行 join 条件 $X.B = Y.B$ 后，可以找到所需要的 2 条数据。

这个例子可以说明：
> [!note]
> 1. 连接查询消耗的系统资源相对较大，系统资源消耗会根据基础表的数据量成倍提升。
> 
> 2. 连接查询需要谨慎确定查询条件，否则会导致错误的查询结果。


三种连接操作：本质上取决于以哪张表为“全集”，以及是否要求两边都必须有匹配记录。

1. 左连接 left join：以左表为完整数据，去查看右表的附加情况。最常使用。
2. 内连接 inner join：查看两张表中都有的记录。其次使用。
3. 右连接 right join：和左连接相反。基本不用。


## 数据格式

参考 hive，列出了日常使用频率较高的数据格式。

### 数字类型 Numeric Types

| 类型 | 描述 |
| --- | --- |
| `TINYINT` | 1 byte 有符号整数，范围 -128 到 127 |
| `SMALLINT` | 2 byte 有符号整数，范围 -32,768 到 32,767 |
| `INT` / `INTEGER` | 4 byte 有符号整数，范围-2,147,483,648 到 2,147,483,647 |
| `BIGINT` | 8 byte 有符号整数 |
| `FLOAT` | 4 byte 单精度浮点数，1 位符号位，8位指数位，23位尾数位 |
| `DOUBLE` | 8 byte 双精度浮点数, 1 位符号位，11位指数位，52位尾数位 |
| `DOUBLE PRECISION` | 同 `DOUBLE` |
| `DECIMAL` | 38 位精度十进制数 |
| `NUMERIC` | 同 `DECIMAL` |


### 日期/时间类型 Date/Time Types

| 类型 | 描述 |
| --- | --- |
| `TIMESTAMP` | 时间戳类型，存储为相对于 UNIX 纪元（1970-01-01 00:00:00 UTC）的偏移量，默认是秒数，可以指定为毫秒，不带时区的信息 <br> 符合 JDBC 规范的 java.sql.Timestamp 格式，即 "YYYY-MM-DD HH:MM:SS.fffffffff"（9位小数精度）可以转换为时间戳 |
| `DATE` | 日期类型，基本格式 YYYY-­MM-­DD |
| `INTERVAL` | 时间间隔类型，基本格式 INTERNAL n SECOND/MINUTE/DAY/MONTH/YEAR，其他用法参考官方文档 |


### 字符串类型 String Types

| 类型 | 描述 |
| --- | --- |
| `STRING` | 字符串 |
| `VARCHAR` | 变长字符串 |
| `CHAR` | 字符 |


### 其他类型 Misc Types

| 类型 | 描述 |
| --- | --- |
| `BOOLEAN` | 布尔类型 (TRUE/FALSE) |
| `BINARY` | 变长二进制字节类型，查询时通常显示为十六进制 |


### 复杂类型 Complex Types

| 类型 | 描述 |
| --- | --- |
| `ARRAY<data_type>` | 数组，相同类型元素组成 |
| `MAP<primitive_type, data_type>` | 键值对集合 |
| `STRUCT<col_name : data_type [COMMENT col_comment], ...>` | 可包含不同数据类型的字段集合 |
| `UNIONTYPE<data_type, data_type, ...>` | 联合类型，不同数据类型组成 |


## 函数

参考 hive，列出了日常使用频率较高的函数。


### 聚合函数 Aggregate Functions

```
count()
sum()
avg()
max()
min()
```


### 字符串函数 String Functions

```
length(string str) -> int: 获取字符串长度
concat(string str1, string str2, ...) -> string: 拼接字符串
concat_ws(string SEP, string str1, string str2...) -> string: 使用分隔符 SEP 拼接字符串
substr(string str, int start, int len) -> string: 字符串 str 第 start 位开始截取 len 位。len 省略时截取到末尾
split(string str, string SEP) -> array: 按照分隔符 SEP 分割字符串 str，返回列表，使用 array[index] 的方式获取数据
replace(string str, string OLD, string NEW) -> string：将字符串 str 中的字符串 OLD 替换为 NEW 
repeat(string str, int n) -> string: 重复 str n 次
lpad(string str, int len, string pad) -> string: 字符串 str 左填充 pad 字符直到 len 长度
upper(string str) -> string: 变为大写
lower(string str) -> string: 变为小写
trim(string str) -> string: 去除两侧空格
ltrim(string str) -> string: 去除左侧空格
--------------------------------------------------------------------------------
mask(string str, string upper, string lower, string number) -> string: 对字符串 str 进行脱敏处理。脱敏规则是 upper 默认为 X，lower 默认为 x，number 默认为 #，均可省略。
mask_first_n(string str, int n) -> string: 对字符串 str 前 n 个字符进行脱敏处理。脱敏规则同上。
mask_last_n(string str, int n) -> string: 对字符串 str 后 n 个字符进行脱敏处理。脱敏规则同上。
mask_show_first_n(string str, int n) -> string: 对字符串 str 脱敏后显示前 n 个字符。脱敏规则同上。
mask_show_last_n(string str, int n) -> string: 对字符串 str 脱敏后显示后 n 个字符。脱敏规则同上。
--------------------------------------------------------------------------------
get_json_object(string json_string, string path) -> string: 从 json 字符串数据中获取指定的 key 。
--------------------------------------------------------------------------------
ascii(string str) -> int: 获取字符的 ascii 码
base64(binary bin) -> string: 获取字符串的 base64 加密
```

### 正则表达式

```
regexp_extract(string str, string pattern, int index) -> string: 按正则表达式抽取。从 str 中按正则表达式 pattern 抽取第 index 个数据
regexp_replace(string str, string pattern, string replace_str) -> string: 按正则表达式替换。将 str 中符合正则表达式 pattern 的字符串替换为 replace_str
```

正则表达式：
同 java 正则语法。


### 日期函数

```
now() -> string: 返回当前 unix 时间
unix_timestamp() -> bigint: 返回当前时间所在的 unix 时间戳
unix_timestamp(string date) -> bigint: 返回日期 date 所在的 unix 时间戳
unix_timestamp(string date, string pattern) -> bigint: 返回日期 date 所在的 unix 时间戳，根据匹配模式 parttern 识别 date 格式
from_unixtime(bigint unix_timestamp, string pattern) -> string: 从时间戳 unix_timestamp 获取当前时间。默认匹配模式是 yyyy-MM-dd HH:mm:ss，可省略。
to_date(string timestamp) -> date: 返回时间戳 timestamp 所在的日期 yyyy-MM-dd
--------------------------------------------------------------------------------
year(string date) -> int: 返回日期 date 的年份
quarter(string date) -> int: 返回日期 date 的季度
month(string date) -> int: 返回日期 date 的月份
day(string date) -> int: 返回日期 date 的日期
weekofyear(string date) -> int: 返回日期 date 的周数
hour(string date) -> int: 返回日期 date 的时间，要求 yyyy-MM-dd HH:mm:ss
mihute(string date) -> int: 返回日期 date 的分钟，要求 yyyy-MM-dd HH:mm:ss
second(string date) -> int: 返回日期 date 的秒，要求 yyyy-MM-dd HH:mm:ss
last_day(string date) -> string: 获取当前日期所在月份的最后一天
--------------------------------------------------------------------------------
date_add(string date, int n) -> string: 返回当前日期 date 加上 n 天的日期
date_sub(string date, int n) -> string: 返回当前日期 date 减去 n 天的日期
add_months(string date, int n, string pattern) -> string: 返回当前日期 date 加上 n 月的日期，可以选择匹配模式
--------------------------------------------------------------------------------
datediff(string enddate, string startdate) -> int: 计算 enddate - startdate 的天数，可以为负
months_between(string enddate, string startdate) -> int: 计算 enddate - startdate 的月数，可以为负
--------------------------------------------------------------------------------
date_format(string date/timestamp, string pattern) -> string: 返回日期 date/timestamp 按照匹配模式转换的日期
```

### 窗口函数

`row_number()` 窗口函数可以获取数据所在的行数

`lead()` 窗口函数可以获取当前行后第 N 行的数据。

```sql
--在不指定 offset 的情况下默认为 1
--在不指定 default 的情况下默认为 null
LEAD(return_value [,offset[, default ]]) OVER (
    PARTITION BY expr1, expr2,...
	ORDER BY expr1 [ASC | DESC], expr2,...
)
```

与 `lead` 函数相对的是 `lag` 函数，可以获取前第 N 行的数据。

`first_value` 函数和 `last_value` 函数的用法相似，可以获取当前行第一个或最后一个出现的数据。


### 表生成函数 Table-Generating Functions

`explode(array a)` takes in an array (or a map) as an input and outputs the elements of the array (map) as separate rows. UDTFs can be used in the SELECT expression list and as a part of LATERAL VIEW.

`posexplode(array a)` is similar to explode but instead of just returning the elements of the array it returns the element as well as its position in the original array.


## 示例

```sql
SELECT
    user_name,
    user_level,
    SUM(order_amount) AS total_consumption, -- 算术+聚合表达式：计算总和
    CASE -- 逻辑表达式：数据打标，增加可读性
        WHEN SUM(order_amount) > 10000 THEN '高价值'
        ELSE '一般价值'
    END AS value_segment
FROM orders
WHERE
    order_date >= '2024-01-01' -- 比较表达式：时间筛选
    AND order_date <= '2024-03-31'
    AND user_level IN ('白金', '钻石') -- 逻辑表达式：多值匹配
    AND user_id IS NOT NULL -- 小心 NULL 值
GROUP BY user_name, user_level -- 分组维度
HAVING SUM(order_amount) > 5000 -- 聚合表达式：对汇总结果筛选
ORDER BY total_consumption DESC; -- 排序
```

```sql
SELECT get_json_object(src_json.json, '$.owner') FROM src_json;
SELECT get_json_object(src_json.json, '$.store.fruit\[0]') FROM src_json;
```

