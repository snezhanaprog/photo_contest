from django.test.client import encode_multipart
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.test import TestCase
from models_app.factories.comment import CommentFactory
from models_app.factories.photo import PhotoFactory
from models_app.factories.user import UserFactory


class CreateCommentViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.comment = CommentFactory(author=cls.author)
        cls.associated_photo = PhotoFactory()
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_create_comment_success(self):
        comment_data = {
            'content': 'test comment.',
            'photo_id': self.associated_photo.id
        }

        token = f'Token {self.token}'
        response = self.client.post('/api/create-comment/',
                                    data=comment_data,
                                    HTTP_AUTHORIZATION=token,
                                    format='multipart/form-data')
        self.assertEqual(response.status_code, 201)

    def test_create_comment_without_auth(self):
        comment_data = {
            'content': 'test comment',
            'photo_id': self.associated_photo.id,
        }
        response = self.client.post('/api/create-comment/',
                                    data=comment_data,
                                    format='multipart/form-data')
        self.assertEqual(response.status_code, 401)

    def test_create_comment_with_invalid_data(self):
        comment_data = {
            'content': '',
            'photo_id': self.associated_photo.id,
        }
        token = f'Token {self.token}'
        response = self.client.post('/api/create-comment/',
                                    data=comment_data,
                                    HTTP_AUTHORIZATION=token,
                                    format='multipart/form-data')
        self.assertEqual(response.status_code, 400)


class DeleteCommentViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.comment = CommentFactory(author=cls.author)
        cls.associated_photo = PhotoFactory()
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_delete_comment_success(self):
        token = f'Token {self.token}'
        response = self.client.delete(
            f'/api/delete-comment/{self.comment.id}/',
            HTTP_AUTHORIZATION=token,
            format='json')
        self.assertEqual(response.status_code, 204)

    def test_delete_comment_without_auth(self):
        response = self.client.delete(
            f'/api/delete-comment/{self.comment.id}/',
            content_type='application/json')
        self.assertEqual(response.status_code, 401)


class UpdateCommentViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.comment = CommentFactory(author=cls.author)
        cls.associated_photo = PhotoFactory()
        cls.client = APIClient()
        cls.token, _ = Token.objects.get_or_create(user=cls.author)

    def test_update_comment_success(self):
        comment_data = {
            'content': 'test comment'
        }
        token = f'Token {self.token}'
        content = encode_multipart('BoUnDaRyStRiNg', comment_data)
        response = self.client.put(
            f'/api/update-comment/{self.comment.id}/',
            data=content,
            HTTP_AUTHORIZATION=token,
            content_type='multipart/form-data; boundary=BoUnDaRyStRiNg'
        )
        self.assertEqual(response.status_code, 200)

    def test_update_comment_without_auth(self):
        comment_data = {
            'content': 'test comment',
        }
        response = self.client.put(
            f'/api/update-comment/{self.comment.id}/',
            data=comment_data,
            content_type='application/json')
        self.assertEqual(response.status_code, 401)

    def test_update_comment_with_invalid_data(self):
        comment_data = {
            'content': '',
        }
        token = f'Token {self.token}'
        content = encode_multipart('BoUnDaRyStRiNg', comment_data)
        response = self.client.put(
            f'/api/update-comment/{self.comment.id}/',
            data=content,
            HTTP_AUTHORIZATION=token,
            content_type='multipart/form-data; boundary=BoUnDaRyStRiNg')
        self.assertEqual(response.status_code, 400)


class ListCommentViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.associated_photo = PhotoFactory()
        cls.comments = CommentFactory.create_batch(5, author=cls.author)
        cls.client = APIClient()

    def test_list_comments_success(self):
        comment_data = {'photo_id': self.associated_photo.id}
        response = self.client.get('/api/comments/', comment_data)
        self.assertEqual(response.status_code, 200)


class RetrieveCommentViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = UserFactory(username='admin')
        cls.associated_photo = PhotoFactory()
        cls.comment = CommentFactory(author=cls.author)
        cls.client = APIClient()

    def test_retrieve_comment_success(self):
        response = self.client.get(f'/api/comment/{self.comment.id}/')
        self.assertEqual(response.status_code, 200)

    def test_retrieve_non_existing_comment(self):
        response = self.client.get('/api/comment/999/')
        self.assertEqual(response.status_code, 404)
