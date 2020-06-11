"""
=============================
@Time : 2020/5/16 16:48
@Author : AllyZhou
@FileDec: 
==============================
"""
import random

"""第一题 ： 通过装饰器实现单例模式，只要任意一个类使用该装饰器装饰，
那么就会变成一个单例模式的类。(面试真题)"""


# # z装饰器

def derector(cls):
    """

    :param func: 接收被装饰的函数/类
    :return:
    """
    dict = {}

    def wrapper(*args, **kwargs):
        if dict.get(cls):
            return dict[cls]
        else:
            dict[cls] = cls(*args, **kwargs)
            return dict[cls]

    return wrapper


# 单例模式
@derector  # derector = derector(myclass)  derector()
class Myclass:
    pass


"""第二题：请实现一个类，前五次创建对象，每次都可以返回一个新的对象，
第六次开始，每次创建，都随机返回前5个对象中的一个，"""


class Myobject:
    obj_list = []

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if len(cls.obj_list) < 5:
            cls.__obj = super().__new__(cls)
            cls.obj_list.append(cls.__obj)
            return cls.__obj
        else:
            return random.choice(cls.obj_list)
            # return cls.obj_list[random.randint(0, 4)]



m1 = Myobject()
m2 = Myobject()
m3 = Myobject()
m4 = Myobject()
m5 = Myobject()
m6 = Myobject()
m7 = Myobject()
print(id(m1))
print(id(m2))
print(id(m3))
print(id(m4))
print(id(m5))
print(id(m6))
print(id(m7))

"""第三题：通过类实现一个装饰器，既可以装饰函数，有可以装饰器类，不管函数和类需不需要传参都可以装饰，"""


class derector:
    def __init__(self, func):
        print("调用init")
        self.func = func

    def __call__(self, *args, **kwargs):
        print("调用call")
        return self.func(*args, **kwargs)


# 类装饰器装饰函数 传参
@derector
def add(a, b):
    print("两数相加结果为", a + b)


# 类装饰器装饰函数 不传参
@derector
def prin():
    print("打印函数prin")


# 类装饰器装饰类 传参or不传参  类实例化对象时 一定要在call里return回来 否则类对象为none,不能调用类里的方法
@derector
class Mytest:

    def multiply(self, a):
        print("a值为", a ** 2)

    def plus(self):
        print("类装饰器装饰类，不传参")


add(1, 2)
prin()
m = Mytest()
m.multiply(1)
m.plus()
