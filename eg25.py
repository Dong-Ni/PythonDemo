#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：求1+2!+3!+...+20!的和。
#程序分析：此程序只是把累加变成了累乘。

sum = 0
for i in range(1, 21):
    t = 1
    for j in range(1, i+1):
        t = t*j
    sum += t
    print(t)
print(sum)