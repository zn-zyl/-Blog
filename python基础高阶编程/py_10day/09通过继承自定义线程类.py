"""
=============================
@Time : 2020/5/27 21:55
@Author : AllyZhou
@FileDec: 
==============================
"""
from multiprocessing import Process, Queue
import requests

"""
创建4个进程发送100个请求
"""


class Myprocess(Process):
    def __init__(self, q):
        super().__init__()  # 重写后需要调用父类init 创建线程
        self.q = q

    def run(self):  # 方法名必须是run() 通过start()来调起
        """
        线程执行的任务函数
        :return:
        """
        while not self.q.empty():
            # 当队列中不为空时即进行下面操作
                url = self.q.get()
                requests.get(url)
                print(f"发送请求：{url}")
            # 打印进程id
                print(f"{self.pid}")


# 创建队列
q = Queue()
# 创建一个100个url放进队列里
for u in range(100):
    url = 'https://www.baidu.com'
    q.put(url)
q_list = []

# 开4个进程执行100个url
for i in range(4):
    p = Myprocess(q)
    q_list.append(p)
    p.start()
for i in q_list:
    i.join()
