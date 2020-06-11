"""
=============================
@Time : 2020/5/27 21:45
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
Python 多进程默认不能共享全局变量
主进程与子进程是并发执行的，进程之间默认是不能共享全局变量的(子进程不能改变主进程中全局变量的值)

"""
from multiprocessing import Queue, Process

n = 1


def work1():
    global n
    for i in range(200):

        n += 1
    print("work1执行完后n", n)


def work2():
    global n
    for i in range(200):
        n += 1
    print("work2执行完后n", n)


t = Process(target=work1)
t2 = Process(target=work2)
t.start()
t2.start()
t.join()
t2.join()
print("n:", n)
