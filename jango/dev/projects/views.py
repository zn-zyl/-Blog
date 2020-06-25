from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from django.shortcuts import render


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

    def get(self, request):
        # 5.url后面的？号参数 成为query string查询字符串参数 ？参数名1=参数值1&参数名2=参数值2
        # 6.request.GET获取查询字符串参数
        # 7.request.GET返回QueryDict对象 类似于一个字典 支持字典中的所有操作
        # 8.request.GET[KEY],request.GET.get(key),request.GET.getlist（）去获取值 request.GET.getlist（）可以获取相同key的多个参数值合成一个list
        # return HttpResponse("<h2>Post hihihihihihihi</h2>")

        # 假设data数据是从数据库从读取的
        data = [
            {
                "project_name": "前程贷项目11",
                "leader": "可优",
                "app_name": "P2P平台应用"
            },
            {
                "project_name": "探索火星项目22",
                "leader": "优优",
                "app_name": "吊炸天应用"
            },
            {
                "project_name": "无比牛逼的项目33",
                "leader": "可可",
                "app_name": "神秘应用"
            },
        ]
        # a. render函数主要用于渲染模板生成一个html页面
        # b. 第一个参数为request
        # c. 第二个参数为在templates目录下的文件名
        # d. local()函数能获取当前命名空间中的所有变量信息 然后存放在一个字典中 给index.html模板使用
        # return render(request, "index.html")  # 无参数只返回动态页面情况
        # return render(request, "index.html", locals())
        # e.JsonResponse是HttpResponse的子类
        # 第一个参数为字典或者嵌套字典的列表，如果为非字典类型，需要将safe设置为False
        # 会返回一个json的字符串
        return JsonResponse(data, safe=False)

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
