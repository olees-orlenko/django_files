import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "file_uploading.settings")

app = Celery("file_uploading")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
app.conf.beat_schedule = {
    "upload-files": {
        "task": "file_uploading.tasks.upload_file",
        "schedule": crontab(minute="*/1"),
    },
}
app.conf.timezone = "UTC"
