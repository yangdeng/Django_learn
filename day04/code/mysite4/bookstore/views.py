from django.shortcuts import render

from django.http import HttpResponse
from . import models
from django.http import HttpResponseRedirect
# Create your views here.

def add_view(request):
    if request.method == 'GET':
        return  render(request, 'bookstore/add_book.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        pub = request.POST.get('pub')
        price = float(request.POST.get('price','0'))
        m_price = float(request.POST.get('m_price','0'))
        try:
            models.Book.objects.create(
                title=title,
                pub=pub,
                price=price,
                maket_price=m_price
            )
            return HttpResponse("添加成功")
        except Exception as err:
            return  HttpResponse('添加失败')


def show_all(request):
    books = models.Book.objects.all()
    for book in books:
        print('书名：', book.title)
    return HttpResponse('查询成功')


def mod_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        return HttpResponse('没有此ID')

    if request.method=='GET':
        return render(request,'bookstore/mod.html', locals())
    elif request.method == 'POST':
        m_price = float(request.POST.get('m_price','0'))
        abook.maket_price = m_price
        abook.save()
        return HttpResponseRedirect('bookstore/all')

def del_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except Exception as err:
        return HttpResponse('del fail')
    abook.delete()
    return HttpResponseRedirect('/bookstore/all')
