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

from ddt import data


def musen(name, age):
    def doc(func):
        """
        :param func: 接收被装饰的函数的
        :return:
        """
        def wrapper(*args, **kwargs):
            print('装饰器扩展的功能代码')
            print("装饰器传递的参数name：", name)
            print("装饰器传递的参数age：", age)
            # 调用原功能函数
            func(*args, **kwargs)
            print('----------执行完毕-----------')

        return wrapper
    return doc


@musen('python27', 18)  # ===>  work = var('python')(work)
def work(a, b):
    print("a+b:", a + b)


work(11, 22)
