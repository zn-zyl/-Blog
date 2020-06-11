"""
=============================
@Time : 2020/5/25 21:15
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
通过线程类的形式来实现多线程
开启多线程去做同一个事情
一个线程类只能写一个run方法，如果有多个任务要执行，则要创建多个线程类
"""
from threading import Thread


class Mytread(Thread):
    def __init__(self, a, b):
        super().__init__()  # 重写后需要调用父类init 创建线程
        self.a = a
        self.b = b

    def run(self):  # 方法名必须是run() 通过start()来调起
        """
        线程执行的任务函数
        :return:
        """

        for i in range(1000):
            print("我想要计算a+b", self.a + self.b)

# 创建多个线程

for u in range(100):
    Mytread(1, 2).start()
