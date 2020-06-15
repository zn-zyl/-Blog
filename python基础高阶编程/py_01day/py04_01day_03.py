"""
============================
Author:柠檬班-木森
Time:2020/5/6   20:31
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests
from requests import get

name = '木森'  # 名字

# 年龄
age = 18


# 查看模块的文档字符串注释
# print(requests.__doc__)


def func(name, age, gender):
    """
    自定义演示文档字符串的函数

    :param name:名字
    :type name:str
    :param age: 年龄
    :type age:int
    :param gender: 性别
    :type :str
    :return:
    :rtype: None
    """
    print(name, age, gender)


class MyTest:
    """
    自定义的类
    """

    def get(self,url,data,params):
        """

        :param url:
        :param data:
        :param params:
        :return:
        """