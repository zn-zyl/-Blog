"""
=============================
@Time : 2020/5/25 22:15
@Author : AllyZhou
@FileDec: 
==============================
"""

# 1、描述并发和并行的区别
"""
并发：并发是任务书多于cpu核数，通过操作系统的调度算法，实现多个任务一起进行（实际上总有一些任务不在执行），
为交替执行的状态，因为切换任务的速度特别快 所以看起来像是多个任务一起在执行
并行：如果任务数小于cpu核数，任务真的是一起执行的
     
"""

# 2、简单描述python线程的缺陷，以及适用场景
"""
因为有GIL锁的存在，python中的多线程在同一时间没办法同时执行（即没办法实现并行）
适用场景：涉及到网络 磁盘IO的任务都是IO密集型任务，这类任务的特点是cpu消耗很少
任务的大部分时间都在等到IO操作完成（因为IO的速度要远远低于cpu和内存的速度）
"""


# 3、一个列表中有100个url地址（假设请求每个地址需要0.5秒），请设计程序一个程序，获取列表中的url地址，使用4个线程去发送这100个请求，计算出总耗时！
import time
import threading
import requests




# class RequestThread(threading.Thread):
#     """
#     通过类来实现多线程
#     """
#     def __init__(self, url):
#         self.url = url
#         super().__init__()  # 如果自己重定义init初始化方法调用父类的innit方法
#
#     '''发送request请求'''
#
#     def run(self):
#         for i in range(100):
#             res = requests.get(self.url)
#             print('---线程：{}---返回的状态码:{}---'.format(threading.current_thread(), res.status_code))
#
#
def timeit(func):
    """
    计算耗时装饰器
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        s_time = time.time()
        func(*args, **kwargs)
        e_time = time.time()
        print('此程序耗时：', e_time - s_time)

    return wrapper
#
#
# @timeit
# def run_threading(num):
#     t_list = []
#     for i in range(num):
#         # 创建线程
#         t = RequestThread('http://httpbin.org/post')
#         # 启动线程
#         t.start()
#         t_list.append(t)
#
#     for t in t_list:
#         # 主线程等待子线程执行后再执行
#         t.join()
#
#
# run_threading(4)


#url_list = [f"https:www.baidu.com-{i}"for i in range(100)]
urls_g = ("https:www.baidu.com" for j in range(10000))
class MyThread(threading.Thread):
    def fun(self):
        while True:
            try:
                url = next(urls_g)
            except StopIteration:
                break
            else:
                print(f"{self}发送请求{url}")
                time.sleep(0.5)

@timeit
def main():
    t_list = []
    # 创建4个线程
    for i in range(1000):
        t = MyThread()  # 创建线程对象
        t.start()  # 开启该线程
        t_list.append(t)

    # 遍历所有线程对象，设置主线等待子线程执行完
    for t in t_list:
        t.join()


res = main()
