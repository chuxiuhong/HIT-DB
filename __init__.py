# coding=utf8
from Memory import *

if __name__ == '__main__':
    p = Memory(10, 100, 10)
    p.set(2, 180)
    p.store(2, 5)
    p.load(7, 5)
    print p.get(7)
