"""
=============================
@Time : 2020/5/28 21:43
@Author : AllyZhou
@FileDec: 
==============================
"""
import time
from multiprocessing import Process, Queue

"""
一、使用队列和进程完成下面要求

1、用一个队列来存储数据

2、创建一个专门生产数据的进程类，当队列中数据数量少于50时，开始生产数据，每次生产200个数据，添加到队列中，每生产完一轮 暂停1秒  

3、创建一个专门获取数据的进程类，当 队列中数据数量  大于10时就开始获取，,循环获取，每次获取20个。当 队列中数据数量  少于10的时候，暂停2秒 

4、 创建一个进程生产数据 ，5个进程获取数据


"""


class Produce(Process):
    """
    生产商品进程类
    """

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        # 当队列中数据数量<50时开始生产数据
        if self.q.qsize() < 50:
            for i in range(200):
                self.q.put(i)
            time.sleep(1)


class Consumer(Process):
    """
    获取数据进程类
    """

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        if self.q.qsize() >= 10:
            for i in range(20):
                self.q.get()
                self.q.task_done()
        else:
            time.sleep(2)


def main():
    q = Queue()
    # 创建一个生产数据进程
    p = Produce(q)
    p.start()
    p.join()
    # 创建5个消费数据进程
    q_list = []
    for i in range(5):
        C = Consumer(q)
        C.start()
        q_list.append(C)
    for i in q_list:
        i.join()


if __name__ == '__main__':
    main()
