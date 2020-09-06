from django.shortcuts import render
from django.conf import settings
import os

# Create your views here.
def index_view(request):
    return render(request, 'index/index.html', locals())


from django.http import HttpResponse
def test_view(request):
    print('test_view被调用')
    return HttpResponse('请求到达了/test页面')


def upload_view(request):
    if request.method == 'GET':
        return render(request, 'index/upload.html')
    elif request.method == 'POST':
        a_file = request.FILES['myfile']
        print('收到上传的文件：',a_file.name)
        #计算文件保存的位置
        filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        #a_file.file.read()获取文件内容
        with open(filename, 'wb') as fw:
            try:
                fw.write(a_file.file.read())
                return HttpResponse('收到文件：'+ a_file.name)
            except Exception as error:
                return HttpResponse('文件上传失败',error)
