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
可迭代对象：能够使用for遍历的数据都是可迭代对象
    迭代对象内部实现了迭代协议（这个对象拥有__iter__这个方法）

迭代器:迭代器也是可迭代对象的一种
    迭代器： 不仅仅实现了__iter__这个方法，还实现了__next__方法
    迭代对象转换为迭代器：迭代器 = iter(可迭代对象)
    迭代器：可以使用内置函数next进行迭代
生成器:


"""
li = [11, 22, 33, 44]
li_tor = iter(li)


# next函数
print(next(li_tor))
print(next(li_tor))
print(next(li_tor))
print(next(li_tor))
# 注意点：当使用next获取完迭代器中所有的元素之后，再次使用next进行迭代，
# 会抛出迭代器停止的异常
print(next(li_tor))
# li = list(range(10000))
# li_tor = iter(range(10000))




# print('------------------')
# for i in li_tor:
#     print(i)