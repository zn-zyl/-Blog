"""
============================
Author:柠檬班-木森
Time:2020/5/15   21:22
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
__init__:类创建对象的时候会触发
__call__:可以让对象像函数一样调用（对象加括号去调用的时候会出触发）

__new__:在通过类创建对象的时候调用！

注意点：一般情况下不要去重写new方法，实现单例模式的时候可以重写new方法来实现

如果重写了new方法，一定要调用父类的new方法，并将结果返回


"""


class Mytest(object):

    def __init__(sel, name, age):
        print("--------init方法--------")

    @staticmethod
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


m = Mytest(111, 22)

print(m)
