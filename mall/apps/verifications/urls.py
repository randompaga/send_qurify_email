


from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'phones/(?P<mobile>1[3-9]\d{9})/count/$',views.RegisterPhoneCountAPIView.as_view(),name='phonecount'),
    url(r'imagecodes/(?P<image_code_id>.+)/$',views.RegisterImageCodeView.as_view(),name='imagecode'),
    url(r'smscodes/(?P<mobile>1[345789]\d{9})/$', views.RegisterSmsCodeView.as_view(), name='smscodes')

]


