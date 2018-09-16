#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，
# 然后输出到一个磁盘文件"test"中保存。

if __name__ == "__main__":
    fp = open("text.txt", "w")
    str = input("please input a str:")
    print("before", str)
    str = str.upper()
    print("after", str)
    fp.write(str)
    fp = open("text.txt", "r")
    print(fp.read())
    fp.close()

