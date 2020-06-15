"""
============================
Author:柠檬班-木森
Time:2020/5/15   21:37
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
装饰器模式
单例模式
作业：装饰器实现单例模式（笔试题）

"""


class MyClass:
    __obj = None

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if not cls.obj:
            # 如果没有创建过对象，就调用父类的new方法创建一个
            cls.obj = super().__new__(cls)
            return cls.obj
        else:
            # 如果创建了，则把第一次的对象返回
            return cls.obj


m1 = MyClass()
m2 = MyClass()
m3 = MyClass()
m4 = MyClass()
m5 = MyClass()

print(id(m1))
print(id(m2))
print(id(m3))
print(id(m4))
print(id(m5))

# MyClass.obj=0
#
# m6 = MyClass()
# print(id(m6))
