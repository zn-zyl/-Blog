"""
=============================
@Time : 2020/5/24 15:27
@Author : AllyZhou
@FileDec: 伪多态
==============================
"""
"""
面向对象编程的三大特征：
封装 继承 多态
封装：将数据和方法放在一个类中就构成了封装。
继承：Python中一个类可以继承于一个类，也可以继承多个类。被继承的类叫父类或者叫基类baseclass。继承的类叫子类。
多态：指的是一类事物，有多种形态，一个抽象类有多个子类。因而多态的概念依赖于继承。
不同的子类对象调用相同的方法产生不同的执行结果。多态可以增加代码的灵活度。
"""

class Base(object):
    def run(self):
        print("base的run方法：吃饭")


class A(Base):
    def run(self):
        print("A的run方法：喝咖啡")


class B(Base):
    def run(self):
        print("B的run方法：喝茶")


def fun(name: Base):
    if not Base:
        raise TypeError("{} is not Base".format(name))
    name.run()


b = Base()
fun(b)
a = A()
fun(a)
b = B()
fun(b)
