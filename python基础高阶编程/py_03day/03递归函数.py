"""
============================
Author:柠檬班-木森
Time:2020/5/11   21:12
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
递归函数：就是在函数内部调用自身函数


使用递归的时候注意点：一定要设置递归的临界点（终止递归的条件）


"""
import sys


# 错误示范：
# def func(x):
#     print(x)
#     func(x - 1)

# 获取最大递归深度
# res = sys.getrecursionlimit()
# print(res)

# 设置最大递归深度
# sys.setrecursionlimit(400000)
# func(10)


# --------设置递归的终止条件----------------
# def func(x):
# #     if x == 0:
# #         return '执行结束'
# #     print(x)
# #     func(x - 1)
# # func(10)


# -------计算任意数的阶乘----------------------
# 6的阶乘  1*2*3*4*5*6


def mu(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1 * 2
    elif n == 3:
        return 1 * 2 * 3
    elif n == 4:
        return 1 * 2 * 3 * 4
    elif n == 5:
        return 1 * 2 * 3 * 4 * 5
    elif n == 6:
        return 1 * 2 * 3 * 4 * 5 * 6


# def mut(n):
#     if n == 1:
#         return 1
#     else:
#         return mut(n - 1) * n
#
# res = mut(6)
#
# print(res)

"""
通过递归实现斐波拉契数列
# 第一个数是1，后面的每一个数，等于它前两个数相加之和
[1,1,2,3,5,8,13,21,34,55,89] 


"""


#
# def fix(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n == 3:
#         return fix(n-1) + fix(n-2)
#     elif n == 4:
#         return fix(n-1) + fix(n-2)
#     elif n == 5:
#         return fix(n-1) + fix(n-2)

# def fix(n):
#     if n < 1:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fix(n - 1) + fix(n - 2)

# print(fix(1))
