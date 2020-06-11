"""
=============================
@Time : 2020/5/24 17:18
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
__slots__ :
1.可以覆盖__dict__属性 只要这个类定义了__slots__属性，python就不会给这个类添加__dict__属性
2.可以限制类的对象的属性绑定
3.__solots__ = [] 什么属性都不能添加

应用场景：
1.定义的类需要创建大量的对象可以通过__slots_来指定对象属性，覆盖__dict__减少内存开销
2.要限定类对象绑定的属性
"""

class Mytest:
    __slots__ = ["age","gender","name"]
    def __init__(self,age):
        self.age = age

    def func(self):
        print("func")

m = Mytest(18)
m1 = Mytest(20)
m2 = Mytest(23)
# m.name1 = "musen1"  # 报错 m这个实例对象 只有三个属性 没有name1属性 不能添加
# print(m.__dict__)  # 不会给类对象添加__dict__属性
#print(Mytest.__dict__) # 类属性依然有
print(m2.__slots__)

