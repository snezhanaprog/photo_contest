from models_app.models.voice.models import Voice
from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class CreateVoiceService(ServiceWithResult):
    author = forms.Field()
    photo_id = forms.IntegerField()

    def process(self):
        self.result, _ = self._voice
        return self

    @property
    def _photo(self):
        try:
            return Photo.objects.get(id=self.cleaned_data['photo_id'])
        except Photo.DoesNotExist:
            return None

    @property
    def _voice(self):
        try:
            return Voice.objects.get_or_create(
                author=self.cleaned_data['author'],
                associated_photo=self._photo,
            )
        except Photo.DoesNotExist:
            return None
