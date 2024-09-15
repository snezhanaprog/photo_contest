from models_app.models.photo.models import Photo
from utils.constants import VISIBILITY_CHOICES
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class ListAuthorPhotoService(ServiceWithResult):
    author = forms.Field()
    status = forms.ChoiceField(choices=VISIBILITY_CHOICES)

    def process(self):
        self.result = self._photo
        return self

    @property
    def _photo(self):
        try:
            return (
                Photo.items
                .filter_by_author(author=self.cleaned_data['author'])
                .filter_by_status(status=self.cleaned_data['status'])
            )
        except Exception:
            return None
