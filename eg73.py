#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：反向输出一个链表。
#程序分析：无。

if __name__ == "__main__":
    ptr = []
    for i in range(5):
        num = int(input("please input a number:\n"))
        ptr.append(num)

    print(ptr)
    ptr.reverse()
    print(ptr)