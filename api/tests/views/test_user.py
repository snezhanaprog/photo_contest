from rest_framework.test import APIClient
from django.test import TestCase
from models_app.factories.user import UserFactory, ProfileFactory
from rest_framework.authtoken.models import Token


class UserProfileViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(username='user')
        cls.profile = ProfileFactory(user=cls.user)
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.user)

    def test_get_user_profile_success(self):
        token = f'Token {self.token}'
        response = self.client.get('/api/user-info/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user']['id'], self.user.id)

    def test_get_user_profile_without_auth(self):
        response = self.client.get('/api/user-info/')
        self.assertEqual(response.status_code, 401)


class UploadAvatarViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(username='admin')
        cls.profile = ProfileFactory(user=cls.user)
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.user)

    def test_upload_avatar_success(self):
        token = f'Token {self.token}'
        with open('./api/tests/img/default.jpg', 'rb') as avatar:
            response = self.client.post('/api/upload-avatar/',
                                        {'avatar': avatar},
                                        HTTP_AUTHORIZATION=token,
                                        format='multipart')
            self.assertEqual(response.status_code, 201)

    def test_upload_avatar_without_auth(self):
        with open('./api/tests/img/default.jpg', 'rb') as avatar:
            response = self.client.post('/api/upload-avatar/',
                                        {'avatar': avatar},
                                        format='multipart/form-data')
        self.assertEqual(response.status_code, 401)


class RegisterViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_register_user_success(self):
        user_data = {
            'username': 'new_user',
            'password': 'password123',
            'email': 'new_user@example.com'
        }
        response = self.client.post('/api/register/', data=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('auth_token', response.data)

    def test_register_user_with_invalid_data(self):
        user_data = {
            'username': '',
            'password': 'password123',
            'email': 'test@example.com'
        }
        response = self.client.post('/api/register/', data=user_data)
        self.assertEqual(response.status_code, 400)
