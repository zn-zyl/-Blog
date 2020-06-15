"""
============================
Author:柠檬班-木森
Time:2020/5/13   20:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
实现一个计算函数运行时间的装饰器




"""
import time

"""
1、实现一个网络请求超时重试的装饰器，装饰下面的功能函数
如果请求网络超时，或者连接超时，可以重新发送请求，如果重试三次之后，还是超时，抛出对应的异常

def request_http(url):
    import requests
    return requests.get(url, timeout=5)


2、请设计一个装饰器，接收一个int类型的参数number，可以用来装饰任何的函数， 
如果函数运行的时间大于number，则打印出函数名和函数的运行时间 (面试真题)





3、 请设计一个装饰器 ,可以给函数扩展登录认证的功能（提示数账号密码，然后进行校验），
多个函数同时使用这个装饰器， 调用函数的时候，只要登录成功一次，
后续的函数无需再进行登录（默认的认证账号：qwe123，密码：123456）
（面试真题）

"""


def count_time(func):
    """
    :param func: 接收被装饰的函数的
    :return:
    """

    def wrapper(*args, **kwargs):
        # 函数调用之前获取一下当前的实际：start_time
        start_time = time.time()
        # 调用原功能函数
        func(*args, **kwargs)
        # 函数调用之后：再获取一下当前时间 end_time
        end_time = time.time()
        print('函数运行的时间为：', end_time - start_time)

    return wrapper


@count_time
def work():
    for i in range(5):
        time.sleep(1)


@count_time
def number2(a, b):
    print("a+b的结果：", a + b)


# work()

number2(11, 22)

# # 函数调用之前获取一下当前的实际：start_time
# start_time = time.time()
# work()
# end_time = time.time()
# # 函数调用之后：再获取一下当前时间 end_time
#
# # 函数运行的时间:end_time -start_time
# print('函数运行的时间为：', end_time - start_time)




import requests


def request_http(url):
    return requests.get(url, timeout=5)


request_http('http://www.baidu.com')
