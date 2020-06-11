"""
=============================
@Time : 2020/5/25 20:41
@Author : AllyZhou
@FileDec: 
==============================

"""
from threading import Thread

# python中如何实现多任务
"""
线程 进程 协程
多线程模块：threading
"""


def work1():
    for i in range(100):
        print(f"浇花的第{i+1}秒")


def work2():
    for i in range(100):
        print("work2")

#创造线程
t = Thread(target=work1)
t2 = Thread(target=work2)
# 开启线程
t.start()
t2.start()
# 等待线程执行结束后再往下执行
t.join()
t2.join()
print("aaaa")