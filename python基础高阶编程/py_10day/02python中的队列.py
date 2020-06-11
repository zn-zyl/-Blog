"""
=============================
@Time : 2020/5/27 20:13
@Author : AllyZhou
@FileDec: 
==============================
"""
from queue import Queue, LifoQueue, PriorityQueue

"""
队列：多个线程进行通信时能确保安全
1.先入先出
2.后入先出
3.优先级队列
"""
# 初始化一个队列 默认是不限定队列的长度，也可以通过参数去指定队列中数据的最大长度
q = Queue()
q1 = Queue(maxsize=4)

# 1、往队列中添加数据
q.put(100)
q1.put(1000)
q1.put(1000)
print(q.qsize())
# 队列中数据满了会堵塞，等待队列中的数据少了再加 可以设置等待的超时时间
# q1.put(2000, timeout=1)
# 往队列中添加数据不等待，如果队列中数据已满直接报错
q1.put(100, block=False)
# 2.往队列中获取数据
q.get()
q1.get()

# 获取数据 设置等待的超时时间
q1.get(timeout=1)
# 获取数据不等待，如果队列中没有数据直接报错
q1.get(block=False)
# 3.判断队列中数据是否为空 队列中数据为空，返回True
q.empty()
# 4.判断队列中数据是否已满 队列中数据已满 返回True
q.full()
# 5.往队列中添加数据不等待
q.put_nowait()
# 6.获取数据不等待
q1.get_nowait()
# 7.获取队列中任务数量（多少条数据）
q.qsize()
# 8.join
q1.join()
