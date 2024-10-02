from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.test import TestCase
from models_app.factories.voice import VoiceFactory
from models_app.factories.photo import PhotoFactory
from models_app.factories.user import UserFactory


class CreateVoiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.associated_photo = PhotoFactory()
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_create_voice_success(self):
        voice_data = {'photo_id': self.associated_photo.id}
        token = f'Token {self.token}'
        response = self.client.post('/api/create-voice/',
                                    data=voice_data,
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)

    def test_create_voice_without_auth(self):
        voice_data = {'photo_id': self.associated_photo.id}
        response = self.client.post('/api/create-voice/',
                                    data=voice_data)
        self.assertEqual(response.status_code, 401)

    def test_create_voice_with_invalid_data(self):
        voice_data = {'photo_id': ""}
        token = f'Token {self.token}'
        response = self.client.post('/api/create-voice/',
                                    data=voice_data,
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 400)


class DeleteVoiceViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.associated_photo = PhotoFactory()
        cls.voice = VoiceFactory(author=cls.author,
                                 associated_photo=cls.associated_photo)
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_delete_voice_success(self):
        voice_data = {'photo_id': self.associated_photo.id}
        token = f'Token {self.token}'
        response = self.client.post('/api/delete-voice/',
                                    data=voice_data,
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 204)

    def test_delete_voice_without_auth(self):
        voice_data = {'photo_id': self.associated_photo.id}
        response = self.client.post('/api/delete-voice/',
                                    data=voice_data)
        self.assertEqual(response.status_code, 401)

    def test_delete_voice_with_invalid_data(self):
        voice_data = {'photo_id': ""}
        token = f'Token {self.token}'
        response = self.client.post('/api/delete-voice/',
                                    data=voice_data,
                                    content_type='application/json',
                                    HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 400)
