
from django.http import HttpResponse


index_html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <a href="/mypage?a=888&b=999">进入mypage</a>
    <form action="/mypage" method="get">
        <input type="text" name="a">
        <input type="text" name="b">
        <input type="submit" value="提交">
    </form>
</body>
</html>
"""


def page1_view(request):
    html = "<h1>这是一个web页面</h1>"
    return  HttpResponse(html)

def page2_view(request):
    html = "<p>段落<p>"
    return  HttpResponse(html)

def index_view(request):
    #html = "<p>主页<p>"
    return  HttpResponse(index_html)

def pagen_view(request,n):
    html = "<h1>这是一个%s页面</h1>" % n
    return HttpResponse(html)

def math_view(request,x,op,y):
    x = int(x)
    y = int(y)
    result = None
    if op == 'add':
        result  = x + y
    elif op == 'sub':
        result = x - y
    elif op == 'mul':
        result = x * y
    if result is None:
        return  HttpResponse('出错')
    return HttpResponse("结果:" + str(result))

def person_view(request,name=None,age=None):
    s = '姓名：'+ name
    s += "年龄："+ age
    return HttpResponse(s)

# def person_view(request, **kwargs):
#     s = str(kwargs)
#     return HttpResponse(s)

def birthday_view(request,y,m,d):
    html = "<h1>生日："+ y + '/' + m + '/' + d + '</h1>'
    return HttpResponse(html)

def mypage_view(request):
    if request.method == 'GET':
        a = request.GET.get('a', '没有对应的值')
        html = "a=" + a
        return HttpResponse(html)
    else:
        return  HttpResponse("不是ＧＥＴ请求")
