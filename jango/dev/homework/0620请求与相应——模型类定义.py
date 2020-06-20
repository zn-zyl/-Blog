"""
=============================
@Time : 2020/6/20 21:14
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
1.简单描述两种开发模式的区别
"""
# MVC设计模式
# M全拼为Model，主要封装对数据库层的访问，对数据库中的数据进行增、删、改、查操作。

# V全拼为View，用于封装结果，生成页面展示的html内容。

# C全拼为Controller，用于接收请求，处理业务逻辑，与Model和View交互，返回结果。

# MVT设计模式
# M全拼为Model，与MVC中的M功能相同，负责和数据库交互，进行数据处理。

# V全拼为View，与MVC中的C功能相同，接收请求，进行业务处理，返回应答。

# T全拼为Template，与MVC中的V功能相同，负责封装构造要返回的html。

"""
2.Django中前端向后端传参的方式有哪些? 后端如何接收?
"""
""" 
a.request.GET  
获取querystring 查询字符串参数,返回QueryDict对象，类似一个字典，request.GET[key] request.GET.get(key) request.GET.getlist()当key值重复时返回value值组成的一个list

b.request.POST
获取application/x-www.urlencoded类型的参数  request.POST[key] request.POST.get(key) request.POST.getlist()

c.request.body  
获取application/json类型的参数,json参数需要转化为字典  data_dict = json.loads(request.body, encoding='utf-8')
通过data_dict["key"]来取值

d.request.META
获取请求头参数，key为HTTP_请求头key的大写 request.META["HTTP_AUTHORIZATION"]
"""
"""
3.定义Projects模型类

"""
"""
二、选做题
1.创建一个返回json格式数据的接口
"""