"""
=============================
@Time : 2020/5/24 13:16
@Author : AllyZhou
@FileDec: __add__魔术方法
==============================
"""
# python只能同类型的数据之间相加

class Myclass:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        """
        在打印类对象的时候会被调用
        :return:
        """
        return str(self.age)

    def __add__(self, other):
        return self.age + other.age


m = Myclass("ZZ", 18, "NV")
m1 = Myclass("ZC", 19, "NAN")
print(m + m1)
