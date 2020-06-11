"""
=============================
@Time : 2020/6/2 17:38
@Author : AllyZhou
@FileDec: 手动替换
==============================
"""
"""
在协程之间只能手动去切换
"""
import greenlet
import time


def work1():
    for i in range(6):
        time.sleep(1)
        cor2.switch()
        print(f"浇花的第{i + 1}次")


def work2():
    for i in range(6):
        time.sleep(1)
        cor1.switch()
        print(f"打枪的第{i + 1}次")


cor1 = greenlet.greenlet(work1)
cor2 = greenlet.greenlet(work2)
# 不加这行代码，不会执行 通过switch切换到这个协程中去
cor1.switch()
