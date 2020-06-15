"""
============================
Author:柠檬班-木森
Time:2020/5/6   21:46
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
三目运算：

推导式

"""

number = 100

# if number > 60:
#     print("大于")
# else:
#     print('小于')

# 三目运算
# res = True if number > 60 else False


# 需求，生成 [py1，，，，，py20]


# li = []
# for i in range(1,21):
#     li.append('py{}'.format(i))
# print(li)


# 列表推导式
# li = ['py{}'.format(i) for i in range(1,21)]
# print(li)

# 集合推导式
se = {'py{}'.format(i) for i in range(1,21)}
print(se)
print(type(se))


# 字典推导式
dic = {'name{}'.format(i): i * 100 for i in range(1, 21)}
print(dic)
# cook_str = 'BIDUPSID=D0727533D7147B7;PSTM=1530348042;BAIDUID=B1005C9BC2EB28;sugstore=0;__cfduid=d0a13458f8ac2a;BD_UPN=12314353;ispeed_lsm=2;BDORZ=B490B5EBF6F3CD402'

# res = cook_str.split(';')
# print(res)

# dic = {i.split('=')[0]: i.split('=')[1] for i in cook_str.split(';')}
# print(dic)

# 生成器表达式


