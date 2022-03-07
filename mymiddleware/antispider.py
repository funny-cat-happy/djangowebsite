import time
from django.core.cache import cache
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class antispider(MiddlewareMixin):
    def process_request(self, request):
        user_ip = request.META.get('REMOTE_ADDR')
        request_time = cache.get(user_ip, [])
        if request_time is not None:
            for eve in request_time:
                if time.time() - eve > 60:
                    request_time.remove(eve)
        if len(request_time) > 50:
            return HttpResponse('您的访问过于频繁，请冷静冷静', status=403)
        request_time.insert(0, time.time())
        cache.set(user_ip, request_time, timeout=60)

    def process_exception(self, request, exception):
        return HttpResponse('啊，出现了错误，(✪ω✪)，如果你很善良，请将你的点击内容和操作方式上报给作者', status=500)
