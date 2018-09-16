#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
#程序分析：学会分解出每一位数。

nInput = int(input("输入一个不多于5位的正整数："))

a = nInput // 10000
b = nInput % 10000 // 1000
c = nInput % 1000 // 100
d = nInput % 100 // 10
f = nInput % 10

print("万位:%d" %a)
print("千位:%d" %b)
print("百位:%d" %c)
print("十位:%d" %d)
print("个位:%d" %f)
