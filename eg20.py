#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
# 再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

#程序分析：

high = 100
total = 0
for i in range(1, 11):
    if i == 1:
        total += high
    else:
        total += high * 2
    high *= 0.5

print("total mile %d" %total)
print("last mile %f" %high)