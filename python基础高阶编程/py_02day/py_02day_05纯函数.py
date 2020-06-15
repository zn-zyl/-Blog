"""
============================
Author:柠檬班-木森
Time:2020/5/8   21:32
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
纯函数：
简单来说，一个函数的返回结果只依赖于它的参数，
并且在执行过程里面没有副作用，我们就把这个函数叫做纯函数。
函数的副作用：调用函数会对当前的环境造成影响（修改当前环境中的数据）

"""

li = [11, 22]


# 调用的时候会对环境进行修改（修改当前环境中的数据），有副作用
def add_number(a, b):
    li.append(a)
    return a + b


# 返回值会受到外部数据的影响
def add_num(a, b):
    return a + b + li[0]


print(add_num(11, 22))
li.insert(0, 99)
print(add_num(11, 22))


# 没有副作用的函数
def add_number2(a, b):
    return a + b

# print(li)
# add_number(111, 222)
# print(li)
# add_number(123, 3342)
# print(li)
