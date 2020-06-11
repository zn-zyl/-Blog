"""
=============================
@Time : 2020/5/24 12:25
@Author : AllyZhou
@FileDec: 
==============================
"""


class Myopen:

    def __init__(self, filename, mode, encoding='utf8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.f = open(self.filename, self.mode, encoding=self.encoding)

    def __enter__(self):
        return self.f  # 返回的内容被f接收

    def __exit__(self, exc_type, exc_val, exc_tb):  # 接收异常
        self.f.close()


o = Myopen("test.text", "w")

# with python中的关键字 开启一个对象的上下文管理器协议
with o as f:
    f.write("wwwwwdddccc")
