# ClassLoader

## 概述

java 类加载器。

java 程序源代码，并在内存中创建对应的 class 对象，这个过程称之为类的加载，整个过程如图所示：

```
src(*.java) -(javac 编译)->  dist(*.class)

dist --> 加载(loading) --> 验证(vertification) --> 准备(preparation) --> 解析(resolution) --> 初始化(initialization) --> jvm 内存堆区存储 --> jvm 内存栈区引用
```

