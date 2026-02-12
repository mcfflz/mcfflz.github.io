# File

## java.io.File

### 基本介绍

java.io.File 类代表 java 对文件和目录的抽象表示形式。

操作：

* 创建文件/文件目录
* 删除文件/文件目录
* 获取文件/文件目录
* 判断文件/文件目录是否存在
* 对文件目录进行遍历
* 获取文件的大小

File 类中的三个概念：

* file: 文件
* directory: 目录
* path: 路径

### 静态变量

* `static final String pathSeparator`:  系统相关的环境变量路径分隔符，为了方便，它被表示为字符串：

  > windows 操作系统环境变量的路径分隔符为 `;` 
  >
  > linux 操作系统环境变量路径分隔符为 `:`

* `static final char pathSeparatorChar`: 与系统有关的路径分隔符

* `static final String separator`: 系统相关的文件名称分隔符，为了方便，它被表示为字符串。

  > windows 操作系统文件名称分隔符为 `\`（反斜杠）
  >
  > linux 操作系统文件名称分隔符为 `/`（正斜杠）

* `static final char separatorChar`: 系统相关的文件名称分隔符

```java
import java.io.File;

public class Test {
	public static void main(String[] args) {
		System.out.println(File.pathSeparator);
		System.out.println(File.pathSeparatorChar);
		System.out.println(File.separator);
		System.out.println(File.separatorChar);
	}
}
```

**注意：编码过程中，文件路径不能写死，尽量以 File 类中的静态变量来表示。**

### 绝对路径和相对路径

* 绝对路径：完整的路径

  > windows 以盘符为开始，例如 c:\\desktop\\test.java
  >
  > linux 以根目录为开始，例如 /root/test.java

* 相对路径：简化的路径，相对于当前项目的根目录

  > windows test.java
  >
  > linux ../test.java

### 构造方法

* `public File(String pathname)`: 最常用的构造方法。

  > pathname 路径：
  >
  > * 可以是文件结尾，也可以是问价夹结尾；
  > * 可以是相对路劲，可以是绝对路径；
  > * 可以是存在的，也可以是不存在的；
  >
  > 创建 File 对象，只是把字符串封装为 File 对象，不考虑路径的真假情况

* `public File(String parent, String child)`: 第二常用的构造方法。

  > parent 父路径 child 子路径：
  >
  > 父路径和子路径分离，使用起来非常灵活。

* `public File(File parent, String child)`: 第三常用的构造方法。

  > File parent 父路径 child 子路径：
  >
  > 父路径和子路径分离，使用起来非常灵活。
  >
  > 父路径是 File 类型，可以使用 File 的一些方法进行操作

* `public File(URI uri)`: 不常用的构造方法，在网络编程中可能用到

```java
import java.io.File;

public class Test {
	public static void main(String[] args) {
        file01();
        file02();
        file03();
	}
    private static void file01 () {
        File file1 = new File("H:\\windows\\testfile");
        System.out.println(file1);
        // 输出为：H:\windows\testfile
        // 证明 File 类重写了 toString() 方法
    }
    private static void file02 () {
        String parent = "H:\\windows\\";
        String child = "testfile";
        System.out.println(new File(parent, child));
    }
    private static void file03 () {
        File parent = new File("H:\\");
        String child = "windows\\testfile";
        System.out.println(new File(parent, child));
    }
}
```

### 常用方法

判断类方法：

* `public boolean exists()`: File 对象表示的文件或目录是否存在

* `public boolean isDirectory()`: File 对象表示的是否为真实存在的目录：

  > 如果 File 对象表示的不是目录，返回 `false`
  >
  > 如果目录不是真实存在，返回 `false`

* `public boolean isFile()`: File 对象表示的是否为真实存在的文件：

  > 如果 File 对象表示的不是文件，返回 `false`
  >
  > 如果文件不是真实存在，返回 `false`

获取功能类常用方法：

* `public String getAbsolutePath()`: 获取文件绝对路径
* `public String getPath()`: 获取文件构造路径
* `public String getName()`: 获取文件或目录的名称
* `public long length()`: 获取文件的大小，目录或不存在的文件返回 `0`

创建和删除类功能：

* `public boolean createNewFile()`: 当 File 对象表示的文件不存在时，创建该文件
* `public boolean delete()`: 删除此 File 对象表示的文件或目录。**注意：被删除的文件不会放入回收站，谨慎使用**
* `public boolean mkdir()`: 创建此 File 对象表示的目录
* `public boolean mkdirs()`: 创建此 File 对象表示的目录，包括任何必须但不存在的父目录

目录遍历：

* `public String[] list()`: File 对象表示的目录下的所有文件名
* `public File[] listFiles()`: File 对象表示的目录下的所有文件
* 如果不是目录，则返回为空数组

文件权限类功能：

* `public boolean canExecute()`: File 对象表示的文件是否具有 execute 权限
* `public boolean canRead()`: File 对象表示的文件是否具有 read 权限
* `public boolean canWrite()`: File 对象表示的文件是否具有 write 权限
* `public boolean setExecutable(boolean executable)`: 为 File 对象表示的文件的所有者设置 execute 权限
* `public boolean setExecutable(boolean executable, boolean ownerOnly)`: 为 File 对象表示的文件的所有者或者所有用户设置 execute 权限
* `public boolean setReadable(boolean readable)`: 为 File 对象表示的文件的所有者设置 read 权限
* `public boolean setReadable(boolean readable, boolean ownerOnly)`: 为 File 对象表示的文件的所有者或者所有用户设置 read 权限
* `public boolean setWritable(boolean writable)`: 为 File 对象表示的文件当前的所有者设置 write 权限
* `public boolean setWritable(boolean writable, boolean ownerOnly)`: 为 File 对象表示的文件的所有者或者所有用户设置 write 权限

### 练习题1：递归打印多级目录

```java
import java.io.File;

public class test {
    public static void main(String[] args) {
        String parent = "d:\\360\\";
        helper(new File(parent));
    }
    
    private static void helper(File parent) {
        System.out.println(parent); // 打印目录及文件
        if (parent.isFile()) {
            // System.out.println(parent); // 仅打印文件
            return;
        }
        for(File child: parent.listFiles()) {
            helper(child);
        }
    }
}
```

### 练习题2：查找目录或文件

```java
import java.io.File;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class test {
	public static void main(String[] args) {
		String parent = "d:\\360\\";
		String keyword = "safe";
		helper(new File(parent), keyword);
	}

	private static void helper(File parent, String keyword) {
		Pattern pattern = Pattern.compile(keyword);
		Matcher matcher = pattern.matcher(parent.getName());
		if (matcher.find()) {
			System.out.println(parent);
		}

		if (parent.isFile()) {
			return;
		}
		for(File child: parent.listFiles()) {
			helper(child, keyword);
		}
	}
}
```

## java.io.FileFilter

java 文件过滤器，是个接口，此接口的实例用户 java.io.File 类中的：

* `File[] listFiles(FileFilter filter)` 方法

### 抽象方法

该接口下仅有一个抽象方法 `boolean accept(File pathname)`，需要自行重写实现方法，自定义过滤规则

* listFiles 方法会对构造方法中，传递的目录进行遍历，获取目录中每一个文件和目录，封装为 File 对象
* listFiles 方法会调用参数传递过滤器中的 accept(File pathname) 方法
* listFiles 方法会将得到的每一个 File 对象，传递给 accetp 方法的参数 pathname
* 如果 accept 方法返回 true，则 listFiles 方法会将其保存到 File[] 数组中
* 如果 accept 方法返回 false，则不会保存

用于测试指定路径下是否包含指定路径名，示例如下：

```java
import java.io.FileFilter;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class FileFilterImpl implements FileFilter {
    @Override
    public boolean accept(File pathname) {
        String regex = "";
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(pathname.getName());
        if (matcher.find()) {
            return true;
        }
        return false;
    }
}
```

可以使用 lambda 表达式，简化匿名内部类（接口中只有一个抽象方法）

```java
File dir = new File("");
File[] files = dir.listFiles((d, name) -> new File(d, name).isDirectory())
```



## java.io.FileNameFilter

java 文件过滤器，是个接口，此接口的实例用于 java.io.File 类中的：

* `String[] list(FileNameFilter filter)` 方法
* `File[] listFiles(FileNameFilter filter)` 方法

### 抽象方法

该接口下仅有一个抽象方法 `boolean accept(File dir, String name)`，需要自行重写实现方法，自定义过滤规则

其原理和 `java.io.FileFilter` 类中的抽象方法相同

用于测试指定路径下是否包含指定路径名

# IO 流概述

## 概念

I：input，输入（读取）

O：output，输出（写入）

流：数据流，字符、字节

IO 流的输入和输出是相对内存来说的：

* 输入：把硬盘/远端服务器中的数据，读取到内存中
* 输出：把内存中的数据，写入到硬盘/远端服务器中

```sequence
participant 内存 as a
participant 硬盘 as b
a->b: 从内存读取，输出到硬盘\n（输出流/输出字符）
b->a: 从硬盘读取，输入到内存\n（输入流/输入字符）
```



## 顶级父类

一般而言，顶级父类是指：该类直接继承 java.lang.Object 类。

* 字节流：

  字节 `byte` 是指不附带编码格式的原始字节数据（二进制数据）。

  > 字节输入流：java.io.InputStrem
  >
  > 字节输出流：java.io.OutputStrem

* 字符流：

  字符 `character` 是指对原始字节数据按照指定字符集的编码格式进行解码后的字符数据。

  > 字符输入流：java.io.Reader
  >
  > 字符输出流：java.io.Writer

# IO 异常处理新特性

## JDK 1.7 以前

使用 try {} catch () {} finally {} 处理异常

```java
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.Charset;

public class test {
	public static void main(String[] args) {
		FileWriter fw;
        try {
            // 可能产生异常的代码
            fw = new FileWriter("new 3", Charset.forName("gbk"));
			fw.write("Hello World!");
            fw.flush();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fw != null) {
                try {
                    fw.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
	}
}
```



## JDK 1.7 新特性

使用 try () {} catch () {} 处理异常，资源可以在 try () 内定义，try 结束后自动关闭

```java
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.Charset;

public class test {
	public static void main(String[] args) {
        // 在 try 内定义资源，try 结束后自动释放资源
        try (FileWriter fw = new FileWriter("new 3", Charset.forName("gbk"))) {
            // 可能产生异常的代码
			fw.write("Hello World!");
            fw.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
	}
}
```



## JDK 1.9 新特性

使用 try () {} catch () {} 处理异常，但资源可以事先定义，在 try () 内引用，try 结束后自动关闭

```java
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.Charset;

public class test {
	public static void main(String[] args) throws IOException {
        // 在 try 之前定义资源，在 try 内引用资源，try 结束后自动释放资源
        FileWriter fw = new FileWriter("new 3", Charset.forName("gbk"));
        try (fw) {
            // 可能产生异常的代码
			fw.write("Hello World!");
            fw.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
	}
}
```



# 字节流

一切文件数据（文本、图片、视频等）在存储时，都是以二进制的形式进行存储，都是一个一个的字节，因此，在文件数据传输时同样如此。

字节流可以传输任意文件数据。在操作流的时候，无论使用了什么样的流对象，底层传输的始终为二进制数据。

## java.io.InputStream

抽象类，顶级父类，所有字节输入流的超类

### 构造方法

* `public InputStream()`: 子类调用的构造函数

### 常用方法

* `public void close() throws IOException`: 关闭输入流，释放所有与该流相关的系统资源
* `public void readAllBytes() throws IOException`: 刷新输出流，强制写出所有缓存字节。如果有任何字节被该输出流的实现类缓存，这些字节必须立刻被写入到它们的预定目的地
* `public int read(byte[] b, int off, int len) throws IOException`: 从输入流中尝试读取长度为 `len` 的字节数据，暂存在字节数组 `b[]` 中，返回 `int` 为实际读取的字节长度。读取的第一个字节存放在字节数组的 `b[off]` 的位置，第二个字节在 `b[off+1]`，以此类推，最大为 `b[off+len-1]`。
* `public int read(byte[] b) throws IOException`: 从输入流中尝试读取长度为 `b.length` 的字节数据，暂存在字节数组 `b[]` 中，返回 `int` 为实际读取的字节长度。
* `public abstract int read() throws IOException`: 从输入流中尝试读取长度为 `1` 的字节数据，返回 `int` 为实际读取的字节，范围在 `[0-255]`。如果未读取到数据，则返回 `-1`。

### 子类

* java.io.AudioInputStream：音频字节输入流
* java.io.ByteArrayInputStream：字节数组输入流
* java.io.FileInputStream：文件字节输入流
* java.io.FilterInputStream：带文件过滤器的文件字节输入流
* java.io.ObjectInputStream：对象字节输入流
* java.io.PipedInputStream：管道字节输入流
* java.io.SequenceInputStream：队列字节输入流
* java.io.StringBufferInputStream：字符串缓冲区字节输入流

## java.io.FileInputStream

### 构造方法

常用构造方法如下：

* `public FileInputStream(String name) throws FileNotFoundException`: name 文件路径名，绝对路径或相对路径
* `public FileInputStream(File file) throws FileNotFoundException`: file 文件对象

### 常用方法

参考父类 java.io.InputStream 常用方法

### 读取数据的过程

java 程序 -> JVM（java 虚拟机） -> OS（操作系统） -> OS 调用内存、硬盘相关驱动读取和缓存数据

java 程序：

```java
public static void main(String[] args) throws Exception {
    // 创建文件输入流对象
    FileInputStream fis = new FileInputStream("a.txt");
    // 设置缓冲区数组，文件输入流对象读取字节流数据
    byte[] buffer = new byte[1024];
    int len;
    while ((len = fis.read(buffer)) != -1) {
        System.out.println(new String(buffer, 0, len));
    }
    // 释放资源
    fis.close();
}
```



## java.io.OutputStream

抽象类，顶级父类，所有字节输出流的超类

### 构造方法

* `public OutputStream()`: 子类调用的构造函数

### 常用方法

* `public void close() throws IOException`: 关闭输出流，释放所有与该流相关的系统资源
* `public void flush() throws IOException`: 刷新输出流，强制写出所有缓存字节。如果有任何字节被该输出流的实现类缓存，这些字节必须立刻被写入到它们的预定目的地
* `public void write(byte[] b, int off, int len) throws IOException`: 从指定字节数组 `b[]` 中，从偏移量 `off` 位置开始，读取 `len` 字节的数据写入该输出流。
* `public void write(byte[] b) throws IOException`: 将指定的字节数组 `b[]` 写入该输出流

### 子类

* java.io.ByteArrayOutputStream: 字节数组输出流，向字节数组中写入字节数据
* java.io.FileOutputStream: 文件字节输出流，向文件中写入字节数据
* java.io.FilterOutputStream: 带过滤器的字节输出流
* java.io.ObjectOutputStream: 对象字节输出流
* java.io.PipedOutputStream: 管道字节输出流

## java.io.FileOutputStream

文件字节输出流用于向文件中写入原始字节数据。

### 构造方法

常用构造方法如下：

* `public FileOutputStream(String name) throws FileNotFoundException`: name 文件路径名，绝对路径或相对路径
* `public FileOutputStream(String name, boolean append) throws FileNotFoundException`: boolean append 是否在文件尾部追加；true 文件追加；false 新建文件，覆盖原文件
* `public FileOutputStream(File file) throws FileNotFoundException`: file 文件对象
* `public FileOutputStream(File file, boolean append) throws FileNotFoundException`: boolean append 是否在文件尾部追加

### 常用方法

参考父类 java.io.OutputStream 常用方法

### 写入数据的过程

java 程序 -> JVM（java 虚拟机） -> OS（操作系统） -> OS 调用内存、硬盘相关驱动读取和写入数据

java 程序：

```java
public static void main(String[] args) throws Exception {
    // 创建文件输出流对象
    FileOutputStream fos = new FileOutputStream("a.txt");
    // 文件输出流对象输出字节流数据
    fos.write("Hello World!".getBytes());
    // 释放资源
    fos.close();
}
```



## 练习题1：文件复制

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class test {
    public static void main(String[] args) {
        String src = "new1\\new 1.txt";
        String filename = new File(src).getName();
        String dst = "new2\\" + filename;
        FileInputStream fis = null;
        FileOutputStream fos = null;
        try {
            fis = new FileInputStream(src);
            fos = new FileOutputStream(dst);
            byte[] buffer = new byte[1024];
            int len;
            while ((len = fis.read(buffer)) != -1) {
                fos.write(buffer, 0, len);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fos != null) {
                try {
                    fos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (fis != null) {
                try {
                    fis.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

# 字符流

使用字节流时，由于一些字符（例如：中文字符）可能会使用多个字节来表示，因此如果逐字节来读取，按照 ASCII 编码转码会出现乱码，无法识别字符数据。

因此，java 提供字符流类，以字符为单位处理数据。

## java.io.Reader

抽象类，顶级父类，所有字符输入流的超类

### 构造方法

`public Reader()`: 子类调用的构造函数

### 常用方法

* `public void close() throws IOException`: 关闭输入流，释放所有与该流相关的系统资源
* `public abstract int read(char[] cbuf, int off, int len) throws IOException`: 从输入流中尝试读取长度为 `len` 的字符数据，暂存在字符数组 `cbuf[]` 中，返回 `int` 为实际读取的字符长度。读取的第一个字符存放在字符数组的 `cbuf[off]` 的位置，第二个字节在 `cbuf[off+1]`，以此类推，最大为 `cbuf[off+len-1]`。
* `public int read(char[] cbuf) throws IOException`: 从输入流中尝试读取长度为 `cbuf.length` 的字符数据，暂存在字符数组 `cbuf[]` 中，返回 `int` 为实际读取的字符长度。
* `public int read() throws IOException`: 从输入流中尝试读取长度为 `1` 的字符数据，返回 `int` 为实际读取的字符，范围在 `[0-255]`。如果未读取到数据，则返回 `-1`。

### 子类

* java.io.BufferedReader：缓冲字符输入流
* java.io.CharArrayReader：字符数组输入流
* java.io.FilterReader：带过滤的字符输出流
* java.io.InputStreamReader：转换流
  * java.io.FileReader：文件字符输入流
* java.io.PipedReader：管道字符输入流
* java.io.StringReader：字符串字符输入流

## java.io.FileReader

### 构造方法

常用构造方法如下：

* `public FileReader(String fileName, Charset charset) throws FileNotFoundException`: fileName 文件路径名，绝对路径或相对路径；charest 字符集
* `public FileReader(String fileName) throws FileNotFoundException`: fileName 文件路径名，绝对路径或相对路径，使用平台默认字符集（默认字符集在虚拟机启动期间确定，通常取决于底层操作系统的区域设置和字符集）
* `public FileReader(File file, Charset charset) throws FileNotFoundException`: file 文件对象；charset 字符集
* `public FileReader(File file) throws FileNotFoundException`: file 文件对象，使用平台默认字符集（默认字符集在虚拟机启动期间确定，通常取决于底层操作系统的区域设置和字符集）

### 常用方法

参考父类 java.io.InputStreamReader、java.io.Reader 常用方法

### 读取数据的过程

1. 创建 FileReader 对象，绑定目的地址
2. 使用 FileReader 对象的 read() 方法，把数据写入内存缓冲区（字符和字节的转换过程）
3. 释放资源

```java
import java.io.FileReader;
import java.nio.charset.Charset;

public class test {
	public static void main(String[] args) throws Exception {
		FileReader fr = new FileReader("new 2", Charset.forName("utf-8"));
		char[] cbuf = new char[1024];
		int len;
		while ((len = fr.read(cbuf)) != -1) {
			System.out.println(new String(cbuf, 0, len));
		}
        fr.close();
	}
}
```



## java.io.Writer

抽象类，顶级父类，所有字符输出流的超类

### 构造方法

`public Writer()`: 子类调用的构造函数

### 常用方法

* `public void close() throws IOException`: 关闭输出流，释放所有与该流相关的系统资源
* `public void flush() throws IOException`: 刷新输出流，强制写出所有缓存字符。如果有任何字符被该输出流的实现类缓存，这些字符必须立刻被写入到它们的预定目的地
* `public void write(char[] cbuf, int off, int len) throws IOException`: 从指定字符数组 `cbuf[]` 中，从偏移量 `off` 位置开始，读取 `len` 字符的数据写入该输出流。
* `public void write(char[] cbuf) throws IOException`: 将指定的字符数组 `cbuf[]` 写入该输出流
* `public void write(String str) throws IOException`: 将指定的字符串 `str` 写入该输出流
* `public void write(String str, int off, int len) throws IOException`: 将指定的字符串 `str` 的某一部分写入该输出流，从偏移量 `off` 位置开始，读取 `len` 字符的数据写入该输出流。

### 子类

* java.io.BufferedWriter：缓冲字符输出流
* java.io.CharArrayWriter：字符数组输出流
* java.io.FilterWriter：带过滤的字符输出流
* java.io.OutputStreamWriter：转换流
  * java.io.FileWriter：文件字符输出流
* java.io.PipedWriter：管道字符输出流
* java.io.PrintWriter：打印字符输出流
* java.io.StringWriter：字符串字符输出流

## java.io.FileWriter

### 构造方法

常用构造方法如下：

* `public FileWriter(String fileName) throws FileNotFoundException`: name 文件路径名，绝对路径或相对路径
* `public FileWriter(String fileName, Charset charset) throws FileNotFoundException`: charset 字符集
* `public FileWriter(String fileName, Charset charset, boolean append) throws FileNotFoundException`: boolean append 是否在文件尾部追加；true 文件追加；false 新建文件，覆盖原文件
* `public FileWriter(File file) throws FileNotFoundException`: file 文件对象
* `public FileWriter(File file, Charset charset) throws FileNotFoundException`: charset 字符集
* `public FileWriter(File file, Charset charset, boolean append) throws FileNotFoundException`: boolean append 是否在文件尾部追加

### 常用方法

参考父类 java.io.OutputStream 常用方法

### 写入数据的过程

1. 创建 FileWriter 对象，绑定目的地址
2. 使用 FileWriter 对象的 write() 方法，把数据写入内存缓冲区（字符和字节的转换过程）
3. 使用 FileWriter 对象的 flush() 方法，把数据从内存缓冲区，刷新到目的地址
4. 释放资源

```java
import java.io.FileWriter;
import java.nio.charset.Charset;

public class test {
	public static void main(String[] args) throws Exception {
		FileWriter fw = new FileWriter("new 3", Charset.forName("gbk"));
		fw.write("Hello World!");
		fw.flush();
        fw.close();
	}
}
```

### 换行

```java
fw.write("\r\n"); // windows
fw.write("/n"); // linux
fw.write("/r"); // maxOs
```



# 缓冲流

缓冲流是对基本 IO 流的增强，可以极大提高读写效率。

其基本原理是，在创建流对象时，同时创建一个默认大小的缓冲区数组，通过缓冲区读写，减少系统 IO 次数，从而提高读写的效率。

* java.io.BufferedInputStream：缓冲字节输入流
* java.io.BufferedOutputStream：缓冲字节输出流
* java.io.BufferedReader：缓冲字符输入流
* java.io.BufferedWriter：缓冲字符输出流

实现原理：

* 基本 IO 流读取文件过程：java 程序（字节/字符读取） -> JVM -> OS -> 硬盘
* 缓冲流读取文件过程：java 程序（设置缓冲区大小，字节/字符数组读取） -> JVM -> OS -> 硬盘

## java.io.BufferedInputStream

以 BufferedInputStream 为示例讲解：

### 构造方法

* `public BufferedInputStream(InputStream in)`: 创建一个 BufferedInputSteam 对象
* `public BufferedInputStream(InputStream in, int size)`: size 指定缓冲区大小

### 使用示例

```java
import java.io.FileInputStream;
import java.io.BufferedInputStream;
import java.nio.charset.Charset;

public class test {
	public static void main(String[] args) throws Exception {
		FileInputStream fis = new FileInputStream("new 2");
		BufferedInputStream bis = new BufferedInputStream(fis);
		byte[] bytes = new byte[1024];
		int len;
		while ((len = bis.read(bytes)) != -1) {
			System.out.println(new String(bytes, "utf-8"));
		}
	}
}
```

## java.io.BufferedReader

以 BufferedReader 为示例讲解：

### 构造方法

* `public BufferedReader(Reader in)`: 创建一个 BufferedReader 对象
* `public BufferedReader(Reader in, int size)`: size 指定缓冲区大小

### 常用方法

* `public String readLine() throws IOException`:  读取一行数据。一行的定义取决于操作系统的换行符定义。

```java
import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;

public class test {
	public static void main(String[] args) {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;
		try (br) {
			while ((line = br.readLine()) != null) {
				System.out.println(line);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
```



## 练习题1：缓冲流文件复制

使用缓冲流进行文件复制，其效率要比普通的文件流复制效率更高。

```java
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class test {
	public static void main(String[] args) {
		String src = "new 2";
		String dst = "new 3";
		try (
			    BufferedInputStream bis = new BufferedInputStream(new FileInputStream(src));
			    BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream(dst));
			) {
			byte[] buffer = new byte[1024];
			int len;
			while ((len = bis.read(buffer)) != -1) {
				bos.write(buffer, 0, len);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
```



# 转换流

转换流是从字节流到字符流的转换桥梁。

* java.io.InputStreamReader：字节转换字符输入流
* java.io.OutputStreamWriter：字节转换字符输出流

## java.io.InputStreamReader

以 InputStreamReader 为示例讲解：

### 构造方法

* `public InputStreamReader(InputStream in)`: in 字节输入流，使用操作系统默认字符集
* `public InputStreamReader(InputStream in, Charset charset)`: charset 字符集
* `public InputStreamReader(InputStream in, String charsetName) throws UnsupportedEncodingException`: charsetName 字符集名称

### 使用示例

```java
import java.io.FileInputStream;
import java.io.InputStreamReader;

public class test {
	public static void main(String[] args) throws Exception {
		InputStreamReader isr = new InputStreamReader(new FileInputStream("new 2"), "utf-8");
		char[] chars = new char[1024];
		int len;
		while ((len = isr.read(chars)) != -1) {
			System.out.print(new String(chars));
		}
        isr.close();
	}
}
```



## 练习题1：转换文件编码

```java
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.io.UnsupportedEncodingException;

public class test {
	public static void main(String[] args) {
		// 字符集转换，一般为小字符集转换为大字符集
		String charset_ori = "gbk";
		String charset_dst = "utf-8";
		String filepath_ori = "new 2";
		String filepath_dst = "new 3";

		try (
			    BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(filepath_ori), charset_ori));
			    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filepath_dst), charset_dst));
			) {
			char[] chars = new char[1024];
			int len;
			while ((len = br.read(chars)) != -1) {
				bw.write(chars, 0, len);
				bw.flush();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
```



# 序列化流

* java.io.ObjectInputStream：序列化字节输入流，也叫“反序列化流”
* java.io.ObjectOutputStream：序列化字节输出流，也叫“序列化流”

## 序列化对象

序列化和反序列化的对象需要实现 java.io.Serializable 接口，否则会抛出 java.io.NotSerializableException 异常

```java
package io;

import java.io.Serializable;

public class Person implements Serializable {
	private String name;
	private int age;

	public Person() {}
	public Person(String name, int age) {
		this.name = name;
		this.age = age;
	}

	public void setName(String name) {
		this.name = name;
	}
	public String getName() {
		return this.name;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public int getAge() {
		return this.age;
	}
}
```

## transient 瞬态关键字

`static` 关键字修饰的对象、方法、变量等，优先于非静态进入内存，不能被序列化。

`transient` 关键字修饰的变量，不能被序列化。如果不想某个成员变量被序列化，可以使用 `transient` 关键字。

## serialVersionUID 序列化版本号

当被序列化的对象的 *.class 文件被修改后，无法再根据该 class 文件进行反序列化，会抛出 java.io.InvalidClassException。

当对象实现了序列化接口后，会根据类的内容，自动计算生成一个序列化版本号 `private static final long serialVersionUID` ，在反序列化期间用于验证序列化对象的发送方和接收方是否加载了该对象的可兼容类。

因此如果不希望重新生成新的序列号，可以手动指定该序列号。

## java.io.ObjectOutputStream 序列化

把内存中的对象，以流的方式输出。

### 构造方法

* `public ObjectOutputStream(OutputStream out) throws IOException`: OutputStream 输出流

### 常用方法

* `public final void writeObject(Object obj) throws IOException`: obj 对象

```java
package io;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import io.Person; // construct & setter & getter

public class WirteObject {
	public static void main(String[] args) throws Exception {
		Person person1 = new Person("张三", 18);
		Person person2 = new Person("李四", 19);
		
		ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("new 1"));
		oos.writeObject(person1);
		oos.writeObject(person2);
		oos.flush();
		oos.close();
	}
}
```

## java.io.ObjectInputStream 反序列化

把存储的对象，以流的方式读取并加载到内存中。

### 构造方法

* `public ObjectInputStream(InputStream in) throws IOException`: InputStream 输出流

### 常用方法

* `public final void readObject(Object obj) throws IOException, ClassNotFoundException`: obj 对象

```java
package io;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.FileInputStream;
import java.io.ObjectInputStream;
import io.Person; // construct & setter & getter

public class ReadObject {
	public static void main(String[] args) throws Exception {
		ObjectInputStream ois = new ObjectInputStream(new FileInputStream("new 1"));
		Person person1 = (Person) ois.readObject();
		Person person2 = (Person) ois.readObject();
		ois.close();
		System.out.println(person1.getName() + ": " + person1.getAge());
		System.out.println(person2.getName() + ": " + person1.getAge());
	}
}
```

# 打印流

* java.io.PrintStream：打印（字节输出）流

## java.io.PrintStream

PrintStream 不会输出 IOException

### 构造方法

* `public PrintStream(File file) throws FileNotFoundException`: file 文件对象
* `public PrintStream(File file, String charsetName) throws FileNotFoundException, UnsupportedEncodingException`: charsetName 字符集名称
* `public PrintStream(File file, Charset charset) throws IOException`: charset 字符集对象
* `public PrintStream(String fileName) throws FileNotFoundException`: fileName 文件路径
* `public PrintStream(OutputStream out)`: out 字节输出流
* `public PrintStream(OutputStream out, boolean autoFlush)`: autoFlush 自动刷新，写入字节数组后自动调用 flush() 方法
* `public PrintStream(OutputStream out, boolean autoFlush, Charset charset)`: charset 字符集对象

### 常用方法

* `public void print(任意类型的数据)`: 打印
* `public void println(任意类型的数据)` : 打印结束后，换行

## 标准打印输出流

java.lang.System 类中的静态变量 `public static final PrintStream out`

使用 System 类中的 `public static void setOut(PrintStream out)` 可以改变输出路径，不再为控制台输出



# Test

```java
import java.util.Arrays;
import java.util.Scanner;
import java.io.UnsupportedEncodingException;

public class test {
    private static final String srcCharset = "GBK";
    private static final String dstCharset = "GB18030";

    public static void main(String[] args) throws UnsupportedEncodingException {
        System.out.println("Charset GBK To GB18030 Test Start...");
        // GBK Charset: 8140-FEFE
        // 首字节在 81-FE 之间，尾字节在 40-FE 之间，剔除 xx7F 一条线
        char[] hexCode = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
        Scanner sc = new Scanner(System.in);
        int count = 0;
        for (int i = 8; i < 16; i++) {
            for (int j = 1; j < 16; j++) {
                if (i == 15 && j >= 14) continue;
                for (int m = 4; m < 16; m++) {
                    for (int n = 0; n < 16; n++) {
                        if (m == 7 && n == 15) continue;
                        if (m == 15 && n >= 14) continue;
                        byte[] bytes = new byte[2];
                        bytes[0] = (byte) (i * 16 + j);
                        bytes[1] = (byte) (m * 16 + n);
                        String gbk = new String(bytes, srcCharset);
                        System.out.print(gbk);
                        count++;
                        if (count % 16 == 0) System.out.println();
                    }
                }
            }
        }
    }
}
```

