#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：学习使用按位或 | 。
#程序分析：0|0=0; 0|1=1; 1|0=1; 1|1=1

if __name__ == "__main__":
    a = 0x77
    b = a | 0x3
    print('a | b is 0x%x' % b)
    b |= 0x7
    print("a | b is 0x%x" %b)