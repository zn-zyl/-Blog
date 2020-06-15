"""
============================
Author:柠檬班-木森
Time:2020/5/13   20:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
装饰器装饰有参数的函数

"""


def doc(func):
    """
    :param func: 接收被装饰的函数的
    :return:
    """

    def wrapper(*args, **kwargs):

        # 调用原功能函数
        func(*args, **kwargs)

    return wrapper


@doc
def number():
    print("没有参数的函数")


@doc
def number1(a):
    print('a的二次方:', a ** 2)


@doc
def number2(a, b):
    print("a+b的结果：", a + b)


@doc
def number3(a, b, c):
    print("a+b+c的结果：", a + b + c)


number()
print('----------------------------')
number1(a=100)
print('----------------------------')
number2(a=11, b=22)
print('----------------------------')
number3(1, 2, 3)
