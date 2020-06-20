from django.http import HttpResponse
from django.views import View


def index_page(request):
    '''
    视图函数：
    1.第一个参数为HttpRequest对象或者HttpRequest子类的对象 无需手动传递
    2.一般会使用request
    3.一定要返回一个HttpRequest对象或者HttpRequest子类对象
    :param request:
    :return:
    '''
    return HttpResponse("<h2>hello world! 这是诺诺周的第一个django作业 </h2>")


def index_page2(request):
    return HttpResponse("<h2>hihihihihihihi</h2>")


class IndexPage(View):
    """
    类视图

    """

    def get(self, request):
        return HttpResponse("<h2>hello world! 这是诺诺周的第一个django作业 </h2>")
