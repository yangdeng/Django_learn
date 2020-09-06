
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class MyMW(MiddlewareMixin):
    def process_request(self,request):
        print('中间件process_request调用')
        print('路由是：',request.path)
        print('请求方法是：',request.method)
        if request.path == '/aaaa':
            return  HttpResponse('当前路由是/aaaa')

    # def process_view(self,request, callback):
    #     pass

from django.http import HttpResponse
from django.http import Http404

class VisitLimit(MiddlewareMixin):
    visit_time = {} #此字典的键为ＩＰ地址，值为访问次数
    def process_request(self,request):
        ip = request.META['REMOTE_ADDR'] #得到客户端ＩＰ
        if request.path_info != '/test':
            return None
        times = self.visit_time.get(ip, 0) #获取以前的访问次数
        print('IP', ip, '已访问过/test',times,'次')
        self.visit_time[ip] = times + 1
        if times < 5:
            return  None
        return HttpResponse('您已经访问过:%s次'% str(times))


