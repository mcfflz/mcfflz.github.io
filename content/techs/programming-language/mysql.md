# mysql 安装

## windows community版本 zip安装

1. community下载地址

   ```markdown
   https://dev.mysql.com/downloads/mysql/

2. 解压mysql到 D:\DevEnv\mysql-8.0.25

3. 在解压目录下，新建my.ini，添加配置

   ```ini
   [mysql]
   # 设置mysql客户端默认字符集
   default-character-set=utf8mb4 
   
   [mysqld]
   # 设置mysql服务端默认监听的端口
   port=3306
   
   # set basedir to your installation path
   basedir=D:/DevEnv/mysql-8.0.25
   # set datadir to the location of your data directory
   datadir=D:/DevEnv/mysql-data
   
   # 设置mysql服务端默认字符集
   character-set-server=utf8mb4
   collation-server=utf8mb4_unicode_ci 
   
   # 创建新表时将使用的默认存储引擎
   default-storage-engine=INNODB
   
   # 允许最大连接数
   max_connections=200
   ```

4. 理解 mysql client 和 mysql server

   ```markdown
   客户 --> mysql client --> mysql server --> 物理数据
   
   mysql client是指对外服务的客户端，生成管理数据库实例，数据库实例任务调度线程之类，并提供相关接口供不同客户端调用，增删改查命令等
   mysql server是运行的mysql服务，操作数据库实例的工具，从官网下载的mysql server默认包含了client客户端
   ```

5. 环境变量配置

   ```markdown
   配置：
   MYSQL_HOME: D:\DevEnv\mysql-8.0.25
   PATH: %MYSQL_HOME%\bin
   ```

6. mysql初始化，管理员权限cmd

   ```markdown
   # 移除mysql server
   mysqld --remove servername
   
   # 初始化mysql server
   mysqld --initialize
   
   # 安装mysql server
   mysqld --install servername
   默认数据库服务名为: mysql
   
   # 启动mysql server
   # windows环境需要管理员权限
   net start servername
   
   # 连接mysql server
   mysql -u username -p
   password储存在临时密码为mysql data路径下的machinename.err文件内，在初始化时生成
   初始化用户名为root
   ```

7. 修改root用户密码

   ```sql
   # 修改密码
   ALTER user 'root'@'localhost' IDENTIFIED BY 'password';
   
   # Psbc@123456
   ```

## ubuntu linux community 版本 generic binaries 安装

1. generic 下载并解压

   ```bash
   tar -xvf mysql-8.0.26-linux-glibc2.12-x86_64.tar.xz
   ```
   
2. my.cnf 配置

   ```toml
   [mysql]
   # 设置数据库默认字符集
   default-character-set=utf8mb4
   # 开启命令补全
   no-auto-rehash
   
   [client]
   # 设置mysql客户端默认字符集
   default-character-set=utf8mb4 
   # 设置客户端socket
   socket=/home/admin/etc/mysql/mysql.sock
   
   [mysqld]
   # 设置mysql服务端默认监听的端口
   port=3306
   
   # set basedir to your installation path
   basedir=/home/admin/mysql-8.0.26
   # set datadir to the location of your data directory
   datadir=/home/admin/data/mysql
   # 设置临时文件路径
   tmpdir=/home/admin/tmp/mysql
   # 设置pid-file
   pid-file=/home/admin/etc/mysql/mysql.pid
   # 设置服务端socket
   socket=/home/admin/etc/mysql/mysql.sock
   # 设置serverid，主从唯一表直
   server-id=1
   
   # 设置mysql服务端默认字符集
   character-set-server=utf8mb4
   collation-server=utf8mb4_unicode_ci 
   
   # 创建新表时将使用的默认存储引擎
   default-storage-engine=INNODB
   
   # 允许最大连接数
   max_connections=200
   
   # 设置mysql错误日志路径
   log-error=/home/admin/logs/mysql/error.log
   
   # 设置mysql一般日志路径
   general-log=1
   general-log-file=/home/admin/logs/mysql/mysql.log
   
   # 设置mysql二进制日志binlog
   log-bin=/home/admin/logs/mysql/binlog
   log-bin-index=/home/admin/logs/mysql/binlog/binlog.index
   binlog-ignore-db=mysql
   binlog-ignore-db=sys
   binlog-ignore-db=information_schema
   binlog-ignore-db=performance_schema
   max_binlog_size=100M
   binlog_cache_size=4M
   # sync_binlog=1000 # 当每进行n次事务提交之后，MySQL将进行一次fsync之类的磁盘同步指令来将binlog_cache中的数据强制写入磁盘
   
   # 设置mysql重做日志relaylog
   relay-log=/home/admin/logs/mysql/relaylog
   relay-log-index=/home/admin/logs/mysql/relaylog/relaylog.index
   ```

3. 初始化

   ```bash
   ./mysqld --defaults-file=/home/admin/etc/mysql/my.cnf --initialize --console --user=admin
   ./mysqld_safe --defaults-file=/home/admin/etc/mysql/my.cnf --user=admin &
   
   vi /home/admin/logs/mysql/error.log
   
   ldd mysql
   libtinfo.so.5 => not found
   ln -s /usr/lib/x86_64-linux-gnu/libtinfo.so.6.2 /usr/lib/libtinfo.so.5
   
   ln -s /home/admin/etc/mysql/mysql.sock /tmp/mysql.sock
   
   
   ./mysql -u root -p
   
   ./mysqladmin -u root -p shutdown 
   ```

4. 建立环境变量

   ```shell
   MYSQL_HOME=/home/admin/mysql-8.0.26
   PATH=$PATH:$MYSQL_HOME/bin
   ```

5. 重置root用户密码

   ```sql
   alter user 'root'@'localhost' identified by 'Psbc@123456';
   ```

# mysql 连接数据库服务

```bash
mysql -u username -ppassword
# 在 -p 和 password 中带空格，是连接到数据库服务中的某个库
# mysql -u username -p database
```

#  mysql 用户管理

## 查看用户

```sql
select * from mysql.user;
select distinct concat('User: [', user, '''@''', host, '];') AS user_host from mysql.user;
```

## 创建用户

```sql
CREATE USER 'username'@'host' IDENTIFIED BY 'password';

# 说明：
-- username：创建的用户名
-- host：指定该用户在哪个主机上可以登陆，如果是本地用户可用localhost，如果想让该用户可以从任意远程主机登陆，可以使用通配符%
-- password：该用户的登陆密码，密码可以为空，如果为空则该用户可以不需要密码登陆服务器
-- 新建的用户，默认是没有任何权限的
# 举例：
CREATE USER 'dog'@'localhost' IDENTIFIED BY '123456';
CREATE USER 'pig'@'192.168.1.101' IDENDIFIED BY '123456';
CREATE USER 'pig'@'%' IDENTIFIED BY '123456';
CREATE USER 'pig'@'%' IDENTIFIED BY '';
CREATE USER 'pig'@'%'; 
```

## 修改用户密码

```mysql
# mysql 数据库 user 表中的密码是通过 password 函数进行加密的
update mysql.user set password = password('newpassword') where user = 'root' and host = 'localhost';
```

## 删除用户

```sql
DROP USER 'username'@'host';
```

## 分配用户权限

```sql
GRANT all privileges ON database_name.table_name TO 'username'@'host';
flush privileges;

# 说明：
-- databasename：用户的操作权限，如select，insert，update，delete，create，drop等，如果要授予所的权限则使用ALL
-- tablename：数据库名
-- username：表名，如果要授予该用户对所有数据库和表的相应操作权限则可用*表示，如*.*
-- host：指定该用户的主机

# 举例：
GRANT SELECT, INSERT ON test.user TO 'pig'@'%';
GRANT ALL ON *.* TO 'pig'@'%';
GRANT ALL ON maindataplus.* TO 'pig'@'%';
```

5. 授权用户给其他用户授权

    ```sql
    GRANT privileges ON database_name.table_name TO 'username'@'host' WITH GRANT OPTION;
    ```

6. 设置用户密码

    ```mysql
    ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';
    ```

7. 设置或更改用户密码

    ```sql
    SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
    ```

8. 取消用户授权

    ```sql
    REVOKE privilege ON database_name.table_name FROM 'username'@'host';
    ```

## 收回用户权限

```mysql
revoke ...
```

# mysql databases

## 查看数据库

```sql
SHOW DATABASES;
```

## 创建数据库

```sql
CREATE DATABASE database_name;
# 举例：
CREATE DATABASE IF NOT EXISTS database_name DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

## 删除数据库

```mysql
DROP DATABASE database_name;
```

## 选择数据库

```sql
# 选择数据库后，所有的sql操作默认在该库下，无需指定数据库
use database_name;

# 如果不选择数据库，所有的sql操作需要指定数据库
```

# information_schema 数据库

```mysql
# 记录了所有的数据库名
select schema_name from information_schema.schemata;

# 记录了所有的表名
select table_schema, table_name from information_schema.tables;

# 记录了所有的列名
select table_schema, table_name, column_name from information_schema.columns;
```

# mysql table

## 查看表

```sql
show tables;
```

## 描述表

```sql
desc table_name;
```

## 创建表

```mysql
create table if not exists `tb_user`(
`id` int unsigned auto_increment primary key COMMENT "用户编号",
`username` varchar(40) NOT NULL COMMENT "用户名",
`password` varchar(40) NOT NULL COMMENT "密码"
) comment = "用户表";

insert into tb_user (username,password) values ("admin","admin");
commit;
```



## 删除表

```mysql
drop table tableName;
```

## 查看 DDL 语句

```mysql
show create table tableName;
```

# mysql 使用



##  执行*.sql脚本

进入mysql命令行后，使用source命令

```sql
source filepath;
```

或者，使用\.

```sql
\. filepath;
```

## 创建表

```mysql
create table table_name (
    column_name_1 column_type_1 column_definition comment 'comment desc',
    column_name_2 column_type_2 column_definition comment 'comment desc',
    ...
    column_name_n column_type_n column_definition comment 'comment desc'
);

commit;

/*
    column_type包括：
    https://www.runoob.com/mysql/mysql-data-types.html
    数值
      -- TINYINT
      -- SMALLINT
      -- MEDIUMINT
      -- INT或INTEGER
      -- BIGINT
      -- FLOAT
      -- DOUBLE
      -- DECIMAL
    日期和时间
      -- DATE
      -- TIME
      -- YEAR
      -- DATETIME
      -- TIMESTAMP
    字符串
      -- CHAR
      -- VARCHAR
      -- TINYBLOB
      -- TINYTEXT
      -- BLOB
      -- TEXT
      -- MEDIUMBLOB
      -- MEDIUMTEXT
      -- LONGBLOB
      -- LONGTEXT

    column_definition包括
*/
```

## 查看表

```mysql
-- https://www.cnblogs.com/gide/p/6179975.html
-- 查看表结构
desc tablename;

-- 查看列注释
select * from information_schema.columns
where table_schema = 'databasename' and table_name = 'tablename';

-- 查看列名和注释
select column_name, column_comment from information_schema.columns
where table_schema ='databasename' and table_name = 'tablename';

-- 查看表注释
select table_name, table_comment from information_schema.tables
where table_schema = 'databasename' and table_name = 'tablename';

-- 查看表生成的DDL
show create table table_name;
```



## 查询语句

```mysql
select column_name from table_name;
select column_name1, column_name2 from table_name;
select * from table_name;
select column_name from table_name where ...;
```

## 修改语句

```mysql
update table_name set column_name = '';
update table_name set column_name = '' where ...;
```

## 插入语句

```mysql
# 插入一行，并为所有字段赋值
insert into table_name values(value1, value2, ...);
# 插入一行，并表内某些字段赋值
insert into table_name (column_name1, column_name2) values (value1, value2);
# 插入多行，并表内所有字段赋值
insert into table_name values(value11, value12, ...), (value21, value22, ...);
# 插入多行，并表内某些字段赋值
insert into table_name (column_name1, column_name2) values(value11, value12, ...), (value21, value22, ...);
```

## 删除语句

```mysql
delete from table_name where ...;
```



# mysql 遇到过的问题

## mysql 注释

```mysql
-- https://dev.mysql.com/doc/refman/8.0/en/comments.html
/*
From a # character to the end of the line.

From a --  sequence to the end of the line. In MySQL, the --  (double-dash) comment style requires the second dash to be followed by at least one whitespace or control character (such as a space, tab, newline, and so on). This syntax differs slightly from standard SQL comment syntax, as discussed in Section 1.7.2.4, “'--' as the Start of a Comment”.

在使用"--"来注释时，必须在第二个"-"后加入至少一个空白或控制字符（例如 空格 tab 换行 或其他），否则无法识别为注释。

From a /* sequence to the following */ sequence, as in the C programming language. This syntax enables a comment to extend over multiple lines because the beginning and closing sequences need not be on the same line.
*/
```

## mysql comment

```mysql
/*
在oracle和postgresql中，可以使用如下sql语句为表或字段添加注释
comment on table tablename is 'desc';
comment on column tablename.column_name is 'desc';

此语法在mysql中不支持
*/
```

## 查看 mysql 字符集

[查看三种MySQL字符集的方法-51CTO.COM](https://www.51cto.com/article/229171.html)

查看 mysql 数据库服务器和数据库字符集：

```mysql
show variables like '%char%';
```

查看MySQL数据表（table）的MySQL字符集：

```mysql
show table status from databaseName like 'tableName';
```

查看MySQL数据列（column）的MySQL字符集：

```mysql
show full columns from tableName;
```

## drop table 卡死

[mysql drop table的时候卡住了_jasonxty的博客-CSDN博客_drop table 卡死](https://blog.csdn.net/xtydtc/article/details/100741121)

在访问这个table的时候，出现了错误，但是没有 rollback，导致这个进程一直占用这个表格。当把这个进程 kill 掉之后就可以删除了。

```mysql
# 显示进程
show processlist;
# kill 进程id
kill 12;
```

