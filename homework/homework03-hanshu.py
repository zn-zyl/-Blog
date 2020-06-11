"""
=============================
@Time : 2020/5/9 10:22
@Author : AllyZhou
@FileDec: 迭代器 生成器和匿名函数
==============================
"""

"""1、现在有一个列表   li = [11,21,4,55,6,67,123,54,66,9,90,56,34,22],
请将 大于5的数据过滤出来，然后除以2取余数，结果放到新的列表中（匿名函数结合filter去做）
"""
li = [11, 21, 4, 55, 6, 67, 123, 54, 66, 9, 90, 56, 34, 22]


# print([i % 2 for i in list(filter(lambda x:x > 5, li))])


# """
# 2、定义一个可以使用send传入域名，自动生成一个在前面加上http://，在后面加上路径/user/login的url地址，
#
# 生成器最多可以生成5次数据，生成5条数据之后再去生成，则报错StopIteration
#
# 使用案例：
#
# # 例如:
# res = g.send('www.baidu.com')
# # 生成数据res为：http://www.baidu.com/user/logim
# """
def get_url():
    url = yield
    for i in range(5):
        url = yield "生成的数据res为：{}".format("http://" + url + "/user/login")


# g=get_url()
# next(g)
# print(g.send('www.baidu.com'))
# print(g.send('www.google.com'))
# print(g.send('www.taobao.com'))
# print(g.send('www.baidu.com'))
# print(g.send('www.sohu.com'))
# print(g.send('www.alibaba.com'))

# 3、算法面试题

# 有一个正整数列表(数据是无序的,并且允许有相等的整数存在),
# 编写能实现下列功能的函数，传入列表和正整数x，返回下面要求的三个数据
# def func(array, x)
#     '''逻辑代码'''
#     return count, li1, new_array
# 1、统计并返回在列表中,比正整数x大的数有几个(相同的数只计算一次)，并返回-----返回值中的的count
# 2、计算列表中比正整数X小的所有偶数，并返回  -----------返回值中的li
# 3、将列表中比正整数X小的偶数去掉,未去掉的数添加到新列表中，并返回-------返回值中的new_array

# def func(array, x):
#     count = len([i for i in array if i >= x])
#     # li = [i for i in arry if i < x and i % 2 == 0]
#     li = list(filter(lambda i: i < x and i % 2 == 0, array))
#     new_array = [array.remove(i) for i in li]
#     return count, li, new_array


# 4、定义一个函数实现以下功能，第一个元素是数据标识，第二个元素的数值必须大于等于50才返回，不够50往后累加加到最后如果不够50也直接返回，因为没有可加的数据了
#
# 例子1 ：
#
a = [[1, 3], [2, 51], [3, 49], [4, 42], [5, 42]]  # 入参

a1 = [[2, 54], [4, 91], [5, 42]]  # 返回


#
#
#
# 例子2：
#
#  b = [[1,50],[2,5],[3,10],[4,42],[5,42],[6,10]] #入参
#
#  b1 = [[1,50],[4,57],[6,52]] #返回
# def func1(array):
#     count = 0
#     list = []
#
#     for i in a:
#             count += i[1]
#             if count >= 50 or len(array) == i[0]:
#                 list.append([i[0], count])
#                 count = 0
#     return list
# print(func1(a))


names=["bbguo","bbliang","bbxi","bbwang","bbbo","bbya","bbyi","bbqing"]
print(names[1:5:2])