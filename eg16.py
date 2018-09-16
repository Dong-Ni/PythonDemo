#!/usr/bin/python
# -*- coding: UTF-8 -*-

#题目：输出指定格式的日期。
#程序分析：使用 datetime 模块。

import datetime

if __name__ == '__main__':
    print(datetime.date.today().strftime("%d/%m/%Y"))

    miyazakiBirthDate = datetime.date(1941, 1, 5)
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))

    nextDay = miyazakiBirthDate + datetime.timedelta(days=1)
    print(nextDay.strftime('%d/%m/%Y'))

    firstDay = miyazakiBirthDate.replace(year=miyazakiBirthDate.year +1)
    print(firstDay.strftime('%d/%m/%Y'))


