from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class ListPhotoService(ServiceWithResult):
    search = forms.CharField(max_length=200, required=False)
    sort = forms.CharField(max_length=50)

    def process(self):
        self.result = self._photos
        return self

    @property
    def _photos(self):
        try:
            return (
                Photo.items.filter_by_status(status='public')
                .search(self.cleaned_data['search'])
                .sort_by_field(self.cleaned_data['sort'])
            )
        except Exception:
            return None
