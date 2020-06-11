"""
=============================
@Time : 2020/5/24 17:06
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
类调用__dict__返回类属性和方法的字典
实例调用__dict__属性，返回的值是实例相关的实例属性
"""


class Mytest:
    name = "ss"

    def __init__(self, age):
        self.age = age

    def func(self):
        print("func")


m = Mytest(18)
m1 = Mytest(24)
m3 = Mytest(19)
print(m.__dict__)
print(m1.__dict__)
print(m3.__dict__)
print(Mytest.__dict__)
