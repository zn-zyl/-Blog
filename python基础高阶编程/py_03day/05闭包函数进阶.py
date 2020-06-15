"""
============================
Author:柠檬班-木森
Time:2020/5/11   21:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
闭包：
闭包函数实现的三个条件：
    1、函数中嵌套一个函数
    2、外层函数返回的是嵌套的内层函数
    3、嵌套的内层函数对外部作用域有非全局变量的引用

闭包函数调用：返回的不仅仅是个函数，这个函数还有一个封闭的外部作用域

"""


def func():
    print('1234')


# 这也是闭包
def func3(n):
    print('闭包函数的func3调用了')
    a = 999

    def wrapper():
        print(n)
        print(a)
        print('闭包中的嵌套函数的wrapper调用了')

    return wrapper


fun = func3(100)
a = 100
n = 10000

fun2 = func3(200)

fun()

"""

"""


from ddt import data