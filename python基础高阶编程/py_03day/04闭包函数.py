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

"""


# 这个不是闭包
# a = 100
# def func():
#     # a = 100
#
#     def wrapper():
#         print(a * 2)
#
#     return wrapper

# 这个才是闭包
def func2():
    a = 100

    def wrapper():
        print(a * 2)

    return wrapper


# 这也是闭包
def func3(n):
    def wrapper():
        print(n)
    return wrapper


def work(n):
    a = 100
    print(a)


work(99)
