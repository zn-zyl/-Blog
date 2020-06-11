"""
=============================
@Time : 2020/4/28 23:04
@Author : AllyZhou
@FileDec: 命名元祖 推导式
==============================
"""

from collections import namedtuple

Student = namedtuple("students", ['name', 'age', 'gender'])
tu2 = Student("小明", 18, "男")
tu3 = Student("小红", 18, "女")
print(tu2.name)
print(isinstance(tu2, tuple))

"""
推导式
列表推导式
字典推导式
生成器表达式
"""
# 列表推导式
li2 = ["day{}".format(i) for i in range(100)]
print(li2)
#列表推导式结合条件if判断一起使用
li3 = ["day{}".format(i) for i in range(100) if i % 2 == 0]
print(li3)
# 字典推导式
# dic = {key :value for i  in range(100)}
#{"data0":1,"data1":2,"data2":3}
dict2 = {"data{}".format(i):i+1 for i in range(3)}
print(dict2)