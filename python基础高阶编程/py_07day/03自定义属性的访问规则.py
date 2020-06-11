"""
=============================
@Time : 2020/5/24 17:37
@Author : AllyZhou
@FileDec: 
==============================
"""
"""

"""


class Mytest:
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        """访问属性的时候 会调用这个方法，这个方法的返回值，就是查找的属性值"""
        return super().__getattribute__(item)

    def __getattr__(self, item):
        """该方法在属性查找不存在的情况下会报错：属性不存在。只要定义了该方法 会自动捕获异常，调用该方法"""
        print(f"item:{item}")
        return super().__getattr__(item)



    def __setattr__(self, key, value):
        """属性设置的时候会触发"""
        print(f"key:{key}")
        print(f"value:{value}")
        super().__setattr__(key, value)

    def __delattr__(self, item):
        """删除属性的时候会触发"""
        super().__delattr__(item)

m = Mytest("musen")
# print(m.name)
#print(m.age)
del m.name
print(m.name)
