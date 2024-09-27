from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from utils.django_service_objects.service_objects.errors import ForbiddenError  # noqa: E501
from django.contrib.auth.models import User
from utils.django_service_objects.service_objects.errors import NotFound


class DeletePhotoService(ServiceWithResult):
    id = forms.IntegerField()
    author_id = forms.IntegerField()

    custom_validations = [
        'validate_permission',
        'validate_presence_author',
        'validate_presence_photo'
    ]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._photo
            self._photo.delete()
        return self

    @property
    def _photo(self):
        return Photo.objects.get(id=self.cleaned_data['id'])

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])

    def validate_permission(self):
        if self._author != self._photo.author:
            ForbiddenError("Пользователь не имеет прав на удаление")

    def validate_presence_author(self):
        if not self._author:
            self.add_error(
                "id",
                NotFound(
                    message=f"Not found user with id = {
                        self.cleaned_data['author_id']}"
                ),
            )

    def validate_presence_photo(self):
        if not self._photo:
            self.add_error(
                "id",
                NotFound(
                    message=f"Not found photo with id = {
                        self.cleaned_data['id']}"
                ),
            )
