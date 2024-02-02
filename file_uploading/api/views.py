from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from file_uploading.tasks import upload_file

from .models import File
from .serializers import FileSerializer


class FileAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            file = serializer.save()
            upload_file.delay(file.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileUploadedAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = self.serializer_class(files, many=True)
        return Response({"files": serializer.data}, template_name="index.html")
