# DDD 概念

领域驱动设计 (Domian-Driven Design, DDD)，是目前流行的微服务设计模式，其主要是代码设计层次的微服务领域概念。

在著名的《领域驱动设计 软件核心复杂性应对之道》（Domain-Driven Design, Tackling Complexity in the Heart of Software）中，作者对 DDD 定义了一个通用的模型：

![image-20220104153506614](D:/Codes/study-notes/Domain-Driven%20Design.assets/image-20220104153506614.png)

图片来源：极客时间 DDD 实战课 欧创新

DDD 方法论将一个软件工程拆分为四层：

1. interface 用户接口层：定义用户界面、web 接口等
2. application 应用层：定义应用服务
3. domain 领域层：定义聚合与领域服务
4. infrastructure 基础设施层：定义数据库、消息队列、缓存等基础设施

# 示例代码一

路径：github.com/practialddd，使用基于 springboot 框架的示例代码（Chapter 5）。

gitee 上有搬运，以 practicalddd 作为关键词检索即可

## 工程结构

``` 
工程分为四个独立部署的微服务
├─bookingms
├─handlingms
├─routingms
└─trackingms

每个微服务下，src/main/java/{ProjectName}

└─cargotracker({ProjectName})
    ├─bookingms(微服务名)
    │   ├─application(应用层)
    |   |   └─internal
    |   |       ├─commandservices
    |   |       ├─outboundservices
    |   |       └─queryservices
    │   ├─domain(领域层)
    |   |   └─model
    |   |       ├─aggregates
    |   |       ├─commands
    |   |       ├─entities
    |   |       └─valueobjects
    │   ├─infrastructure(基础设施层)
    |   |   ├─brokers
    |   |   └─repositories
    │   └─interfaces(接口层)
    |       └─rest
    |           ├─dto
    |           └─transform
    └─shareddomain
        ├─events
        └─model
```

## interface 层

在 interface 层中，可以定义对外提供的服务的方式，例如 REST 服务，或者传统的 SOAP 服务，此处的选择不影响领域内的服务。

在 REST 服务下，定义了 dto 和 transform 两层：

1. RESTful api 直接在 rest 包下定义，并未再单独建立一层
    * api 服务内没有业务逻辑，只有简单的对象转换
2. dto 包用于定义 RESTful api 所需要的输入对象和输出对象
3. transform 用于将 RESTful api 所需的 dto 对象转换为 service 所需的 command 对象
4. 一些使用 GET 方式的简单查询服务，api 服务直接将 RESTful url 参数转换为了 do 对象

## application 层

在 application 层中，可以定义对内提供的服务 internal，并将其按照 CQRS 的概念分拆。

application 层内是主要的业务逻辑，访问 infrastructure 层，操作 aggregate、entity 或 valueobject 对象：

1. queryservices：提供本地的查询服务
2. commandservices：提供本地的增删改服务
3. 以及 outboundservices：提供外围服务，可以理解为微服务远程调用，可以被 queryservice 或 commandservice 访问

## domain 层

在 domain 层中，定义了 application 层操作的对象：

1. aggregate（聚合）：聚合定义了微服务最主要的服务对象，包含 entity 和 valueobject
2. entity（实体）：定义了聚合包含的实体，实体是通过标识定义的，具有连续性
3. valueobject（值对象）：定义了聚合包含的值对象，值对象没有标识，只关心属性，无需复杂的标识
4. 以及 commands（命令）：定义了 commandservices 的传入对象

## infrastructure 层

在 infrastructure 层，定义了：

1. repositories：封装了本地数据库操作资源
2. brokers：消息队列中的 broker

# 示例代码二

路径：github.com/ouchuangxin/leave-sample，使用基于 springboot 框架的示例代码。

gitee 上有搬运，以 leave-sample 作为关键词检索即可

## 工程结构

```
工程为一个微服务：leave

在 src/main/java/{ProjectName} 目录下：

└─leave
    ├─application
    │  └─service
    ├─domain
    │  ├─leave
    │  │  ├─entity
    │  │  │  └─valueobject
    │  │  ├─event
    │  │  ├─repository
    │  │  │  ├─facade
    │  │  │  ├─mapper
    │  │  │  ├─persistence
    │  │  │  └─po
    │  │  └─service
    │  ├─person
    │  │  ├─entity
    │  │  │  └─valueobject
    │  │  ├─repository
    │  │  │  ├─facade
    │  │  │  ├─mapper
    │  │  │  ├─persistence
    │  │  │  └─po
    │  │  └─service
    │  └─rule
    │      ├─entity
    │      ├─repository
    │      │  ├─facade
    │      │  ├─mapper
    │      │  ├─persistence
    │      │  └─po
    │      └─service
    ├─infrastructure
    │  ├─client
    │  ├─common
    │  │  ├─api
    │  │  └─event
    │  └─util
    └─interfaces
        ├─assembler
        ├─dto
        └─facade
```

## interfaces 层

interface 层的划分与示例代码一基本相同：

1. facade ([fəˈsɑːd]) 包内定义了对外提供的 api 服务。值得一提的是，facade 设计模式（又称：门面模式、外观模式等）的内涵在于屏蔽内部接口的差异，对外提供统一的接口，较为符合对外提供 api 服务的内涵
    * api 服务内没有业务逻辑，只有简单的对象转换
2. dto 包内定义了入参和出参。其借鉴了 CQRS 的设计模式：
    * 将 query 服务的入参定义为 RESTful url 参数，出参定义为 dto 传输对象
    * 将 command 服务的入参定义为 dto 传输对象，出参定义为 RESTful http 响应码
3. assembler ([əˈsemblər]) 包内定义了 dto 和 do 的转换关系，其中包含两个静态方法：
    * toDO 方法将 interface 层处理的 dto 对象转换为 application 层处理的 do 对象（包括：aggregate root、entity、valueobject）
    * toDTO 方法将 application 层处理的 do 对象转换为 interface 层处理的 dto 对象

## application 层

application 层的划分与示例代码一有较大的不同：

1. application 层内按照 aggregate 进行了划分，并没有参考 CQRS 拆分出 queryservice 和 commandservice
2. application 层内定义 services 几乎没有逻辑加工，而是使用 do 对象直接调用 domain 层 services。实际上，在示例代码二中，也确实如此
3. application 层内按照其他微服务的 aggregate 划分了跨微服务的远程接口调用

## domain 层

domain 层的划分与示例代码一有较大的不同：

在 DDD 的概念中，domain 内需要将 entity（实体）按照一定的 bound（边界）进行 aggregate（聚合），以一个 entity 作为 aggregate root（聚合根）。跨 aggregate 仅可访问 aggregate root，而 aggregate 内部可以互相访问。

因此在示例代码二中，domain 层首先按照 aggregate root 进行了划分：leave、person、rule。

值得注意的是，此处的代码层次代表了对领域进行划分的结果，而不是思考的过程，要理解为何如此划分，需要寻找最初的设计。

domian 层在划分了 aggregate root 后，继续向下划分了：

1. entitiy：entity 包内定义了 domain 层所操作的 aggregate root、entity 和 valueobject 对象
    * aggregate root 是一个充血模型的 java class，存在简单的的业务逻辑
    * entity 一般是贫血模型的 java class
    * valueobject 一般是贫血模型的 java class、enum
    * aggregate root、entity、valueobject 中所有的变量，都使用缺省的 package 修饰符
2. service：定义了 domain services，且 domain service 内包含绝大多数的业务逻辑
    * application service 直接访问 domain service
    * domain service 也可以抽象出接口
    * domain service 访问本 aggregate 下的 repository
    * aggregate root、entity、valueobject 等对象与 po 的转换
3. repository：定义了 domain service 所需要使用的本地资源，包括数据库、缓存、消息等
    * facade：定义了 repository 层为 domain 层提供的服务，抽象为 interface
    * persistence：对 facade 定义接口的实现，不包含业务逻辑，访问 mapper
    * mapper：数据库访问 DAO 层，可以使用 JPA、Mybatis-Plus 等框架，依赖 po
    * po：数据库持久化对象，定义了 repository 层所需操作的 po 对象
4. event：定义了事件，可以理解为一种异步消息

## infrastructure 层

infrastructure 层的划分与示例代码一有较大的不同：

1. common：定义了公共方法，例如：响应码
2. utils：定义了公共方法，例如：日期格式转换、全局唯一流水号
3. client：定义了微服务远程调用
4. event：定义了微服务内存在的事件

# 示例代码三

路径：github.com/citerus/dddsample-core，使用基于 springboot 框架的示例代码。

此文档版本较久，仅供参考

gitee 上有搬运，以 dddsample-core 作为关键词检索即可

## 工程结构

```
工程为一个微服务：dddsample

在 src/main/java/{ProjectName} 目录下：

└─dddsample
    ├─application
    │  ├─impl
    │  └─util
    ├─config
    ├─domain
    │  ├─model
    │  │  ├─cargo
    │  │  ├─handling
    │  │  ├─location
    │  │  └─voyage
    │  ├─service
    │  └─shared
    │      └─experimental
    ├─infrastructure
    │  ├─messaging
    │  │  └─jms
    │  ├─persistence
    │  │  └─hibernate
    │  └─routing
    └─interfaces
        ├─booking
        │  ├─facade
        │  │  ├─dto
        │  │  └─internal
        │  │      └─assembler
        │  └─web
        ├─handling
        │  ├─file
        │  └─ws
        └─tracking
```

## interface 层

interface 层的划分与示例代码一、二基本相同，但由于是早期非前后端分离的工程，故保留了 web 层：

1. facade 定义 interface
2. impl 实现 interface
3. dto 定义 interface 所需的数据对象
4. assembler 将 interface 所需的 dto 对象转换为 service 所需的 do 对象（在 domain 层内定义），或者将 do 对象转换为 dto 对象



与示例代码一、二不同的是，此代码所定义的 dto 里，还包含一些基础 dto 经过转换后的组合对象，例如：

```java
public class SampleDTO implements Serializable {
    private final List<DTO> dto;

    public List<DTO> getDTO() {
        return Collections.unmodifiableList(dto);
    }    
}
```

而在示例代码一、二内，是直接在 RESTful api 层进行了类似的转换，并未单独定义一个新的 dto 对象

## config 层

较为早期的写法，使用 @Bean 和 @Autowired 注解来注入接口和实现类

## application 层

interface 层的划分与示例代码一基本相同：

1. service 定义 interface
2. event 定义 interface
3. impl 实现 interface，包含主要的业务逻辑，使用 domain 层对象，访用 domain 层
4. utils 定义公共方法

## domain 层

domain 层的划分与示例代码一、二均有较大差异：

1. shared：定义公共的 interface，包括：
    * entity、valueobject、domainevent、specification 等公共定义抽象出的 interface，其中包括一些抽象的方法，例如：
    
        * entity interface 抽象出 `boolean sameIdentityAs(T t);` 方法，其内涵是 entity 使用 id 来识别，当两个 entity 的 id 一致时，可以认为是同一个 entity
    
            ```java
            public interface Entity<T> {
            
              /**
               * Entities compare by identity, not by attributes.
               *
               * @param other The other entity.
               * @return true if the identities are the same, regardless of other attributes.
               */
              boolean sameIdentityAs(T other);
            
            }
            ```
    
        * valueobject interface 抽象出 `boolean sameValueAs(T t);` 方法，其内涵是 valueobject 使用 value 来识别，当两个 valueobject 的 value 完全相同时，可以认为是同一个 valueobject
    
            ```java
            public interface ValueObject<T> extends Serializable {
            
              /**
               * Value objects compare by the values of their attributes, they don't have an identity.
               *
               * @param other The other value object.
               * @return <code>true</code> if the given value object's and this value object's attributes are the same.
               */
              boolean sameValueAs(T other);
            
            }
            ```
    
        * domainevent interface 抽象出 `boolean sameEventAs(T t);` 方法，其内涵是 domainevent 是特殊的，并非 entity 或 valueobject，可以使用 id 或 value 来识别
    
            ```java
            /**
             * A domain event is something that is unique, but does not have a lifecycle.
             * The identity may be explicit, for example the sequence number of a payment,
             * or it could be derived from various aspects of the event such as where, when and what
             * has happened.
             */
            public interface DomainEvent<T> {
            
              /**
               * @param other The other domain event.
               * @return <code>true</code> if the given domain event and this event are regarded as being the same event.
               */
              boolean sameEventAs(T other);
            
            }
            ```
    
        * specification interface 抽象出 `boolean isSatisfiedBy(T t);` 、 `and` 、 `not` 、 `or` 四个方法，其内涵是符合特定格式的数据对象：
    
            ```java
            /**
             * Specificaiton interface.
             * <p/>
             * Use {@link se.citerus.dddsample.domain.shared.AbstractSpecification} as base for creating specifications, and
             * only the method {@link #isSatisfiedBy(Object)} must be implemented.
             */
            public interface Specification<T> {
            
              /**
               * Check if {@code t} is satisfied by the specification.
               *
               * @param t Object to test.
               * @return {@code true} if {@code t} satisfies the specification.
               */
              boolean isSatisfiedBy(T t);
            
              /**
               * Create a new specification that is the AND operation of {@code this} specification and another specification.
               * @param specification Specification to AND.
               * @return A new specification.
               */
              Specification<T> and(Specification<T> specification);
            
              /**
               * Create a new specification that is the OR operation of {@code this} specification and another specification.
               * @param specification Specification to OR.
               * @return A new specification.
               */
              Specification<T> or(Specification<T> specification);
            
              /**
               * Create a new specification that is the NOT operation of {@code this} specification.
               * @param specification Specification to NOT.
               * @return A new specification.
               */
              Specification<T> not(Specification<T> specification);
            }
            ```
    
    * 对 entity、valueobject、domainevent、specification 等对象抽象出的公共方法，但这些公共方法很少
    
1. model：定义了 application 层、domain 层操作的对象，按照 aggregate 进行划分，在每个 aggregate 内包括：
    * aggregate root：可以是 entity、domainevent 或 specification，并且可以引用其他的 aggregate root
    * entity、domainevent 或 specification：定义在 aggregate 内所需操作的对象，但不完全是贫血模型，也会提供一些额外的方法，主要用于对象的组合、转换、判断等
    * repository：定义在 aggregate 内所需使用的所有操作，是 interface 类型，具体的实现在 infrastructure 层
    * exception：定义在 aggregate 内需要使用的自定义的 exception
    
3. service：定义 domain service interface，可以由 application 层实现，也可以由 infrastructure 层实现

## infrastructure 层

infrastructure 层的划分与示例代码一、二均有较大差异：

1. messaging：提供消息服务
2. persistence：提供持久化服务
3. routing：提供路由服务
