"""
=============================
@Time : 2020/6/2 18:06
@Author : AllyZhou
@FileDec: 
==============================
"""
from gevent import monkey
monkey.patch_all()
import gevent
import time

"""
gevent模块又对greenlet进行了一层封装 当程序遇到io耗时等待的时候 会自动进行切换
gevent中默认是遇到gevent.sleep()会进行切换
如果让gevent遇到io自动切换,节省运行时间 需要在程序的导包处加一个monkey补丁,注意：只能在单线程中用，不支持多线程
加了monkey补丁 遇到time.sleep也会自动切换

线程的切换：耗时io操作  网络磁盘 input output 
协程切换：遇到io操作
"""

#
# def work1():
#     for i in range(6):
#         gevent.sleep(1)
#         print(f"浇花的第{i + 1}次")
#
#
# def work2():
#     for i in range(6):
#         gevent.sleep(1)
#         print(f"打枪的第{i + 1}次")
# # 创建两个协程
# g1 = gevent.spawn(work1)
# g2 = gevent.spawn(work2)
# # 线程等待协程执行结束再往下执行
# # gevent中是遇到gevent.sleep()会自动进行切换
# g1.join()
# g2.join()

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


def work2():
    for i in range(5):
        gevent.sleep(1)
        print(f"打枪第{i+1}次")


# 10000个请求 开5000个协程来跑
urls = ["https:www.baidu.com" for i in range(10000)]

def work3():
    while urls:
        url = urls.pop()
        time.sleep(0.5)
        print(f"正在请求url:{url}")

# 创建5000个协程
@timeit
def main():
    cor_list = []
    for i in range(5000):
        cor = gevent.spawn(work3)
        cor_list.append(cor)

    for i in cor_list:
        i.join()

main()


