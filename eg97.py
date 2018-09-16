#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    filename = input("输入一个文件名字：\n")
    fp = open(filename, "w")
    ch = input("输入一个字符：")
    while ch!="#":
        fp.write(ch)
        print(ch, end=" ")
        ch = input("")

    fp.close()