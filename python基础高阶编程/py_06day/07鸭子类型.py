"""
=============================
@Time : 2020/5/24 15:43
@Author : AllyZhou
@FileDec: 
==============================
"""

"""
鸭子类型：他并不要求严格的继承体系，关注的不是对象的类型本身，而是他是如何使用的，一个对象只要
看起来像鸭子，走起路来像鸭子 那么他就可被看作是鸭子
"""

class Base(object):
    def run(self):
        print("base的run方法：吃饭")


class A:
    def run(self):
        print("A的run方法：喝咖啡")


class B:
    def run(self):
        print("B的run方法：喝茶")


def fun(name: Base):
    """
    python函数的参数没有类型限制 所以不存在多态
    :param name:
    :return:
    """
    name.run()


b = Base()
fun(b)
a = A()
fun(a)
b = B()
fun(b)
