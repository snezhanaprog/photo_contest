from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.contrib.auth.models import User


class DeletePhotoService(ServiceWithResult):
    id = forms.IntegerField()
    author_id = forms.IntegerField()

    custom_validations = ['validate_permission']

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
            PermissionError("Пользователь не имеет прав на удаление")
