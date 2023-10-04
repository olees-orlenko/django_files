from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField()

    def __str__(self):
        return str(self.uploaded_at.date())
