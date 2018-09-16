#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：求输入数字的平方，如果平方运算后小于 50 则退出。
#程序分析：无


while(True):
    num = float(input("输入任意一个数："))
    if num*num < 50:
        break

print("exit")
