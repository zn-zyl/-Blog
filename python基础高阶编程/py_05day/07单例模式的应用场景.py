"""
============================
Author:柠檬班-木森
Time:2020/5/15   21:53
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""

单例模式应用：
应用的目的：减少程序的内存开销
web自动化框架，接口自动化框架：

日志：

"""
# import logging
#
# res = logging.getLogger("musen")
# res2 = logging.getLogger("musen2")
#
# print(id(res))
# print(id(res2))


from requests.sessions import Session


class MySession(Session):
    __obj = None

    @staticmethod
    def __new__(cls, *args, **kwargs):
        if not cls.__obj:
            # 如果没有创建多对象，就调用父类的new方法创建一个
            cls.obj = super().__new__(cls)
            return cls.__obj
        else:
            # 如果创建了，则把第一次的对象返回
            return cls.__obj


s = MySession()
b = MySession()

print(id(s))
print(id(b))
