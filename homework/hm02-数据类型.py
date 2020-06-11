"""
=============================
@Time : 2020/5/7 21:54
@Author : AllyZhou
@FileDec: 数据类型扩展
==============================
"""
"""
1、通过列表推导式完成下面数据类型转换,现在有以下数据， li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]
需要转换为以下格式： li1 = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]"""

li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]
print([eval(i) for i in li1])

# 运行结果 [{'a': 11, 'b': 2}, [11, 22, 33, 44]]

"""2、使用列表推倒式生成一个[0, 5, 10, 15, 20,...50]的列表"""

print([i for i in range(51) if i % 5 == 0])

# 运行结果  [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

"""3、使用列表推到式生成一个[page1，page2, page3....page10]的列表 """

li = (["page{}".format(i) for i in range(1, 11)])


# 运行结果  ['page1', 'page2', 'page3', 'page4', 'page5', 'page6', 'page7', 'page8', 'page9', 'page10']


"""4、 Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest',
            'pymysql'], 请通过列表推导式，获取names中字符串长度大于4的元素,提示 ：列表推导式可以结合三目运算符一起使用"""

Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest',
         'pymysql']
print([i for i in Names if len(i) > 4])
# 运行结果 ['python', 'django', 'unittest', 'pytest', 'pymysql']

"""
5、通过列表推导式和字典推导式完成下面数据转换
# 原来数据
str = ""
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555""
# 转换后数据
list = [{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
        {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}]
"""
str = """
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
"""
#
# list_4 = [{j.split(':')[0].strip('\n'): j.split(':')[1].strip('\n') for j in i.split(',')} for i in str.split()]
# print(list_4)
for i in str.split():
    print(i)