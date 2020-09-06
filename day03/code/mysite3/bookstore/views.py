from django.shortcuts import render

from django.http import HttpResponse
from . import models
# Create your views here.

def add_view(request):
    try:
        # abook = models.book.objects.create(
        #     title='C++',price=68)
        abook = models.book(price=98)
        abook.title='西游记'
        abook.save()#执行sql语句
        return HttpResponse("添加成功")
    except Exception as err:
        return HttpResponse('添加失败')






