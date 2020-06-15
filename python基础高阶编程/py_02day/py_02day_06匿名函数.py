"""
============================
Author:柠檬班-木森
Time:2020/5/8   21:32
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
匿名函数：
语法：lambda 参数：返回值表达式


"""


def func(a, b):
    return a + b


# res = (lambda x,y:x+y)(11,22)
# print(res)

# func_add = lambda x, y: x + y
# res = func_add(100, 200)
# print(res)


#  --------------匿名函数结合 内置函数：filter一起使用------------
Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest', 'pymysql']

# def fun(x):
#     return len(x)>4
# res = filter(fun,Names)

# res = filter(lambda x: len(x) > 4, Names)
# print(list(res))

# ------------匿名函数结合推导式使用----------
# li = [123, 234, 234, 56, 78, 333, 666]
# li2 = [(lambda x: x/5)(i) for i in li]
# print(li2)
