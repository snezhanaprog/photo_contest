from models_app.models.photo.models import Photo
from utils.constants import VISIBILITY_CHOICES
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.contrib.auth.models import User


class ListAuthorPhotoService(ServiceWithResult):
    author_id = forms.IntegerField()
    status = forms.ChoiceField(choices=VISIBILITY_CHOICES)

    def process(self):
        self.result = self._photo
        return self

    @property
    def _photo(self):
        return (
            Photo.items
            .filter_by_author(author=self._author)
            .filter_by_status(status=self.cleaned_data['status'])
        )

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])
