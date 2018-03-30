#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(abs(-5))
a = abs
print(a(-6))


def myabs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad type ')
    if x > 0:
        return x
    else:
        return - x


print(myabs(-8))


def non(age):
    # empty function
    pass


import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 5)
print(x, y)
# when return one more object , they will be a tuple
res = move(100, 100, 60, math.pi / 5)
print(res)


def sumAll(arrayNum):
    result = 0
    for num in arrayNum:
        result += num
    return result


print(sumAll([1, 3, 5]))


def sumAll2(*tuple):
    result = 0
    for num in tuple:
        result += num
    return result


print(sumAll2(1, 2, 4, 5))


# keyword parameters
def person(name, age, **keyword):
    print("name:", name, "age:", age, keyword)


person('fzz', 23, height=170, weight=60)


def student(name, age, *, height, weight):
    print(name, age, weight, height)
    return


student('grr', 23, height=165, weight=50)


# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def fact(n):
    return fact_ite(n,1)

def fact_ite(num,pro):
    if num==1:
        return pro
    return fact_ite(num-1,pro*num)

print(fact(5))

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')