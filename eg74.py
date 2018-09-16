#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：列表排序及连接。
#程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。

if __name__ == "__main__":
    a = [1, 4, 3]
    b = [5, 6, 8]
    a.sort()
    print(a)

    #连接
    print(a+b)

    #连接
    a.extend(b)
    print(a)