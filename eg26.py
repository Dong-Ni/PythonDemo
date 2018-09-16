#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：利用递归方法求5!。
#程序分析：递归公式：fn=fn_1*4!

def fact(complex):
    sum = 0
    if complex > 1:
       sum = complex * fact(complex-1)
    else:
        sum = complex
    return sum

print(fact(5))
