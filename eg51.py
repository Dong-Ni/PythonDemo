#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：学习使用按位与 & 。
#程序分析：0&0=0; 0&1=0; 1&0=0; 1&1=1。

a = 77
b = 7

print(77&3)
print(3&7)

a = 0x77 #16进制
b = a & 3
print('a & b = %d' % b)
b &= 7
print('a & b = %d' % b)