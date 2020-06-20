from django.http import HttpResponse
from django.views import View
import json


def index_page(request):
    '''
    视图函数：
    1.第一个参数为HttpRequest对象或者HttpRequest子类的对象 无需手动传递
    2.一般会使用request
    3.一定要返回一个HttpRequest对象或者HttpRequest子类对象
    :param request:前端请求的所有参数封装的一个对象
    :return:
    '''
    return HttpResponse("<h2>hello world! 这是的第一个django作业 </h2>")


def index_page2(request):
    if request.method == "GET":

        return HttpResponse("<h2>GET hihihihihihihi</h2>")
    elif request.method == "POST":
        return HttpResponse("<h2>POST hihihihihihihi</h2>")


class IndexPage(View):
    """
    类视图
    1.一定要继承django中的View父类或者View的子类才可以成为类视图
    2.可以定义 get post put delete方法 来实现get post put delete请求
    3.get post put delete 方法名称固定且均为小写
    4.第一个参数self 类视图对象View的引用
      第二个参数为HttpRequest对象的

    """

    def get(self, request, pk):
        # 5.url后面的？号参数 成为query string查询字符串参数 ？参数名1=参数值1&参数名2=参数值2
        # 6.request.GET获取查询字符串参数
        # 7.request.GET返回QueryDict对象 类似于一个字典 支持字典中的所有操作
        # 8.request.GET[KEY],request.GET.get(key),request.GET.getlist（）去获取值 request.GET.getlist（）可以获取相同key的多个参数值合成一个list
        return HttpResponse("<h2>GET hihihihihihih我们的组个是就是激素就i</h2>")

    def post(self, request, pk):
        # 1. 可以使用request.POST方法获取application/x-www.urlencoded类型的参数
        # 2.可以使用request.body方法获取application/json类型的参数
        # 3. data_dict = json.loads(request.body, encoding='utf-8')
        # 4. return HttpResponse("<h2>POST:{}</h2>".format(data_dict["name"]))
        # 5. 可以使用request.META方法，获取请求头参数，key为HTTP_请求头key的大写 request.META["HTTP_AUTHORIZATION"]
        return HttpResponse("<h2>Post hihihihihihihi</h2>")

    def put(self, request, pk):
        # 1.HttpResponse对象 第一个参数为字符串或者字节类型 会将字符串内容返回到前端
        # 2.可以使用content_type来指定响应体的内容类型
        # 3.可以使用status参数来指定响应状态码
        one_dict = '{"name": "aa", "age": 18}'
        return HttpResponse(one_dict, content_type="application/json", status=201)
