# Java EE 介绍

https://docs.oracle.com/javaee/7/index.html

Oracle 官方给出了两个教程：

* Your First Cup: An Introduction to the Java EE Platform
* The Java EE 7 Tutorial

## Your First Cup: An Introduction to the Java EE Platform

在第一个教程中，给出了对于 Java EE 的一个概述：

> https://docs.oracle.com/javaee/7/firstcup/java-ee001.htm
>
> As stated above, the Java EE platform is designed to help developers create large-scale, multi-tiered, scalable, reliable, and secure network applications.
>
> …
>
> Java EE application development concentrates on the middle tier to make enterprise application management easier, more robust, and more secure.

并且，通常将 Java EE 应用划分为独立的四层，每层主要使用的 Java EE 技术如下：

* The Client Tier：客户端层

* The Web Tier：web 层

  > The web tier consists of components that handle the interaction between clients and the business tier.

  web 层主要应用的 Java EE 技术包括：

  * JavaServer Faces technology
  * Expression Language
  * Servlets
  * Contexts and Dependency Injection for Java EE

* The Business Tier：业务层
  
  > The business tier consists of components that provide the business logic for an application.
  
  业务层主要应用的 Java EE 技术包括：
  
  * Enterprise JavaBeans (enterprise bean) components
  * JAX-RS RESTful web services
  * Java Persistence API entities
  
* The Enterprise Information Systems Tier：企业信息系统层（数据层）
  
  > The enterprise information systems (EIS) tier consists of database servers, enterprise resource planning systems, and other legacy data sources, like mainframes.
  
  数据层主要应用的 Java EE 技术包括：
  
  * The Java Database Connectivity API (JDBC)
  * The Java Persistence API
  * The Java EE Connector Architecture
  * The Java Transaction API (JTA)

https://docs.oracle.com/javaee/7/firstcup/java-ee002.htm

Java EE 服务器（Java EE server）

> A Java EE server is a server application that implements the Java EE platform APIs and provides standard Java EE services. Java EE servers are sometimes called application servers, because they allow you to serve application data to clients, much as web servers serve web pages to web browsers.
>
> Java EE servers host several application component types that correspond to the tiers in a multi-tiered application. The Java EE server provides services to these components in the form of a container.

Java EE 容器（Java EE containers）

> Java EE containers are the interface between the component and the lower-level functionality provided by the platform to support that component. The functionality of the container is defined by the platform and is different for each component type.

Web 容器（The web container）

> The web container is the interface between web components and the web server. A web component can be a servlet or a JavaServer Faces Facelets page. The container manages the component's lifecycle, dispatches requests to application components, and provides interfaces to context data, such as information about the current request.

EJB （企业 javabean）容器（The EJB container）

> The EJB container is the interface between enterprise beans, which provide the business logic in a Java EE application, and the Java EE server. The EJB container runs on the Java EE server and manages the execution of an application's enterprise beans.

应用客户端容器（The application client container）

> The application client container is the interface between Java EE application clients (special Java SE applications that use Java EE server components) and the Java EE server. The application client container runs on the client machine and is the gateway between the client application and the Java EE server components that the client uses.



## The Java EE 7 Tutorial

### 引言

在第二个教程中，同样给出了对于 Java EE 的一个概述：

> https://docs.oracle.com/javaee/7/tutorial/overview.htm
>
> Developers today increasingly recognize the need for distributed, transactional, and portable applications that leverage the speed, security, and reliability of server-side technology. **Enterprise applications** provide the business logic for an enterprise. They are centrally managed and often interact with other enterprise software. In the world of information technology, enterprise applications must be designed, built, and produced for less money, with greater speed, and with fewer resources.

企业级应用：必须以更少的资金、更快的速度和更少的资源来设计、构建和生产企业应用程序。

Java EE 涉及到的组织：

* Java Community Process (JCP)：

    > The Java EE platform is developed through the Java Community Process (JCP), which is responsible for all Java technologies.

* Java Specification Requests (JSRs)：

    > Expert groups composed of interested parties have created Java Specification Requests (JSRs) to define the various Java EE technologies. 

* Java Community：

    > The work of the Java Community under the JCP program helps to ensure Java technology's standards of stability and cross-platform compatibility.



一段关于 DI 的介绍：

> In the Java EE platform, dependency injection can be applied to all resources a component needs, effectively hiding the creation and lookup of resources from application code.
>
> Dependency injection can be used in Enterprise JavaBeans (EJB) containers, web containers, and application clients.
>
> Dependency injection allows the Java EE container to automatically insert references to other required components or resources, using annotations.



Java EE 模型

> The Java EE application model begins with the Java programming language and the Java virtual machine.



关于 Java EE 分层的描述：

https://docs.oracle.com/javaee/7/tutorial/overview003.htm

* Client-tier components run on the client machine.
* Web-tier components run on the Java EE server.
* Business-tier components run on the Java EE server.
* Enterprise information system (EIS)-tier software runs on the EIS server.

![Description of Figure 1-1 follows](D:/Codes/study-notes/java%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6.assets/jeett_dt_001.png)

**详细描述：**

客户端层（Clients）

A Java EE client is usually either a web client or an application client.

* Web Clients（web 客户端）
* Application Clients（应用客户端）
* Applets（小程序）
* The JavaBeans Component Architecture（java bean）
* Java EE Server Communications（服务端通信）

web 组件层（web components）

Java EE web components are either servlets or web pages created using JavaServer Faces technology and/or JSP technology (JSP pages).

* servlet：

    > **Servlets** are Java programming language classes that dynamically process requests and construct responses.

* JSP：

    > **JSP pages** are text-based documents that execute as servlets but allow a more natural approach to creating static content.

* JavaServer Faces

    > **JavaServer Faces technology** builds on servlets and JSP technology and provides a user interface component framework for web applications.

* The JavaBeans Component Architecture（java bean）

业务组件层（business components）

Business code, which is logic that solves or meets the needs of a particular business domain such as banking, retail, or finance, is handled by enterprise beans running in either the business tier or the web tier.

EIS 层（Enterprise Information System Tier）

The enterprise information system tier handles EIS software and includes enterprise infrastructure systems.

更详细的展示：

![Description of Figure 1-4 follows](D:/Codes/study-notes/java%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6.assets/jeett_dt_004.png)



容器服务（Container Services）

> **Containers** are the interface between a component and the low-level, platform-specific functionality that supports the component.
>
> Before it can be executed, a web, enterprise bean, or application client component must be assembled into a Java EE module and deployed into its container.

- **Java EE server**: The runtime portion of a Java EE product. A Java EE server provides EJB and web containers.
- **EJB container**: Manages the execution of enterprise beans for Java EE applications. Enterprise beans and their container run on the Java EE server.
- **Web container**: Manages the execution of web pages, servlets, and some EJB components for Java EE applications. Web components and their container run on the Java EE server.
- **Application client container**: Manages the execution of application client components. Application clients and their container run on the client.
- **Applet container**: Manages the execution of applets. Consists of a web browser and a Java Plug-in running on the client together.



web 服务（web services）

> Web services are web-based enterprise applications that use open, XML-based standards and transport protocols to exchange data with calling clients.



SOAP 传输协议（SOAP Transport Protocol）

> Client requests and web service responses are transmitted as Simple Object Access Protocol (SOAP) messages over HTTP to enable a completely interoperable exchange between clients and web services, all running on different platforms and at various locations on the Internet. 
>
> HTTP is a familiar request-and-response standard for sending messages over the Internet, and SOAP is an XML-based protocol that follows the HTTP request-and-response model.



Java EE 7 APIs

Java EE 所使用到的技术及其概述：https://docs.oracle.com/javaee/7/tutorial/overview007.htm



java web maven 工程结构：https://docs.oracle.com/javaee/7/tutorial/usingexamples006.htm



### 创建资源

https://docs.oracle.com/javaee/7/tutorial/resource-creation001.htm

* Resource

    > A **resource** is a program object that provides connections to systems, such as database servers and messaging systems.
    >
    > You inject resources by using the `@Resource` annotation in an application.

* Java Naming and Directory Interface (JNDI)

    > In the Java EE platform, the Java Naming and Directory Interface (JNDI) naming service enables components to locate other components and resources.
    >
    > Each resource object is identified by a unique, people-friendly name, called the JNDI name.

### 注入

* Injection

    > Java EE provides injection mechanisms that enable your objects to obtain references to resources and other dependencies without having to instantiate them directly.
    >
    > The two injection mechanisms provided by the platform: resource injection and dependency injection.

* Resource Injection

    > **Resource injection** enables you to inject any resource available in the JNDI namespace into any container-managed object, such as a servlet, an enterprise bean, or a managed bean.

    ```java
    // 示例：
    public class MyServlet extends HttpServlet {
        // 方式一：构造方法注入
        @Resource(name="java:comp/DefaultDataSource")
        private javax.sql.DataSource dsc;
    
        // 方式二：set 注入
        private javax.sql.DataSource dsc;
        ...
        @Resource(name="java:comp/DefaultDataSource")
        public void setDsc(java.sql.DataSource ds) {
            dsc = ds;
        }
    }
    ```

    ```java
    // 根据类型注入，同时注入多个资源
    @Resources ({
        @Resource(name="myDB" type=javax.sql.DataSource.class),
        @Resource(name="myMQ" type=javax.jms.ConnectionFactory.class)
    })
    ```

* Dependency Injection

    > **Dependency injection** enables you to turn regular Java classes into managed objects and to inject them into any other managed object.

    ```java
    // 示例：
    // 定义 javabean
    @javax.enterprise.context.RequestScoped
    public class CurrencyConverter { ... }
    
    public class MyServlet extends HttpServlet {
        // 注入 javabean
        @Inject CurrencyConverter cc;
        ...
    }
    ```

资源注入（resource injection）和依赖注入（dependency injection）的区别：

https://docs.oracle.com/javaee/7/tutorial/injection003.htm

| Injection Mechanism  | Can Inject JNDI Resources Directly | Can Inject Regular Classes Directly | Resolves By   | Typesafe |
| :------------------- | :--------------------------------- | :---------------------------------- | :------------ | :------- |
| Resource Injection   | Yes                                | No                                  | Resource name | No       |
| Dependency Injection | No                                 | Yes                                 | Type          | Yes      |

### 打包

* Java Archive (JAR) file
* Web Archive (WAR) file
* Enterprise Archive (EAR) file



Java EE modules 分类：

* EJB modules

    > which contain class files for enterprise beans and, optionally, an EJB deployment descriptor. EJB modules are packaged as JAR files with a `.jar` extension.

* Web modules

    > which contain servlet class files, web files, supporting class files, GIF and HTML files, and, optionally, a web application deployment descriptor. Web modules are packaged as JAR files with a `.war` (web archive) extension.

* Application client modules

    > which contain class files and, optionally, an application client deployment descriptor. Application client modules are packaged as JAR files with a `.jar` extension.

* Resource adapter modules

    > which contain all Java interfaces, classes, native libraries, and, optionally, a resource adapter deployment descriptor. Together, these implement the Connector architecture for a particular EIS. Resource adapter modules are packaged as JAR files with an .rar (resource adapter archive) extension.



EJB modules 结构：

![Description of Figure 5-2 follows](D:/Codes/study-notes/java%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6.assets/jeett_dt_011.png)

Web modules 结构：

![Description of Figure 5-3 follows](D:/Codes/study-notes/java%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6.assets/jeett_dt_012.png)

### web 应用程序

https://docs.oracle.com/javaee/7/tutorial/webapp.htm

web 应用程序分为两类：

* 面向展示的（**Presentation-oriented**）

    > A **presentation-oriented web application** generates interactive web pages containing various types of markup language (HTML, XHTML, XML, and so on) and dynamic content in response to requests.

* 面向服务的（**Service-oriented**）

    > A **service-oriented web application** implements the endpoint of a web service. Presentation-oriented applications are often clients of service-oriented web applications.



web 应用的处理过程：

1. The client sends an HTTP request to the web server.
2. A web server that implements Java Servlet and JavaServer Pages technology converts the request into an `HTTPServletRequest` object.
3. This object is delivered to a web component, which can interact with JavaBeans components or a database to generate dynamic content.
4. The web component can then generate an `HTTPServletResponse` or can pass the request to another web component. A web component eventually generates a `HTTPServletResponse` object.
5. The web server converts this object to an HTTP response and returns it to the client.

<img src="D:/Codes/study-notes/java%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6.assets/jeett_dt_013.png" alt="Description of Figure 6-1 follows"  />

关于 servlet 和 javaserver faces 的用法建议：

* Although servlets and JavaServer Faces and Facelets pages can be used to accomplish similar things, each has its own strengths. 
* Servlets are best suited for service-oriented applications (web service endpoints can be implemented as servlets) and the control functions of a presentation-oriented application, such as dispatching requests and handling nontextual data. 
* JavaServer Faces and Facelets pages are more appropriate for generating text-based markup, such as XHTML, and are generally used for presentation-oriented applications.



JavaServer Faces technology：

> JavaServer Faces technology simplifies building user interfaces for JavaServer applications.
>
> Developers can build web applications by assembling reuseable UI components in a page; connecting these components to an application data source; and wiring client-generated events to server-side event handlers.

- An API for representing components and managing their state; handling events, server-side validation, and data conversion; defining page navigation; supporting internationalization and accessibility; and providing extensibility for all these features
- Tag libraries for adding components to web pages and for connecting components to server-side objects



JavaServer Faces 流程概述：

![Description of Figure 7-1 follows](D:/Codes/study-notes/java%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6.assets/jeett_dt_014.png)

- Handling incoming requests
- Decoding parameters
- Modifying and saving state
- Rendering web pages to the browser



web 程序的逻辑和展示分离：

One of the greatest advantages of JavaServer Faces technology is that it offers a clean separation between behavior and presentation for web applications.

![Description of Figure 7-2 follows](D:/Codes/study-notes/java%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6.assets/jeett_dt_015-16515788834806.png)



JavaServer Faces 两大阶段：

* 执行（Execute）：
    * Restore View Phase
    * Apply Request Values Phase
    * Process Validations Phase
    * Update Model Values Phase
    * Invoke Application Phase
    * Render Response Phase
* 渲染（Render）



Facelets technology：

> The term **Facelets** refers to the view declaration language for JavaServer Faces technology. Facelets is a part of the JavaServer Faces specification and also the preferred presentation technology for building JavaServer Faces technology–based applications.
>
> JavaServer Pages (JSP) technology, previously used as the presentation technology for JavaServer Faces, does not support all the new features available in JavaServer Faces in the Java EE 7 platform. JSP technology is considered to be a deprecated presentation technology for JavaServer Faces.



Note：

后端动态生成页面的两种表现形式：

* 写在代码里，以 PrintWriter 流的方式输出到前端；
* 使用模板页面，例如 jsp，读取并解析 jsp 模板页面，动态填充数据，将动态页面输出到前端。



EL 表达式：

> The Expression Language (also referred to as the EL), which provides an important mechanism for enabling the presentation layer (web pages) to communicate with the application logic (managed beans).



EL 表达式的用法：

* Dynamically read application data stored in JavaBeans components, various data structures, and implicit objects
* Dynamically write data, such as user input into forms, to JavaBeans components
* Invoke arbitrary static and public methods
* Dynamically perform arithmetic, boolean, and string operations
* Dynamically construct collection objects and perform operations on collections



EL 表达式有即时计算（Immediate evaluation）和延时计算（Deferred evaluation）两种计算方法：

* ${}：**Immediate evaluation** means that the expression is evaluated and the result returned as soon as the page is first rendered.
* #{}：**Deferred evaluation** means that the technology using the expression language can use its own machinery to evaluate the expression sometime later during the page's lifecycle, whenever it is appropriate to do so.



EL 表达式有值表达式（Value expressions）和方法表达式（method expressions）两种表达式：

* **Value expressions** can be evaluated to yield a value.
    * 左值表达式（lvalue expression）
    * 右值表达式（rvalue expression）：
* **Method expressions** are used to reference a method.



EL 表达式支持的运算符：

https://docs.oracle.com/javaee/7/tutorial/jsf-el005.htm



EL 表达式的一些使用举例：

https://docs.oracle.com/javaee/7/tutorial/jsf-el007.htm





JavaServer Faces technology，提供转换器（Converters）、监听器（Listeners）和验证器（Validators）：

- Converters are used to convert data that is received from the input components. Converters allow an application to bring the strongly typed features of the Java programming language into the String-based world of HTTP servlet programming.
- Listeners are used to listen to the events happening in the page and perform actions as defined.
- Validators are used to validate the data that is received from the input components. Validators allow an application to express constraints on form input data to ensure that the necessary requirements are met before the input data is processed.





https://docs.oracle.com/javaee/7/tutorial/jsf-ajax001.htm

AJAX 异步请求

> Ajax is an acronym for Asynchronous JavaScript and XML, a group of web technologies that enable creation of dynamic and highly responsive web applications. Using Ajax, web applications can retrieve content from the server without interfering with the display on the client.
>
> Early web applications were created mostly as static web pages. When a static web page is updated by a client, the entire page has to reload to reflect the update. In effect, every update needs a page reload to reflect the change. Repetitive page reloads can result in excessive network access and can impact application performance. Technologies such as Ajax were created to overcome these deficiencies.





Java Servlet

> Java Servlet technology provides dynamic, user-oriented content in web applications using a request-response programming model.
>
> 
>
> A servlet is a Java programming language class used to extend the capabilities of servers that host applications accessed by means of a request-response programming model. Although servlets can respond to any type of request, they are commonly used to extend the applications hosted by web servers. For such applications, Java Servlet technology defines HTTP-specific servlet classes.



Servlet Lifecycle（生命周期）

The lifecycle of a servlet is controlled by the container in which the servlet has been deployed. When a request is mapped to a servlet, the container performs the following steps.

1. If an instance of the servlet does not exist, the web container:
   1. Loads the servlet class
   2. Creates an instance of the servlet class
   3. Initializes the servlet instance by calling the `init` method
2. The container invokes the `service` method, passing request and response objects.

If it needs to remove the servlet, the container finalizes the servlet by calling the servlet's `destroy` method.



Servlet Scope（作用域）

Table 17-2 Scope Objects

| Scope Object | Class                                     | Accessible From                                              |
| :----------- | :---------------------------------------- | :----------------------------------------------------------- |
| Web context  | `javax.servlet.ServletContext`            | Web components within a web context. See [Accessing the Web Context](https://docs.oracle.com/javaee/7/tutorial/servlets008.htm#BNAGL). |
| Session      | `javax.servlet.http.HttpSession`          | Web components handling a request that belongs to the session. See [Maintaining Client State](https://docs.oracle.com/javaee/7/tutorial/servlets009.htm#BNAGM). |
| Request      | Subtype of `javax.servlet.ServletRequest` | Web components handling the request.                         |
| Page         | `javax.servlet.jsp.JspContext`            | The JSP page that creates the object.                        |







杨博超

SSM = spring + springMVC + mybatis

# 开发框架基本介绍
struts1, struts2, hibernate, spring, springMVC, mybatis

apache: struts1, struts2, mybatis  
jboss: hibernate  
interface21: spring, springMVC  

MVC框架：struts1, struts2, springMVC  
持久层框架：hibernate(全自动的持久层框架), mybatis(半自动的持久层框架)  
整合性框架/设计型框架：spring  

## 原始
servlet + jsp + jdbc

## struts1
struts1封装了servlet

## struts2
struts2封装的是过滤器filter

# servlet

[Servlet 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/servlet/servlet-tutorial.html)

在我的认知里，java 自 servlet 起步。





# java bean

![img](D:/Codes/study-notes/java%E5%BC%80%E5%8F%91%E6%A1%86%E6%9E%B6.assets/26dec215ba4359bdc30a1e2cc6007213.png)

## PO（Persistent Object） 数据持久化对象

数据持久化对象 PO（Persistent Object），与数据库结构一一映射，是数据持久化过程中的数据载体。

## DO（Domain Object） 领域对象

领域对象 DO（Domain Object），微服务运行时的实体，是核心业务的载体。

## DTO（Data Transfer Object） 数据传输对象

数据传输对象 DTO（Data Transfer Object），用于前端与应用层或者微服务之间的数据组装和传输，是应用之间数据传输的载体。

## VO（View Object） 视图对象

视图对象 VO（View Object），用于封装展示层指定页面或组件的数据。

# Spring 基本介绍

Spring是一个IOC和AOP的容器框架。

**非侵入式**：也可以称为轻量级，基于Spring开发的应用中的对象，可以不依赖于Spring的API。  
**依赖注入**：DI--Dependency Injection, 依赖注入，控制反转(IOC)最经典的实现。  
**面向切面编程**：AOP--Aspect Oriented Programming。  
**容器**：Spring是一个容器，因为它包含并且管理对象的生命周期。  
>由类实例化产生对象，由对象调用方法，最终实现功能。  
>Spring管理对象，管理对象的生命周期。  

**组件化**：Spring实现了简单的组件配置组合成一个复杂的应用。  
>Spring中的组件指的就是Spring管理的对象。  
>Spring能降低程序间的耦合。

**一站式**: 在IOC和AOP的基础上，可以整合各种企业应用的开源框架和第三方类库。


Spring Framework

|-- Web
|   |-- Web
|   |-- WebSocket
|   |-- Servlet
|   |-- Portlet
|-- Data Access/Intergration
|   |-- JDBC: Java DataBase Connectivity
|   |-- ORM: Object Relational Mapping
|   |-- OXM
|   |-- JMS
|   |-- Transactions
|-- AOP
|   |-- Aspects
|-- Instrumentation
|-- Messaging
|-- Core Container
|   |-- Beans
|   |-- Core
|   |-- Context
|   |-- SpEL: Spring Expression Language


# Spring IOC(DI)

IOC: Inversion of Control, 控制反转。  
DI: Dependency Injection, 依赖注入，控制反转(IOC)最经典的实现。


Spring applicationContext.xml
```xml
<?xml version="1.0" encoding="utf-8">
<!-- xmlns:xml namespaces 定义xml所可使用的标签 -->
<beans xmlns="" xmlns:xsi="" xsi:schemaLocation="">
  <!-- 
    <bean>: 定义一个Spring所管理的对象
	id: 定义该对象的唯一标识
	name: 定义该对象全限定名（包名+类名）
  -->
  <bean id="" class="" scope="">
    <!-- 
	  <property>: 为对象的某个属性赋值
	  name: 对象的属性名
	  value: 对象的属性值
	-->
	<property name="" value=""></property>
    <property name="" value=""></property>
	...
  </bean>
  ...
</beans>
```

<bean>: 



# Spring AOP
AOP: Aspect Oriented Programming, 面向切面编程。  
OOP: Object Oriented Programming, 面向对象编程。  

万物皆对象，但OOP存在某些缺陷，而AOP是为了补充这种缺陷而存在。



配置bean，id唯一标识，class标识路径



1.初始化Spring容器
2.通过getBean方法获取对象
Application.

