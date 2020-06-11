"""
=============================
@Time : 2020/5/27 20:44
@Author : AllyZhou
@FileDec: 
==============================
"""
from queue import Queue
from threading import Thread

q = Queue()
q.put(1)


def work1():
    for i in range(20):
        n = q.get()
        n += 1
        q.put(n)


def work2():
    for i in range(20):
        n = q.get()
        n += 1
        q.put(n)


t = Thread(target=work1)
t2 = Thread(target=work2)
t.start()
t2.start()
t.join()
t2.join()
print("n:", q.get())
