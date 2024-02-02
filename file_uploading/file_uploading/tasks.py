from celery import shared_task

from api.models import File


@shared_task
def upload_file(file_id=None):
    if file_id is not None:
        file = File.objects.get(id=file_id)
        file.processed = True
        file.save()
        print(f"File {file_id} uploaded")
    else:
        files = File.objects.filter(processed=False)
        for file in files:
            file.processed = True
            file.save()
        print("All files uploaded")
