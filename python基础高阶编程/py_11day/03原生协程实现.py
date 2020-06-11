"""
=============================
@Time : 2020/6/2 16:06
@Author : AllyZhou
@FileDec: 
==============================
"""
import asyncio

"""
原生的协程
async 加在def前面定义协程函数
await:只能写在协程函数中  await后面必须是一个可等待对象(协程 任务 asyncio.sleep()
"""

"""
# -------------协程函数的定义和调用----------------

# 定义一个协程函数
async def work1():
    for i in range(10):
        print(f"work1---浇花--{i}")
  
# 调用协程函数，返回的是一个协程对象      
cor1 = work1()  
# 执行协程
asyncio.run(cor1)

"""


# -------------使用原生的协程实现多任务----------------
# 协程中切换必须要添加等待 await.sleep()

# 定义一个协程函数
async def work1():
    for i in range(10):
        print(f"work1---浇花--{i}")
        await asyncio.sleep(1)

async def work2():
    for i in range(10):
        print(f"work1---打枪--{i}")
        await asyncio.sleep(1)

# 定义一个启动函数
async def run():
    # 调用协程函数，返回的是一个协程对象
    cor1 = work1()
    cor2 = work2()
    # 把协程创建成任务
    task1 = asyncio.create_task(cor1)
    task2 = asyncio.create_task(cor2)
    task3 = asyncio.create_task(work1())
    task4 = asyncio.create_task(work2())
    await task1
    await task2
    await task3
    await task4

if __name__ == '__main__':
    m = run()
    asyncio.run(m)