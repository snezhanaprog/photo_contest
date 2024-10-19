from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from utils.django_service_objects.service_objects.errors import ForbiddenError  # noqa: E501
from utils.django_service_objects.service_objects.errors import NotFound


class CancelDeletePhoto(ServiceWithResult):
    id = forms.IntegerField()
    author_id = forms.IntegerField()

    custom_validations = [
        'validate_permission',
        'validate_presence_author',
        'validate_presence_photo'
    ]

    def process(self):
        self.change_status_private()
        return self

    @property
    def _photo(self):
        return Photo.objects.get(id=self.cleaned_data['id'])

    def change_status_private(self):
        photo = self._photo
        photo.status = "private"
        photo.save()

    def validate_permission(self):
        if self._author != self._photo.author:
            ForbiddenError("Пользователь не имеет прав на удаление")

    def validate_presence_author(self):
        if not self._author:
            self.add_error(
                "id",
                NotFound(
                    message="Not found user with id = " +
                    self.cleaned_data['author_id']
                ),
            )

    def validate_presence_photo(self):
        if not self._photo:
            self.add_error(
                "id",
                NotFound(
                    message="Not found photo with id = " +
                    self.cleaned_data['id']
                ),
            )
