"""
============================
Author:柠檬班-木森
Time:2020/5/6   21:32
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
数值：int float 
序列：list  str  tuple
散列：set  dict

可迭代对象：

"""
from collections import namedtuple

tu = (11, 22, 33)

# stu = ('木森', 18, 'python自动化')
# print(stu[0])

# 命名元组
student = namedtuple('Students', ('name', 'age', 'skill'))
stu = student('木森', 18, 'python自动化')
# print(type(stu))
# print(isinstance(stu, tuple))
# print(stu[1])
# print(stu.age)

