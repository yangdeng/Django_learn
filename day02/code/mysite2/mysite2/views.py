
from django.http import HttpResponse
from django.template import loader

def sum_view(request):
    if request.method == 'GET':
        start = request.GET.get('start','0')
        start = int(start)
        stop = request.GET.get('stop', '0')
        stop = int(stop)
        step = request.GET.get('step', '1')
        step = int(step)
        mysum = sum(range(start,stop,step))
        html = "和是：%d" % mysum
        return HttpResponse(html)

login_form_html="""
<form action="/login" method="POST">
        用户名：<input type="text" name="username">
        密码：<input type="text" name="pass">
        <input type="submit" value="登录">
    </form>
"""

def login_view(request):
    if request.method == "GET":
        return HttpResponse(login_form_html)
    elif request.method == 'POST':
        name = request.POST.get('username','属性错误')
        s = str(dict(request.POST))
        html = s
        #html ='姓名：'+ name
        return HttpResponse(html)


def login2_view(request):
    if request.method == 'GET':
        # t = loader.get_template('mylogin.html')
        # html = t.render({'name':'tarena'})
        # return HttpResponse(html)
        from django.shortcuts import render
        return render(request, 'mylogin.html', {'name':'王八'})

from django.shortcuts import render

def say_hello():
    return 'nihao'

class Dog:
    def say(self):
        return 'wangwang'

def test_view(requset):
    s = 'hello tarena'
    lst = ['北京','上海','武汉']
    mydic = {'name':'tedu','age':20}
    dic = {'s':s,'lst':lst, 'mydic':mydic, 'say_hello':say_hello,'dog1':Dog}
    return render(requset, 'test.html', dic)

def mytemp_view(request):
    # dic = {
    #     'x':10
    # }
    x = -5
    return render(request,'mytemp.html', locals())


def mycal_view(request):
    if request.method == 'GET':
        return render(request,'sum.html')
    elif request.method == 'POST':
        x = int(request.POST.get('x', '0'))
        y = int(request.POST.get('y','0'))
        op = request.POST.get('op')
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y
    return render(request, 'sum.html', locals())

def for_view(request):
    lst = ['北京','上海','武汉']
    s = '<b>Hello World</b>'
    n = 100
    s2 = 'aa db ds cf ed af sf'
    return render(request, 'for.html', locals())

def index_view(request):
    return render(request, 'base.html')

def sport_view(request):
    return render(request, 'sport.html')

def news_view(request):
    pass
















