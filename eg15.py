#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，
# 60-89分之间的用B表示，60分以下的用C表示。
#程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

iSocre = int(input("请输入一个1到100之内的成绩："))

if iSocre >= 90:
    grade = 'A'
elif iSocre >= 60:
    grade = 'B'
else:
    grade = 'C'

print("%d 属于 %s" %(iSocre, grade))