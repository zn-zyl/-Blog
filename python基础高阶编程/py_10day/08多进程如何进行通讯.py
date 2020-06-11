"""
=============================
@Time : 2020/5/27 21:45
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
进程之间通信：使用队列
multiprocessing.Queue:可以多个进程之间共用（通用）跨进程通讯
queue.Queue模块只能在一个进程中使用 一个进程中多个线程使用
"""
from multiprocessing import Queue, Process



def work1(q):
    for i in range(1000):
        n = q.get()
        n += 1
        q.put(n)

    print("work1 n执行后的值", q.get())


def work2(q):
    for i in range(1000):
        n = q.get()
        n += 1
        q.put(n)
    print("work2 n执行后的值", q.get())


if __name__ == '__main__':
    # 队列要在主进程中创建 当成参数传给子进程
    q = Queue()
    q.put(100)
    t = Process(target=work1, args=(q,))
    t1 = Process(target=work2, args=(q,))
    t.start()
    t1.start()
    t.join()
    t1.join()
    print("n", q.get())
