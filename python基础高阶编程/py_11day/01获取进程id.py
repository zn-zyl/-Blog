"""
=============================
@Time : 2020/6/2 17:36
@Author : AllyZhou
@FileDec: 
==============================
"""

from multiprocessing import Process
import os

n = 100


def work1():
    global n
    for i in range(500000):
        n += 1
    print(f"进程{os.getpid()}work1执行完毕n的值：", n)
    print(f"子进程的父进程id:{os.getppid()}")


def work2():
    global n
    for i in range(500):
        n += 1
    # 获取子进程id
    print(f"进程{os.getpid()}work2执行完毕n的值：", n)
    # 获取子进程里的父进程id
    print(f"子进程的父进程id:{os.getppid()}")


if __name__ == '__main__':
    p1 = Process(target=work1)
    p2 = Process(target=work2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print('两个子进程执行结束之后，主进程打印的n:', n)
    # 获取主进程id
    print(f"主进程获取id:{os.getpid()}")
