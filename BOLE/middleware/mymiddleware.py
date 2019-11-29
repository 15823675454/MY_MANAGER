import re
import redis
from django.http import *
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):
    visit_times = {}
    r = redis.Redis(host='127.0.0.1', port=6379, db=5)

    # 请求到达前,查看该ip是否恶意攻击
    def process_request(self, request):
        # 得到远程客户端ip地址
        ip_address = request.META['REMOTE_ADDR']
        if not re.match(r'/', request.path_info):
            return
        if self.r.exists(ip_address):
            times = int(self.r.get(ip_address).decode())+1
            # print(times, type(times))
            self.r.set(ip_address, times, ex=5)
        else:
            times = self.r.set(ip_address, 0, ex=5)
            # print(times, type(times))
        print('IP:', ip_address, '已经访问了', self.r.get(ip_address).decode(), '次!')

        if int(self.r.get(ip_address).decode()) < 5:
            return
        return HttpResponse('您访问得太过频繁，请您冷静一会儿再来！')

    def process_view(self, request, callback, callback_args, callback_kwargs):
        # 进入视图之前调用
        # 返回值同上
        print('MyMiddleware process_view do ---')

    def process_response(self, request, response):
        # 响应返回给浏览器之前调用
        print('MyMiddleware process_response do ---')
        return response


