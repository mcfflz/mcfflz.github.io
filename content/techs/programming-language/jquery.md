# 文档就绪函数

所有 jQuery 函数位于一个 document ready 函数中：

```javascript
$(document).ready(function(){

--- jQuery functions go here ----

});
```

这是为了防止文档在完全加载（就绪）之前运行 jQuery 代码。

如果在文档没有完全加载之前就运行函数，操作可能失败。下面是两个具体的例子：

- 试图隐藏一个不存在的元素
- 获得未完全加载的图像的大小

# jQuery 选择器

## id 选择器

$("#id") 选取所有 id="id" 的元素。

## class 选择器

$(".class") 选取所有 class="class" 的元素。

## 标签选择器

$("HtmlTag") 选取所有标签为 <HtmlTag> 的元素。

## 组合

例如：

$("p.intro") 选取所有 class="intro" 的 <p> 元素。

$("p#demo") 选取所有 id="demo" 的 <p> 元素。

# jQuery 事件

**jQuery 是为事件处理特别设计的。**

jQuery 事件处理方法是 jQuery 中的核心函数。

事件处理程序指的是当 HTML 中发生某些事件时所调用的方法。术语由事件“触发”（或“激发”）经常会被使用。

通常会把 jQuery 代码放到 <head>部分的事件处理方法中：