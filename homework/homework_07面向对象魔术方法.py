"""
=============================
@Time : 2020/5/19 22:50
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
第一题：基于pymysql模块实现一个数据库操作的上下文管理器（目的：实现自动关闭连接对象和游标）"""
import pymysql

# 1、实现一个操作mysql的上下文管理器（可以自动断开连接）

# class Mysql(object):
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#
#
#     def __enter__(self):
#         # 连接数据库
#         self.conn = pymysql.Connect(self.args,self.kwargs)
#         self.cursor = self.conn.cursor()
#         return self.cursor
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.cursor.close()  # 关闭游标
#         self.conn.close()  # 关闭数据库连接
#         print(exc_type)
#
#
# with Mysql(host="127.0.1", port=3306, user="root",
#            passwd="mysql", charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor) as f:
#     f.execute('SELECT * FROM students')
#     res = f.fetchone()
#     print(res)  # 返回字典

"""
第二题：自定义一个列表类型，实现对象可以之间可以 使用 -  来进行操作
# 要求：如果一个对象减去另一个对象，则把和被减对象中一样的数据给删除掉
# 如下：
li1 = MyList([11, 22, 33, 44])
li2 = MyList([1, 22, ])
res = li1 - li2
# res 打印的结果为[11,33,44]
"""


class MyList(list):
    def __sub__(self, other):
        for j in self:
            if j in other:
                self.remove(j)
        return self

    # def __sub__(self, other):
    #     new_list = []
    #     for i in self:
    #         if i not in other:
    #             new_list.append(i)
    #     return new_list
    # def __sub__(self, other):
    #     return [i for i in self if i not in other]


li1 = MyList([11, 22, 33, 44])
li2 = MyList([1, 22, ])
print(li1 - li2)
