"""
=============================
@Time : 2020/5/27 20:35
@Author : AllyZhou
@FileDec: 
==============================
"""
# join 等待队列中的任务执行完毕（不是队列为空，是队列中所有的任务都执行完，队列调用了task_done）
# 告诉队列 任务执行完毕
from queue import Queue

q = Queue()
q.put(100)
q.put(200)
print(q.get())
# 每从队列中获取一个数据，要通知队列数据用完了，就会继续往下执行
q.task_done()
print(q.get())
q.task_done()
# 等待队列中的任务执行完毕（不是队列为空，是队列中所有的任务都执行完，调用了task_done）
q.join()
a = 100
print(a)
