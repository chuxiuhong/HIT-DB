#coding=utf8
from memory import memory

m = memory(10,12,10)

m[0] = [1,2,3,4,5]
m.store(0,1)
m.load(5,1)
print m
'''
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