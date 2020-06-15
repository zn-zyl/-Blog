"""
============================
Author:柠檬班-木森
Time:2020/5/13   21:26
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""


@data()

"""

import time

print()


def doc(func):
    """
    :param func: 接收被装饰的函数的
    :return:
    """

    def wrapper(*args, **kwargs):
        print('------2-----')
        print('装饰器doc扩展的功能代码')
        # 调用原功能函数
        func(*args, **kwargs)
        print('----------执行完毕--4---------')

    return wrapper


def count_time(func):
    """
    :param func: 接收被装饰的函数的
    :return:
    """

    def wrapper(*args, **kwargs):
        # 函数调用之前获取一下当前的实际：start_time
        start_time = time.time()
        print('-------1----------')
        # 调用原功能函数
        func(*args, **kwargs)
        # 函数调用之后：再获取一下当前时间 end_time
        end_time = time.time()
        print('-----------5-------')
        print('函数运行的时间为：', end_time - start_time)

    return wrapper


#  work = count_time(doc(work))
@count_time  # work = count_time(work)
@doc  # work = doc(work)
def work(a, b):
    print('----3-------')
    print("a+b:", a + b)


work(11, 22)

from ddt import data
