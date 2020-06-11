"""
=============================
@Time : 2020/5/27 21:14
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
进程：进程是操作系统资源分配的基本单位
     一个进程中可以有多个线程
线程： 线程是操作系统任务调度的基本单位
python中同一个进程中的线程 是没办法并行的（GIL)
多个进程可以同时进行

每个进程之间资源是独立的
"""
from multiprocessing import Process


def work1(name):
    for i in range(20):
        print(f"{name}在浇花")


def work2(name):
    for i in range(20):
        print(f"{name}在做饭")


t = Process(target=work1, args=("jerry",))
t2 = Process(target=work2, args=("jerry",))
t.start()
t2.start()
t.join()
t2.join()
