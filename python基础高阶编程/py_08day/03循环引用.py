"""
============================
Author:柠檬班-木森
Time:2020/5/22   21:33
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""



"""

a = [11, 22]
b = [1, 2]
a.append(b)
b.append(a)

print(a)
print(b)
del a
del b

# a = ['aa', 'bb']
# b = ['a', 'b']
# a.append(b[0])
# b.append(a[0])
#
# print(a)
# print(b)
import gc

print(gc.get_threshold())

"""
问题一：b=Base()这个实例化后，什么都没有做，对象是不是也要被回收清理掉？这个属于第三种：离开了作用域。
问题二：单独的py文件运行完了的话，那这个就不是python的垃圾回收机智了？是操作系统的进程自己回收掉了？

"""


class Base:
    pass


a = Base()


def func():
    b = Base()


func()
