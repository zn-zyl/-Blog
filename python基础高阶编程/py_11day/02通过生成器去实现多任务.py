"""
=============================
@Time : 2020/6/2 15:54
@Author : AllyZhou
@FileDec: 
==============================
"""
import time
"""
同步是先后执行，必须先做A再做B,同步=并发 
异步 做一件事同时可以做另一件事 互不干扰 异步=并行
协程切换几乎不耗费资源
"""
#计算时间的装饰器
def decorator(func):
    def wrapper():
        # 函数执行之前获取系统时间
        start_time = time.time()
        func()
        # 函数执行之后获取系统时间
        end_time = time.time()
        print('执行时间为：', end_time - start_time)
        return end_time - start_time

    return wrapper


def work1():
    for i in range(5):
        print(f"第{i + 1}次浇花")
        yield


def work2():
    for i in range(5):
        print(f"第{i + 1}次打墙")
        yield
@decorator
def main():
    g1 = work1()
    g2 = work2()
    while True:
        try:
            next(g1)
            next(g2)
        except StopIteration:  # next()迭代器完成会引发stopiteration异常
            break



main()
