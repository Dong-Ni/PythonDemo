#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：按相反的顺序输出列表的值。
#程序分析：无。

#所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。

a = ['one', 'two', 'three']
for i in a[::-1]:
    print(i)