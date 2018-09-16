#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，
# 插入后此元素之后的数，依次后移一个位置。

if __name__ == "__main__":
    a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]
    print("原始队列：", end="")
    print(a)
    nInsert = int(input("请输入一个数字："))
    end = a[9]
    if nInsert > a[9]:
        a[10] = end
    else:
         for i in range(10):
            if a[i] > nInsert:
                tmp = a[i]
                a[i] = nInsert
                for j in range(i+1, 11):
                    tmp2 = a[j]
                    a[j] = tmp
                    tmp = tmp2
                break
    print("排序后列表：")
    print(a)



