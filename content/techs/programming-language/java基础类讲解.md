# java.util.Scanner

BV1EE411T7kK

```java
import java.util.Scanner;

public class ScannerDemo {
    public static void main(String[] args) {
        // 1.创建对象（接收键盘的输入流）
        Scanner sc = new Scanner(System.in);
        // 2.接收变量
        String str = sc.nextLine();
        // 3.关闭输入流对象
        sc.close();
    }
}
```

# 正则表达式（Regular Expression）

## java.util.regex.Pattern

BV1Eq4y1E79W

```java
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class  RegexDemo {
    public static void main(String[] args) {
        String content = "";
        String regex = "[1-9][0-9]{4-9}";
        // 1.创建模式对象（正则表达式对象）
        Pattern pattern = Pattern.compile(regex);
        // 2.创建一个匹配器对象
        // 理解：Matcher 匹配器对象按照 Pattern(模式/样式)，到 content 文本中匹配
        Matcher matcher = pattern.matcher(content);
        // 3.开始匹配器循环
        // 匹配内容，放到 matcher.group(0)
        while (matcher.find()) {
            /* 
            1.matcher.find() 根据 Pattern 规则，定位满足规则的字符串
            2.找到后，将字符串记录到 matcher 对象的 group 属性 group[0] = 0，把该子字符串的结束的索引+1的值，记录到 group[1] = index
            3.
            */
            System.out.println("找到：" + matcher.group(0));
        }
        
    }
}
```



## Matches

BV1JW411h7Up

```java
public class  RegexDemo {
    public static void main(String[] args) {
        String str = "";
        // QQ 号正则规则
        String regex = "[1-9][0-9]{4-9}";
        boolean flag = str.matches(regex);
    }
}
```

