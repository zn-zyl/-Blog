"""
============================
Author:柠檬班-木森
Time:2020/5/15   21:02
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
优化方案
"""
from functools import lru_cache


@lru_cache(maxsize=128)
def func(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        res = func(n - 1) + func(n - 2)
        return res

#
# res = func(500)
#
# print(res)
