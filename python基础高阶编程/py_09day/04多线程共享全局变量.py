"""
=============================
@Time : 2020/5/25 21:31
@Author : AllyZhou
@FileDec: 
==============================
"""
from threading import Thread
import os
"""
python中的多线程可以共享全局变量
缺点：但是会出现资源竞争，导致全局变量数据不准确

操作系统如何切换py中的线程？
GIL全局解释器锁 同一时间只会执行一个线程，如果线程要执行必须要先获取全局解释器锁
1.遇到耗时等待 例如time.sleep(1)会自动释放GIL锁
2.当线程执行时间达到一定的阈值
所以线程没有办法并行只能并发


"""


n = 100


def work1():
    global n
    for i in range(100):
        n += 1
    print(f"进程{os.getpid()}work1执行玩不的值:",n)
    # 在子进程里获取父进程id
    print(f"子进程的父进程id:{os.getppid()}")


def work2():
    global n
    for i in range(100):
        n += 1


t1 = Thread(target=work1)
t2 = Thread(target=work2)
# 启动线程
t1.start()
t2.start()
t1.join()
t2.join()
print(f"主进程id:{os.getpid()}")
