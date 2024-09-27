from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from utils.django_service_objects.service_objects.errors import ValidationError  # noqa: E501
from django.contrib.auth.models import User
from utils.django_service_objects.service_objects.errors import NotFound


class CreatePhotoService(ServiceWithResult):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=500)
    image = forms.FileInput()
    author_id = forms.IntegerField()

    custom_validations = ['validate_format', 'validate_presence_author']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._photo
        return self

    @property
    def _photo(self):
        return Photo.objects.create(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            author=self._author,
            image=self.data['image']
        )

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])

    def validate_format(self):
        format = ['image/jpeg', 'image/png']
        if self.data['image'].content_type not in format:
            raise ValidationError(
                "Недопустимый тип изображения. Разрешены только JPEG, PNG."
            )

    def validate_presence_author(self):
        if not self._author:
            self.add_error(
                "id",
                NotFound(
                    message=f"Not found user with id = {
                        self.cleaned_data['author_id']}"
                ),
            )
