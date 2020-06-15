"""
============================
Author:柠檬班-木森
Time:2020/5/8   21:32
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# all:判读可迭代对象中所有的数据都为真（布尔值为True）

# name = 1
# age = 18
# gender = '男'
# res = all((name, age, gender))
# print(res)

# any:迭代对象内只要有一个元素为真，返回True
name = 0
age = 0
gender = None
res2 = any((name, age, gender))
print(res2)

aa = 2000


# locals:获取当前局部的作用域所有的变量，以字典形式进行输入

# globals:获取当前作用域类的所有全局变量，以字典形式属性
def func():
    a = 100
    b = 200
    print(locals())
    print(globals())


func()
