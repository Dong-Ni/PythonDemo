#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：找到年龄最大的人，并输出。请找出程序中有什么问题。
#程序分析：无。

if __name__ == "__main__":
    person = {"Li": 18, "hello": 40, "world": 50}
    beg = "Li"
    for key in person:
        if person[beg]< person[key]:
            beg = key

    print(key, person[key])

    print(max(person), person[max(person)])
    print(min(person))