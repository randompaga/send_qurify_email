from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



# Create your models here.
from mall import settings

# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
class User(AbstractUser):
    """用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    email_active = models.BooleanField(default=False, verbose_name='邮箱验证状态')


    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'

        verbose_name_plural = verbose_name


    # def generate_verify_email_url(self):
    #     from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
    #     serializer = Serializer(settings.SECRET_KEY,3600)
    #     token = serializer.dumps({'user_id': self.id, 'email': self.email})
    #     print(token)
    #     verify_url = 'http://www.meiduo.site:8080/success_verify_email.html?token=' + token.decode()
    #     return verify_url
    # #


