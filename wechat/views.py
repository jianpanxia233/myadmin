from django.shortcuts import render
import hashlib
import json
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def handle(request):
    if request.method == "GET":
        # ����΢�ŷ�����get���󷢹����Ĳ���
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)
        # �����������е�token
        token = 'qwertyu'
        # �Ѳ����ŵ�list�������ϳ�һ���ַ���������sha1���ܵõ��µ��ַ�����΢�ŷ�����signature�Աȣ������ͬ�ͷ���echostr����������У��ͨ��
        hashlist = [token, timestamp, nonce]
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        hashstr = hashlib.sha1(hashstr.encode()).hexdigest()
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:
        othercontent = autoreply(request)
        return HttpResponse(othercontent)
