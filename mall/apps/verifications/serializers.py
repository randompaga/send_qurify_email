import serializers as serializers
from django_redis import get_redis_connection
from redis import RedisError
from rest_framework import serializers

from utils.exception import logger


class RegisterSmsCodeViewSerializer(serializers.Serializer):
    text = serializers.CharField(label='用户输入的验证码', max_length=4, min_length=4, required=True)
    image_code_id = serializers.UUIDField(label='验证码唯一性id')



    def validate(self, attrs):
        text = attrs.get('text')
        redis_conn = get_redis_connection('code')
        image_code_id = attrs.get('image_code_id')

        redis_text = redis_conn.get('img_%s'%image_code_id)
        if redis_text is None:
            raise serializers.ValidationError('验证码已过期')
        try:
            redis_conn.delete('img_%s'%image_code_id)
        except RedisError as e:
            logger.error(e)

        if redis_text.decode().lower()!=text.lower():
            raise serializers.ValidationError('验证码错误')
        return attrs



