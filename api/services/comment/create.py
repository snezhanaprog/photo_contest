from models_app.models.comment.models import Comment
from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.contrib.auth.models import User
from utils.django_service_objects.service_objects.errors import NotFound


class CreateCommentService(ServiceWithResult):
    content = forms.CharField(max_length=500)
    author_id = forms.IntegerField()
    photo_id = forms.IntegerField()
    parent = forms.IntegerField(required=False)

    custom_validations = [
        'validate_presence_author',
        'validate_presence_photo'
    ]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._comment
        return self

    @property
    def _comment(self):
        return Comment.objects.create(
            content=self.cleaned_data['content'],
            associated_photo=self._photo,
            author=self._author,
            parent=self._parent
        )

    @property
    def _photo(self):
        return Photo.objects.get(id=self.cleaned_data['photo_id'])

    @property
    def _parent(self):
        try:
            return Comment.objects.get(id=self.cleaned_data['parent'])
        except Comment.DoesNotExist:
            return None

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])

    def validate_presence_author(self):
        if not self._author:
            self.add_error(
                "id",
                NotFound(
                    message="Not found user with id = " +
                    self.cleaned_data['author_id']
                ),
            )

    def validate_presence_photo(self):
        if not self._photo:
            self.add_error(
                "id",
                NotFound(
                    message="Not found photo with id = " +
                    self.cleaned_data['photo_id']
                ),
            )
