# Thymeleaf官网

https://www.thymeleaf.org/

# 模板引擎

![模板引擎](E:/study-notes/thymeleaf.assets/%E6%A8%A1%E6%9D%BF%E5%BC%95%E6%93%8E.png)



# spring mvc model

```java
/* 
	参数：Model 可以存放数据，放入request作用域
	返回值：String 表示视图
 */
public String hello(Model model){
    // 添加数据
    model.addAttribute("key", "value");
    // 指定模板视图
    return "view";
}
```

