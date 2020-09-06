from django.shortcuts import render
from . import models
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def reg_view(request):
    if request.method == 'GET':
        return  render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        password2 = request.POST.get('password2','')
        #验证数据的合法性
        if len(username) < 6:
            username_error = '用户名太短!'
            return render(request, 'user/register.html', locals())

        if len(password1) == 0:
            password_error = '密码不能为空'
            return render(request, 'user/register.html', locals())
        if password1 != password2:
            password2_error = '两次密码不一致'
            return render(request, 'user/register.html', locals())

        try:
            auser = models.User.objects.get(username=username)
            username_error = '用户名已存在'
            return render(request, 'user/register.html', locals())
        except:
            auser = models.User.objects.create(
                username=username,
                password = password1
            )
            html = '注册成功<a href="user/login.html">进入登录</a>'
            resp =  HttpResponse(html)
            resp.set_cookie('username', username)
            return resp

def login_view(request):
    # #设置session的值
    # request.session['abc'] = 123
    # # val = request.session.get('abc', 'xxx')
    # # print('val=', val)
    # return HttpResponse('添加成功')
    if request.method == 'GET':
        username = request.COOKIES.get('username', '')
        return  render(request, 'user/login.html', locals())
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password', '')
        if username == '':
            username_error = '用户名不能为空'
            return render(request, 'user/login.html', locals())
        #处理登录逻辑
        try:
            auser = models.User.objects.get(username=username,
                                            password=password1)
            #登录成功,记录登录状态
            request.session['user'] = {
                'username':username,
                'id':auser.id
            }
            resp = HttpResponseRedirect('/')
            if 'remember' in request.POST:
                resp.set_cookie('username', username)
            return resp
            #return HttpResponse('登录成功')
        except:
            return HttpResponse('登录失败')


def logout_view(request):
    if 'user' in request.session:
        del request.session['user'] #清除记录
    return HttpResponseRedirect('/') #返回主页


































