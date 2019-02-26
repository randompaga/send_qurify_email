

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url(r'usernames/(?P<username>\w{5,20})/count/$',views.RegisterUserAPIView.as_view(),name='usernamecount'),
    url(r'^$', views.RegisterUserAPIView.as_view()),
    url(r'auths/', obtain_jwt_token, name='auths'),
    url(r'^infos/$', views.UserCenterInfoAPIView.as_view(), name='detail'),
    url(r'^emails/$', views.UserEmailAPIView.as_view(), name='send_mail'),
    # url(r'^emails/verification/$', views.UserEmailVerificationAPIView.as_view()),

]

