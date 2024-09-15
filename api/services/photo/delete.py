from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class DeletePhotoService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    author = forms.Field()

    def process(self):
        self.result = self._photo
        self._photo.delete()
        return self

    @property
    def _photo(self):
        try:
            return Photo.objects.get(
                id=self.cleaned_data['id'],
                author=self.cleaned_data['author']
            )
        except Exception:
            return None
