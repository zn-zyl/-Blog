"""
=============================
@Time : 2020/5/24 15:56
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
类里面的私有属性:声明这个属性仅限类内部使用，外部不要引用
(如有私有属性进行修改，恕不通知，引用者后果自负)
_开头 在类外面可以访问
__开头 在类外面可以间接访问，不能直接访问
"""


class Mytest:
    attr = 100
    _attr = 100
    __attr = 100

    def __init__(self, name):
        self.name = name

    def func(self):
        """
        实例方法内部：封装和实例对象相关的操作
        方法内部通常会涉及到实例对象的属性或方法的应用
        :return:
        """


        print("我的名字是{}".format(self.name))

    @classmethod
    def fun2(cls):
        """
        类方法内部：需要应用到类属性或者是类方法 内部的逻辑
        只和类有关，和具体的某一个对象是没有关联的
        :return:
        """
        print("attr的属性为：{}".format(cls.attr))

    @staticmethod
    def fun3():
        """
        方法内部封装的代码：通常不会涉及到类也不会涉及到具体的对象
        纯粹的功能代码，不会受到内部的任何影响
        :return:
        """
        pass


print(Mytest.attr)
print(Mytest._attr)
print(Mytest._Mytest__attr)
