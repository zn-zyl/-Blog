"""
=============================
@Time : 2020/6/20 21:14
@Author : AllyZhou
@FileDec: 
==============================
"""
"""
1.简单描述两种开发模式的区别

1.前后端不分离 
后端控制数据的展示 前后端不分家 耦合严重
返回的是html页面 实用性 拓展性差
只能用于浏览器 其他终端不适配

2.前后端分离
当前主流 后端只对数据进行处理 只提供数据
后端只对数据进行处理 只提供数据
前端效率 页面好不好看 全由前端负责 前后端完全独立
解耦合
前后端同时开始开发 缩写业务上线周期
绝大多数情况下前端发送json格式的参数，后端同样以json格式的数据返回
适应性拓展性好
是和多终端运行同一套接口（pc app 小程序等）
"""


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
见附件
"""
"""
二、选做题
1.创建一个返回json格式数据的接口
见附件
"""