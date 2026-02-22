---
date: 2026-02-12T12:00:00+08:00
title: Spring
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

SSH框架：Strust2 + Spring + Hibernate

SSM框架：SpringMVC + Spring + Mybatis

# Spring

[Core Technologies (spring.io)](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#spring-core)

优势：

* spring 是一个开源的免费的框架（容器）
* spring 是一个轻量级的、非侵入式的框架
* 支持事务的处理，对框架的支持

弊端：

* 发展了太久，后期配置十分繁琐，人称：“配置地狱”

Spring 的核心包括：模型配置和依赖注入。

# 控制反转 IOC

## IOC 理论推导

原始开发一个服务的过程

* UserDAO
* UserDAOImpl
* UserService
* UserServiceImpl

```java
public interface UserDAO {
    User getUser();
}

public class UserDAOImpl implements UserDAO {
    @Override
    public User getUser() {
        return new User(1, "张三", "zhangsan");
    }    
}

public interface UserService {
    User getUser();
}

// 服务的实现类，写死了 UserDaoImpl
public class UserServiceImpl implements UserService {
    private UserDAO userDAO = new UserDAOImpl();
    public User getUser() {
        return userDAO.getUser();
    }
}

// 测试程序
public class MyTest {
    public static void main(String[] args) {
        UserService userService = new UserServiceImpl();
        System.out.println(userService.getUser());
    }
}
```

当需求增加，需要调整服务时：

```java
public class UserDAOImpl2 implements UserDAO {
    @Override
    public User getUser() {
        return new User(2, "李四", "lisi");
    }    
}
public class UserDAOImpl3 implements UserDAO {
    @Override
    public User getUser() {
        return new User(3, "王五", "wangwu");
    }    
}
```

此时，需要修改代码。当程序变得复杂时，代码修改的代价变得非常高昂，此时引入 IOC 思想。

## IOC 带来的改变

在我们之前的业务中，用户的需求可能会影响我们原来的代码，我们需要根据用户的需求修改源代码，如果程序代码量很庞大，则修改一次的成本代价非常高昂。

使用一个 Set 接口实现，实现了业务代码的解耦：

* 之前程序主动创建对象，控制权在程序员手中；
* 使用了 Set 注入后，当前程序不再具有主动性，而是变成了被动地接受对象！

程序不再主动管理对象的创建，系统耦合性大大降低，可以更加关注业务的实现。这成为了 IOC 的原型。

```java
// 服务的实现类
public class UserServiceImpl implements UserService {
    private UserDAO userDAO;
    // 利用 set 方法，实现动态注入    
    public void setUserDAO(UserDAO userDAO) {
        This.userDAO = userDAO;
    }
    public User getUser() {
        return userDAO.getUser();
    }
}

public class MyTest {
    public static void main(String[] args) {
        UserServiceImpl userService = new UserServiceImpl();
        userService.setUserDAO(new UserDAOImpl2());
        System.out.println(userService.getUser());
    }
}
```

## IOC 本质分析

控制反转（Inversion of Control，IOC），是一种设计思想，依赖注入（DI）是实现 IOC 的一种方法。

在没有 IOC 的程序中，我们使用面向对象编程，对象的创建与对象间的依赖关系完全硬编码在程序中，对象的创建由程序自己控制。

在 IOC 的程序中，对象的创建移交给了第三方，获取依赖对象的方式发生了反转。

IOC 是 Spring 框架的核心内容，有很多种方式可以实现，例如：XML 配置、注解，也可以实现零配置（自动装配）

Spring 在初始化时，会读取配置文件，根据配置文件创建与组织对象存入 IOC 容器中，程序使用时，再从 IOC 容器中取出需要的对象。

# Spring IOC

## beans.xml 配置 bean

使用 Spring 来创建对象，这些对象在 Spring 中称为 Bean，使用 XML 进行配置。

* id 是标识这个 bean 定义的字符串
* class 定义这个 bean 的类型，使用对象的全类名
* property 配置对象中的属性
  * value：具体的值，必须是基本数据类型
  * ref：引用 Spring 容器中创建好的对象

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
        xsi:schemaLocation="http://www.springframework.org/schema/beans 
        https://www.springframework.org/schema/beans/spring-beans.xsd">

    <bean id="user" class="com.ckl.test.sqlinj.pojo.User">
        <property name="id" value="1"></property>
        <property name="username" value="张三"></property>
        <property name="password" value="zhangsan"></property>
    </bean>
    <bean id="userDAOImpl" class="com.ckl.test.sqlinj.dao.UserDAOImpl"></bean>
    <bean id="userDAOImpl2" class="com.ckl.test.sqlinj.dao.UserDAOImpl"></bean>
    <bean id="userServiceImpl" class="com.ckl.test.sqlinj.service.UserServiceImpl">
        <property name="UserDao" ref="userDAOImpl"></property>
    </bean>
</beans>
```

## 实例化 Spring IOC 容器

对象交由 spring 管理，在需要使用时，从中获取。

```java
// 读取 beans.xml 文件中的配置，实例化 Spring IOC 容器
ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");
```

## 使用容器创建对象

getBean() 方法，并强转为需要的类型

```java
// 方法 1
Type type = (Type) context.getBean("beanId");
// 方法 2
Type type = context.getBean("beanId", Type.class);
// 方法 3：注册的 Type 唯一时使用
Type type = context.getBean(Type.class);
```

Spring 默认使用无参构造方法创建对象。

如果要使用有参构造方法，需要在 beans.xml 中配置 constructor-arg 标签，配置后默认使用有参构造方法，配置参考如下：

```xml
    <bean id="user" class="com.ckl.test.sqlinj.pojo.User">
        <!-- 使用参数名 -->
        <constructor-arg ref="username" value="zhangsan"></constructor-arg>
        <!-- 下标匹配 -->
        <constructor-arg index="0" value="1"></constructor-arg>
        <!-- 参数类型匹配，不建议使用 -->
        <constructor-arg type="java.lang.String" value="zhangsan"></constructor-arg>
   </bean>
```

如果 bean 本身没有无参构造方法，且未配置有参构造方法参数，会抛出异常。

## 单例模式

在配置文件加载的时候，容器中管理的对象就已经初始化了。默认创建为单实例的。

# beans.xml 配置详解

## alias 别名

别名配置仅用于 id 映射，不能用于全类名映射

```xml
<!-- 错误使用方法，会报错 -->
<alias name="com.ckl.test.sqlinj.pojo.User" alias="User" />
<bean id="user" class="User"></bean>

<!-- 正确使用方法 -->
<alias name="user" alias="newUser" />
<bean id="user" class="com.ckl.test.sqlinj.pojo.User"></bean>
```

## bean 对象

* id：对象名
* class：全类名
* name：也是别名，与 alias 为替代关系，可以同时取多个别名，可以用常用的任何分隔符
* scope：作用域，可以

```xml
<bean id="userTest" class="com.ckl.test.sqlinj.pojo.User" name="user,USER,u2 u3;u4">
```

## import 导入

一般用于团队开发，可以将多个配置文件，导入为一个。

```xml
<import resource="beans2.xml" />
<import resource="beans3.xml" />
```

当多个配置文件中有相同时，Spring 默认处理方式为合并；如果存在冲突，后导入的会替代前导入的。

## 集合注入配置

```java
public class Student {
    private Integer id;
    private String name;
    private Account account;
    private String[] books;
    private List<String> hobbys;
    private Set<String> games;
    private Map<String, String> address;
    private Properties info;
    // setter & getter
}
```

```xml
<bean id="student" class="com.ckl.test.sqlinj.pojo.Student">\
    <!-- 基本数据类型 -->
    <property name="name" value="张三"></property>
    <!-- arrays -->
    <property name="books">
        <array>
            <value>语文</value>
            <value>数学</value>
            <value>英语</value>
        </array>
    </property>
    <!-- java.util.List -->
    <property name="hobbys">
        <list>
            <value>篮球</value>
            <value>唱歌</value>
        </list>
    </property>
    <!-- java.util.Set -->
    <property name="games">
        <set>
            <value>原神</value>
            <value>崩坏三</value>
            <value>剑与远征</value>
        </set>
    </property>
    <!-- java.util.Map -->
    <property name="address">
        <map>
            <entry key="home" value="家庭地址：xxxxxx"></entry>
            <entry key="school" value="学校地址：xxxxxx"></entry>
        </map>
    </property>
    <!-- java.util.Properties -->
    <property name="info">
        <props>
            <prop key="identity">410</prop>
            <prop key="ICBC">621220</prop>
        </props>
    </property>
	<!-- null -->
    <property name="wife">
        <null></null>
    </property>
</bean>
```

## XML 配置简化

```xml
<!-- p 命名空间，简化 set 注入配置 -->
xmlns:p="http://www.springframework.org/schema/p"
<!-- c 命名空间，简化构造函数注入配置 -->
xmlns:c="http://www.springframework.org/schema/c"
```

## scope bean作用域

https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-factory-scopes

| Scope          | Description                                                  |
| :------------- | :----------------------------------------------------------- |
| singleton 单例 | (Default) Scopes a single bean definition to a single object instance for each Spring IoC container. |
| prototype原型  | Scopes a single bean definition to any number of object instances. |
| request        | Scopes a single bean definition to the lifecycle of a single HTTP request. That is, each HTTP request has its own instance of a bean created off the back of a single bean definition. Only valid in the context of a web-aware Spring `ApplicationContext`. |
| session        | Scopes a single bean definition to the lifecycle of an HTTP `Session`. Only valid in the context of a web-aware Spring `ApplicationContext`. |
| application    | Scopes a single bean definition to the lifecycle of a `ServletContext`. Only valid in the context of a web-aware Spring `ApplicationContext`. |
| websocket      | Scopes a single bean definition to the lifecycle of a `WebSocket`. Only valid in the context of a web-aware Spring `ApplicationContext`. |

一般仅使用 单例模式 或者 原型模式，其余仅在 web 生命声明周期中使用。

单线程一般使用单例模式；多线程一般使用原型模式。

# 依赖注入 DI

## 基于构造函数的依赖注入

```java
public class SimpleMovieLister {

    // the SimpleMovieLister has a dependency on a MovieFinder
    private final MovieFinder movieFinder;

    // a constructor so that the Spring container can inject a MovieFinder
    public SimpleMovieLister(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }

    // business logic that actually uses the injected MovieFinder is omitted...
}
```

## 基于 set 方法的依赖注入

```java
public class SimpleMovieLister {

    // the SimpleMovieLister has a dependency on the MovieFinder
    private MovieFinder movieFinder;

    // a setter method so that the Spring container can inject a MovieFinder
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }

    // business logic that actually uses the injected MovieFinder is omitted...
}
```

## 构造函数注入和 set 方法注入

Spring 建议优先使用构造函数注入，因为构造函数注入时，可以获得一个不可变的对象，并且确保依赖的对象不为 null。

Spring 仅建议对一些可变的依赖对象设置 set 注入，这些依赖项可以设置合理的默认值，否则就必须在任何执行的地方执行非空检查。

## 循环依赖问题

当 A 的构造需要 B，而 B 的构造需要 A 时，就会触发循环依赖问题，Spring IOC 容器会抛出循环依赖异常。

解决这个问题，需要避免循环依赖，或者通过 set 注入。

# bean 的自动装配 

## xml 配置自动注入

```java
public class Computer {
    private Integer id;
    private Game game;
    private Note note;
    // setter & getter & toString()
}
public class Game {
    public Game() {
        System.out.println("this is a game!");
    }
}
public class Note {
    public Note() {
        System.out.println("this is a note!");
    }
}
```

```xml
<bean id="game" class="com.ckl.test.sqlinj.pojo.Game"></bean>
<bean id="note" class="com.ckl.test.sqlinj.pojo.Note"></bean>
<bean id="computer" class="com.ckl.test.sqlinj.pojo.Computer" autowire="byName">
    <property name="id" value="1720"></property>
</bean>
```

autowire 参数：

* byType：在 IOC 容器中查找，和自己对象属性类型相同的 bean
* byName：在 IOC 容器中查找，和自己对象 set 方法后面值相同的 bean id

## 注解的使用是否优于 XML 配置？

使用注解需要首先回答一个问题，注解的使用是否优于 XML 配置？

Spring 官方的答复如下：

> Are annotations better than XML for configuring Spring?
>
> The introduction of annotation-based configuration raised the question of whether this approach is “better” than XML. The short answer is “it depends.” The long answer is that each approach has its pros and cons, and, usually, it is up to the developer to decide which strategy suits them better. Due to the way they are defined, annotations provide a lot of context in their declaration, leading to shorter and more concise configuration. However, XML excels at wiring up components without touching their source code or recompiling them. Some developers prefer having the wiring close to the source while others argue that annotated classes are no longer POJOs and, furthermore, that the configuration becomes decentralized and harder to control.
>
> No matter the choice, Spring can accommodate both styles and even mix them together. It is worth pointing out that through its [JavaConfig](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-java) option, Spring lets annotations be used in a non-invasive way, without touching the target components source code and that, in terms of tooling, all configuration styles are supported by the [Spring Tools for Eclipse](https://spring.io/tools).

因此，使用注解，或者使用 xml 配置的方式，取决于使用的场景，以及个人风格。

Spring 同时支持注解以及 xml 配置的方式。需要注意的是：注解的注入要优先于 xml 注入。

## 使用注解自动注入

### 导入注解约束

使用注解需要导入约束

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd">

    <!-- 使用注解 -->
    <context:annotation-config/>
    <!-- 指定需要扫描的包，这个包下的注解就会生效 -->
    <context:component-scan base-package="com.ckl.test.sqlinj.pojo"></context:component-scan>

</beans>
```

### @Required

@Required 注解适用于为 bean 的属性设置方法

```java
public class SimpleMovieLister {

    private MovieFinder movieFinder;

    @Required
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }

    // ...
}
```

### @Autowired

@Autowired 注解适用于构造函数，也可以适用于 setter 方法

```java
public class MovieRecommender {

    private final CustomerPreferenceDao customerPreferenceDao;

    @Autowired
    private MovieFinder movieFinder;

    @Autowired
    public MovieRecommender(CustomerPreferenceDao customerPreferenceDao) {
        this.customerPreferenceDao = customerPreferenceDao;
    }
    
    @Autowired(required = false)
    public void setMovieFinder(MovieFinder movieFinder) {
        this.movieFinder = movieFinder;
    }
    /**
    @Autowired
    public void setMovieFinder(@Nullable MovieFinder movieFinder) {
        ...
    }
    /

    // ...
}
```

@Autowired 注解使用时，默认需要注入候选的 bean，当没有找到 bean 时，自动装配会失败。

通过将其标记为不需要（required = false，或者使用 @Nullable 注解），可以让 spring 框架跳过不满足的注入点。

@Autowired 默认按照 autowire="byType" 的方式在 IOC 容器内获取 bean，当查找到多个匹配的 type 时，按照 byName 的方式选取 bean，如果无法匹配，则报错。

当 spring bean 的配置比较复杂时，也可以结合 @Qualifier(value = "beanId") 的方式获取 bean。

```java
@Autowired
@Qualifier(value="beanId")
private MovieFinder movieFinder;
```

测试方法：

```xml
    @Autowired
    private Game game;

	<bean id="game1" class="com.ckl.test.sqlinj.pojo.Game"></bean>
    <bean id="game2" class="com.ckl.test.sqlinj.pojo.Game"></bean>
    <bean id="game" class="com.ckl.test.sqlinj.vo.Game"></bean>

Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.UnsatisfiedDependencyException: Error creating bean with name 'computer': 
Unsatisfied dependency expressed through field 'game'; nested exception is org.springframework.beans.factory.NoUniqueBeanDefinitionException: 
No qualifying bean of type 'com.ckl.test.sqlinj.pojo.Game' available: expected single matching bean but found 2: game1,game2
```

### @Resource

@Resource 注解同样可以实现与 @Autowired 自动注入的功能，但 @Resource 默认按照 beanId 来获取 bean，如果找不到再按照 byType 来获取。

```java
@Resource(name="beanId")
private MovieFinder movieFinder;
```

测试方法：

```xml
    @Resource
    private Game game;

    <bean id="game1" class="com.ckl.test.sqlinj.pojo.Game"></bean>
    <bean id="game2" class="com.ckl.test.sqlinj.pojo.Game"></bean>
    <bean id="game" class="com.ckl.test.sqlinj.vo.Game"></bean>

Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'computer': Injection of resource dependencies failed; nested exception is org.springframework.beans.factory.BeanNotOfRequiredTypeException: Bean named 'game' is expected to be of type 'com.ckl.test.sqlinj.pojo.Game' but was actually of type 'com.ckl.test.sqlinj.vo.Game'
```

# 使用注解配置 bean

## @Component

注册为 Spring IOC 容器中的 bean。

```java
// 等价于 <bean id="user" class="com.ckl.test.sqlinj.pojo.User" />
@Component
public class User {
    private Integer id;
    private String username;
    private String password;
}
```

@Component 的衍生注解，在 web 开发中，会按照 Spring MVC 三层架构进行分离（但实际使用效果完全相同）：

* Dao 层：使用 @Repository
* Service 层：使用 @Service
* Controller 层：使用 @Controller

它们都将自身装配到 Spring IOC 容器中。

## @Scope

配置 Spring IOC 容器中 bean 的作用域。

```java
@Component
// 等价于 <bean id="user" class="com.ckl.test.sqlinj.pojo.User" scope="prototype" />
@Scope("prototype")
public class User {
    private Integer id;
    private String username;
    private String password;
}
```

## @value

配置 bean 的属性，也可以配置在 setter 方法上。

```java
/** 等价于
    <bean id="user" class="com.ckl.test.sqlinj.pojo.User">
        <property name="id" value="123"></property>
        <property name="username" value="张三"></property>
        <property name="password" value="zhangsan"></property>
    </bean>
 */
@Component
public class User {
    @Value("123")
    private Integer id;
    @Value("张三")
    private String username;
    private String password;
    
    @Value("zhangsan")
    public void setPassword(String password) {
        this.password = password;
    }
}
```

## xml 和注解的最佳策略

xml 全面完整，可以实现任意功能；

注解简单方便，但维护复杂；

一般而言，可以选择通过 xml 维护 bean，而通过注解完成属性的注入。

# 完全基于注解的注入方式

可以完全基于 java 程序的方式，不再使用 xml 文件，配置 Spring IOC 容器中的 bean。

## @Configuration & @Bean

https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-java

使用 @Configuration 注解标记配置类，使用 @Bean 注解配置 java bean，方法名即为 beanId。

```java
@Configuration
@ComponentScan(basePackages="com.ckl.test.sqlinj.pojo")
@Import(AppConfig.class)
public class PojoConfig {
    
    @Bean
    public Cust getCust(){
        return new Cust();
    }
}

/**
 等同于
 <beans>
    <context:component-scan base-package="com.ckl.test.sqlinj.pojo"/>
    <bean id="getCust" class="com.ckl.test.sqlinj.pojo.Cust"/>
 </beans>
 */
```

## @ComponentScan

使用 @ComponentScan 注解可以扫描指定包中的注册为 java bean 的注解（@Component 及相关类）。

@Component 注解可以指定 value，如果不指定，默认查找当前所在的包。

## @Import

使用 @Import 注解可以将引入另一个使用 @Configuration 注解标记的配置类。





# 面向切面编程 AOP

## AOP 动机

AOP 的动机是，一些横跨每个类中的问题，例如安全策略、日志、监控、事务等，如果需要改造每个类，那么工作量和成本将是巨大的。

AOP 的出现就是为了解决这样的问题。

在 Spring 框架中，对于 AOP 支持支持 Aspectj（https://www.eclipse.org/aspectj/）和 Spring AOP 两种框架。

Spring AOP 的实现基础是 java 代理。

## 代理模式

是 Spring AOP 的底层。

代理就像是中介，例如租户、房东、中介三者的关系。

* 服务接口：定义服务，例如租房服务
* 实现类：定义服务的实现，例如房东实现租房服务
* 代理类：代理实现类，例如中介代替房东实现租房服务，同时可以提供额外的服务，例如看房、签合同、分期付款等
* 调用类：访问代理类，实现某些服务

代理分为：静态代理和动态代理。

### 静态代理

静态代理：在原有的业务逻辑之上，增加一层代理层，在不改变原有的业务逻辑的同时，可以新增业务逻辑。

> 举例：
>
> service 层原有的业务逻辑已经实现了，此时如果需求要新增功能，不能改变原有业务逻辑，此时可以使用代理模式，新增一层代理 proxy，实现新增功能的基础上，调用原有业务实现类。

静态代理优点：

* 可以使真实角色的操作更加纯粹，不关心公共业务；
* 公共业务交给代理角色，实现了业务分工；
* 公共业务发展拓展的时候，方便集中管理。

静态代理缺点：

* 一个真实角色就会产生一个代理角色；代码量会翻倍。

### 动态代理

静态代理的缺陷在于代理类是写好的，动态代理解决了这个缺陷。

动态代理的代理类是动态生成的！

动态代理分为三大类：

* 基于接口的动态代理：例如 jdk 动态代理
* 基于类的动态代理：例如 cglib
* 基于 java 字节码：例如 javassist

基于接口的动态代理，需要了解两个类：java.lang.reflect.Proxy、java.lang.reflect.InvocationHandler

#### java.lang.reflect.Proxy

Proxy 提供静态方法来创建对象，类似于接口的实例，但允许自定义方法调用。

方法：

* `public static InvocationHandler getInvocationHandler(Object proxy) throws IllegalArgumentException`: 返回指定代理实例的调用处理程序。
* `public static boolean isProxyClass(Class<?> cl)`: 如果给定的类是代理类，则返回 true。
* `public static Object newProxyInstance(ClassLoader loader, Class<?>[] interfaces, InvocationHandler h)`: 返回指定接口的代理实例，该接口将方法调用给指定调用处理程序。

#### java.lang.reflect.InvocationHandler

InvocationHandler 是代理实例的调用处理程序实现的接口。

每个代理实例都有一个关联的 Invocation Handler 。当在代理实例上调用方法时，方法调用被编码并分派到其调用处理程序的 invoke 方法。

方法：

* `Object invoke(Object proxy, Method method, Object[] args) throws Throwable`: 处理代理实例上的方法调用，并返回结果。

#### 动态代理的公共实现类

```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

public class ProxyInvocationHandler implements InvocationHandler {
    // 被代理的接口
    private Object target;

    public void setTarget(Object object) {
        this.target = object;
    }

    // 生成得到代理类
    public Object getProxy() {
        return Proxy.newProxyInstance(this.getClass().getClassLoader(), target.getClass().getInterfaces(), this);
    }

    // 处理代理实例，并返回结果
    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        // 动态代理的本质，就是使用反射机制实现
        Object object = method.invoke(target, args);
        return object;
    }

}
```

动态代理优点：

* 静态代理的优点都有
* 一个动态代理类，代理了一类业务，可以代理多个类，只要是实现了同一个接口

# Spring AOP

## 名词和术语

https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#aop-introduction-defn

面向切面编程（Aspect-oriented Programming, AOP）从另一种角度思考程序结构，是对面向对象编程（Object-oriented Programming, OOP）的一种补充。

在 OOP 中，模块化的关键是 class，而在 AOP 中，模块化的关键是 aspect（切面）。aspect 提供横跨多个类或对象的关注问题的模块化处理。

Spring IOC 的实现不依赖于 Spring AOP，但 Spring AOP 补充了 Spring IOC 以提供了强大的中间件解决方案。

AOP 名词和术语：

* 横切关注点：跨越应用程序多个模块的方法或功能。即：与我们业务逻辑无关的，但是我们需要关注的部分，就是横切关注点。例如日志、安全、缓存、事务等等。
* Aspect：切面，横跨多个类的模块化的关注点（A modularization of a concern that cuts across multiple classes）。在 Spring AOP 中，aspect 通常是通过普通类，或者带 @Aspect 注解的普通类来实现的，
* Join point：连接点，程序执行过程中的一个点，例如方法的执行，或异常的处理等。在 Spring AOP 中，一个 join point 代表一个方法的执行。
* Advice：通知/增强，切面在连接点采取的行动（Action taken by an aspect at a particular join point）。advice 的类型包括 “around”、“before” 和 “after”。包括 Spring 在内的许多 AOP 框架，将 advice 作为一个拦截器，并且在 join point 周围设置一系列的拦截器。
  * Before advice：通知可以在连接点之前执行，但无法阻止流程执行到连接点（除非抛出异常）。
  * After returning advice：通知可以在连接点正常结束（方法没有返回异常）之后执行。
  * After throwing advice：通知可以在一个方法抛出异常时执行。
  * After (finally) advice：通知可以在连接点退出后执行，无论是否发生异常。
  * Around advice：通知可以环绕一个连接点，例如一个方法调用。
* Pointcut：切入点，匹配 join point 的断言。advice 和 pointcut 的表达式关联，并且在 pointcut 匹配的任何一个 joint point 上执行，例如：执行特定名称的方法等。pointcut 表达式匹配 join point 的概念是 AOP 的核心，Spring 默认使用 Aspectj pointcut 表达式。
* Introduction：引入，代表一个 type 声明方法或字段（Declaring additional methods or fields on behalf of a type）。Spring AOP 允许向任何 adviced 的对象引入新的接口（和相应的实现）。introduction 被 Aspectj 社区称为类型间声明（inter-type declaration）。
* Target object：目标对象，被一个或多个 aspect adviced 的对象。由于 Spring AOP 使用运行时代理实现的，因此这个对象始终是一个代理对象。
* AOP proxy：AOP 代理，被 AOP 框架创建的对象，用于实现 aspect 、advise 方法执行等。在 Spring 框架中，AOP proxy 是一个 jdk 动态代理，或者 CGLIB 代理。
* Weaving：编织，将 aspect 和其他应用程序的 types 或对象连接，以创建一个 advised 对象。这个过程可以在编译、加载或运行时完成。Spring AOP 框架和其他纯 java AOP 框架一样，在运行时执行 weaving。

> * Aspect: A modularization of a concern that cuts across multiple classes. Transaction management is a good example of a crosscutting concern in enterprise Java applications. In Spring AOP, aspects are implemented by using regular classes (the schema-based approach) or regular classes annotated with the @Aspect annotation (the @AspectJ style).
> * Join point: A point during the execution of a program, such as the execution of a method or the handling of an exception. In Spring AOP, a join point always represents a method execution.
> * Advice: Action taken by an aspect at a particular join point. Different types of advice include “around”, “before” and “after” advice. (Advice types are discussed later.) Many AOP frameworks, including Spring, model an advice as an interceptor and maintain a chain of interceptors around the join point.
> * Pointcut: A predicate that matches join points. Advice is associated with a pointcut expression and runs at any join point matched by the pointcut (for example, the execution of a method with a certain name). The concept of join points as matched by pointcut expressions is central to AOP, and Spring uses the AspectJ pointcut expression language by default.
> * Introduction: Declaring additional methods or fields on behalf of a type. Spring AOP lets you introduce new interfaces (and a corresponding implementation) to any advised object. For example, you could use an introduction to make a bean implement an IsModified interface, to simplify caching. (An introduction is known as an inter-type declaration in the AspectJ community.)
> * Target object: An object being advised by one or more aspects. Also referred to as the “advised object”. Since Spring AOP is implemented by using runtime proxies, this object is always a proxied object.
> * AOP proxy: An object created by the AOP framework in order to implement the aspect contracts (advise method executions and so on). In the Spring Framework, an AOP proxy is a JDK dynamic proxy or a CGLIB proxy.
> * Weaving: linking aspects with other application types or objects to create an advised object. This can be done at compile time (using the AspectJ compiler, for example), load time, or at runtime. Spring AOP, like other pure Java AOP frameworks, performs weaving at runtime.



## 方式一：使用 Spring AOP APIs

第一种方法：使用 Spring API 实现 AOP。

```java
public class BeforeLog implements MethodBeforeAdvice {
    @Override
    public void before(Method method, Object[] args, Object target) throws Throwable {       
        System.out.println(target.getClass().getName() + "的方法" + method.getName() + "被执行了");
    }
}

public class AfterLog implements AfterReturningAdvice {
    @Override
    public void afterReturning(Object returnValue, Method method, Object[] args, Object target) throws Throwable {
        System.out.println(target.getClass().getName() + "的方法" + method.getName() + "执行结束，返回值为：" + returnValue);
    }
}
```



```xml
<beans xmlns="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:context="http://www.springframework.org/schema/context" xmlns:aop="http://www.springframework.org/schema/aop" xsi:schemaLocation="http://www.springframework.org/schema/beans
        https://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        https://www.springframework.org/schema/context/spring-context.xsd
        http://www.springframework.org/schema/aop 
        https://www.springframework.org/schema/aop/spring-aop.xsd">
    <bean id="log" class="com.ckl.test.sqlinj.utils.Log"></bean>
    <bean id="afterlog" class="com.ckl.test.sqlinj.utils.AfterLog"></bean>
    <bean id="userservice" class="com.ckl.test.sqlinj.service.UserServiceImpl"></bean>

    <!-- 方式一：使用原生 Spring API 接口-->
    <aop:config>
        <!-- 切入点：expression 表达式 execution(要执行的位置 *（修饰词） *（返回值） *（类名） *（方法名） *（参数）) -->
        <aop:pointcut id="pointcut01" expression="execution(* com.ckl.test.sqlinj.service.UserServiceImpl.*(..))" />
        <!-- 执行环绕：把 log 切入到 pointcut 点 -->
        <aop:advisor advice-ref="log" pointcut-ref="pointcut01" />
        <aop:advisor advice-ref="afterlog" pointcut-ref="pointcut01" />
    </aop:config>
</beans>
```

## 方式二：自定义切入点类

```java
public class AopLog {
    public void before() {
        System.out.println("before method...");
    }

    public void after() {
        System.out.println("after method...");
    }
}
```

```xml
    <!-- 切面实现类 -->
    <bean id="aoplog" class="com.ckl.test.sqlinj.aopdemo01.AopLog"></bean>
    <aop:config>
        <!-- 指定切面 -->
        <aop:aspect ref="aoplog">
            <!-- 指定切入点 -->
            <aop:pointcut id="pointcut02" expression="execution(* com.ckl.test.sqlinj.service.UserServiceImpl.*(..))" />
            <!-- 指定切入方法 -->
            <aop:before method="before" pointcut-ref="pointcut02" />
            <aop:after method="after" pointcut-ref="pointcut02" /> 
        </aop:aspect>
    </aop:config>
```

## 方式三：使用注解实现

