---
date: 2026-02-12T12:00:00+08:00
title: Java Set
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

https://www.bilibili.com/video/BV1Yb4y1h7qD?p=5

# 集合

# ArrayList

## 概述

ArrayList 的底层实现是数组。

在对数组增加元素或删除元素时，需要对数组进行逐项的移位操作，开销较大，因此，ArrayList 常用的场合仅限于在尾部追加元素，或是根据下标取值。

ArrayList 常用于根据索引查询，或大量的遍历操作。一般而言，常用 ArrayList。

## new ArrayList<>()

```java
// 实现 List 接口
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable {
    
    // 定义默认的数组容量
    private static final int DEFAULT_CAPACITY = 10;
    // 定义值为空的 object 数组，用于为 new ArrayList<>() 赋值，在不同的构造方法内使用
    private static final Object[] EMPTY_ELEMENTDATA = {};
    private static final Object[] DEFAULTCAPACITY_EMPTY_ELEMENTDATA = {};
    // 定义空 object 数组，用于传递数据元素
    transient Object[] elementData;
    // 数组的长度
    private int size;
    
    // 无参构造方法
    public ArrayList() {
        // 默认为空元素数组
        this.elementData = DEFAULTCAPACITY_EMPTY_ELEMENTDATA;
    }
    
    // 有参构造方法
    public ArrayList(int initialCapacity) {
        // 可以指定数组的长度参数，一般不指定
    }
    public ArrayList(Collection<? extends E> c) {
        // 可以使用 Collection 接口的实现对象来创建数组
    }
    
}
```

## ArrayList.add()

```java
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable {

    ...
    
    public boolean add(E e) {
        // 线程安全处理
        modCount++;
        add(e, elementData, size);
        return true;
    }
    
    private void add(E e, Object[] elementData, int s) {
        if (s == elementData.length)
            // ArrayList 的自动扩容
            elementData = grow();
        elementData[s] = e;
        size = s + 1;
    }
    
    private Object[] grow() {
        return grow(size + 1);
    }
    private Object[] grow(int minCapacity) {
        // 复制 elementData 的值，并创建新长度的数组
        return elementData = Arrays.copyOf(elementData,
                                           newCapacity(minCapacity));
    }
    
    private int newCapacity(int minCapacity) {
        int oldCapacity = elementData.length;
        // 新数组的长度，为原数组长度的 1.5 倍
        int newCapacity = oldCapacity + (oldCapacity >> 1);
        if (newCapacity - minCapacity <= 0) {
            // 初始数组，默认长度为 10
            if (elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA)
                return Math.max(DEFAULT_CAPACITY, minCapacity);
            if (minCapacity < 0) // overflow
                throw new OutOfMemoryError();
            return minCapacity;
        }
        return (newCapacity - MAX_ARRAY_SIZE <= 0)
            ? newCapacity
            : hugeCapacity(minCapacity);
    }
    
}
```



## ArrayList.get()

```java
public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable {

    ...
    
    public E get(int index) {
        // 检查数组下标是否超过数组的 size
        // 注意，根据 ArrayList 的自动扩容机制，数组长度和数组的 size 是不同的
        Objects.checkIndex(index, size);
        return elementData(index);
    }
    
}
```



# LinkedList 

## 概述

LinkedList 的底层实现是双向链表。

链表对于数据的插入、删除效率相较数组要更快。因此，LinkedList 常用的场合仅限于在头、尾部追加元素。不适用于根据下标取值。

LinkedList 常用于插入、删除较多的操作。

## new LinkedList<>()

```java
// 实现了 List 接口
public class LinkedList<E>
    extends AbstractSequentialList<E>
    implements List<E>, Deque<E>, Cloneable, java.io.Serializable
{
    // 链表的长度
    transient int size = 0;
    // Node<E> 节点对象
    // 当前链表的第一个节点对象
    transient Node<E> first;
    // 当前链表的最后一个节点对象
    transient Node<E> last;
    
    // 无参构造方法
    public LinkedList() {
    }
    // 有参构造方法
    public LinkedList(Collection<? extends E> c) {
        // 可以使用 Collection 接口的实现对象来创建数组
    }
    
    // 静态内部类
    private static class Node<E> {
        E item;
        Node<E> next;
        Node<E> prev;

        Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }
    
}
```



## LinkedList.add()

```java
public class LinkedList<E>
    extends AbstractSequentialList<E>
    implements List<E>, Deque<E>, Cloneable, java.io.Serializable
{
    ...
    public boolean add(E e) {
        linkLast(e);
        return true;
    }
    
    void linkLast(E e) {
        // l 是一个 temp 中间值，为了交换链表上一个 node 的 last，和下一个 node 的 first 的值
        final Node<E> l = last;
        final Node<E> newNode = new Node<>(l, e, null);
        last = newNode;
        // 如果为空链表
        if (l == null)
            first = newNode;
        else
            l.next = newNode;
        size++;
        modCount++;
    }
}
```



## LinkedList.get()

链表在底层上没有下标的概念，链表中的每个节点，都记录了节点本身的值，以及前、后两个节点的位置。

因此根据下标获取链表的值，实质上是根据链表插入的顺序逐个寻找链表的值。

链表的这种特性，决定了根据下标获取链表的值，没有数组更有效。

```java
public class LinkedList<E>
    extends AbstractSequentialList<E>
    implements List<E>, Deque<E>, Cloneable, java.io.Serializable
{
    ... 
    public E get(int index) {
        // 判断下标是否越界
        checkElementIndex(index);
        return node(index).item;
    }
    
    Node<E> node(int index) {
        // 将链表二分，如果下标小于链表长度/2，则从链表的头部开始取；如果大于，则从链表的尾部开始取
        if (index < (size >> 1)) {
            Node<E> x = first;
            for (int i = 0; i < index; i++)
                x = x.next;
            return x;
        } else {
            Node<E> x = last;
            for (int i = size - 1; i > index; i--)
                x = x.prev;
            return x;
        }
    }
}
```



## LinkedList.remove()

```java
public class LinkedList<E>
    extends AbstractSequentialList<E>
    implements List<E>, Deque<E>, Cloneable, java.io.Serializable
{
   public boolean remove(Object o) {
       // 如果要移除的是 null
        if (o == null) {
            // 从链表的头开始寻找
            for (Node<E> x = first; x != null; x = x.next) {
                if (x.item == null) {
                    // 移除对象
                    unlink(x);
			       // 移除第一个找到的对象后，即结束
                    return true;
                }
            }
        } else {
            for (Node<E> x = first; x != null; x = x.next) {
                if (o.equals(x.item)) {
                    unlink(x);
                    return true;
                }
            }
        }
        return false;
    }
    
    E unlink(Node<E> x) {
        final E element = x.item;
        final Node<E> next = x.next;
        final Node<E> prev = x.prev;
        // 如果移除的是链表头部节点
        if (prev == null) {
            first = next;
        } else {
            // 将移除节点的前一个节点的尾部指针，指向移除节点的后一个节点
            prev.next = next;
            x.prev = null;
        }
        // 如果移除的是链表尾部节点
        if (next == null) {
            last = prev;
        } else {
            // 将移除节点的后一个节点的头部指针，指向移除节点的前一个节点
            next.prev = prev;
            x.next = null;
        }

        x.item = null;
        size--;
        modCount++;
        return element;
    }
}
```



## LinkedList 特有方法

LinkedList.addFirst()：在起始的位置追加。

LinkedList.addLast()：在末尾的位置追加。

LinkedList.removeFirst()：在起始的位置删除元素。

LinkedList.removeLast()：在末尾的位置删除元素。

LinkedList.getFirst()：获得起始位置的元素。

LinkedList.getLast()：获得末尾位置的元素。

# Stack

## 概述

java 早期栈结构的实现，先进后出

## new Stack<>()

```java
public
class Stack<E> extends Vector<E> {
    // 仅有无参构造
    public Stack() {
    }
}
```

## Stack.push()

压栈

```java
public
class Stack<E> extends Vector<E> {
    ...
    public E push(E item) {
        addElement(item);
        return item;
    }
}

public class Vector<E>
    extends AbstractList<E>
    implements List<E>, RandomAccess, Cloneable, java.io.Serializable
{
    ...
        protected Object[] elementData;
        protected int elementCount;
        protected int capacityIncrement;
    public synchronized void addElement(E obj) {
        modCount++;
        add(obj, elementData, elementCount);
    }
    
    private void add(E e, Object[] elementData, int s) {
        if (s == elementData.length)
            elementData = grow();
        elementData[s] = e;
        elementCount = s + 1;
    }
}
```

## Stack.pop()

出栈

## Stack.peek()

输出栈顶元素

# Queue

## 概述

单端队列，先进先出

队列的定义为接口，有多种实现，最典型的实现为 LinkedList

单端队列：仅有一端进，一端出

## Queue<> queue = new LinkedList<>()

```java
public interface Queue<E> extends Collection<E> {
    // 入队
    boolean offer(E e);
    // 出队
    E poll();
}
```

## Queue.offer();

## Queue.poll();

# Deque

双端队列

双端队列：两端均可进可出，既可以当作队列，也可以当作栈

## Deque<> deque = new LinkedList<>()

## Deque.push()

## Deque.pop()



# HashSet

## 概述

无序，且唯一。

HashSet 的底层实现是哈希表（HashTable）。

哈希表 保证唯一的方式：调用对象的 `hashCode()` 和 `equals()` 方法

Object 类中的 `equals()` 方法，比较的是内存地址，因此如果需要保证某个对象的唯一，需要重写对象的 `hashCode()` 和 `equals()` 方法

`hashCode()`: 计算哈希码，是一个整数，通过哈希码可以计算出数据在哈希表中存放的位置
`equals()`: 添加时出现了冲突，需要通过 `equals()` 方法判断是否相同，

## new HashSet<>()

```java
public class HashSet<E>
    extends AbstractSet<E>
    implements Set<E>, Cloneable, java.io.Serializable
{
    /**
     * HashSet() 底层是 HashMap()
     */
    public HashSet() {
        map = new HashMap<>();
    }

    public HashSet(Collection<? extends E> c) {
        map = new HashMap<>(Math.max((int) (c.size()/.75f) + 1, 16));
        addAll(c);
    }
    public HashSet(int initialCapacity, float loadFactor) {
        map = new HashMap<>(initialCapacity, loadFactor);
    }
    public HashSet(int initialCapacity) {
        map = new HashMap<>(initialCapacity);
    }
}
```

## HashSet.add()

```java
public class HashSet<E>
    extends AbstractSet<E>
    implements Set<E>, Cloneable, java.io.Serializable
{
    /**
     * 添加元素的实质，是将元素放到了 HashMap 的 keySet 中
     */
    public boolean add(E e) {
        return map.put(e, PRESENT)==null;
    }
}
```

## HashSet.contains()

# LinkedHashSet

## 概述

LinkedHashSet 的底层实现是使用链表维护次序的哈希表。

唯一，有序，添加元素的顺序

## new LinkedHashSet<>()

```java
/**
 * LinkedHashSet() 继承 HashSet()
 */
public class LinkedHashSet<E>
    extends HashSet<E>
    implements Set<E>, Cloneable, java.io.Serializable {}
```

# TreeSet

## 概述

TreeSet 的底层实现是二叉树（红黑树）。

唯一，有序，元素的大小顺序

红黑树 保证唯一的方式：实现 `comparable` 接口，通过比较器保证唯一，重写 `compareTo()` 方法

## new TreeSet<>()

```java
public class TreeSet<E> extends AbstractSet<E>
    implements NavigableSet<E>, Cloneable, java.io.Serializable
{
    /**
     * TreeSet() 底层是 TreeMap()
     */
    public TreeSet() {
        this(new TreeMap<>());
    }

    public TreeSet(Comparator<? super E> comparator) {
        this(new TreeMap<>(comparator));
    }
    public TreeSet(Collection<? extends E> c) {
        this();
        addAll(c);
    }
    public TreeSet(SortedSet<E> s) {
        this(s.comparator());
        addAll(s);
    }
}
```



# 哈希表

## 特点

1. 哈希表可以根据内容精确查找，效率很高，例如 get(19)
2. 哈希表无法根据范围来查找，例如 get(num) > 19，范围查找通过二叉树实现更为优秀

## 哈希表内如何添加数据

1. 计算哈希码（调用 `hashCode()` 方法），结果是一个 int 值，证书的哈希码直接取自身即可；

2. 计算哈希表中的存储位置 y = k(x) = x%11

   x: 哈希码 k(x): 函数 y: 在哈希表中的存储位置

3. 添加到哈希表内

   * 情况一：一次添加成功
   * 情况二：多次添加成功（出现了冲突，调用 `equals()` 方法和对应链表的元素进行比较，比较到最后，结果都是 false，此时创建新的节点，存储数据，并加入链表末尾）
   * 情况三：添加失败（出现了冲突，调用 `equals()` 方法和对应链表的元素进行比较，结果出现 ture，表明重复，不添加）

## 哈希表的结构

哈希表，类似于，数组和链表的组合

表1：原数据

| num(内存地址) | x 哈希码 | y = k(x) = x%11 |
| ------------- | -------- | --------------- |
| 23(0x1012)    | 23       | 1               |
| 36(0x2012)    | 36       | 3               |
| 48(0x3012)    | 48       | 4               |
| 86(0x4012)    | 86       | 9               |
| 67(0x5012)    | 67       | 1               |
| 23(0x6012)    | 23       | 1               |
| 47(0x7012)    | 47       | 3               |

表2：哈希表示意

| 索引 | 哈希表                   |
| ---- | ------------------------ |
| 0    |                          |
| 1    | 23(0x1012) -- 67(0x5012) |
| 2    |                          |
| 3    | 36(0x2012) -- 47(0x7012) |
| 4    | 48(0x3012)               |
| 5    |                          |
| 6    |                          |
| 7    |                          |
| 8    |                          |
| 9    | 86(0x4012)               |
| 10   |                          |

## 哈希表取值效率高的原理分析

哈希表将数据分散保存在多个链表内，使用数组进行索引，效率相对较高。

在高版本 jdk 中，哈希表为 数组 + 链表 + 红黑树 的结构，至多比较 7 次，便可以获取一个值

## 哈希表的取值性能

哈希表的取值性能，取决于：

1. 哈希值的计算方法
2. 哈希表的长度，使用 负载因子来衡量，根据实践，负载系数一般在 0.5 左右可以达到查询性能最优，但一般取值为 0.75，可以达到查询性能和空间占用的平衡

$$
负载因子(load factor) = \frac{容量(capacity)}{哈希表长度}
$$

# HashMap

## 概述

key:value 键值对的数据结构，key 和 value 一一对应，其中 key 唯一。

HashMap 的底层是 哈希表，存取速度快。

key 无序

如果 key 重复，后者覆盖前者

HashMap 允许 key 为 null

## new HashMap<>()

```java
public class HashMap<K,V> extends AbstractMap<K,V>
    implements Map<K,V>, Cloneable, Serializable {

    @java.io.Serial
    private static final long serialVersionUID = 362498820763181265L;
    
    /**
     * The default initial capacity - MUST be a power of two.
     */
    static final int DEFAULT_INITIAL_CAPACITY = 1 << 4; // aka 16
    static final int MAXIMUM_CAPACITY = 1 << 30; // 大约 10 亿
    static final float DEFAULT_LOAD_FACTOR = 0.75f; // 默认的负载因子
    static final int TREEIFY_THRESHOLD = 8;
    static final int UNTREEIFY_THRESHOLD = 6;
    static final int MIN_TREEIFY_CAPACITY = 64;
    transient Node<K,V>[] table;
    transient Set<Map.Entry<K,V>> entrySet;
    transient int size;
    transient int modCount;
    int threshold;
    final float loadFactor;
    
    // 有参无参构造方法
    public HashMap() {
        this.loadFactor = DEFAULT_LOAD_FACTOR; 
    }
    public HashMap(int initialCapacity) {
        this(initialCapacity, DEFAULT_LOAD_FACTOR);
    }
    public HashMap(int initialCapacity, float loadFactor) {
        if (initialCapacity < 0)
            throw new IllegalArgumentException("Illegal initial capacity: " +
                                               initialCapacity);
        // 容量最大为 MAXIMUM_CAPACITY
        if (initialCapacity > MAXIMUM_CAPACITY)
            initialCapacity = MAXIMUM_CAPACITY;
        if (loadFactor <= 0 || Float.isNaN(loadFactor))
            throw new IllegalArgumentException("Illegal load factor: " +
                                               loadFactor);
        // 负载因子初始为 16
        this.loadFactor = loadFactor;
        this.threshold = tableSizeFor(initialCapacity);
        // 构造 HashMap 时，并没有创建哈希表
    }
    public HashMap(Map<? extends K, ? extends V> m) {
        this.loadFactor = DEFAULT_LOAD_FACTOR;
        putMapEntries(m, false);
    }
    
    /**
     * 内部类，HashMap 中每一个节点的属性，单向链表结构
     */
    static class Node<K,V> implements Map.Entry<K,V> {
        final int hash; // hashCode
        final K key;  // key
        V value;  // value
        Node<K,V> next; // 下一个节点的地址
        ...
    }
    
}
```

## Map.put()

```java
public class HashMap<K,V> extends AbstractMap<K,V>
    implements Map<K,V>, Cloneable, Serializable {
    
    static final int hash(Object key) {
        int h;
        return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
    }
    
    public V put(K key, V value) {
        return putVal(hash(key), key, value, false, true);
    }
    
    final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
        Node<K,V>[] tab;
        Node<K,V> p;
        int n, i;
        // 当 hashtable 为空时，初始化
        if ((tab = table) == null || (n = tab.length) == 0)
            n = (tab = resize()).length;
        if ((p = tab[i = (n - 1) & hash]) == null)
            tab[i] = newNode(hash, key, value, null);
        else {
            Node<K,V> e; K k;
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))
                e = p;
            else if (p instanceof TreeNode)
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            else {
                for (int binCount = 0; ; ++binCount) {
                    if ((e = p.next) == null) {
                        p.next = newNode(hash, key, value, null);
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        break;
                    p = e;
                }
            }
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }
        ++modCount;
        if (++size > threshold)
            resize();
        afterNodeInsertion(evict);
        return null;
    }
}
```

## Map.get()

# LinkedHashMap

## 概述

key 有序，添加顺序



# TreeMap

## 概述

key 有序，

TreeMap 不允许 key 为 null，null 不可比较大小

# Iterator

## 概述

迭代器是专门用来遍历集合的实现。

for each 的底层实现是迭代器，凡是可以使用 for each 方式实现的遍历，都可以使用 Iterator 来实现

# Collections 工具类

# Properties

java.io.Properties 类是线程安全的：多个线程可以共享一个 Properties 对象，而无需外部同步。

## 构造方法

* `public Properties()`: 创建一个没有默认值的空属性列表。

## 常用方法

* `public void load(InputStream inStream) throws IOException`: 从字节输入流中读取属性列表（键和元素对），按照每行的格式，使用 ISO 8859-1 (Latin 1) 字符集，忽略所有非键值对的数据

* `public void load(Reader reader) throws IOException`: 按照每行的格式，从字符输入流中读取属性列表（键和元素对），忽略所有非键值对的数据

  一般使用指定字符集的字符流对象来加载 properties 对象。

* `public Set<String> stringPropertyNames()`: 返回不可变更的 String 类型的 key 集合（Properties 对象的改变不会影响这个集合）。

* `public void store(OutputStream out, String comments) throws IOException`: 将属性列表，使用字节输出流持久化存储

* `public void store(Writer writer, String comments) throws IOException`: 将属性列表，使用字符输出流持久化存储

* `public Object setProperty(String key, String value)`: 向 Properties 对象中更新键值对数据。调用 HashTable 的 put() 方法

* `public V put(K key, V value)`: 继承 HashTable 的 put() 方法

##  示例

```java
import java.util.Properties;
import java.io.FileReader;
import java.io.FileWriter;
import java.nio.charset.Charset;

public class test1 {
    public static void main(String[] args) throws Exception {
        String filepath = "test.properties";
        // 读取
        Properties properties = new Properties();
        FileReader fr = new FileReader(filepath, Charset.forName("utf-8"));
        properties.load(fr);
        // 遍历打印
        for (String key : properties.stringPropertyNames()) {
            System.out.println(key + "---" + properties.getProperty(key));
        }
        // 修改
        properties.setProperty("name", "李四"); // 等价于 properties.put("name", "李四");
        // 保存
        FileWriter fw = new FileWriter(filepath);
        properties.store(fw, "test");
        // 关闭流资源
        fr.close();
        fw.close();
    }
}
```



