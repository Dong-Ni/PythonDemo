#!/usr/bin/python
# -*- coding: UTF-8 -*-

testList=[10086, "中国移动", [1,2,4,5]]

print(len(testList))

print(testList[1:])

matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

print(matrix)
print(matrix[1])

col2 = [row[1] for row in matrix]
print(col2)

col2even = [row[1] for row in matrix if row[1]%2 == 0]
print(col2even)