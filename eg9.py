#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：暂停一秒输出。
#程序分析：使用 time 模块的 sleep() 函数。

import  time
a = [1, 'hello', 'nd', 'world', 999]
for i in a:
    print(i)
    time.sleep(1)
