---
date: 2026-02-12T12:00:00+08:00
title: Servlet
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

# Servlet

基本概念：

* Server Applet 的简称，是服务端运行的程序，可交互式的处理客户端发送到服务端的请求，完成操作并响应。
* 使用动态网页技术（JSP）。
* 是 javaweb 的开发基础，javaEE 的一个组成部分。

动态网页技术：

* 接收客户端请求，完成响应；
* 动态生成网页（页面数据可变）；
* 将包含结果的动态网页响应给客户端。

# Web 服务器

开源：

* Tomcat（主流）
* jetty（淘宝开源，运行效率比 Tomcat 高）
* resin（新浪开源，运行效率最高的）

商用：

* WebLogic（Oracle）
* WebSphere（IBM）

一般学习过程中，选用 Tomcat。

# Tomcat 配置

https://www.bilibili.com/video/BV1Ga4y1Y7Ah

Tomcat 9

* WEB-INF 文件夹，用于存放核心内容，无法被直接访问
  * classes：存放 *.class 文件
  * lib：存放依赖包
  * web.xml：存放项目配置文件
* HTML 文件
* JS 文件
* CSS 文件
* Static 文件

# Servlet 规范

目前最新发布的 servlet 规范为 4.0 版本。

https://jcp.org/en/jsr/detail?id=369

https://www.cnblogs.com/haimishasha/p/5609261.html



## web.xml

# Maven 依赖

```xml
<!-- Tomcat 9 依赖 -->
<dependency>
    <groupId>javax.servlet</groupId>
    <artifactId>servlet-api</artifactId>
    <version></version>
</dependency>

<!-- Tomcat 10 依赖 -->

```

# Servlet 编写

## 方式一：实现 Servlet 接口

在 Servlet 中，最重要的就是 javax.servlet.Servlet 接口，Servlet 接口定义了在 Servlet 的生命周期中特定时间以及特定顺序被调用的方法。

所有的 servlet 都会直接或间接与该接口产生联系。

实现 Servlet 接口需要重写以下几个方法：

* init：创建方法
* service：主要的 servlet 实现方法
* destroy：销毁
* getServletConfig：获取 servlet 的配置信息
* getServletInfo：获取 servlet 的基本信息

```java
public class Servlet01 implements Servlet {

    @Override
    public void init(ServletConfig config) throws ServletException {
    }

    @Override
    public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
    }

    @Override
    public ServletConfig getServletConfig() {
        return null;
    }

    @Override
    public String getServletInfo() {
        return null;
    }

    @Override
    public void destroy() {
    }

}
```

## 方式二：继承 GenericServlet 抽象类

javax.servlet.GenericServlet 抽象类中简单实现了 Servlet 接口中的一些方法，继承它之后必须重写 service 抽象方法。

```java
public class Servlet02 extends GenericServlet {

    @Override
    public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
        System.out.println("继承 GenericServlet，仅需要重写 service 方法");
    }

}
```

## 方式三：重写 HttpServlet 类

javax.servlet.http.HttpServlet 抽象类继承了 GenericServlet 抽象类，处理遵循 HTTP 协议的 servlet 请求与响应，并且遵循 HTTP 协议中的各种请求类型。

使用时，仅需重写涉及到的方法，例如：doGet doPost

```java
public class Servlet03 extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        super.doGet(req, resp);
    }

    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        doGet(req, resp);
    }

}
```



# 遇到过的问题

### The superclass javax.servlet.http.HttpServlet was not found on the Java Build Path

我们在用Eclipse进行Java web开发时，可能会出现这样的错误：The superclass javax.servlet.http.HttpServlet was not found on the Java Build Path。我们该怎么解决这个问题呢？

[java错误：The superclass "javax.servlet.http.HttpServlet" was not found on the Java Bu - 穆晟铭 - 博客园 (cnblogs.com)](https://www.cnblogs.com/achengmu/p/8082457.html)



