"""
=============================
@Time : 2020/5/13 23:45
@Author : AllyZhou
@FileDec: 
==============================
"""
import requests
import time
import unittest

"""
1、实现一个网络请求超时重试的装饰器，装饰下面的功能函数
如果请求网络超时，或者连接超时，可以重新发送请求，如果重试三次之后，还是超时，抛出对应的异常
"""

#
# def retry_my(times):
#     def wrapper(func):
#         def wrapper(*args, **kwargs):
#
#             # 循环执行包装的函数
#             for num in range(times + 1):
#                 print("开始第{}次请求".format(num + 1))
#                 try:
#                     res = func(*args, **kwargs)
#                     if res == 200:
#                         print("第{}次请求成功".format(num + 1))
#                 except Exception as e:
#                     print("第{}次请求失败".format(num + 1))
#                     if num == times - 1:
#                         print("第{}次请求失败不在重试,抛出异常".format(times))
#                         raise e
#
#         return wrapper
#
#     return wrapper
#
#
# @retry_my(4)
# def request_http(url):  # request_http=derector(request_http)  request_http()=wrapper()   func()
#     requests.get(url, timeout=5)
#
#
# request_http("http://106.53.68.245:8002/sleep")


# 第二种解法

def derector01(func):
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                print("第{}次执行用例".format(i + 1))
                func(*args, **kwargs)
            except Exception as e:
                print("第{}次执行出现了网络超时，正在重新执行".format(i + 1))
                if i == 2:
                    raise e
            else:
                break  # 请求成功没有报错退出循环

    return wrapper


class TestLogin(unittest.TestCase):
    @derector01
    def test_login(self):
        url = "https://www.baidu.com"
        response = requests.get(url, timeout=0.01)
        assert response.status_code == 200

TestLogin().test_login()
"""
2、请设计一个装饰器，接收一个int类型的参数number，可以用来装饰任何的函数， 
如果函数运行的时间大于number，则打印出函数名和函数的运行时间 (面试真题)
"""


def number(n):
    def derector(func):
        def wrapper(*args, **kwargs):
            t1 = time.time()
            func(*args, **kwargs)
            t2 = time.time()
            if t2 - t1 > n:
                print("函数运行时间大于numer的函数为：{}".format(func.__name__))
                print("函数运行的时间为：{}".format(t2 - t1))

        return wrapper

    return derector


@number(1)
def fun(a, b):
    for i in range(1000):
        time.sleep(2)
        return a * b


fun(1, 2)

"""
3、 请设计一个装饰器 ,可以给函数扩展登录认证的功能（提示数账号密码，然后进行校验），
多个函数同时使用这个装饰器， 调用函数的时候，只要登录成功一次，
后续的函数无需再进行登录（默认的认证账号：qwe123，密码：123456）
（面试真题）
"""

account_status = False  # 默认登录状态为false


def derector2(func):
    def wrapper(*args, **kwargs):
        global account_status
        if not account_status:
            account = input("请输入账号:")
            pwd = input("请输入密码:")
            if account == "qwe123" and pwd == "123456":
                print("登录成功!")
                account_status = True
                func(*args, **kwargs)
            else:
                print("用户名或密码错误登录失败，请重新输入")
        else:
            func(*args, **kwargs)

    return wrapper


#

@derector2
def add(a, b):
    print("两数相加：", a + b)


@derector2
def multiply(a, b):
    print("两数相乘", a * b)


add(1, 2)
multiply(1, 2)

# 第二种解法
