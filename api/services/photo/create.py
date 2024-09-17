from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class CreatePhotoService(ServiceWithResult):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=500)
    image = forms.FileInput()
    author_id = forms.IntegerField()

    custom_validations = ['validate_format']

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
