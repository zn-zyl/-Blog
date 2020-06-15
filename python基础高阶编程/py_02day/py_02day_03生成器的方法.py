"""
============================
Author:柠檬班-木森
Time:2020/5/8   20:13
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

# 生成器generator

# 生成器表达式
# tu = (i for i in range(10))
# print(tu)

"""
生成器:它是一种特殊的迭代器

创建生成器的两种方式：
1、生成器表达式：(i for i in range(10000))
2、生成器函数：只要函数中使用了yield这个关键字，那么这个函数就是一个生成器函数

3、生成器的send方法可以和生成器内部进行数据交互
4、close：关闭生成器

"""


# 生成器函数：
# def gen():
#     for i in range(10):
#         s = yield i * 5
#         print('send传递进来的数据为:',s)
#
# g = gen()
# next函数
# print('第1次生成数据：', next(g))
# 生成器的send方法：调用send方法执行要执行一次next
# print('第1次使用send方法生成的数据', g.send(100))
# print('第2次使用send方法生成的数据', g.send(200))
# print('第3次使用send方法生成的数据', g.send(300))


# 生成器的send方法可以和生成器内部进行数据交互
# def gen():
#     s = 0
#     for i in range(10):
#         s = yield s**2
#         print('send传递进来的数据为s:',s)
#
#
# g = gen()
# print('第1次生成数据：', next(g))
# print('第1次使用send方法生成的数据', g.send(100))
# print('第2次使用send方法生成的数据', g.send(5))
# print('第2次使用send方法生成的数据', g.send(7))

# close：关闭生成器
# g.close()

def gen2():
    try:
        yield 11
        yield 22
    except Exception as e:
        print(e)

g2 = gen2()

# throw:往生成内部发送一个异常
# print(next(g2))
# g2.throw(ValueError,'主动抛出的异常')



