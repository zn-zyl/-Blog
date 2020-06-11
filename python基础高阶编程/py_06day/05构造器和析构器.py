"""
=============================
@Time : 2020/5/24 15:07
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
构造器：__new__创建对象 + __init__初始化对象 组成构造器
析构器：__del__ 在对象被删除的时候调用 清理销毁对象
"""

class Myclass:
    def __init__(self):
        print("__init__")
    def __del__(self):
        print("在对象被删除的时候调用")
m = Myclass()
del m