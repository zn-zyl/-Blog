"""
=============================
@Time : 2020/6/3 18:09
@Author : AllyZhou
@FileDec: 
==============================
"""
import time
from multiprocessing import Pool


def work1(name):
    for i in range(3):
        time.sleep(1)
        print(f"{name}:------work1----{i}-")


def main():
    # 创建一个拥有5个进程的线程池
    po = Pool(5)
    # 往进程池添加4任务  当任务数超过进程数数时，会先按照最大进程数来执行，执行完后，空出来的进程会继续执行
    # po.apply_async(work1, ("musen1",))
    # po.apply_async(work1, ("musen1",))
    # po.apply_async(work1, ("musen1",))
    # po.apply_async(work1, ("musen1",))
    # po.apply_async(work1, ("musen1",))
    # po.apply_async(work1, ("musen1",))
    for i in range(20):
        po.apply_async(work1, ("musen1",))
    # 关闭进程池（进程池停止接收任务）
    po.close()
    # 主进程等待进程池中的任务结束在往下执行
    po.join()


if __name__ == '__main__':
    main()
