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
    def wrapper(a, b):
        print("通过装饰器扩展的功能代码写这里")
        print("扩展的功能a*b：", a * b)
        # 调用原功能函数
        func(a, b)

    return wrapper


@doc
def add_number(a, b):
    print("a+b的结果：", a + b)


add_number(11, 22)
