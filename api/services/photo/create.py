from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.core.exceptions import ValidationError


class CreatePhotoService(ServiceWithResult):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=500)
    image = forms.FileInput()
    author = forms.Field()

    custom_validations = ['validate_format']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._photo
        return self

    @property
    def _photo(self):
        try:
            return Photo.objects.create(
                title=self.cleaned_data['title'],
                description=self.cleaned_data['description'],
                author=self.cleaned_data['author'],
                image=self.data['image']
            )
        except Photo.DoesNotExist:
            return None

    def validate_format(self):
        format = ['image/jpeg', 'image/png']
        print(self.__dict__)
        if self.data['image'].content_type not in format:
            raise ValidationError(
                "Недопустимый тип изображения. Разрешены только JPEG, PNG."
            )
