"""
=============================
@Time : 2020/5/25 21:55
@Author : AllyZhou
@FileDec: 
==============================
"""
import threading

n = 100

def work1():
    global n
    for i in range(100):
        lock.acquire()
        n += 1
        lock.release()


def work2():
    global n
    for i in range(100):
        lock.acquire()
        n += 1
        lock.release()


t1 = threading.Thread(target=work1)
t2 = threading.Thread(target=work2)

# 创建一把锁
lock = threading.Lock()
# 启动线程
t1.start()
t2.start()
t1.join()
t2.join()
print(n)
