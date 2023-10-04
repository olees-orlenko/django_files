from django.contrib import admin

from .models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'uploaded_at', 'processed')


admin.site.register(File, FileAdmin)
