"""
============================
Author:柠檬班-木森
Time:2020/5/15   20:04
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from ddt import ddt, data

#  第三方模块ddt装饰器类，
# @ddt        #  TestLoginCase = ddt(TestLoginCase)
# class TestLoginCase(unittest.TestCase):
#     pass

# [('k','v'),()]


#  自定义可以装饰类的装饰器
# def class_decorate(cls):
#     cls.name = 'musen'
#     cls.age = 18
#     return cls


# @class_decorate
# class MyTest:
#     pass


# @class_decorate
# class MyClass:
#     pass


# print(MyTest.name)
# print(MyTest.age)

print("---------------------------------------")

count = {}


def doc(func):
    """
    :param func: 接收被装饰的函数/类
    :return:
    """
    count[func] = 0
    def wrapper(*args, **kwargs):
        # 调用原功能函数
        count[func] += 1
        return func(*args, **kwargs)

    return wrapper


#
@doc  # MyTestCase = doc(MyTestCase)
class MyTestCase:
    pass


MyTestCase()
# MyTestCase()
# MyTestCase()
#
# print(count)
