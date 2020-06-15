"""
============================
Author:柠檬班-木森
Time:2020/5/15   20:37
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
python中的魔术方法：__开头  __结尾的方法统统都叫魔术方法

魔术方法都不需要手动去调用，都是在特定的情况下自动执行的

__init__:类创建对象的时候会触发
__call__:可以让对象像函数一样调用（对象加括号去调用的时候会出触发）



"""

# class MyClass:
#
#     def __init__(self):
#         print("这个是init方法")
#
#     def __call__(self, *args, **kwargs):
#         print("这个是__call__方法")
#
#
# m = MyClass()
# m()

"""
通过类来实现装饰器
"""


class Decorate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("装饰器添加的功能代码一")
        self.func()
        print("装饰器添加的功能代码二")


# res = Decorate(11)

@Decorate  # func = Decorate(func)
def func():
    print("原功能函数")


func()
