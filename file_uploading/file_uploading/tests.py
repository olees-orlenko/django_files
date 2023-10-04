from http import HTTPStatus

from django.test import Client, TestCase
from django.utils import timezone
from rest_framework.test import APITestCase

from api.models import File

from .tasks import upload_file


class FileUploadingTest(TestCase):
    def test_file_uploading(self):
        file = File.objects.create(file='files/filename.txt', processed=True)
        upload_file(file.id)
        file.refresh_from_db()
        self.assertTrue(file.processed)


class ApiPagesURLTests(APITestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_files_url_exists_at_desired_location(self):
        response = self.guest_client.get('/api/files/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_upload_url_get_requests(self):
        response_get = self.guest_client.get('/api/upload/')
        self.assertEqual(response_get.status_code,
                         HTTPStatus.METHOD_NOT_ALLOWED)


class FileViewTests(TestCase):
    def test_file_created(self):
        file = File.objects.create(uploaded_at=timezone.now(),
                                   processed=True)
        self.assertIsNotNone(file)


class FileModelTests(TestCase):
    def test_str(self):
        file = File.objects.create(file='test.txt',
                                   uploaded_at=timezone.now(),
                                   processed=True)
        self.assertEqual(str(file), '2023-10-04')

    def test_upload_to(self):
        file = File.objects.create(file='test.txt',
                                   uploaded_at=timezone.now(),
                                   processed=True)
        self.assertEqual(file.file.field.upload_to, 'files/')

    def test_processed(self):
        file = File.objects.create(file='test.txt',
                                   uploaded_at=timezone.now(),
                                   processed=False)
        self.assertFalse(file.processed)
