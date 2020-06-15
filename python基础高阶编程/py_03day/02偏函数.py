"""
============================
Author:柠檬班-木森
Time:2020/5/11   20:48
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
偏函数：可以用来固定函数中的函数



"""

from functools import partial

# 要获取数据中大于5的数据
li1 = [1, 2, 3, 11, 22, 33]
li2 = [2, 3, 4, 22, 33]
li3 = [3, 4, 5, 33, 44, 55]
#
# res1 = filter(lambda x: x > 5, li1)
# res2 = filter(lambda x: x > 5, li2)
# res3 = filter(lambda x: x > 5, li3)
# #
# print(list(res1))
# print(list(res2))
# print(list(res3))

filter2 = partial(filter,lambda x:x>5)
print(list(filter2(li1)))
print(list(filter2(li2)))
print(list(filter2(li3)))

import requests

# res1 = requests.get(url='http://httpbin.org/get', params={'kw': 123}, header={"asss": 1212})
# res2 = requests.get(url='http://httpbin.org/get', params={'kw': 124}, header={"asss": 1212})
# res3 = requests.get(url='http://httpbin.org/get', params={'kw': 125}, header={"asss": 1212})
# res4 = requests.get(url='http://httpbin.org/get', params={'kw': 126}, header={"asss": 1212})
#
# get = partial(requests.get, url='http://www.baidu.com', header={"asss": 1212})
#
# res1 = get(params={'kw': 123})
# res2 = get(params={'kw': 124})
# res3 = get(params={'kw': 124})
