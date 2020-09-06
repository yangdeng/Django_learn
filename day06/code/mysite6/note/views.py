from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from user.models import User
from . import models

#装饰器
def chcke_login(fn):
    def wrap(request, *args, **kwargs):
        if not hasattr(request, 'session'):  # 如果没有session属性
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        return fn(request, *args, **kwargs)
    return wrap

def list_view(request):
    if not hasattr(request, 'session'):  # 如果没有session属性
        return HttpResponseRedirect('/user/login')
    if 'user' not in request.session:
        return HttpResponseRedirect('/user/login')
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    notes = auser.note_set.all()
    return render(request, 'note/showall.html', locals())

#装饰器
@chcke_login
def add_view(request):
    if request.method == 'GET':
        return render(request, 'note/add_note.html')
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        #得到当前用户信息
        user_id = request.session['user']['id']
        auser = User.objects.get(id=user_id)
        anote = models.Note(user=auser)
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note/')

@chcke_login
def mode_view(request,id):
    #得到当前登录用户的模型队形
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    anote = models.Note.objects.get(user=auser,id=id)
    if request.method == 'GET':
        return render(request, 'note/mod_note.html', locals())
    elif request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        anote.title = title
        anote.content = content
        anote.save()
        return HttpResponseRedirect('/note')


def del_view(request, id):
    user_id = request.session['user']['id']
    auser = User.objects.get(id=user_id)
    anote = models.Note.objects.get(user=auser, id=id)
    anote.delete()
    return HttpResponseRedirect('/note/')








