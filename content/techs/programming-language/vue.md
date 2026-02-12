# vue cli 脚手架

[webpack](https://webpack.js.org/)

[Vue CLI (vuejs.org)](https://cli.vuejs.org/zh/)

[axios中文网|axios API 中文文档 | axios (axios-js.com)](http://www.axios-js.com/)

[Element Plus - The world's most popular Vue 3 UI framework (gitee.io)](https://element-plus.gitee.io/#/zh-CN)



https://zhuanlan.zhihu.com/p/342569137

# echarts

[Handbook - Apache ECharts](https://echarts.apache.org/handbook/zh/get-started/)

## 下载

```bash
npm install -g @vue/cli
npm install -g webpack
npm install axios --save
npm install element-plus --save



vue init webpack projectname
```



## element ui plus

```html
<!-- 引入样式 -->
<link rel="stylesheet" href="https://unpkg.com/element-plus/lib/theme-chalk/index.css">
<!-- 引入组件库 -->
<script src="https://unpkg.com/element-plus/lib/index.full.js"></script>
```



# vue 2 和 vue 3 的区别

## 创建应用实例

### vue 2

[vue 2 介绍 — Vue.js (vuejs.org)](https://cn.vuejs.org/v2/guide/index.html)

```html
<script>
    // vue 2
    var app = new Vue({
        el: "#app",
        data: {
            //data
        },
        methods: {
            methodName:function();
        }
    })
</script>
```



### vue 3

[vue 3 介绍 | Vue.js (vuejs.org)](https://v3.cn.vuejs.org/guide/introduction.html)

```html
<script>
    // vue 3
    const app = Vue.createApp({
        data() {
            return {
                //data
            }
        },
        methonds: {
            methodName(){}
        },
        computed: {
            conputedName(){}
        },
        watch: {
            watchName(){}
        }
    });
    const vm = app.mount("#app")
</script>
```



## vue 3 新特性

### 计算

```html
<script>
    Vue.createApp({
        computed: {
            computedName(){}
        }
    })
</script>
```



### 侦听器

```html
<script>
    Vue.createApp({
        watch: {
            watchName(){}
        }
    })
</script>
```



### 防抖和节流

[Data Property 和方法 | Vue.js (vuejs.org)](https://v3.cn.vuejs.org/guide/data-methods.html#防抖和节流)

# vue 的特点

1. 不再操作 DOM 元素，页面由数据生成
2. 

## vue 引用

```html
<script src="https://unpkg.com/vue@next"></script>
```



# API 参考

[API | Vue.js (vuejs.org)](https://v3.cn.vuejs.org/api/)

# el: 挂载点

[黑马程序员VUE经典视频-4小时+5个拣选案例让你快速入门Vue.js-想学习vue的童鞋可以围观了_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1HE411e7vY?p=4)

## 基本描述

1. vue el 的作用？

   > 设置 vue 实例挂载（管理）的元素

2. vue 实例的作用范围？

   > vue 会管理el选项命中的元素，及其内部的后代元素

3. 是否可以使用其他的选择器？

   > 可以使用其他的选择器，但是建议使用 id 选择器

4. 是否可以设置其他的dom元素？

   > 可以使用其他的双标签，但不能使用 html 和 body

## css id 选择器

```vue
<body>
    <div id="app">
        {{ message }}
    </div>
    
    <script>
    var app = new Vue ({
        el: "#app",
        data: {
            message: "id 选择器的通配符是#"
        }
    })
    </script>
</body>
```

## css class 选择器

```vue
<body>
    <div id="app" class="app">
        {{ message }}
    </div>
    
    <script>
    var app = new Vue ({
        el: ".app",
        data: {
            message: "class 选择器的通配符是."
        }
    })
    </script>
</body>
```

## css 标签选择器

```vue
<body>
    <div id="app">
        {{ message }}
    </div>
    
    <script>
    var app = new Vue ({
        el: "div",
        data: {
            message: "可以直接使用标签选择器"
        }
    })
    </script>
</body>
```

# data: 数据对象

## 在元素中使用

1. 使用“Mustache”语法 (双大括号) 的文本插值 {{  }}
2. vue 中用到的数据定义在 data 中
3. data 中可以写复杂类型的数据，渲染复杂类型数据时，遵守 js 的语法即可使用
4. 引用数据时支持内部表达式

```html
<body>
    <div id="app">
        {{ message }}
        <h1>
            {{ school.name }} {{ school.grade }}
        </h1>
        <ul>
            <li> {{ "周一吃" + food[0] }} </li>
            <li> {{ "周二吃" + food[1] }} </li>
            <li> {{ "周三吃" + food[2] }} </li>
        </ul>
    </div>
    
    <script>
        var app = new Vue ({
            el: "#app",
            data: {
                message: "data 内存储 vue 所需要使用到的数据，可以按照js语法使用"
                school: {
                    name: "小学",
                    grade: "六年级"
                },
                food: ["banana", "apple", "orange"]
            }
        })
    </script>
</body>
```

## 在方法中使用

使用 this 关键字

```html
<body>
    <script>
        var vue = new Vue ({
            el: "",
            data: {
                food: "orange"
            },
            methods: {
                methodName:function (
                	console.log(this.food)
                )
            }
        })
    </script>
</body>
```

## 支持 JavaScript 表达式

对于所有的数据绑定，Vue.js 都提供了完全的 JavaScript 表达式支持。

```html
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

<div v-bind:id="'list-' + id"></div>
```



# methonds: 事件

```html
<body>
    <script>
        var app = new Vue ({
            el: "#app",
            methods: {
                methodName:function(
                //逻辑
                )
            }
        })
    </script>
</body>
```



# vue 指令

vue 指令是以 v- 开头的一组特殊语法

## 内容绑定，事件绑定

### v-text 设置标签的 textContent 属性（文本值）

```html
<body>
    <div id="app">
        <h1 v-text="message"></h1>
        <h1>v-text: {{ message }} </h1>
    </div>
    
    <script>
        var app = new Vue ({
            el: "#app",
            data: {
                message: "v-text 设置标签的 textContent 属性（文本值）"
        })
    </script>
</body>
```

### v-html 设置标签的 innerHTML 属性

1. v-html 会将数据中的 html 结构解析为标签
2. 如果数据中没有  html 结构，则显示结果和 v-text 是一致的，只会解析为文本
3. v-text 指令，无论数据是什么，只会解析为文本
4. 解析文本，需要使用 v-text；解析html，需要使用 v-html

```html
<body>
    <div id="app">
        <h1 v-html="message"></h1>
        <h1 v-html="html"></h1>
        <h1 v-text="html"></h1>
    </div>
    
    <script>
        var app = new Vue ({
            el: "#app",
            data: {
                message: "v-html 设置标签的 innerHTML 属性"
                html: "<a href='https://www.baidu.com'>百度一下 你就知道</a>"
        })
    </script>
</body>
```

### v-on 为元素绑定事件

```html
<body>
    <div id="app">
        <!-- input type="button" value="v-on 指令绑定事件" v-on:事件名="方法"> -->
        <input type="button" value="v-on 指令绑定事件" v-on:click="methodName">
        <input type="button" value="v-on 指令绑定事件" v-on:monseenter="methodName">
        <input type="button" value="v-on 简写" @click="methodName">  <!- 简写 ->
    </div>
    
    <script>
        var app = new Vue ({
            el: "#app",
            methods:{
                methodName:function(
                //
                )
            }
        })
    </script>
</body>
```



## 显示切换，属性绑定

### v-show 切换元素的显示与隐藏 （操作 display）

1. 根据表达式的真假，切换元素的显示状态
2. 原理是修改元素的 display
3. 写在后面的内容，最终都会解析为布尔值
4. 如果为 ture，显示；如果为 flase，隐藏
5. 数据更改后，元素的状态也会同步刷新
6. 频繁切换的元素用 v-show

```html
<body>
    <div id="app">
        <img src="" v-show="true">     <!- 显示 ->
        <img src="" v-show="isShow">   <!- 显示 ->
        <img src="" v-show="age>=18">  <!- 显示 ->
    </div>
    
    <script>
        var app = new Vue ({
            el: "#app",
            data: {
                isShow: true,
                age: 18
            }
        })
    </script>
</body>
```

### v-if  切换元素的显示与隐藏 （操作 DOM）

1. 本质是通过操作 DOM 元素的移除或添加
2. 切换 DOM 树对性能的消耗较大，因此适用于不频繁的操作

```html
<body>
    <div id="app">
        <img src="" v-if="true">     <!- 显示 ->
        <img src="" v-if="isShow">   <!- 显示 ->
        <img src="" v-if="age>=20">  <!- 隐藏 ->
    </div>
    
    <script>
        var app = new Vue ({
            el: "#app",
            data: {
                isShow: true,
                age: 18
            }
        })
    </script>
</body>
```

### v-bind 设置元素的属性

例如 src, title, class 等

元素的属性都写在元素的内部

```html
<body>
    <div id="app">
        <img v-bind:src="imgSrc">
        <img v-bind:title="imgTitle + '!'">        <!- 可以使用表达式 ->
        <img v-bind:class="isActive?'active':''">  <!- 三元表达式，繁琐不建议 ->
        <img v-bind:class="{active:isActive}">     <!- 对象形式，建议使用 ->
        <img :src="imgSrc">       <!- 简写，建议使用 ->
        <img :class="isActive">   <!- 简写 ->
    </div>
    
    <script>
        var app = new Vue ({
            el: "#app",
            data: {
                imgSrc: "https://www.baidu.com",
                imgTitle: "百度一下，你就知道",
                isActive: true
            }
        })
    </script>
</body>
```



## 列表循环，表单元素绑定

### v-for

### v-on

### v-model

## 其他

### v-html 输出原始 html 代码

```html
<div id="example1" class="demo">
    <p>Using mustaches: {{ rawHtml }}</p>
    <p>Using v-html directive: <span v-html="rawHtml"></span></p>
</div>
```





# 绑定元素属性

## v-bind

# 条件渲染 v-if & v-show

## v-if

## v-show

# 列表渲染

## v-for

# 事件处理

## v-on

## 事件修饰符

```html
.stop
.prevent
.capture
.self
.once
.passive
```

# 表单绑定

## v-model

获取和设置表单元素的数据。双向数据绑定

## 文本（text）

## 多行文本（textarea）

## 单选框（radio）

## 复选框（checkbox）

## 选择框（select）

## 修饰符

### 
