---
date: 2026-02-12T12:00:00+08:00
title: Java Regular Expression
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


# 正则表达式（Regular Expression）

## 参考资料

[java.util.regex.Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)


## 常用规则

| 元字符 | 含义 | 示例 |
|--------|------|------|
| `.` | 匹配除换行符外的任意单个字符 | `a.c` 匹配 "abc"、"a-c" |
| `^` | 匹配字符串开始 | `^abc` 匹配以 "abc" 开头的字符串 |
| `$` | 匹配字符串结束 | `xyz$` 匹配以 "xyz" 结尾的字符串 |
| `*` | 前一个字符0次或多次 | `ab*c` 匹配 "ac"、"abc"、"abbc" |
| `+` | 前一个字符1次或多次 | `ab+c` 匹配 "abc"、"abbc"（不匹配 "ac"） |
| `?` | 前一个字符0次或1次 | `ab?c` 匹配 "ac" 或 "abc" |
| `X|Y` | 匹配X或Y | `a|b` 匹配 "a" 或 "b" |
| `{n}` | 精确匹配n次 | `a{3}` 匹配 "aaa" |
| `{n,}` | 匹配至少n次 | `a{2,}` 匹配 "aa"、"aaa"、... |
| `{n,m}` | 匹配n到m次 | `a{2,4}` 匹配 "aa"、"aaa"、"aaaa" |
| `()` | 分组，可以使用 `$1` 来引用分组条件 | `'Smith, John', '([A-Za-z]+), ([A-Za-z]+)', '$2 $1'` 匹配 John Smith |

--------------------------------------------------------------------------------

| 字符类 | 含义 | 示例 |
|--------|------|------|
| `[abc]` | 匹配a、b、c中的任意一个 | `[aeiou]` 匹配任意元音字母 |
| `[^abc]` | 匹配除a、b、c外的任意字符 | `[^0-9]` 匹配非数字字符 |
| `[a-z]` | 匹配a到z的任意小写字母 | `[a-z]+` 匹配一个或多个小写字母 |
| `[A-Z]` | 匹配A到Z的任意大写字母 | |
| `[0-9]` | 匹配任意数字 | `\d` 的等价写法 |
| `[a-zA-Z]` | 匹配任意字母 | |
| `[a-z&&[^bc]]` | 匹配a到z的任意小写字母，除了b和c | |
| `[a-z&&[^b-g]]` | 匹配a到z的任意小写字母，除了b到g | |

--------------------------------------------------------------------------------

| 预定义字符 | 含义 | 等价写法 |
|------------|------|----------|
| `\d` | 数字 | `[0-9]` |
| `\D` | 非数字 | `[^0-9]` |
| `\w` | 单词字符（字母、数字、下划线） | `[a-zA-Z0-9_]` |
| `\W` | 非单词字符 | `[^a-zA-Z0-9_]` |
| `\s` | 空白字符（空格、制表符、换行等） | `[ \t\n\x0B\f\r]` |
| `\S` | 非空白字符 | `[^ \t\n\x0B\f\r]` |
| `\h` | 扩展的空白字符 | `[ \t\xA0\u1680\u180e\u2000-\u200a\u202f\u205f\u3000]` |
| `\H` | 非扩展的空白字符 | |


## java.util.regex.Pattern 类

```java
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class RegexDemo {
    public static void main(String[] args) {
        String content = "";
        // 1.定义正则表达式，创建模式对象（正则表达式对象）
        // 示例为 QQ 号正则规则
        String regex = "[1-9][0-9]{4-9}";
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
            */
            System.out.println("匹配到第 "+ matcher.group(1) + "个对象，匹配内容：" + matcher.group(0));
        }
        
    }
}
```


## java.lang.String.matches 方法

```java
public class RegexDemo {
    public static void main(String[] args) {
        String str = "";
        // QQ 号正则规则
        String regex = "[1-9][0-9]{4-9}";
        boolean flag = str.matches(regex);
    }
}
```

