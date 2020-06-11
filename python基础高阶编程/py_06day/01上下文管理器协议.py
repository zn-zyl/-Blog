"""
=============================
@Time : 2020/5/24 12:06
@Author : AllyZhou
@FileDec: 
==============================
"""


class Myopen:
    def __enter__(self):
        print("--enter----")
        return "python"  # 返回的内容被f接收

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("---exit----")


o = Myopen()

# with python中的关键字 开启一个对象的上下文管理器协议
with o as f:
    print("with中的代码")
    print("f:", f)
