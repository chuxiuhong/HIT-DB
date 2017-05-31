# memory模拟器使用文档

--------
## 简介
本模拟器主要是用来进行模拟内外存交互的过程，本身为哈工大数据库实验编写，也可用作其他用途。采用Python编写，无第三方依赖库，目前支持Python2版本。外存部分采用文件形式模拟，对用户透明。除基本功能外，提供格式化输出，日志记录。

## Quick Start

```python
#coding=utf8
from memory import memory
m = memory(10,12,10) #初始化创建10个内存块，12个外存块，每个块最多装10个整数
m[0] = [1,2,3,4,5]  #将内存块的第一块赋值，多个数据可以用列表或者元组，等价于m.set(0,[1,2,3,4,5])
m.store(0,1) #将内存块的0号块存到外存的1号块
m.load(5,1) #将外存块的1号块调入内存块的5号块
print m #将当前内外存状态打印出来，包括当前已发生的的IO次数


'''
输出结果如下
Index                Buffer                                             Disk
0                    1 2 3 4 5
1                                                                       1 2 3 4 5
2
3
4
5                    1 2 3 4 5
6
7
8
9
10
11
Disk IO load/store times = 2
'''
```
记录下的日志在同目录下的action.log
```
Wed, 31 May 2017 11:03:22 init 12 disk blocks
Wed, 31 May 2017 11:03:22 set No.0 buffer block = 1 2 3 4 5
Wed, 31 May 2017 11:03:22 store No.0 buffer block to No.1 disk blocks
Wed, 31 May 2017 11:03:22 load No.1 disk block to No.5 buffer block
```

模拟的文件在同目录下的disk文件夹下存储。

主要使用方法如图
![image](https://raw.githubusercontent.com/chuxiuhong/cloudphoto/master/memory.png)

详细的每个方法的参数含义，可见memory.html

