from random import randint

from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework import status



from rest_framework.response import Response

from apps.verifications.serializers import RegisterSmsCodeViewSerializer
from libs.captcha.captcha import captcha
from libs.yuntongxun.sms import CCP

# Create your views here.


from rest_framework.views import APIView

from users.models import User


class RegisterPhoneCountAPIView(APIView):
    """
    查询手机号的个数
    GET: /users/phones/(?P<mobile>1[345789]\d{9})/count/
    """
    def get(self,request,mobile):

        #通过模型查询获取手机号个数
        count = User.objects.filter(mobile=mobile).count()
        #组织数据
        context = {
            'count':count,
            'phone':mobile
        }

        return Response(context)



class RegisterImageCodeView(APIView):
    def get(self,request,image_code_id):
        text,image = captcha.generate_captcha()
        redis_conn = get_redis_connection('code')
        redis_conn.setex('img_%s'%image_code_id,600,text)
        print(image_code_id)
        return HttpResponse(image,content_type='image/jpeg')

from rest_framework.generics import GenericAPIView
class RegisterSmsCodeView(GenericAPIView):
    serializer_class = RegisterSmsCodeViewSerializer

    def get(self, request, mobile):
        query_params = request.query_params
        print(query_params)

        serializer = self.get_serializer(data=query_params)
        serializer.is_valid(raise_exception=True)
        redis_conn = get_redis_connection('code')
        if redis_conn.get('sms_flag_%s'%mobile):
            return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)
        sms_code = '%06d'%randint(0,999999)
        print(sms_code)
        redis_conn.setex('sms_%s' % mobile, 5 * 60, sms_code)
        redis_conn.setex('sms_flag_%s' % mobile, 60, 1)

        ccp = CCP()
        ccp.send_template_sms(mobile,[sms_code,5],1)
        return Response({'message':'ok'})





