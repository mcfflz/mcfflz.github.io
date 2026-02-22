---
date: 2026-02-12T12:00:00+08:00
title: Javascript
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

# DOM 树

js可以操作 html dom 树

# JavaScript 简介

在 HTML 中，JavaScript 语句是由 web 浏览器“执行”的“指令”。

## JavaScript 基本功能

JavaScript 能够改变 HTML 内容：

```javascript
document.getElementById("demo").innerHTML = "Hello JavaScript";
```

JavaScript 能够改变 HTML 属性：

```javascript
document.getElementById('myImage').src='/i/eg_bulbon.gif';
```

JavaScript 能够改变 CSS 样式：

```javascript
document.getElementById("demo").style.fontSize = "25px";
```

## JavaScript 事件和函数

JavaScript **函数** 是一种 JavaScript 代码块，它可以在调用时被执行。

JavaScript **事件** 是一种 触发方式，当事件触发时调用函数，比如当用户点击按钮时。

# JavaScript 常见使用

## 显示数据

JavaScript 不提供任何内建的打印或显示函数。JavaScript 能够以不同方式“显示”数据：

* 使用 window.alert() 写入警告框
* 使用 document.write() 写入 HTML 输出（提示：document.write() 方法仅用于测试）
* 使用 innerHTML 写入 HTML 元素
* 使用 console.log() 写入浏览器控制台

## 代码块

JavaScript 语句可以用花括号（{...}）组合在代码块中。

代码块的作用是定义一同执行的语句。

您会在 JavaScript 中看到成块组合在一起的语句：

```javascript
function myFunction() {
    document.getElementById("demo").innerHTML = "Hello Kitty.";
    document.getElementById("myDIV").innerHTML = "How are you?";
}
```

# 声明变量

## var

### undefined

在计算机程序中，被声明的变量经常是不带值的。值可以是需被计算的内容，或是之后被提供的数据，比如数据输入。

不带有值的变量，它的值将是 undefined。

变量 variable 在这条语句执行后的值是 undefined：

```javascript
var variable;
```

### 重复声明变量

如果再次声明某个 JavaScript 变量，将不会丢它的值。

```javascript
var variable = "Hello JavaScript";
var variable;
```

## let

可以使用 let 关键词声明拥有块作用域的变量。

```javascript
let i = 7;
for (let i = 0; i < 10; i++) {
  // 此处 i 循环 0-10
}
// 此处 i 为 7
```

通过 let 关键词定义的全局变量不属于 window 对象：

```javascript
let carName = "porsche";
// 此处的代码不可使用 window.carName
```

## const

通过 const 定义的变量与 let 变量类似，有相同的作用域。

关键字 const 有一定的误导性：

* **它没有定义常量值。它定义了对值的常量引用。**
* **因此，我们不能更改常量原始值，但我们可以更改常量对象的属性。**

举例如下：

常量对象可以更改：

```javascript
// 您可以创建 const 对象：
const car = {type:"porsche", model:"911", color:"Black"};

// 您可以更改属性：
car.color = "White";

// 您可以添加属性：
car.owner = "Bill";
```

但是无法重新为常量对象赋值：

```javascript
const car = {type:"porsche", model:"911", color:"Black"};
car = {type:"Volvo", model:"XC60", color:"White"};    // ERROR
```

常量数组可以更改：

```javascript
// 您可以创建常量数组：
const cars = ["Audi", "BMW", "porsche"];

// 您可以更改元素：
cars[0] = "Honda";

// 您可以添加元素：
cars.push("Volvo");
```

但是无法重新为常量数组赋值：

```javascript
const cars = ["Audi", "BMW", "porsche"];
cars = ["Honda", "Toyota", "Volvo"];    // ERROR
```

## 提升

通过 var 定义的变量会被提升到顶端。

您可以在声明 var 变量之前就使用它：

```javascript
carName = "Volvo";    // 您可以在此处使用 carName
var carName;
```

通过 const 定义的变量不会被提升到顶端。

const 变量不能在声明之前使用：

```javascript
carName = "Volvo";    // 您不可以在此处使用 carName
const carName = "Volvo";
```

# 数据类型

字符串值，数值，布尔值，数组，对象。

Undefined 与 null 的值相等，但类型不相等。

# 函数

## 函数定义

JavaScript 函数是被设计为执行特定任务的代码块。

```javascript
function funcName(para1, para2, para3) {
    // 要执行的代码
}
```

JavaScript 函数会在某代码调用它时被执行。

在其他编程语言中，函数近似程序（Procedure）或子程序（Subroutine）。

## 函数执行

函数中的代码将在其他代码调用该函数时执行：

- 当事件发生时（当用户点击按钮时）
- 当 JavaScript 代码调用时
- 自动的（自调用）

## 函数调用

使用 () 运算符调用函数。不使用 () 访问函数将返回函数声明而不是函数结果。

```javascript
function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
}

document.getElementById("demo").innerHTML = toCelsius(86);
// 返回 30
document.getElementById("demo").innerHTML = toCelsius;
// 返回 function toCelsius(fahrenheit) { return (5/9) * (fahrenheit-32); }
```

## 函数返回

当 JavaScript 到达 return 语句，函数将停止执行。

如果函数被某条语句调用，JavaScript 将在调用语句之后“返回”执行代码。

函数通常会计算出返回值。这个返回值会返回给调用者：

```javascript
var x = myFunction(7, 8);        // 调用函数，返回值被赋值给 x

function myFunction(a, b) {
    return a * b;                // 函数返回 a 和 b 的乘积
}
```

## this

在函数定义中，this 引用该函数的“拥有者”。

```javascript
var person = {
  firstName: "Bill",
  lastName : "Gates",
  id       : 678,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```

# 对象

## 概述

对象也是变量。但是对象包含很多值。

值以 名称(key):值(value) 对的方式来书写（名称和值由冒号分隔）。

JavaScript 对象是被命名值的容器。

```javascript
var car = {type:"porsche", model:"911", color:"white"};
```

如果通过关键词 "new" 来声明 JavaScript 变量，则该变量会被创建为对象：

```javascript
var x = new String();        // 把 x 声明为 String 对象
var y = new Number();        // 把 y 声明为 Number 对象
var z = new Boolean();       //	把 z 声明为 Boolean 对象
```

## 对象方法

对象也可以有方法。

方法以函数定义被存储在属性中。

```javascript
var person = {
  firstName: "Bill",
  lastName : "Gates",
  id       : 678,
  fullName : function() {
    return this.firstName + " " + this.lastName;
  }
};
```

## 访问对象属性

```javascript
// 方法1：objectName.propertyName;
person.lastName;
// 方法2：objectName["propertyName"];
person["lastName"];
```

## 访问对象方法

```javascript
// objectName.methodName()
name = person.fullName();
```

# 事件

## HTML 事件

HTML 事件是发生在 HTML 元素上的“事情”。HTML 事件可以是浏览器或用户做的某些事情。

下面是 HTML 事件的一些例子：

- HTML 网页完成加载
- HTML 输入字段被修改
- HTML 按钮被点击

通常，当事件发生时，用户会希望做某件事。

当在 HTML 页面中使用 JavaScript 时，JavaScript 能够“应对”这些事件。JavaScript 允许您在事件被侦测到时执行代码。

通过 JavaScript 代码，HTML 允许您向 HTML 元素添加事件处理程序。

```html
<button onclick='document.getElementById("demo").innerHTML=Date()'>现在的时间是？</button>
<p id="demo"></p>
```

## 事件调用函数

JavaScript 代码通常有很多行。事件属性调用函数更为常见：

```html
<button onclick="displayDate()">现在的时间是？</button>
<p id="demo"></p>
<script>
    function displayDate(){
        document.getElementById("demo").innerHTML = Date();
    }
</script>
```

# 字符串

## length 属性

内建属性 length 可返回字符串的长度：

```javascript
var txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
var sln = txt.length;
```

## indexOf(*para*, *start*) 方法

indexOf(para, index) 方法返回字符串中指定文本首次出现的索引（位置）：

start 定义了查找开始的位置，默认为0，即从头开始。

```javascript
var str = "The full name of China is the People's Republic of China.";
var pos = str.indexOf("China");
// 返回 17
```

如果未找到文本， indexOf() 返回 -1。

## lastIndexOf(*para*, *start*) 方法

lastIndexOf(para, start) 方法返回指定文本在字符串中最后一次出现的索引（位置）：

start 定义了查找开始的位置，默认为0，即从头开始。

```javascript
var str = "The full name of China is the People's Republic of China.";
var pos = str.lastIndexOf("China");
// 返回 51
```

如果未找到文本， lastIndexOf() 返回 -1。

## search(*para*) 方法

search(para) 方法搜索特定值的字符串，并返回匹配的位置：

```javascript
var str = "The full name of China is the People's Republic of China.";
var pos = str.search("china");
// 返回 17
```

如果未找到文本， search() 返回 -1。

## slice(*start*, *end*) 方法

slice() 提取字符串的某个部分并在新字符串中返回被提取的部分。

```javascript
var str = "Apple, Banana, Mango";
var res = str.slice(7,13);
// res 的值为 Banana
```

如果某个参数为负，则从字符串的结尾开始计数。

```javascript
var str = "Apple, Banana, Mango";
var res = str.slice(7,-7);
// res 的值为 Banana
```

如果省略 end 参数，则该方法将裁剪字符串的剩余部分：

```javascript
var str = "Apple, Banana, Mango";
var res = str.slice(7);
// res 的值为 Banana, Mango
```

## substring(*start*, *end*) 方法

substring() 类似于 slice()。但 substring() 无法接受负的索引。

## substr(*start*, *length*) 方法

substr() 类似于 slice()。

不同之处在于第二个参数规定被提取部分的长度。

```javascript
var str = "Apple, Banana, Mango";
var res = str.substr(7,6);
// res 的值为 Banana
```

第二个参数不能为负，因为它定义的是长度。

## replace(*para1*, *para2*) 方法

replace() 方法用另一个值替换在字符串中指定的值：

```javascript
str = "Please visit Microsoft!";
var n = str.replace("Microsoft", "W3School");
```

默认地，replace() 对大小写敏感，如需执行大小写不敏感的替换，请使用正则表达式 /i（大小写不敏感）。

## toUpperCase() 方法

通过 toUpperCase() 把字符串转换为大写：

```javascript
var text1 = "Hello World!";       // 字符串
var text2 = text1.toUpperCase();  // text2 是被转换为大写的 text1
// text2 的值为 HELLO WORLD!
```

## toLowerCase() 方法

通过 toLowerCase() 把字符串转换为小写：

```javascript
var text1 = "Hello World!";       // 字符串
var text2 = text1.toLowerCase();  // text2 是被转换为小写的 text1
// text2 的值为 hello world!
```

## concat() 方法

concat() 连接两个或多个字符串，可用于代替加运算符：

```javascript
var text1 = "Hello";
var text2 = "World";
var text3 = text1.concat(" ",text2);
var text4 = "Hello" + " " + "World!";
// text3 和 text4 是等效的，均为 Hello World!
```

## trim() 方法

trim() 方法删除字符串两端的空白符：

```javascript
var str1 = "       Hello World!        ";
var str2 = str.trim();
// str2 的值为 Hello World!
```

## charAt(*position*) 方法

charAt() 方法返回字符串中指定下标（位置）的字符串：

```javascript
var str = "HELLO WORLD";
str.charAt(0);
// 返回 H
```

## charCodeAt(*position*) 方法

charCodeAt() 方法返回字符串中指定索引的字符 unicode 编码：

```javascript
var str = "HELLO WORLD";
str.charCodeAt(0);
// 返回 72
```

## split(*para*) 方法

可以通过 split(*para*) 将字符串按照 para 分割转换为数组：

```javascript
var txt = "a,b,c,d,e";   // 字符串
txt.split(",");          // 用逗号分隔 返回数组 ["a", "b", "c", "d", "e"]
txt.split(" ");          // 用空格分隔 返回数组 ["a,b,c,d,e"]
txt.split("|");          // 用竖线分隔 返回数组 ["a,b,c,d,e"]
```

如果省略分隔符，被返回的数组将包含 index [0] 中的整个字符串。

如果分隔符是 ""，被返回的数组将是间隔单个字符的数组。

## includes(*searchvalue*, *start*) 方法

如果字符串包含指定值，includes() 方法返回 true。

```javascript
let text = "Hello world, welcome to the universe.";
text.includes("world");
// 返回 true
```

start 默认为 0，开始搜索的位置。

## startsWith(*searchvalue*, *start*) 方法

如果字符串以指定值开头，则 startsWith() 方法返回 true，否则返回 false：

```javascript
let text = "Hello world, welcome to the universe.";
text.startsWith("Hello");
// 返回 true
```

## endswith(*searchvalue*, *length*) 方法

如果字符串以指定值结尾，则 endsWith() 方法返回 true，否则返回 false：

```javascript
var text = "John Doe";
text.endsWith("Doe");
// 返回 true
```

## 字符串对象

字符串可以是对象，但请不要把字符串创建为对象。它会拖慢执行速度。

```javascript
var x = "Bill";
var y = new String("Bill");

// typeof x 将返回 string
// typeof y 将返回 object
```

JavaScript 对象无法进行对比，比较两个 JavaScript 将始终返回 false。

```javascript
var x = new String("Bill");
var y = new String("Bill");
// (x == y) 为 false，因为 x 和 y 是不同的对象
```

## 字符串模板

### 模板字面量

模板字面量使用反引号 (``) 而不是引号 ("") 来定义字符串：

```javascript
let text = `He's often called "Johnny"`;
```

通过使用模板字面量，您可以在字符串中同时使用单引号和双引号。

### 插值

模板字面量提供了一种将变量和表达式插入字符串的简单方法。

该方法称为字符串插值（string interpolation）。

```javascript
let firstName = "John";
let lastName = "Doe";

let text = `Welcome ${firstName}, ${lastName}!`;
```

# 数值

## 概述

JavaScript 只有一种数值类型。书写数值时带不带小数点均可。

与许多其他编程语言不同，JavaScript 不会定义不同类型的数，比如整数、短的、长的、浮点的等等。

JavaScript 数值始终以双精度浮点数来存储，根据国际 IEEE 754 标准。

此格式用 64 位存储数值，其中 0 到 51 存储数字（片段），52 到 62 存储指数，63 位存储符号：

![image-20211122141133058](D:/Codes/study-notes/javaScript.assets/image-20211122141133058.png)

整数（不使用指数或科学计数法）会被精确到 15 位。

```javascript
var x = 999999999999999;   // x 将是 999999999999999
var y = 9999999999999999;  // y 将是 10000000000000000
```

小数的最大数是 17 位，但是浮点的算数并不总是 100% 精准：

```javascript
var x = 0.2 + 0.1;
// x 将是 0.30000000000000004
```



## NaN - 非数值

NaN 属于 JavaScript 保留词，指示某个数不是合法数。

NaN 是数值，typeof NaN 返回 number。

## Infinity

Infinity （或 -Infinity）是 JavaScript 在计算数时超出最大可能数范围时返回的值。

除以 0（零）也会生成 Infinity。

Infinity 是数值：typeOf Infinity 返回 number。

## 十六进制

JavaScript 会把前缀为 0x 的数值常量解释为十六进制。

## 数值对象

数值可以是对象，通过关键词 new 定义为对象：var y = new Number(123)。

## toString() 方法

toString() 以字符串返回数值。

```javascript
var x = 123;
x.toString();            // 从变量 x 返回 123的字符串
```

## toExponential(*length*) 方法

toExponential() 返回字符串值，它包含已被四舍五入并使用指数计数法的数字。参数定义小数点后的字符数：

```javascript
var x = 9.656;
x.toExponential(2);     // 返回 9.66e+0
x.toExponential(4);     // 返回 9.6560e+0
x.toExponential(6);     // 返回 9.656000e+0
```

如果 length 没有设置，JavaScript 不会对数字进行舍入。

## toFixed(*length*) 方法

toFixed() 返回字符串值，它包含了被四舍五入并指定位数小数的数字：

```javascript
var x = 9.656;
x.toFixed(0);           // 返回 10
x.toFixed(2);           // 返回 9.66
x.toFixed(4);           // 返回 9.6560
x.toFixed(6);           // 返回 9.656000
```

如果 length 没有设置，JavaScript 不会对数字进行舍入。

## toPrecision(*length*) 方法

toPrecision() 返回字符串值，它包含了被四舍五入并指定长度的数字：

```javascript
var x = 9.656;
x.toPrecision();        // 返回 9.656
x.toPrecision(2);       // 返回 9.7
x.toPrecision(4);       // 返回 9.656
x.toPrecision(6);       // 返回 9.65600
```

如果 length 没有设置，JavaScript 不会对数字进行舍入。

## valueOf() 方法

valueOf() 以数值返回数值：

```javascript
var x = 123;
x.valueOf();            // 从变量 x 返回 123
```

## Number() 方法

Number() 可用于把 JavaScript 变量转换为数值：

```javascript
x = true;
Number(x);        // 返回 1
x = false;     
Number(x);        // 返回 0
x = new Date();
Number(x);        // 返回 1404568027739
x = "10"
Number(x);        // 返回 10
x = "10 20"
Number(x);        // 返回 NaN
```

如果无法转换数字，则返回 NaN。

## parseInt() 方法

parseInt() 解析一段字符串并返回数值。允许空格。只返回首个数字：

```javascript
parseInt("10");         // 返回 10
parseInt("10.33");      // 返回 10
parseInt("10 20 30");   // 返回 10
parseInt("10 years");   // 返回 10
parseInt("years 10");   // 返回 NaN
```

## parseFloat() 方法

parseFloat() 解析一段字符串并返回数值。允许空格。只返回首个数字：

```javascript
parseFloat("10");        // 返回 10
parseFloat("10.33");     // 返回 10.33
parseFloat("10 20 30");  // 返回 10
parseFloat("10 years");  // 返回 10
parseFloat("years 10");  // 返回 NaN
```

## MAX_VALUE 属性

返回 JavaScript 中可能的最大数。属于名为 Number 的 JavaScript 数字对象包装器。

```javascript
var x = Number.MAX_VALUE;
// x 的值为 1.7976931348623157e+308
```

## MIN_VALUE 属性

返回 JavaScript 中可能的最小数。属于名为 Number 的 JavaScript 数字对象包装器。

```javascript
var x = Number.MIN_VALUE;
// x 的值为 5e-324
```

## POSITIVE_INFINITY 属性

表示负的无穷大（溢出返回）。属于名为 Number 的 JavaScript 数字对象包装器。

```javascript
var x = Number.POSITIVE_INFINITY;
// x 的值为 Infinity
```

## NEGATIVE_INFINITY 属性

表示无穷大（溢出返回）。属于名为 Number 的 JavaScript 数字对象包装器。

```javascript
var x = Number.NEGATIVE_INFINITY;
// x 的值为 -Infinity
```

## NaN 属性

表示非数字值（"Not-a-Number"）。属于名为 Number 的 JavaScript 数字对象包装器。

```javascript
var x = Number.NaN;
// x 的值为 NaN
```

# 数组

JavaScript 数组用于在单一变量中存储多个值。

数组是对象：

可以直接定义数组，或使用 new Array() 来定义数组。

```javascript
var cars1 = ["Saab", "Volvo", "BMW"];
var cars2 = new Array("Saab", "Volvo", "BMW");
// 以上两个例子效果完全一样。
```

## length 属性

length 属性返回数组的长度（数组元素的数目）。

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.length;
// fruits 的长度是 4
```

## 遍历数组

遍历数组的最安全方法是使用 "for" 循环：

```javascript
fruits = ["Banana", "Orange", "Apple", "Mango"];
fLen = fruits.length;
text = "<ul>";
for (i = 0; i < fruits.length; i++) {
     text += "<li>" + fruits[i] + "</li>";
} 
```

## isArray(*array*) 方法

返回 array 是否为数组

```javascript
fruits = ["Banana", "Orange", "Apple", "Mango"];
Array.isArray(fruits);     // 返回 true
```

自己创建 isArray() 方法：

```javascript
function isArray(x) {
    return x.constructor.toString().indexOf("Array") > -1;
}
```

## toString() 方法

toString() 把数组转换为数组值（逗号分隔）的字符串。

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.toString(); 
// 返回值为 "Banana,Orange,Apple,Mango"
```

## join(*split*) 方法

join() 方法也可将所有数组元素结合为一个字符串，但还可以规定分隔符：。

```javascript
var fruits = ["Banana", "Orange","Apple", "Mango"];
fruits.join(" * "); 
// 返回 Banana * Orange * Apple * Mango
```

## pop() 方法

pop() 方法从数组中删除最后一个元素，返回“被弹出”的值：：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.pop();
// fruits 的值为 ["Banana", "Orange", "Apple"]
// 返回值为 "Mango"
```

## push(*para*) 方法

向数组添加新元素的最佳方法是使用 push() 方法，返回新数组的长度：：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.push("Lemon");
// fruits 的值为 ["Banana", "Orange", "Apple", "Mango", "Lemon"]
// 返回值为 5
```

## shift() 方法

shift() 方法会删除首个数组元素，并把所有其他元素“位移”到更低的索引，返回被“位移出”的字符串：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.shift();
// fruits 的值为 ["Orange", "Apple", "Mango"]
// 返回值为 "Banana"
```

## unshift(*para*) 方法

unshift() 方法（在开头）向数组添加新元素，并“反向位移”旧元素，返回新数组的长度：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.unshift("Lemon");
// fruits 的值为 ["Lemon", "Banana", "Orange", "Apple", "Mango"];
// 返回值为 5
```

## delete 方法

数组属于对象，其中的元素就可以使用 JavaScript delete 运算符来删除：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
delete fruits[0];
// fruits 的值为 [undefined, "Orange", "Lemon", "Kiwi"]
```

## splice(*start*, *delete*, *paras*) 方法

splice() 方法可用于向数组添加新项：

start 定义插入位置； delete 定义删除数量； paras 定义添加的元素。

返回一个包含已删除项的数组：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 2, "Lemon", "Kiwi");
// fruits 的值为 ["Banana", "Orange", "Lemon", "Kiwi"]
// 返回值为 ["Apple", "Mango"]
```

## concat(array1, array2 , ...) 方法

concat() 方法通过合并（连接）现有数组来创建一个新数组，可以使用任意数量的数组参数：

```javascript
var myGirls = ["Cecilie", "Lone"];
var myBoys1 = ["Emil", "Tobias", "Linus"];
var myBoys2 = ["zhangsan", "lisi"]
var myChildren = myGirls.concat(myBoys1, myBoys2);
// myChildren 的值为 ["Cecilie", "Lone", "Emil", "Tobias", "Linus", "zhangsan", "lisi"]
```

## slice(*start*, *end*) 方法

slice() 方法创建新数组。它不会从源数组中删除任何元素。

```javascript
var fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
var citrus = fruits.slice(3); 
// citrus 的值为 ["Apple", "Mango"]
```

## sort() 方法

sort() 方法以字母顺序对数组进行排序：

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();
// fruits 的值为 ["Apple", "Banana", "Mango", "Orange"]
```

默认地，sort() 函数按照字符串顺序对值进行排序。因此在对数值进行排序时，会出现"2"在"100"之后的情况

可以通过比值函数来修正此问题：

```javascript
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b}); 
// points 的值为 [1, 5, 10, 25, 40, 100]
```

## reverse() 方法

reverse() 方法反转数组中的元素。

```javascript
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.reverse();
// fruits 的值为 ["Mango", "Apple", "Orange", "Banana"]
```

sort() 和 reverse() 方法可以实现倒排序

## Math.max.apply() 方法

可以使用 Math.max.apply 来查找数组中的最高值：

```javascript
var points = [40, 100, 1, 5, 25, 10];
Math.max.apply(null, points);
// 返回值为 100
```

## Math.min.apply() 方法

可以使用 Math.min.apply 来查找数组中的最低值：

```javascript
var points = [40, 100, 1, 5, 25, 10];
Math.min.apply(null, points);
// 返回值为 1
```

## forEach() 方法

forEach() 方法为每个数组元素调用一次函数（回调函数）

## map() 方法

## filter() 方法

## reduce() 方法

## reduceRight() 方法

## every() 方法

## some() 方法

## indexOf() 方法

## lastIndexOf() 方法

## find() 方法

## findIndex() 方法

# 回调

回调是作为参数传递给另一个函数的函数。

将函数作为参数传递时，请记住不要使用括号。

```javascript
function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

function myCalculator(num1, num2, myCallback) {
  let sum = num1 + num2;
  myCallback(sum);
}

myCalculator(5, 5, myDisplayer);
```

# AJAX

![AJAX](D:/Codes/study-notes/javaScript.assets/ajax.gif)

1. 网页中发生一个事件（页面加载、按钮点击）
2. 由 JavaScript 创建 XMLHttpRequest 对象
3. XMLHttpRequest 对象向 web 服务器发送请求
4. 服务器处理该请求
5. 服务器将响应发送回网页
6. 由 JavaScript 读取响应
7. 由 JavaScript 执行正确的动作（比如更新页面）

## 创建 XMLHttpRequest 对象

```javascript
variable = new XMLHttpRequest();
```

## XMLHttpRequest 对象方法

| 方法                                          | 描述                                                         |
| :-------------------------------------------- | :----------------------------------------------------------- |
| new XMLHttpRequest()                          | 创建新的 XMLHttpRequest 对象                                 |
| abort()                                       | 取消当前请求                                                 |
| getAllResponseHeaders()                       | 返回头部信息                                                 |
| getResponseHeader()                           | 返回特定的头部信息                                           |
| open(*method*, *url*, *async*, *user*, *psw*) | 规定请求method：<br />请求类型 GET 或 POST<br />url：文件位置<br />async：true（异步）或 false（同步）<br />user：可选的用户名称<br />psw：可选的密码 |
| send()                                        | 将请求发送到服务器，用于 GET 请求                            |
| send(*string*)                                | 将请求发送到服务器，用于 POST 请求                           |
| setRequestHeader()                            | 向要发送的报头添加标签/值对                                  |

## XMLHttpRequest 对象属性

| 属性               | 描述                                                         |
| :----------------- | :----------------------------------------------------------- |
| onreadystatechange | 定义当 readyState 属性发生变化时被调用的函数                 |
| readyState         | 保存 XMLHttpRequest 的状态。<br />0：请求未初始化<br />1：服务器连接已建立<br />2：请求已收到<br />3：正在处理请求<br />4：请求已完成且响应已就绪 |
| responseText       | 以字符串返回响应数据                                         |
| responseXML        | 以 XML 数据返回响应数据                                      |
| status             | 返回请求的状态号<br />200: "OK"<br />403: "Forbidden"<br />404: "Not Found" |
| statusText         | 返回状态文本（比如 "OK" 或 "Not Found"）                     |

## open()

```javascript
xhttp.send();        // 向服务器发送请求（用于 GET）
xhttp.send(String);  // 向服务器发送请求（用于 POST）
```

## async

如需异步发送请求，open() 方法的 async 参数必须设置为 true。

尽量不要发送同步请求。

## setRequestHeader(*key*, *value*)

通过 setRequestHeader() 添加一个 HTTP 头部

## onreadystatechange

readyState 属性存留 XMLHttpRequest 的状态。

onreadystatechange 属性定义当 readyState 发生变化时执行的函数。

status 属性和 statusText 属性存有 XMLHttpRequest 对象的状态。

每当 readyState 发生变化时就会调用 onreadystatechange 函数。

当 readyState 为 4，status 为 200 时，响应就绪：

```javascript
function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("demo").innerHTML =
            this.responseText;
       }
    };
    xhttp.open("GET", "ajax_info.txt", true);
    xhttp.send(); 
} 
```

## 回调函数

如果您的网站中有多个 AJAX 任务，那么您应该创建一个执行 XMLHttpRequest 对象的函数，以及一个供每个 AJAX 任务的回调函数。

```javascript
loadDoc("url-1", myFunction1);

loadDoc("url-2", myFunction2);

function loadDoc(url, callback) {
  var xhttp;
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      callback(this);
    }
  };
  xhttp.open("GET", url, true);
  xhttp.send();
}

function myFunction1(xhttp) {
  // action goes here
 } 
function myFunction2(xhttp) {
  // action goes here
 } 
```

## responseText

responseText 属性以 JavaScript 字符串的形式返回服务器响应

## responseXML

ResponseXML 属性以 XML DOM 对象返回服务器响应。

## getAllResponseHeaders()

getAllResponseHeaders() 方法返回所有来自服务器响应的头部信息。

## getResponseHeader()

getResponseHeader() 方法返回来自服务器响应的特定头部信息。

# JSON

## json 解析

```javascript
jsonObject = JSON.parse(string);
```

## json 字符串化

```javascript
string = JSON.stringify(jsonObject);
```

