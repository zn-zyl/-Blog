"""
=============================
@Time : 2020/5/27 20:55
@Author : AllyZhou
@FileDec: 
==============================
"""
from queue import LifoQueue, PriorityQueue

"""
"""
# 后入先出队列

"""
优先级队列:队列中的数据为元祖类型 y元祖的第一个元素表示 数据的优先级
优先级越小的越先出来
关于优先级，尽量使用数值，如果全是字符串，会按ASCII码进行排序
quene模块一个队列只能在一个进程中使用 一个进程中多个线程使用
"""
q = LifoQueue()
q.put(100)
q.put(200)
q.put(300)
print(q.qsize())
print(q.get())
print(q.get())
print(q.get())

q1 = PriorityQueue()
q1.put((1, 100))
q1.put((2, 200))
q1.put((4, 400))
q1.put((3, 300))

print(q1.get())

print(q1.get())

print(q1.get())

print(q1.get())
