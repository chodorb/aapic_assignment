import os
from django.conf import settings
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "appic.settings")

app = Celery('appic')

app.config_from_object(settings, namespace="CELERY")

app.autodiscover_tasks()