"""
============================
Author:柠檬班-木森
Time:2020/5/11   14:29
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""


# 第一题
def work1():
    li = [11, 21, 4, 55, 6, 67, 123, 54, 66, 9, 90, 56, 34, 22]
    li1 = filter(lambda x: x > 5, li)
    return [i % 2 for i in li1]


# 第二题
def work2():
    name = yield
    for i in range(5):
        if not isinstance(name, str):
            name = '127.0.0.1:8000'
        name = yield "http://" + name + "/user/login"


# gen = work2()
# next(gen)
# res = gen.send('www.baidu.com')
# print(res)
# res = gen.send('www.qq.com')
# print(res)
"""
# 有一个正整数列表(数据是无序的,并且允许有相等的整数存在),
# 编写能实现下列功能的函数，传入列表和正整数x，返回下面要求的三个数据
# def func(array, x)
#     '''逻辑代码'''
#     return count, li, new_array
# 1、统计并返回在列表中,比正整数x大的数有几个(相同的数只计算一次)，并返回-----返回值中的的count
# 2、计算列表中比正整数X小的所有偶数，并返回  -----------返回值中的li
# 3、将列表中比正整数X小的偶数去掉,未去掉的数添加到新列表中，并返回-------返回值中的new_array
"""


def work3_1(array, x):
    """用推导式"""
    # 比x大的个数
    res1 = len({i for i in array if i > x})
    # 正整数X小的所有偶数:放在li1中
    li1 = list(filter(lambda i: i < x and i % 2 == 0, array))
    # 去除比X小的偶数
    [array.remove(i) for i in li1]
    new_list = array.copy()
    return res1, li1, new_list


"""
4、定义一个函数实现以下功能，第一个元素是数据标识，第二个元素的数值必须大于等于50才返回，
不够50往后累加加到最后如果不够50也直接返回，因为没有可加的数据了
例子1 ：
a = [[1,3],[2,51],[3,49],[4,42],[5,42]] #入参 
a1 = [[2,54],[4,91],[5,42]] #返回 
例子2：
b = [[1,50],[2,5],[3,10],[4,42],[5,42],[6,10]] #入参
b1 = [[1,50],[4,57],[6,52]] #返回
"""


# 第四题：
def work4(array):
    li = []
    sum = 0
    for i in array:
        sum += i[1]
        # 第一种元素值大于等50
        if sum >= 50 or len(array) == i[0]:
            i[1] = sum
            li.append(i)
            sum = 0
    return li


a = [[1, 3], [2, 51], [3, 49], [4, 42], [5, 42]]
b = [[1, 50], [2, 5], [3, 10], [4, 42], [5, 42], [6, 10]]

print(work4(b))
