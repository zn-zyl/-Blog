from django.http import HttpResponse


def index_page(request):
    return HttpResponse("<h2>hello world! 这是诺诺周的第一个django作业 </h2>")


def index_page2(request):
    return HttpResponse("<h2>hihihihihihihi</h2>")
