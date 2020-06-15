"""
============================
Author:柠檬班-木森
Time:2020/5/13   20:20
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
@ddt

@data

@classmethod

@staticmethod

@是装饰器的语法

开放封闭原则：
封闭：以及实现的功能代码对修改是封闭
开放：对代码功能的扩展时开放的

装饰器：时开放封闭原则的一种体现。
作用：在不修改功能代码的同时，给代码扩展新的功能



"""

# 需求：给下面的功能函数添加一个新的功能：自动化测试，要求：要遵循开放封闭的原则（不能更改函数内部代码，以及调用方式）




def docaretor(f):
    def wrapper():
        print('新增的功能：自动化测试')
        # 调用原功能函数
        f()
        # print(f)
    return wrapper


@docaretor  # @docaretor 的作用等同于后面那一行代码==>  func = docaretor(func)
def func():
    print('功能函数原有的代码一：敲代码')
    print('功能函数原有的代码二：写作业')


# func = 100
# print(func)
# func = docaretor(func)
# func()
# print(func)




