"""
=============================
@Time : 2020/5/25 20:52
@Author : AllyZhou
@FileDec: 
==============================
"""

"""
python中的多线程

"""

from threading import Thread

"""
Thread类可以用来创建线程对象  
target：指定线程执行的任务（一般是任务函数）
args kwargs:接受任务函数的参数
name:指定线程的名字 
"""


# 主线程等待子线程执行结束之后再往下执行

def work1(url):
    for i in range(100):
        print(f"第i:{i}个url:{url}")


def work2():
    for i in range(100):
        print("work2")


# 创造线程
t = Thread(target=work1, args=("https:www.baidu.cpmm",), name="周诺诺的线程1")
# t = Thread(target=work1, kwargs={"url": "https:www.baidu.cpmm"}, name="周诺诺的线程1")
t2 = Thread(target=work2, name="周诺诺的线程1")
# 开启线程
t.start()
t2.start()
# 默认等待子线程1执行结束
t.join()  # 等待子线程t执行结束往下运行
t2.join()
# 主线程等待子线程执行结束后再往下执行
print("aaaa")
