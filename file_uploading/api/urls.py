from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import FileAPIView, FileUploadedAPIView

app_name = 'api'

urlpatterns = [
    path('upload/', FileAPIView.as_view()),
    path('files/', FileUploadedAPIView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
