"""
=============================
@Time : 2020/5/24 18:39
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
类  创建对象
类是通过什么创建的？： 元类
通过type能够查看数据的类型，其实返回的类型就是创建对象的类
所有的类都是type类型的，type就是元类
元类的作用：创建类

type和object:
python中所有的类都是type创建出来的，包括object也是type创建出来的
python3中所有的类都继承object type这个类也是继承于object
"""
# class Myclass:
#     pass
# print(type(Myclass))

"""如何通过type去创建类 需要传3个参数 1类名 2继承的父类（tuple) 3 类的属性和方法（dict)"""


# res = type(1)
# print(res)

class Base:
    name = "base_name"


def func(self):
    print("这是方法")


def __init__(self, age):
    self.age = age


Myclass = type("Myclass",
               (Base,),
               {"NAME": "MY", "ATTR": 19, "func": func, "__init__": __init__})
m = Myclass(18)
print(m.age)
print(m.ATTR)
m.func()


# 自定义元类
class Mytype(type):
    def __new__(cls, *args, **kwargs):
        pass
