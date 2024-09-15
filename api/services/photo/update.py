from models_app.models.photo.models import Photo
from django import forms
from django.core.exceptions import ValidationError
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class UpdatePhotoService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=500)
    author = forms.Field()
    image = forms.FileInput()

    custom_validations = ['validate_format']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update()
        return self

    @property
    def _photo(self):
        try:
            return Photo.objects.get(
                id=self.cleaned_data['id'],
                author=self.cleaned_data['author']
            )
        except Photo.DoesNotExist:
            return None

    def _update(self):
        obj = self._photo
        obj.title = self.cleaned_data['title']
        obj.description = self.cleaned_data['description']
        obj.old_image = obj.image
        if 'image' in self.data:
            obj.image = self.data['image']
        obj.status = "private"
        obj.save()
        return obj

    def validate_format(self):
        type = ['image/jpeg', 'image/png']
        if 'image' in self.data:
            if self.data['image'].content_type not in type:
                raise ValidationError(
                    "Ошибка типа. Разрешены только JPEG, PNG.")
