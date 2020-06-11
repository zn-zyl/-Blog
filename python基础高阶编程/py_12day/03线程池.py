"""
=============================
@Time : 2020/6/4 15:21
@Author : AllyZhou
@FileDec: 
==============================
"""
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def work1(name, age):
    for i in range(3):
        time.sleep(1)
        print(f"{name}:------work1----{age}---")


# ThreadPoolExecutor模块实现了上下文管理器协议
# 创建一个线程池，开启5个线程
with ThreadPoolExecutor(max_workers=5) as f:
    f.submit(work1, "musen1", 18)
    f.submit(work1, "musen2", 20)
    f.submit(work1, "musen3", 23)
    f.submit(work1, "musen4", 50)

# 创建一个进程池，开启5个进程  windows要在__main__下面运行

with ProcessPoolExecutor(max_workers=5) as ts:
    ts.submit(work1, "nuonuo", 18)
    ts.submit(work1, "nuonuo", 18)
    ts.submit(work1, "nuonuo", 18)
    ts.submit(work1, "nuonuo", 18)
