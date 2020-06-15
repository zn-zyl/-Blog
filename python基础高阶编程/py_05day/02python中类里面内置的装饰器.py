"""
============================
Author:柠檬班-木森
Time:2020/5/15   20:27
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


class MyTest:
    @classmethod
    def func(cls):
        print("类方法")

    @staticmethod
    def func01():
        print("静态方法")

    @property
    def name(self):
        print('只读属性')
        return '7890'


# MyTest.func()
#
# MyTest.func01()
m = MyTest()

res = m.name

print(res)
