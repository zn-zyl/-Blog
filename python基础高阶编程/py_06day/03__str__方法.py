"""
=============================
@Time : 2020/5/24 13:07
@Author : AllyZhou
@FileDec: 
==============================
"""


class Myclass:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        """
        在打印类对象的时候会被调用
        :return: 1、该方法必须有return，第二返回值必须为字符串
        """
        return self.name


m = Myclass("ZZ", 18, "NV")
m1 = Myclass("ZC", 19, "NAN")
print(m)
print(m1)
