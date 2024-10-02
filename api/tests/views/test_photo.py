import json
from django.test.client import encode_multipart
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.test import TestCase
from models_app.factories.photo import PhotoFactory
from models_app.factories.user import UserFactory


class UploadPhotoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_create_photo_success(self):
        with open('./api/tests/img/default.jpg', 'rb') as image:
            photo_data = {
                'title': 'test title',
                'description': 'test description',
                'image': image
            }

            token = f'Token {self.token}'
            response = self.client.post('/api/upload-photo/',
                                        data=photo_data,
                                        HTTP_AUTHORIZATION=token,
                                        format='multipart')
        self.assertEqual(response.status_code, 201)

    def test_create_photo_without_auth(self):
        with open('./api/tests/img/default.jpg', 'rb') as image:
            photo_data = {
                'title': 'test title',
                'description': 'test description',
                'image': image
            }
            response = self.client.post('/api/upload-photo/',
                                        data=photo_data,
                                        format='multipart')
        self.assertEqual(response.status_code, 401)

    def test_create_photo_with_invalid_data(self):
        with open('./api/tests/img/default.jpg', 'rb') as image:
            photo_data = {
                'title': '',
                'description': 'test description',
                'image': image
            }
            token = f'Token {self.token}'
            response = self.client.post('/api/upload-photo/',
                                        data=photo_data,
                                        HTTP_AUTHORIZATION=token,
                                        format='multipart')
        self.assertEqual(response.status_code, 400)


class DeletePhotoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.client = APIClient()
        cls.photo = PhotoFactory(author=cls.author)
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_delete_photo_success(self):
        token = f'Token {self.token}'
        response = self.client.delete(f'/api/delete-photo/{self.photo.id}/',
                                      HTTP_AUTHORIZATION=token,
                                      format='json')
        self.assertEqual(response.status_code, 204)

    def test_delete_photo_without_auth(self):
        response = self.client.delete(f'/api/delete-photo/{self.photo.id}/',
                                      content_type='application/json')
        self.assertEqual(response.status_code, 401)


class UpdatePhotoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.photo = PhotoFactory(author=cls.author)
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_update_photo_success(self):
        with open('./api/tests/img/default.jpg', 'rb') as image:
            photo_data = {
                'title': 'test title',
                'description': 'test description',
                'image': image
            }
            token = f'Token {self.token}'
            content = encode_multipart('BoUnDaRyStRiNg', photo_data)
            response = self.client.put(
                f'/api/update-photo/{self.photo.id}/',
                data=content,
                HTTP_AUTHORIZATION=token,
                content_type='multipart/form-data; boundary=BoUnDaRyStRiNg'
            )
        self.assertEqual(response.status_code, 200)

    def test_update_photo_without_auth(self):
        with open('./api/tests/img/default.jpg', 'rb') as image:
            photo_data = {
                'title': 'test title',
                'description': 'test description',
                'image': image
            }
            response = self.client.put(
                f'/api/update-photo/{self.photo.id}/',
                data=photo_data,
                content_type='multipart/form-data; boundary=BoUnDaRyStRiNg')
        self.assertEqual(response.status_code, 401)

    def test_update_photo_with_invalid_data(self):
        with open('./api/tests/img/default.jpg', 'rb') as image:
            photo_data = {
                'title': '',
                'description': 'test description',
                'image': image
            }
            token = f'Token {self.token}'
            response = self.client.put(
                f'/api/update-photo/{self.photo.id}/',
                data=photo_data,
                HTTP_AUTHORIZATION=token,
                content_type='multipart/form-data; boundary=BoUnDaRyStRiNg')
        self.assertEqual(response.status_code, 400)


class ListPhotoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.photos = PhotoFactory.create_batch(12,
                                               author=cls.author,
                                               status="public")
        cls.client = APIClient()

    def test_list_photos_success(self):
        response = self.client.get('/api/photos/', {'sort': 'publicated_at'})
        self.assertEqual(response.status_code, 200)

    def test_pagination_is_two(self):
        photo_data = {'current_page': 2,
                      'per_page': 2,
                      'sort': 'publicated_at'}
        response = self.client.get('/api/photos/', photo_data)
        self.assertEqual(response.status_code, 200)
        resp_json = json.loads(response.content)
        self.assertTrue('pagination' in resp_json)
        self.assertTrue('photos' in resp_json)
        self.assertTrue(resp_json['pagination']['current_page'] == 2)
        self.assertTrue(resp_json['pagination']['per_page'] == 2)
        self.assertTrue(resp_json['pagination']['prev_page'] == 1)
        self.assertTrue(resp_json['pagination']['next_page'] == 3)
        self.assertTrue(resp_json['pagination']['total_pages'] == 6)
        self.assertTrue(resp_json['pagination']['total_count'] == 12)
        self.assertTrue(len(resp_json['photos']) == 2)


class AuthorListPhotoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.photos = PhotoFactory.create_batch(15, author=cls.author)
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_author_list_photos_success(self):
        token = f'Token {self.token}'
        response = self.client.get('/api/users-photos/',
                                   {'status': 'public'},
                                   HTTP_AUTHORIZATION=token,)
        self.assertEqual(response.status_code, 200)


class RetrievePhotoViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.photo = PhotoFactory(author=cls.author)
        cls.client = APIClient()

    def test_retrieve_author_success(self):
        response = self.client.get(f'/api/photo/{self.photo.id}/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_non_existing_comment(self):
        response = self.client.get('/api/photo/999/')
        self.assertEqual(response.status_code, 404)
