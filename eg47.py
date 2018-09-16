#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：两个变量值互换。
#程序分析：无

def change(a, b):
    tmp = a
    a = b
    b = tmp
    return(a, b)

if __name__ == "__main__":
    first = 1
    second = 2
    print("before", first, second)
    first, second = change(first, second)
    print("change after", first, second)
