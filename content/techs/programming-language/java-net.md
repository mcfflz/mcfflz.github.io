---
date: 2026-02-12T12:00:00+08:00
title: Java Net
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

# java 网络编程

java SE 在 java.base 模块内，为网络编程提供以下几个基础包，分别是：

* package java.net：提供关于 Addresses、Sockets、URLs、URIs、Connections 等基础的网络对象
* package java.net.http：提供关于 HttpClient 和 WebSocket 等网络对象
* package java.net.spi：提供关于 URL 流处理对象，仅供专业人员使用。
* package javax.net：提供创建套接字的工厂。
* package javax.net.ssl：提供安全套接字相关对象

以及参考：java 安全标准算法：https://docs.oracle.com/en/java/javase/17/docs/specs/security/standard-names.html

# 网络通信

## 概述

网络通信（Network Communication），是指计算机通过“网络”完成数据传输的过程。

## 网络通信的两个要素

1. ip + port
2. 网络通信协议

网络通信 OSI 七层模型和 TCP/IP 四层模型

![image-20220507000841321](D:/Codes/study-notes/java%20%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B.assets/image-20220507000841321.png)

网络编程中的两个问题：

1. 如何准确地定位网络上的主机（找到服务器的 ip 地址和 port）
2. 找到主机后如何进行通信（网络通信协议）

## 万维网（WWW）

![image-20220507111550727](D:/Codes/study-notes/java%20%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B.assets/image-20220507111550727.png)

# URL 和 URI

https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URL.html

https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/URI.html

## URL

统一资源定位符（uniform resource *locator*），指向互联网（www）上的资源。

语法为：`protocol://host:port/file`

* protocol 协议
* host 域名或主机名
* port 端口
* file 资源路径（相对 servlet 容器的路径）

## URI

统一资源标识符（uniform resource *identifier*）

### URI 的含义

RFC 2396：https://www.ietf.org/rfc/rfc2396.txt

> Uniform
> Uniformity provides several benefits: it allows different types of resource identifiers to be used in the same context, even when the mechanisms used to access those resources may differ; it allows uniform semantic interpretation of common syntactic conventions across different types of resource identifiers; it allows introduction of new types of resource identifiers without interfering with the way that existing identifiers are used; and, it allows the identifiers to be reused in many different contexts, thus permitting new applications or protocols to leverage a pre-existing, large, and widely-used set of resource identifiers.
>
> Resource
> A resource can be anything that has identity. Familiar examples include an electronic document, an image, a service (e.g., "today's weather report for Los Angeles"), and a collection of other resources. Not all resources are network "retrievable"; e.g., human beings, corporations, and bound books in a library can also be considered resources.
>  The resource is the conceptual mapping to an entity or set of entities, not necessarily the entity which corresponds to that mapping at any particular instance in time. Thus, a resource can remain constant even when its content---the entities to which it currently corresponds---changes over time, provided that the conceptual mapping is not changed in the process.
>
> Identifier
> An identifier is an object that can act as a reference to something that has identity. In the case of URI, the object is a sequence of characters with a restricted syntax.
>  Having identified a resource, a system may perform a variety of operations on the resource, as might be characterized by such words as `access', `update', `replace', or `find attributes'.

### 最高级别语法

最高级别的 URI 语法为：`[scheme:]scheme-specific-part[#fragment]`，其中：

* 方括号 `[…]` 描述为可选组件；
* 字符 `:` 和 `#` 代表它们本身，无其他含义；

根据是否指定 `scheme` ，URI 可以分为：绝对的（absolute）和相对的（relative）：

* 绝对 URI 需要指定 `scheme` ；
* 相对 URI 不指定 `scheme` 。

根据描述形式，URI 可以分为：不透明的（opaque）和分层次的（hierarchical）：

* 不透明的 URI 是一个绝对 URI。它的 `scheme-specific-part` 不以斜线字符 `/` 开始，不能进一步解析。例如：

    > mailto:java-net@www.example.com
    >
    > news:comp.lang.java
    >
    > urn:isbn:096139210x

* 分层次的 URI 可以是绝对的 URI 或相对的 URI。它的 `scheme-specific-part` 以斜线字符 `/` 或一个相对 URI开始。例如：

    > http://example.com/languages/java/
    >
    > sample/a/index.html#28
    >
    > ../../demo/b/index.html
    >
    > file:///~/calendar


### 分层次的 URI 语法

分层次的 URI 可以按照 `[scheme:][//authority][path][?query][#fragment]` 格式进一步解析：

* 方括号 `[…]` 描述为可选组件；
* 字符 `:` 、 `/` 、 `?` 和 `#` 代表它们本身，无其他含义；
* 最高层次语法中的 `scheme-specific-part` 由 `[//authority]` 、`[path]` 和 `[?query]` 三个部分组成。

分层次的 URI 中的 `authority` 组件可以分为：基于服务的（server-based）和基于注册的（registry-based）：

* 目前，几乎所有的 URI 体系都是基于服务的。
* 基于服务的 `authority` 组件可以按照 `[user-info@]host[:port]` 格式进一步解析：
    * 方括号 `[…]` 描述为可选组件
    * 字符 `@` 和 `:` 代表它们本身，无其他含义；
* 基于注册的 `authority` 组件无法按照 `[user-info@]host[:port]` 格式进一步解析。

分层次的 URI 中的 `path` 组件分为：绝对的（absolute）和相对的（relative）。

* 绝对的 `path` 组件以斜线字符 `/` 开始；
* 相对的 `path` 组件不以斜线字符 `/` 开始；

### URI 组成

根据上文介绍的 URI 语法，一个 URI 包含九个组成部分：

 `[scheme:][//authority][user-info@]host[:port][path][?query][#fragment]` 

* [1] scheme：String
* [2] scheme-specific-part：String
    * [3] authority：String
        * [4] user-info：String
        * [5] host：String
        * [6] port：int
    * [7] path：String
    * [8] query：String
* [9] fragment：String

在 Java 语言中，String 类型的数据如果为空，默认值为 null；int 类型的数据如果为空，默认值为 -1。

### java URI 使用

对所有 URI 有以下关系成立：

```java
new URI(u.toString()).equals(u)
    
new URI(u.getScheme(),
         u.getAuthority(),
         u.getPath(), u.getQuery(),
         u.getFragment())
 .equals(u)
```

对分层次的 URI 有以下关系成立：

```java
new URI(u.getScheme(),
        u.getUserInfo(), u.getHost(), u.getPort(),
        u.getPath(), u.getQuery(),
        u.getFragment())
    .equals(u)
```

## URL 和 URI 的关系

* URI 可以被进一步分类为 URL 或 URN，或者同时满足两者。
* URL 通过访问权限机制来识别资源；
* URN 通过标识名称标识资源保持全球唯一，无论资源是否可用（不存在或不可访问）。

# 主机 host

host 和 ip 绑定，根据 host 可以获取 ip，也可以根据 ip 获取 host。

一般通过 DNS 服务器（Domain Name Server，域名服务器）进行 host 和 ip 的双向查找。

# 端口 port

包括物理端口和虚拟端口。计算机语言中一般是指操作系统提供的虚拟端口，用于标明进程所占用的网络资源。

公有端口：0-1023

* HTTP：80
* HTTPS：443
* FTP：21
* SSH：22
* TELNET：23

常见程序端口：1024-49151

* Tomcat：8080
* MySQL：3306
* PostgreSQL：5432
* Redis：6379

默认端口：49152-65535

* Idea：63342

```bash
# cmd 命令
# 查看端口
netstat -ano
# 查看指定端口
netstat -ano | findstr "8080"
# 查看指定端口的进程
tasklist | findstr "8080"
```

# 通信协议 protocol

## HTTP

HTTP 是应用层协议，是一种无状态协议。

HTTP 1.0 版本是一个请求响应之后直接断开，称之为短链接；

HTTP 1.1 版本不是响应之后直接断开，而是等待几秒钟，如果有新的请求，则还是通过之前的连接来收发消息。如果过了几秒钟用户没有发起新的请求，就会断开连接，称之为长连接。

长连接的保持时间可以通过 servlet 容器进行配置。

## HTTPS

HTTP 协议通过 SSL/TLS 协议进行加密，保证传输层安全。

## TCP/IP

TCP/IP 协议簇：实际上是一组协议

TCP 是用户传输协议，建立于

* 连接，稳定

* 三次握手：

  > Client：[SYN] seq=x
  > Server：[SYN, ACK] seq=y, ack=x+1
  > Client：[ACK] seq=x+1, ack=y+1

* 四次挥手：

  > Client：[FIN, ACK] seq=u, ack=v
  > Server：[ACK] seq=v, ack=u+1
  > Server：[FIN, ACK] seq=u, ack=v+1
  > Client：[ACK] seq=u+1, ack=v+1

* 客户端、服务端界限明确

* 传输完成，释放连接，效率低

UDP：用户数据报协议

* 客户端、服务端：没有明确的界限
* 不管有没有准备好，都可以发送

IP：网络互联协议

# HTTP 报文

## HTTP 请求报文

https://www.ietf.org/rfc/rfc7231.txt

HTTP 请求信息由四部分组成：

* 请求行：请求方法 请求地址 URI协议/版本
* 请求头：RequestHeader
* 空行
* 请求正文：RequestBody

以下是一个 HTTP 请求报文的样例：

```http
POST /sop-portal/api/portal/querySubBusinessForCard HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Connection: keep-alive
Content-Length: 49
Content-Type: application/json;charset=UTF-8
DNT: 1
Host: open.psbc.com
Origin: https://open.psbc.com
Referer: https://open.psbc.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50
X-Requested-With: XMLHttpRequest
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
tokne:

{"bizCode":"09","productName":"","accessType":""}
```



## HTTP 响应报文

HTTP 响应信息同样由四部分组成：

* 状态行：URI协议/版本 状态码 
* 响应头：ResponseHeader
* 空行
* 响应正文：ResponseBody

以下是一个 HTTP 响应报文的样例：

```http
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 30 Apr 2022 14:35:09 GMT
Content-Type: application/json;charset=UTF-8
Transfer-Encoding: chunked
PFPJ-RpcTotalTime: 61
sopApprequestId: 1aafe0fc231f99b62897b01123bef460
sopWebRequestId: 61ea4f496566a3fd05119c324479c787
Connection: Keep-alive
Via: 1.1 ID-5301755310444366 uproxy-11

[{"subBusinessCode":"953670211505704960","businessCode":"953662066242834432","subBusinessName":"绿卡通联名卡卡品种卡类别查询","subBusinessMsg":"绿卡通联名卡卡品种卡类别查询","createTime":"2022-03-16T15:04:57.000+0800","subBusinessIconUrl":"group1/M00/02/BA/CxhAF2Ixi3aAVuKWAAAUg_5viHQ981.png","businessName":null,"h5Count":0,"apiCount":0,"apiTag":true,"h5Tag":false}]
```

## HTTP 响应码

常见的 HTTP 响应码：

* 200 OK：请求成功
* 302 Found：临时重定向
* 403 Forbidden：服务器收到请求，但拒绝提供服务
* 404 Not Found：请求资源不存在
* 500 Internal Server Error：服务器发生不可预期的错误，无法响应数据

## HTTP 状态管理机制

HTTP 本身是一种无状态协议，通过 Cookie 管理状态。

RFC 2965：https://www.ietf.org/rfc/rfc2965.txt

# SSL 和 TLS

SSL 为早期协议，当前已经被 TLS 替代。但由于 SSL 的推广，因此当前仍然被广泛称之为 SSL/TLS 协议。

https://www.bilibili.com/video/BV1KY411x7Jp

https://docs.oracle.com/en/java/javase/17/docs/api/java.base/javax/net/ssl/SSLSocket.html

SSL/TLS 的工作层次：

![image-20220507110830868](D:/Codes/study-notes/java%20%E7%BD%91%E7%BB%9C%E7%BC%96%E7%A8%8B.assets/image-20220507110830868.png)

# java.net.InetSocketAddress

该类可以创建一个 Socket IP 地址。当试图去解析一个 hostname 时使用。

```java
import java.net.InetSocketAddress;

public class InetSocketAddressDemo {
    public static void main(String[] args) {
        // 构造方法
        InetSocketAddress socketAddress = new InetSocketAddress("localhost", 8080);
        // 常用方法
        InetAddress address = socketAddress.getAddress();
    }
}
```

# java.net.InetAddress

该类表示一个 IP 地址

```java
import java.net.InetAddress;

public class InetAddressDemo {
    public static void main(String[] args) {
        try {
            // 构造方法，查询主机 ip 地址
	        InetAddress address = InetAddress.getByName("www.baidu.com");
            // 常用方法
			String hostAddress = address.getHostAddress();
            String hostName = address.getHostName();
        } catch (UnknownHostException e) {
            // 无法解析主机异常
            e.printStackTrace();
        }
    }
}
```



# TcpServer

## java.net.ServerSocket

创建一个 socket server

```java
import java.net.ServerSocket;
import java.net.Socket;
import java.io.InputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class TcpServerSocketDemo {
    public static void main(String[] args) {
        ServerSocket server = null;
        Socket socket = null;
        InputStream is = null;
        ByteArrayOutputStream baos = null;
        try {
            // 1.创建服务地址
            server = new ServerSocket(9999);
            // 2.等待客户端连接
            socket = server.accept();
            // 3.读取客户端消息
            is = socket.getInputStream();
            baos = new ByteArrayOutputStream();
            byte[] buffer = new byte[1024];
            int len;
            while ((len = is.read(buffer)) != -1) {
                baos.write(buffer, 0, len);
            }
            System.out.println(baos.toString());
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // 关闭资源
            if (baos != null) {
                try {
                    baos.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (is != null) {
                try {
                    is.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (socket != null) {
                try {
                    socket.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (server != null) {
                try {
                    server.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```



## java.io.FileOutputStream

socket server 持久化文件流

```java
import java.net.ServerSocket;
import java.net.Socket;
import java.io.File;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.IOException;

public class TcpServerSocketDemo {
    public static void main(String[] args) {
        ServerSocket server = null;
        Socket socket = null;
        InputStream is = null;
        FileOutputStream fos = null;
        OutputStream os = null;
        try {
            // 1.创建服务地址
            server = new ServerSocket(9999);
            // 2.等待客户端连接
            socket = server.accept();
            // 3.读取客户端消息
            is = socket.getInputStream();
            // 4.写入文件
            fos = new FileOutputStream(new File("C:\\Users\\miao\\Desktop\\java-utils\\test.txt"));
            byte[] buffer = new byte[1024];
            int len;
            while ((len = is.read(buffer)) != -1) {
                fos.write(buffer, 0, len);
            }
            System.out.println("ready");
            // 5.通知客户端文件接收完成
            os = socket.getOutputStream();
            os.write("200".getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            // 关闭资源
            if (fos != null) {
                try {
                    fos.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (os != null) {
                try {
                    os.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (is != null) {
                try {
                    is.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (socket != null) {
                try {
                    socket.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (server != null) {
                try {
                    server.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```



# TcpClient

## java.net.Socket

创建一个 socket client

```java
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.io.OutputStream;
import java.io.IOException;

public class TcpClientSocketDemo {
    public static void main(String[] args) {
        Socket socket = null;
        OutputStream os = null;
        try {
            // 1.创建一个 Socket 连接
            InetAddress server = InetAddress.getByName("localhost");
            int port = 9999;
            socket = new Socket(server, port);
            // 2.发送消息 IO 流
            os = socket.getOutputStream();
            os.write("Hello, Server, I'm Client.".getBytes());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (os != null) {
                try {
                    os.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (socket != null) {
                try {
                    socket.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```



## java.io.FileInputStream

socket client 上传文件流

```java
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;

public class TcpClientSocketDemo {
    public static void main(String[] args) {
        Socket socket = null;
        OutputStream os = null;
        FileInputStream fis = null;
		InputStream is = null;
		ByteArrayOutputStream baos = null;
        try {
            // 1.创建一个 Socket 连接
            InetAddress server = InetAddress.getByName("localhost");
            int port = 9999;
            socket = new Socket(server, port);
            // 2.读取文件流
            fis = new FileInputStream(new File("C:\\Users\\miao\\Desktop\\new 1.txt"));
            // 3.发送消息 IO 流
            os = socket.getOutputStream();
            byte[] buffer = new byte[1024];
            int len;
            while ((len = fis.read(buffer)) != -1) {
                os.write(buffer, 0, len);
            }
            // 4.通知服务器文件传输完毕
            socket.shutdownOutput();
            // 5.确定服务器接收完毕
            is = socket.getInputStream();
            baos = new ByteArrayOutputStream();
            byte[] buffer2 = new byte[1024];
            int len2;
            while ((len2 = is.read(buffer2)) != -1) {
                baos.write(buffer2, 0, len2);
            }
            if (baos.toString().equals("200")) {
                System.out.println("200 OK");
            }
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (fis != null) {
                try {
                    fis.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (baos != null) {
                try {
                    baos.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (is != null) {
                try {
                    is.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (os != null) {
                try {
                    os.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            if (socket != null) {
                try {
                    socket.close();              
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```



# UdpReceiver

udp 没有服务器的概念，只有发送端和接收端的概念。

udp 发送端同时也是接收端，二者可以动态转化。

## java.net.DatagramSocket

udp 接收数据包

```java
import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.SocketException;
import java.io.IOException;

public class UdpReceiverSocketDemo {
	public static void main(String[] args) {
		DatagramSocket socket = null;
		try {
			// 1.创建一个 UdpSocket
			socket = new DatagramSocket(9999);
			// 2.接收数据包
			byte[] buffer = new byte[1024];
			DatagramPacket packet = new DatagramPacket(buffer, 0, buffer.length);
			socket.receive(packet);
			System.out.println(new String(packet.getData(), 0, packet.getLength()));
		} catch (SocketException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (socket != null) {
				socket.close();
			}
		}
	}
}
```

# UdpSender

## java.net.DatagramSocket

udp 发送数据包

```java
import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.io.IOException;

public class UdpSenderSocketDemo {
    public static void main(String[] args) {
        DatagramSocket socket = null;
        try {
            // 1.创建一个 UdpSocket
            socket = new DatagramSocket();
            // 2.指定服务器地址
            InetAddress host = InetAddress.getByName("localhost");
            // 3.创建一个要发送的数据包
            String msg = "Hello World!";
            DatagramPacket data = new DatagramPacket(msg.getBytes(), msg.getBytes().length, host, 9999);
            // 4.发送数据包
            socket.send(data);
        } catch (SocketException e) {
            e.printStackTrace();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (socket != null) {
				socket.close();              
            }
        }
    }
}
```

# UdpOnlineChatDemo

利用多线程，实现 udp 在线聊天功能

## ReceiverThread

```java
package UdpOnlineChatDemo;

import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class UdpReceiverSocketDemo implements Runnable {
	DatagramSocket socket = null;
	BufferedReader reader = null;
	private int receiver_port;

	/**
	 * @parameter sender_port
	 */
	public UdpReceiverSocketDemo(int receiver_port) {
		this.receiver_port = receiver_port;
		try {
			socket = new DatagramSocket(receiver_port);
		} catch (SocketException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void run() {
		while (true) {
			try {
				byte[] buffer = new byte[1024];
				DatagramPacket packet = new DatagramPacket(buffer, 0, buffer.length);
				socket.receive(packet);
				byte[] msg = packet.getData();
				System.out.println(packet.getAddress().
				                   getHostAddress() + ":" + packet.getPort() + "---: " + new String(msg, 0, packet.getLength()));
			} catch (IOException e) {
				e.printStackTrace();
			}
			/* finally {
				if (socket != null) {
					socket.close();
				}
			}
			*/
		}
	}
}
```



## SenderThread

```java
package UdpOnlineChatDemo;

import java.net.DatagramSocket;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class UdpSenderSocketDemo implements Runnable {
	DatagramSocket socket = null;
	BufferedReader reader = null;
	private int sender_port;
	private String receiver_ip;
	private int receiver_port;
	/**
	 * @parameter sender_port
	 * @parameter receiver_ip
	 * @parameter receiver_port
	 */
	public UdpSenderSocketDemo(int sender_port, String receiver_ip, int receiver_port) {
		this.sender_port = sender_port;
		this.receiver_ip = receiver_ip;
		this.receiver_port = receiver_port;
		try {
			socket = new DatagramSocket(sender_port);
		} catch (SocketException e) {
			e.printStackTrace();
		}
		reader = new BufferedReader(new InputStreamReader(System.in));
	}

	@Override
	public void run() {
		while (true) {
			try {
				String msg = reader.readLine();
				DatagramPacket packet = new DatagramPacket(msg.getBytes(), msg.getBytes().length, InetAddress.getByName(receiver_ip), receiver_port);
				socket.send(packet);
			} catch (UnknownHostException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
			/* finally {
			    if (reader != null) {
			        try {
			            reader.close();
			        } catch (IOException e) {
			            e.printStackTrace();
			        }
			    }
			    if (socket != null) {
			        socket.close();
			    }
			}
			*/
		}
	}
}
```



## ChatUser1

```java
package UdpOnlineChatDemo;

public class ChatUser1 {
    public static void main(String[] args) {
        // start receiver
		new Thread(new UdpReceiverSocketDemo(8888)).start();
		// start sender
        new Thread(new UdpSenderSocketDemo(8887, "localhost", 9999)).start();
    }
}
```



## ChatUser2

```java
package UdpOnlineChatDemo;

public class ChatUser2 {
    public static void main(String[] args) {
        // start receiver
		new Thread(new UdpReceiverSocketDemo(9999)).start();
		// start sender
        new Thread(new UdpSenderSocketDemo(9998, "localhost", 8888)).start();
    }
}
```

## Start

```java
java UdpOnlineChatDemo.ChatUser1
java UdpOnlineChatDemo.ChatUser2
```

# URL 资源下载

统一资源定位器 URL（Uniform Resource Locator）

## java.net.URL

建立一个 URL 对象

```java
import java.net.URL;
import java.net.MalformedURLException;

public class URLDemo {
	public static void main(String[] args) {
		try {
			URL url = new URL("https://www.baidu.com/");
			String protocol = url.getProtocol(); // 获取协议名
			String host = url.getHost(); // 获取主机名
			int port = url.getPort(); // 获取端口名
			String path = url.getPath(); // 获取路径名
			String file = url.getFile(); // 获取文件名（全路径）
            String file = url.getQuery(); // 获取文件名
		} catch (MalformedURLException e) {
			e.printStackTrace();
		}
	}
}
```



## java.net.URLConnection

建立一个 URL 连接对象

```java
import java.net.URL;
import java.net.URLConnection;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.io.InputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class URLDemo {
	public static void main(String[] args) {
        InputStream is = null;
        FileOutputStream fos = null;
		try {
			URL url = new URL("https://www.baidu.com/");
            HttpURLConnection urlConn = (HttpURLConnection) url.openConnection();
            is = urlConn.getInputStream();
            fos = new FileOutputStream(new File("URLDemo.txt"));
            byte[] buffer = new byte[1024];
            int len;
            while ((len = is.read(buffer) != -1) {
                fos.write(buffer, 0, len);
            }
		} catch (MalformedURLException e) {
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
            if (is != null) {
                try {
                    is.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
	}
}
```



# java 远程调用 Restful 接口

# HttpURLConnection

# HttpClient

## CookieHandler & CookieManager

https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/CookieManager.html

The HTTP cookie management in java.net package looks like:

> ```
>                   use
>  CookieHandler <------- HttpURLConnection
>        ^
>        | impl
>        |         use
>  CookieManager -------> CookiePolicy
>              |   use
>              |--------> HttpCookie
>              |              ^
>              |              | use
>              |   use        |
>              |--------> CookieStore
>                             ^
>                             | impl
>                             |
>                   Internal in-memory implementation
> ```

# OkHttp

# RestTemplate

# Dubbo RPC

# Feign

