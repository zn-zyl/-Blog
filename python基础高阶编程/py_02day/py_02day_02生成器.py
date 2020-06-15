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


"""


# 生成器表达式
# tu = (i for i in range(10000))
# print(next(tu))
# print(next(tu))
# print(next(tu))


# 生成器函数：
def gen():
    print('-------1------')
    for i in range(10):
        yield {'a':i}
        print('-------2--------')
    # yield
    # yield 22
    # yield 33
    # yield 44

g = gen()
# next方法
# print('第1次生成数据：', next(g))
# print('第2次生成数据：', next(g))
# print('第3次生成数据：', next(g))
# print('第4次生成数据：', next(g))
# print('第5次生成数据：', next(g))
# print('第6次生成数据：', next(g))
# print('第7次生成数据：', next(g))
# print('第8次生成数据：', next(g))
# print('第9次生成数据：', next(g))
# print('第10次生成数据：', next(g))
# print('第11次生成数据：', next(g))



