CSS 指层叠样式表 (**C**ascading **S**tyle **S**heets)

# css 基础语法

CSS 规则由两个主要的部分构成：选择器，以及一条或多条声明:

![img](D:/Codes/study-notes/632877C9-2462-41D6-BD0E-F7317E4C42AC.jpg)

# css 选择器

## id 选择器

```css
#idName {
    /* 样式 */
}
<div id="idName"></div>
```



## class 选择器

```css
.classValue {
    /* 样式 */
}
<div class="classValue"></div>
```



## 标签选择器

```css
htmlTag {
    /* 包括 html 中可以使用的几乎所有的标签 */
    /* 样式 */
}

htmlTag.classValue {
    /* 为所有 htmlTag 标签的 class="classValue" 添加样式 */
}
```



## 组合选择器

```css
/*
后代选择器(以空格   分隔)：后代选择器用于选取某元素的后代元素。
子元素选择器(以大于 > 号分隔）：与后代选择器相比，子元素选择器（Child selectors）只能选择作为某元素直接/一级子元素的元素。
相邻兄弟选择器（以加号 + 分隔）：相邻兄弟选择器（Adjacent sibling selector）可选择紧接在另一元素后的元素，且二者有相同父元素。
后续兄弟选择器（以波浪号 ～ 分隔）：后续兄弟选择器选取所有的指定元素之后的兄弟元素。
*/
div p {}
div>p {}
div+p {}
div~p {}
```



## 属性选择器

```css
[attributeName] {
    /* 样式 */
}

[attributeName=attributeValue] {
    /* 属性和值选择器 */
    /* 样式 */
}

[attributeName~=attributeValue] {
    /* 属性和值选择器，~代表通配符 */
    /* 样式 */
}

[attributeName|=attributeValue] {
    /* 属性和值选择器，|代表起始位置 */
    /* 样式 */
}

htmlTag[attributeName...] {
    /* 属性和值选择器，支持和标签的组合使用 */
    /* 样式 */    
}
```



# css 优先级

（内联样式）Inline style > （内部样式）Internal style sheet >（外部样式）External style sheet > 浏览器默认样式

# css 伪类

# css 伪元素

**伪类**选择元素基于的是当前元素处于的状态，或者说元素当前所具有的特性，而不是元素的id、class、属性等静态的标志。由于状态是动态变化的，所以一个元素达到一个特定状态时，它可能得到一个伪类的样式；当状态改变时，它又会失去这个样式。由此可以看出，它的功能和class有些类似，但它是基于文档之外的抽象，所以叫伪类。

与伪类针对特殊状态的元素不同的是，**伪元素**是对元素中的特定内容进行操作，它所操作的层次比伪类更深了一层，也因此它的动态性比伪类要低得多。实际上，设计伪元素的目的就是去选取诸如元素内容第一个字（母）、第一行，选取某些内容前面或后面这种普通的选择器无法完成的工作。它控制的内容实际上和元素是相同的，但是它本身只是基于元素的抽象，并不存在于文档中，所以叫伪元素。



# border-radius

