"""
=============================
@Time : 2020/5/11 21:12
@Author : AllyZhou
@FileDec: 递归函数
==============================
"""
#
import sys


def func(x):
    print(x)
    func(x - 1)


# 获取最大递归深度 一般不用
res = sys.getrecursionlimit()
print(res)
# 设置最大递归深度 一般不用
sys.setrecursionlimit(4000)
func(14)


# -----计算任意数的阶乘------
def fun(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1 * 2
    elif x == 3:
        return 1 * 2 * 3


def func(x):
    if x == 1:
        return 1
    else:
        return func(x - 1) * x


# 通过递归实现斐波拉切数列 第一个数是1，后面的每一个数等于它两两个数相加之和
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def fixbo(x):
    if  x == 1 or x ==2:
        return 1

    # elif x ==3:
    #     return fixbo(2)+fixbo(1)
    #
    # elif x == 4:
    #     return fixbo(2)+fixbo(3)

    # else:
    #     return fixbo(x-1)+fixbo(x-2)


def func3(n):
    def wrapper():
        print(n)
    return wrapper
