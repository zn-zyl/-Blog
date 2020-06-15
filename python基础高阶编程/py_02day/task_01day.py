"""
============================
Author:柠檬班-木森
Time:2020/5/8   17:41
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""

1、通过列表推导式完成下面数据类型转换

现在有以下数据， li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]

需要转换为以下格式： li1 = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]

2、使用列表推倒式生成一个[0, 5, 10, 15, 20,...50]的列表

3、使用列表推到式生成一个[page1，page2, page3....page10]的列表

4、 Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest',
            'pymysql'], 请通过列表推导式，获取names中字符串长度大于4的元素

提示 ：列表推导式可以结合三目运算符一起使用

5、通过列表推导式和字典推导式完成下面数据转换

"""
# 原来数据
str = '''
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
'''
# 转换后数据
lis = [{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
       {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
       {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
       {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
       {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}]

# 第一题：
li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]
list_one = [eval(i) for i in li1]

# 第二题
list_tow = [i for i in range(0, 51, 5)]

# 第三题:
list_three = ['page{}'.format(i) for i in range(1, 11)]

Names = ['python', 'java', 'php', 'c', 'c++', 'django', 'unittest', 'pytest', 'pymysql']
# 第四题：
list_four = [i for i in Names if len(i) > 4]

# 第五题：
string = '''
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
'''
list_five = [{i.split(':')[0]: i.split(':')[1] for i in itme.split(',')} for itme in string.split()]
print(list_one)
print(list_tow)
print(list_three)
print(list_four)
# print(list_five)
