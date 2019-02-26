import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mall.settings")


app = Celery(main='celery_tasks')

app.config_from_object('celery_tasks.config')
app.autodiscover_tasks(['celery_tasks.sms','celery_tasks.email'])
