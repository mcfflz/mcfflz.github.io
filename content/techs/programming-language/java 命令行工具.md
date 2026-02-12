# javac

java 编译工具。

## javac

javac 命令基础用法

```java
// 示例一：编译当前目录下的 HelloWorld.java 文件
javac HelloWorld.java
// 示例二：编译 ./src/main/java/lesson1/ 目录下的 HelloWorld.java 文件
javac ./src/main/java/lesson1/HelloWorld.java
// 示例三：编译当前目录下的 *.java 文件
javac *.java
```



## javac -encoding utf8

java 编译使用 utf-8 字符集（Windows 默认使用 GBK 字符集）

```java
// 示例：使用 utf8 字符集编译 HelloWorld.java 文件
javac -encoding utf8 HelloWorld.java
```



## javac -d classpath

java 编译指定输入文件目录

```java
// 将当前目录下的 *.java 文件编译，并输出至上级目录的 classes 文件夹下
java HelloWorld.java -d ../classes
```



# java

java 命令执行工具

## java

java 命令基础用法

```java
// 示例一：编译当前目录下的 HelloWorld.java 文件
java HelloWorld
// 示例二：编译 ./src/main/java/lesson1/ 目录下的 HelloWorld.java 文件
java ./src/main/java/lesson1/HelloWorld
// 示例三：编译 ./src/main/java/lesson1/ 包下的 HelloWorld.java 文件，需要在包内声明 package
java src.main.java.lesson1.HelloWorld
```

