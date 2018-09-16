#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：暂停一秒输出，并格式化当前时间。
#程序分析：无。

import time

a = [1, 'hello', 'nd', 'world', 999]
for i in a:
    print(i)
    #time.sleep(1)

print(time.time())
print(time.localtime(time.time()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
