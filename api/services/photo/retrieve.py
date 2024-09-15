from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class RetrievePhotoService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    author = forms.Field(required=False)

    def process(self):
        self.result = self._photo
        return self

    @property
    def _photo(self):
        try:
            return Photo.objects.get(id=self.cleaned_data['id'])
        except Photo.DoesNotExist:
            return None
