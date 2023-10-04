from celery import shared_task

from api.models import File


@shared_task
def upload_file(file_id):
    file = File.objects.get(id=file_id)
    file.processed = True
    file.save()
    print('File uploaded')
