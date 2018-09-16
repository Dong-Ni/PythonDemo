#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：输入某年某月某日，判断这一天是这一年的第几天？

#程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：

iYear = int(input("请输入年：\n"))
iMonth = int(input("请输入月：\n"))
iDay = int(input("请输入日：\n"))

sum = 0
leap = 0
mouths = [0,31,59,90,120,151,181,212,243,273,304,334]

if 0 < iMonth and iMonth < 12:
    sum = mouths[iMonth-1]
else:
    print("请输入正确月份！")

sum += iDay

if(iYear % 400 == 0) or (iYear % 4 == 0 and iYear % 100 != 0):
    leap = 1
if(leap == 1) and (iMonth > 2):
    sum += 1

print("total days is %d" %sum)

