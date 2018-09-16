#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：求一个3*3矩阵主对角线元素之和。
#程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。

a = [[3, 4, 5],[4, 5, 6],[5, 6, 7]]
sum = 0

for i in range(0, 3):
    for j in range(0, i+1):
        if i == j:
            sum = sum + a[i][j]
print(sum)