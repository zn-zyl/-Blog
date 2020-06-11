"""
=============================
@Time : 2020/5/13 21:02
@Author : AllyZhou
@FileDec: 装饰器
==============================
"""
"""
开放封闭原则
封闭：函数原有的功能进行封闭不允许修改
开放：允许函数进行扩展
"""


# 无参数装饰器
# def derector(func):
#     """

#     :param func: 来接收被装饰的函数名
#     :return:
#     """
#
#     def wrapper():
#         """
#         :return: 新功能的逻辑写在这里
#         """
#         print("新功能的逻辑")
#         func()  # 调用原功能
#
#     return wrapper
#
#
# @derector  # 装饰器装饰的规则 wrapper = func = derector(func)  fun()=wrapper()
# def func():
#     print("原功能的逻辑")


# func()  # = wrapper()
#
#
# # # 有参数装饰器  固定的模板
# def derector2(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#
#     return wrapper
#
#
# @derector2  # 装饰器装饰的规则 add = derector2(add)
# def aplous(a):
#     print(a ** 2)
#
#
# @derector2
# def add(a, b):
#     print(a + b)
#
#
# add(1, 2)
# aplous(1)
#
#
# # 装饰器传参
# def var(name):
#     def derector3(func):
#         def wrapper(*args, **kwargs):
#             print(name)
#             func(*args, **kwargs)
#
#         return wrapper
#
#     return derector3
#
#
# @var(
#     "python27")  # derecttor3 = var("python27")   再用derector3来装饰mixn  mixn=derector3(mixn) mixn()=wrapper() derector3()=wrapper()
# def mixn(a, b):
#     print(a * b)
#
#
# mixn(2, 3)
#
#
# # 多装饰器装饰一个函数
# def derector2(func):
#     def wrapper1(*args, **kwargs):
#         print("先执行wrapper1")
#         func(*args, **kwargs)  # 执行的其实是wrapper2()
#
#     return wrapper1
#
#
# def derector(func):
#     """
#
#     :param func: 来接收被装饰的函数名
#     :return:
#     """
#
#     def wrapper2(*args, **kwargs):
#         """
#         :return: 新功能的逻辑写在这里
#         """
#         print("后执行wrapper2")
#         func(*args, **kwargs)  # 最后执行func2
#
#     return wrapper2
#
#
# # 多个装饰器传参
# @derector2
# @derector  # func2 = derector(fun2) fun2=wrapper2    wrapper2=derector2(wrapper2) wrapper2=wrepper1 先执行wrapper1() func（）执行的是wrapper()
# def fun2(a, b):
#     print(a - b)
#
#
# fun2(1, 3)
#
#
# # 多装饰器装饰一个函数
# def derector2(func):
#     def wrapper1(*args, **kwargs):
#         print("先执行wrapper1")
#         func(*args, **kwargs)  # 执行的其实是wrapper2()
#
#     return wrapper1
#
#
# def var(name):
#     def derector3(func):
#         def wrapper(*args, **kwargs):
#             print(name)
#             func(*args, **kwargs)  # derector3装饰fun2()
#
#         return wrapper
#
#     return derector3

#
# def derector(func):
#     """
#
#     :param func: 来接收被装饰的函数名
#     :return:
#     """
#
#     def wrapper2(*args, **kwargs):
#         """
#         :return: 新功能的逻辑写在这里
#         """
#         print("后执行wrapper2")
#         func(*args, **kwargs)  # 执行的是derector3()
#
#     return wrapper2


# 多个装饰器装饰一个函数
# @derector
# @var("python27")  # derector3 =var("python27)  derector3 = derector(derecto3) derector3=wrapper2
# def fun2(a, b):
#     print(a - b)
#
#
# fun2(1, 3)
#
#
# # 装饰器去装饰类
def derector6(func):
    """

    :param func: 接收被装饰的函数/类
    :return:
    """

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@derector6
class MyTest:  # MyTest = derector6(MyTest)
    pass


m = MyTest()
#
#
# # 类装饰器装饰函数
# class Myderector:
#     def __init__(self, func):
#         print("调用__init__方法")
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("调用__call__方法")
#         self.func()
#
#
# @Myderector  # func44 = Myderector(func44)  func44即为类Myderector的对象，使用__init__方法初始化了一个对象 调用func44（）即调用类的__call__方法
# def func44():
#     print("这个是原来的功能")
#
#
# func44()
#
#
# # 静态方法 动态方法 类只读属性
# class Mymethod:
#     @classmethod
#     def func(cls):
#         print("这是动态方法 可以通过类名来调用")
#
#     @staticmethod
#     def func2():
#         print("这是静态方法 可以通过类名来调用")
#
#     @property
#     def func33(self):
#         a = 1
#         # print("这是只读属性 只能通过类对象来调用")
#         return "abc"
#
#
# m = Mymethod()
# Mymethod.func()
# Mymethod.func2()
# m.func33
#
#
# class MyTTest:
#     def __init__(self):
#         print("这个是init方法在类创建对象时调用")
#
#     def __call__(self, *args, **kwargs):
#         print("这个是call方法可以让对象像函数一样调用 对象加括号或触发这个方法")
#
#     # def __new__(cls, *args, **kwargs):
#     #     super().__new__()  #一般不常用 需要继承父类的__new方法
#     #     print("这是__new__方法 一般不常用 需要继承父类的__new__方法，在实例化一个对象时会先调用这个方法 初始化完后 在这个函数内部调用__init")
#
#
# m = MyTTest()  # 调用__init__
# m()  # 调用__call__
#
# # 递归时会用到 根据参数缓存每次函数调用结果，对于相同参数的，无需重新函数计算，直接返回之前缓存的返回值；
# from functools import lru_cache
#
#
# @lru_cache(maxsize=128)
# def func(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         res = func(n - 1) + func(n - 2)
#         return res
#
#
# res = func(500)
# print(res)
#
#
# class Mytesttt(object):
#     def __init__(self, name, age):
#         print("这是init方法")
#
#     @staticmethod
#     def __new__(cls, *args, **kwargs):  # 入参先传入__new__方法，然后调用__init__初始化
#         print(args)
#         return super().__new__(cls)
#
#
# m = Mytesttt(11, 22)
#
# # 实现 每次创建对象时无论调用几次都会返回第一次创建的对象
# class MyClass:
#     __obj = None
#     @staticmethod
#     def __new__(cls,*args,**kwargs):
#         if not cls.__obj:
#             # 如果没有创建过对象，就调用父类的方法创一个
#             cls.obj = super().__new__(cls)
#             return cls.__obj
#         else:
#             # 如果创建了，则把第一次的对象返回
#             return cls.__obj
#
# m = MyClass(11,22)
# print(m)
# m1 = MyClass()
# print(m1)


# class ShowClassName(object):
#     def __init__(self, func):
#         print("调用iniit")
#         self._func = func
#
#     def __call__(self, *args, **kwargs):
#         print('class name:', self._func.__name__)
#         print("传入的参数为：", args)
#         return self._func()
#
#
# @ShowClassName
# class Foobar(object):  # foobar = shouclasname(foobar)  foorbar()
#     # def __init__(self, a):
#     #     self.a = a
#     def fun(self,b):
#         # print("a的值为", self.a)
#         print("b的值为", b)
# foo = Foobar()
# foo.fun(4)
a = [1,2,3,4,5]
aa = [1]
print(len(aa))

import random
b = a[random.randint(0,5)]
print(b)
