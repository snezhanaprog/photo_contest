from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from utils.django_service_objects.service_objects.errors import NotFound


class RetrievePhotoService(ServiceWithResult):
    id = forms.IntegerField()

    custom_validations = ['validate_presence_photo']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._photo
        return self

    @property
    def _photo(self):
        return Photo.objects.get(id=self.cleaned_data['id'])

    def validate_presence_photo(self):
        if not self._photo:
            self.add_error(
                "id",
                NotFound(
                    message=f"Not found photo with id = {
                        self.cleaned_data['id']}"
                ),
            )
