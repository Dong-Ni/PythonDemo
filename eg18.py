#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#程序分析：关键是计算出每一项的值。
tmp = 0
lst = []
sum = 0
a = int(input("输入一个数字："))
n = int(input("输入次数："))

for i in range(n):
    tmp = tmp + a
    a = a*10
    lst.append(tmp)
    sum += tmp
    print(tmp)

print(sum)