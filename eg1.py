#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：有四个数字：1、2、3、4，能组成多少个
# 互不相同且无重复数字的三位数？各是多少？

#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。
# 组成所有的排列后再去 掉不满足条件的排列。

a = [1,2,3,4]
num = 0

for i in a:
    for j in a:
        for k in a:
            if (i != j) and (i != k) and (j != k):
                print(i ,j, k)
                num += 1
print(num)
