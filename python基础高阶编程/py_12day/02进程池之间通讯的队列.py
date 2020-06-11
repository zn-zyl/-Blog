"""
=============================
@Time : 2020/6/4 15:01
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
进程池和进程池之间进行通讯使用进程池里的队列
进程池的Queue 如果要使用Pool创建进程，就需要使用multiprocessing.Manager()中的Queue()
而不是multiprocessing.Queue()，否则会报错
"""
import time
from multiprocessing import Pool,Manager


def work1(name,q):
    for i in range(3):
        time.sleep(1)
        print(f"{name}:------work1----{i}----{q.get()}")


def main():
    # 创建一个用于进程池通讯的队列
    q = Manager().Queue()
    for i in range(1000):
        q.put(f"data-{i}")

    # 创建一个拥有5个进程的线程池
    po = Pool(5)

    for i in range(20):
        po.apply_async(work1, ("musen1",q))
    # 关闭进程池（进程池停止接收任务）
    po.close()
    # 主进程等待进程池中的任务结束在往下执行
    po.join()


if __name__ == '__main__':
    main()
