#!/usr/bin/python
#coding=utf-8
#在一般领域，对正整数 n，如果用 2 到根号 N 之间的所有整数去除，均无法整除，则 n 为质数又叫素数。
import math;

num = [] #存放 1-100 之间的素数
for i in range(2, 100):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        num.append(i) #根据定义如果都无法正常才加入
        if i == 97:
            for index, i in enumerate(num):
                if index == len(num) - 1:
                    print(i)
                else:
                    print(i, end='')
