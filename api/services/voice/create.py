from models_app.models.voice.models import Voice
from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.contrib.auth.models import User


class CreateVoiceService(ServiceWithResult):
    author_id = forms.IntegerField()
    photo_id = forms.IntegerField()

    def process(self):
        self.result, _ = self._voice
        return self

    @property
    def _photo(self):
        return Photo.objects.get(id=self.cleaned_data['photo_id'])

    @property
    def _voice(self):
        return Voice.objects.get_or_create(
            author=self._author,
            associated_photo=self._photo,
        )

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])
