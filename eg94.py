#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == "__main__":
    import time
    import random

    realNum = 23
    guessNum = int(input("input a num:"))
    beginTime = time.clock()
    while guessNum != realNum:
        if guessNum > realNum:
            guessNum = int(input("to lager please input a small one:"))
        elif guessNum < realNum:
            guessNum = int(input("to small please input a lager one:"))

    endTime = time.clock()
    var = (endTime - beginTime)/18.2
    print(var)

    if var < 15:
        print('you are very clever!')
    elif var < 25:
        print('you are normal!')
    else:
        print('you are stupid!')

