# 简介

[mybatis – MyBatis 3 | 简介](https://mybatis.org/mybatis-3/zh/index.html#)

MyBatis 最初是 Apache 的一个开源项目 iBatis，2010 年这个项目由 apache software foundation 迁移到了 google code，并且改名为 MyBatis。2013年11月迁移到 Github。

Mybatis 封装了 JDBC，是一个持久层框架，包括 SQL Maps 和 Data Access Objects（DAO）。

Mybatis 特性：

* 支持定制化 sql、存储过程以及高级映射的持久层框架
* 避免了几乎所有的 jdbc 代码和手动设置参数及获取结果集
* 使用简单的 XML（多数情况下）或注解用于配置和原始映射，将接口和 pojo （Plain Old Java Objects，普通的 java 对象）映射为数据库中的记录
* 是一个半自动的 ORM（Object Relation Mapping，对象关系映射）框架

ORM：

* Object：java 中的实体类对象
* Relation：关系型数据库
* Mapping：二者之间的映射关系

| Java 概念 | 数据库概念 |
| --------- | ---------- |
| 类        | 表         |
| 属性      | 字段/列    |
| 对象      | 记录/行    |



# Mybatis 和其他持久化技术

## JDBC

缺陷：

* sql 语句包含在 java 程序中，硬编码，不易维护，不可扩展
* 代码冗长，开发效率低

优势：

* 便于学习和理解持久化基础

## Hibernate 和 JPA

优势：

* 操作简便，开发效率高

缺陷：

* 复杂 SQL 需要绕过框架执行
* 框架自动生成 SQL，难以进行特殊优化
* 基于全映射自动化框架，大量字段的 POJO 映射时比较困难
* 反射操作太多，性能下降

## Mybatis

* 轻量级，性能出色
* sql 和 java 编码分开，易于维护和扩展
* 开发效率相较 Hibernate 低，需要自行编写 sql 语句，但完全可以接受

# mybatis-config.xml 配置文件

```xml-dtd
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!-- 属性配置。可以在 Java properties 文件中配置这些属性，也可以在 properties 元素的子元素中设置 -->
    <properties resource="">
        <property name="driver" value="com.mysql.cj.jdbc.Driver" />
        <property name="url" value="jdbc:mysql://39.106.225.99:3306/user" />
        <property name="username" value="root" />
        <property name="password" value="root" />
    </properties>

    <!--
        类型别名。可为 Java 类型设置一个缩写名字，它仅用于 XML 配置
        类型别名不区分大小写。
        Mybatis 默认配置了一些常用的类型别名，详情参考：https://mybatis.org/mybatis-3/zh/configuration.html#typeAliases
    -->
    <typeAliases>
        <!--
            为某个类设置类型别名，在 mapper.xml 文件中简写使用
            alias 属性可以不写，等价于 <typeAlias type="com.ckl.sqlinj.dao.pojo.User" />
        -->
        <typeAlias alias="User" type="com.ckl.sqlinj.dao.pojo.User" />
        <!-- 以包为单位，设置类型别名 -->
        <package name="com.ckl.sqlinj.dao.pojo" />
    </typeAliases>

    <!-- 环境配置。可以配置多个环境，但只能使用其中一个具体环境 -->
    <environments default="development">
        <environment id="development">
            <!--
                事务管理方式：type="JDBC|MANAGED"
                JDBC：原生的事务管理方式，事务的提交或回滚需要手动处理。
                MANAGED：被管理，例如Spring。
             -->
            <transactionManager type="JDBC" />
            <!--
                数据源：type="POOLED|UNPOOLED|JNDI"
                POOLED：使用数据库连接池缓存数据库连接。
                UNPOOLED：不使用数据库连接池。
                JNDI：使用上下文中的数据源。
             -->
            <dataSource type="POOLED">
                <property name="driver" value="${driver}" />
                <property name="url" value="${url}" />
                <property name="username" value="${username}" />
                <property name="password" value="${password}" />
            </dataSource>
        </environment>
    </environments>
    <!-- 映射文件配置 -->
    <mappers>
        <!-- 引入单个映射文件 -->
        <mapper resource="mapper/UserMapper.xml" />
        <!--
            按包引入映射文件，两个条件：
            1、mapper 接口所在的包要和映射文件所在的包保持一致
            2、mapper 接口的名字要和映射文件的名字保持一致
        -->
        <!-- <package name="com.ckl.sqlinj.dao.mapper" /> -->
    </mappers>
</configuration>
```

# 创建 mapper 接口

mybatis 的 mapper 接口相当于以前的 dao，区别在于：mapper 仅提供接口，不需要提供实现类。

```java
package com.ckl.sqlinj.dao.mapper;

public interface UserMapper {
    /**
     * 创建用户信息
     * @return
     */
    int insertUser();
}
```



# 创建 mapper.xml 映射文件

要保证两个一致：

* 映射文件中的 namespace 要和 mapper 接口的全类名保持一致
* 映射文件中的 sql 语句的 id 要和 mapper 接口中的方法名保持一致

```xml-dtd
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.ckl.sqlinj.dao.mapper.UserMapper">
    <select id="selectById" resultType="User">
        select * from tb_user where id = #{id}
    </select>
</mapper>
```

# mybatis 获取参数的两种方式

## 基本概念

mybatis 获取参数的两种方式 `#{}` 和 `${}`

* `#{}` 的本质是占位符赋值
* `${}` 的本质是字符串拼接，若为字符串类型或日期类型的字段进行赋值时，需要手动添加单引号

## 单个字面量类型的参数

在 mybatis xml 配置中（或注解中），单个参数传参时和名称无关，以下配置仍然可生效：

```java
    User selectById(int id);
```

```xml
    <select id="selectById" resultType="User">
        select * from tb_user where id = #{id}
    </select>
    <!-- 等同于 -->
    <select id="selectById" resultType="User">
        select * from tb_user where id = #{aaa}
    </select>
```

## 多个字面量类型的参数

在 mybatis xml 配置中（或注解中），多个参数传参时和名称有关：

只可以使用变量名，或者 param1 - paramN 的方式，原因是：mybatis 将参数放在了一个 map 集合

```java
    User checkLogin(String username, String password);
```

```xml
    <select id="checkLogin" resultType="User">
        select id, username, password from tb_user where username = #{username} and password = #{password}
    </select>
    <!-- 等同于 -->
    <select id="checkLogin" resultType="User">
        select id, username, password from tb_user where username = #{param1} and password = #{param2}
    </select>
```

## map 集合类型的参数

由于 mybatis 将参数放在了一个 map 集合，因此可以手动构造集合：

此方法一般不使用。

```java
    User checkLogin(Map<String, Object> map);
```

```xml
    <select id="checkLogin" resultType="User">
        select id, username, password from tb_user where username = #{username} and password = #{password}
    </select>
```

```java
    Map<String, Object> map = new HashMap<>();
    map.put("username", "wangwu");
    map.put("password", "wangwu");
    User user = mapper.checkLogin3(map);
```

## 实体类类型的参数

mybatis 支持传递实体类对象参数

建议使用。

```java
    User checkLogin(User user);
```

```xml
    <select id="checkLogin" resultType="User">
        select id, username, password from tb_user where username = #{username} and password = #{password}
    </select>
```

```java
    User user = new User;
    user.setUsername("zhangsan");
    user.setPassword("zhangsan");
    User res = mapper.checkLogin(user);
```

## 使用 @param 命名参数

使用 @Param 参数，Spring 框架会将其生成 map 集合，自动以 param 参数为 key

建议使用。

```java
    User checkLogin(@Param("Username") String username, @Param("password") String password);
```

```xml
    <select id="checkLogin" resultType="User">
        select id, username, password from tb_user where username = #{username} and password = #{password}
    </select>
```

# mybatis 的查询功能

## 查询一个实体类对象

仅允许查询出 null 或一条数据，如果为多条，或抛出异常。

```java
    User selectById(@Param("id") Integer id);
```

```xml
    <select id="selectById" resultType="User">
        select * from tb_user where id = #{id}
    </select>
```

## 查询一个 list 集合

使用 List 集合，允许查询出 null 或多条数据。

```java
    List<User> selectAllById(@Param("id") Integer id);
```

```xml
    <select id="selectAllById" resultType="User">
        select * from tb_user where id = #{id}
    </select>
```

## 查询单个数据

```java
    Integer getCount();
```

```xml
    <select id="getCount" resultType="Integer">
        select count(*) from tb_user
    </select>
```

## 查询一条数据为 map 集合

仅允许查询出 null 或一条数据，如果为多条，或抛出异常。

key 为数据库字段名，value 为字段值，null 不赋值。

```java
    Map<String, Object> getUserByIdToMap(@Param("id") Integer id);
```

```xml
    <select id="getUserByIdToMap" resultType="Map">
        select * from tb_user where id = #{id}
    </select>
```

## 查询多条数据为 map 集合

使用 List 集合，允许查询出 null 或多条数据。

```java
    List<Map<String, Object>> getUserByUsernameToMap(@Param("username") String username);
    // 或者使用 @Mapkey 注解，使用查询结果中的唯一值，手动设置集合的 key
    @Mapkey("id")
    Map<String, Object> getUserByUsernameToMap(@Param("username") String username);
```

```xml
    <select id="getUserByUsernameToMap" resultType="Map">
        select * from tb_user where username = #{username}
    </select>
```

# mybaits 特殊 sql 的执行

## 模糊查询

```xml
    <!-- 方案一，使用 ${} 拼接，有 SQL 注入风险 -->
    <select id="selectAllByUsername" resultType="Map">
        select * from tb_user where username like '%${username}%'
    </select>
    <!-- 方案二，使用 concat 拼接 -->
    <select id="selectAllByUsername" resultType="Map">
        select * from tb_user where username like concat('%',#{username},'%')
    </select>
    <!-- 方案三，使用 "" 拼接，建议 -->
    <select id="selectAllByUsername" resultType="Map">
        select * from tb_user where username like "%"#{username}"%"
    </select>
```

## 批量删除

```xml
    <!--
        方案一，使用 ${} 拼接
        delete from tb_user where username in ("zhangsan", "lisi", "wangwu")
     -->
    <select id="deleteAllByUsername" resultType="Integer">
        delete from tb_user where username in {${username}}
    </select>
    <!-- 方案二，使用 foreach 拼接 -->
```

## 动态设置表名

查询指定表的数据

```xml
    <!-- 方案一，使用 ${} 拼接，有 SQL 注入风险 -->
    <select id="selectByTableName" resultType="Map">
        select * from ${tableName}
    </select>
```

## 获取自增的主键

```java
    void insertUser(User user);
```

```xml
    <!--
        useGeneratedKeys: 设置标签中使用了自增主键
        keyProperty: 将自增的主键，传输到映射文件中，参数的某个属性中
    -->
    <insert id="insertUser" useGeneratedKeys="true" keyProperty="id">
        insert into tb_user (id, username, password) values (null, #{username}, #{password})
    </insert>
```

# 自定义 resultType 映射

# mybatis 动态 sql

动态 sql 主要是为了拼接一些关键字

## if 标签

通过 if 标签，判断标签中内容的执行

if 标签的判断条件成立时，会按顺序拼接到主 sql 语句之后。

```xml
    <select id="selectUser" resultType="Map">
        select * from tb_user where username = #{username}
        <if test="password != null and password!= ''">
            and password = #{password}
        </if>
        <if test="age != null and age!= ''">
            and age = #{age}
        </if>
    </select>
```

## where 标签

通过 where 标签，自动生成 where 关键字，同时将条件语句之前多余的 and、or 等去掉；或者在 if 条件都不满足时，自动删去多余的 where 关键字。

```xml
    <select id="selectUser" resultType="Map">
        select * from tb_user
        <where>
            <if test="username != null and username!= ''">
                and username = #{username}
            </if>            
            <if test="password != null and password!= ''">
                and password = #{password}
            </if>
            <if test="age != null and age!= ''">
                and age = #{age}
            </if>
        </where>
    </select>
```

## trim 标签

通过 trim 标签，可以实现前后缀的重写

* prefix | suffix：在 trim 标签内，前后缀添加内容
* prefixOverrides | suffixOverrides：在 trim 标签内，前后缀重写内容

```xml
    <select id="selectUser" resultType="Map">
        select * from tb_user
        <trim prefix="where" suffixOverrides="and|or">
            <if test="username != null and username!= ''">
                username = #{username} and
            </if>            
            <if test="password != null and password!= ''">
                password = #{password} or
            </if>
            <if test="age != null and age!= ''">
                age = #{age} or
            </if>
        </trim>
    </select>
```

## choose, when, otherwise 标签

相当于 java 中的 switch ... case ... default ...

按顺序判断，当有一个条件满足时，只会执行一个条件

```xml
    <select id="selectUser" resultType="Map">
        select * from tb_user
        <where>
            <choose>
                <when test="username != null and username!= ''">
                    username = #{username}
                </when>
                <when test="password != null and password!= ''">
                    password = #{password}
                </when>
                <when age="age != null and age!= ''">
                    age = #{age}
                </when>
                <otherwise>
                    id = 1
                </otherwise>
            </choose>
        </where>
    </select>
```

## foreach 标签

批量删除

```xml
    <delete id="deleteUser">
        delete tb_user where id in 
        (
        <foreach collection="ids" item="id" seperator=",">
            #{id}
        </foreach>
        )
    </delete>
    <delete id="deleteUser">
        delete tb_user where id 
        <foreach collection="ids" item="id" seperator="or">
            id = #{id}
        </foreach>
    </delete>
```

批量添加

```xml
    <insert id="insertUser">
        insert into tb_user values
        <foreach collection="users" item="user" seperator=",">
            (null, #{user.username}, #{user.password})
        </foreach>
    </insert>
```

## sql, include 标签

设置 sql 片段，直接引入 sql 内容

```xml
    <sql id="tb_user">id, username, password</sql>
    <select id="selectUserById" resultType="User">
        select <include refid="tb_user"></include> from tb_user where id = #{id}
    </select>
```

# 复杂问题：

## mybatis 动态表名、字段名防 SQL 注入

三种解决方案：

* 数据库用户权限控制
* java 编写 sql 解析器，对字段进行控制
* mapper.xml 动态表名、列名拼接

### 方案一：数据库用户权限控制

```mysql
CREATE USER 'test'@'%' IDENTIFIED BY 'test';
GRANT select ON user.tb_user TO 'test'@'%';
flush privileges;

select * from tb_user; -- 正常查询
insert into tb_user (`username`, `password`) values ("zhangsan", "123456"); -- 数据库报错，无权限
select * from tb_acct; -- 数据库报错，无权限
```

### 方案二：java 编写 sql 解析器，手动控制



表名、列名只能使用 `${}` ，因此会导致 sql 注入问题

[mybatis动态表名，列名_红烧鱼i的博客-CSDN博客_mybatis动态表名](https://blog.csdn.net/q1424966670/article/details/120331156)

mybatis动态表名防注入



Apache Calcite SQL 解析工具

## 方案三：mapper.xml 动态
