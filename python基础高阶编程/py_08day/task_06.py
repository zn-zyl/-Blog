"""
============================
Author:柠檬班-木森
Time:2020/5/18   22:21
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================



"""

"""
第一题：基于pymysql模块实现一个数据库操作的上下文管理器（目的：实现自动关闭连接对象和游标）

"""
import pymysql


class DB:
    # 数据库操作的上下文管理器

    def __init__(self, *args, **kwargs):
        self.con = pymysql.connect(*args, **kwargs)
        self.cursor = self.con.cursor()

    def __enter__(self):
        """返回连接对象"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """"""
        self.cursor.close()
        self.con.close()


#
# with DB(host='127.0.0.1', user='root', password="mysql", charset='utf8', port=3306) as db:
#     db.cursor.execute('select * from test.students')
#     res = db.cursor.fetchall()
#     print(res)

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
    """完善代码"""

    def __sub__(self, other):
        # 方式一：for循环去实现
        # new_list = []
        # for i in self:
        #     if i not in other:
        #         new_list.append(i)
        # return new_list

        # 方式二：推导式去实现
        return [i for i in self if i not in other]


m1 = MyList([11, 22, 33, 44])
m2 = MyList([11, 44])
#
# print(m1)
print(m1 - m2)
