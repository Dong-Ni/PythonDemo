#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：编写input()和output()函数输入，输出5个学生的数据记录。
#程序分析：无。

N = 3
S = 2

student = []
for i in range(N):
    student.append(["", "", []])

def input_s(std):
    for i in range(N):
        std[i][0] = input("请输入名字：\n")
        std[i][1] = input("请输入班级：\n")
        for j in range(S):
            std[i][2].append(int(input("输入一个成绩：\n")))

def output_s(std):
    for i in range(N):
        print("名字:", std[i][0])
        print("班级：", std[i][1])
        for j in range(S):
            print("成绩%d：" %j, std[i][2][j])

if __name__ == "__main__":
    input_s(student)
    print(student)
    output_s(student)

