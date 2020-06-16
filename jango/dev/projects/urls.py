"""
=============================
@Time : 2020/6/16 20:23
@Author : AllyZhou
@FileDec: 
==============================
"""
from django.urls import path

# 导入视图函数

from projects.views import index_page, index_page2

# 1.urlpatterns为名称固定的列表 用于存放路由信息
# 2.列表中的元素个数就是路由条数
# 3.路由匹配规则：a 从列表的第一个元素开始（从上到下）开始匹配
#               b 一但调用成功 会自动调用path第二个函数所指定的视图函数
#               c 一但匹配成功，不会再往下匹配
#               d 如果匹配不成功，会返回一个状态码为404的页面
#               e url路由信息推荐使用/结尾


urlpatterns = [
    path('index/', index_page),
    path('index/2/', index_page2)
]
