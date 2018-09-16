#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n

#程序分析：无。

def peven(n):
    sum = 0
    for i in range(2, n+1, 2):
        sum += 1/i

    return sum

def podd(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += 1/i

    return sum

def dcall(fp, n):
    s = fp(n)
    return s

if __name__ == "__main__":
    a = int(input("请输入一个整数："))
    if a % 2 == 0:
        print("是偶数呀：", dcall(peven, a))
    else:
        print("是奇数呀：", dcall(podd, a))

