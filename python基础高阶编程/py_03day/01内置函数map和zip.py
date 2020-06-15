"""
============================
Author:柠檬班-木森
Time:2020/5/11   20:19
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
# li0 = [1, 2, 3, 4]
# li = [11, 22, 33, 44]
# li2 = [111, 222, 333, 444, 555, 666]
#
# # 一个参数
# res = zip(li)
# print(next(res))
# print(next(res))
# print(list(res))
#
#
# # 两个参数
# res2 = zip(li, li2)
# #注意点：迭代器对象中的数据，迭代完就没有了
# print(list(res2))
# print(list(res2))
#
#
# # 三个参数
# res2 = zip(li0,li, li2)
# print(list(res2))
#
#
# # zip：聚合打包
#
#
# title = ['case_id', 'case_title', 'url', 'data', 'expected']
# data = [1, '用例1', 'www.baudi.com', '001', 'ok']
#
# res = zip(title,data)
# print(list(res))
#
# dic = dict(zip(title,data))
# print(dic)
#
#
# cases = [
#     ['case_id', 'case_title', 'url', 'data', 'excepted'],
#     [1, '用例1', 'www.baudi.com', '001', 'ok'],
#     [4, '用例4', 'www.baudi.com', '002', 'ok'],
#     [2, '用例2', 'www.baudi.com', '002', 'ok'],
#     [3, '用例3', 'www.baudi.com', '002', 'ok'],
#     [5, '用例5', 'www.baudi.com', '002', 'ok'],
# ]
#
# title = cases[0]
#
# li = []
# for i in cases[1:]:
#     li.append(dict(zip(title, i)))
#
# print(li)

# res = [dict(zip(cases[0], i)) for i in cases[1:]]
#
# res2 = filter(lambda i: i['case_id'] > 3, res)
#
# print(res)
# print(list(res2))


# --------------------------------map----------------------------------------
# map: 自动将可迭代对象遍历，把遍历出来的数据，当成参数传入map第一个接口的函数中，将函数执行的结果，放到一个迭代器中进行返回
# res = map(lambda x: x * 2, [1, 2, 3, 4, 5])
# print(list(res))
res2 = map(lambda x, y, z: {'sum': x + y}, [1, 2, 3, 4, 5], [11, 22, 33, 44, 55], [111, 222, 333])

print(list(res2))

cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

# res = map(lambda x: dict(zip(cases[0], x)), cases[1:])
# print(list(res))

# def func(a, b, c):
#     return 100
