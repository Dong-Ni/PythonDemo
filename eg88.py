#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    n = 1
    while n <= 7:
        a = int(input("input a number:"))
        while a < 1 or a > 50:
            a = int(input("input a number:"))
        print(a*"*")
        n+=1