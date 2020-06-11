"""
=============================
@Time : 2020/5/27 20:07
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
使用线程多的时候一定要注意避免死锁
"""

import threading

n = 100

def work1():
    global n
    for i in range(100):
        lockA.acquire()
        lockB.acquire()
        n += 1
        lockB.release()
        lockA.release()


def work2():
    global n
    for i in range(100):
        lockB.acquire()
        lockA.acquire()
        n += 1
        lockA.release()
        lockB.release()


t1 = threading.Thread(target=work1)
t2 = threading.Thread(target=work2)

# 创建一把锁
lockA = threading.Lock()
lockB = threading.Lock()
# 启动线程
t1.start()
t2.start()
t1.join()
t2.join()
print(n)
