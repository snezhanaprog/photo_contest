from models_app.models.photo.models import Photo
from django import forms
from utils.constants import VISIBILITY_CHOICES
from django.core.exceptions import ValidationError
from utils.django_service_objects.service_objects.services import Service


class UpdatePhotoService(Service):
    id = forms.IntegerField(required=True)
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=500)
    author = forms.IntegerField()
    image = forms.FileInput()
    status = forms.ChoiceField(choices=VISIBILITY_CHOICES)

    def process(self):
        format = ['image/jpeg', 'image/png']
        if self.data['image'].content_type not in format:
            raise ValidationError(
                "Недопустимый тип изображения. Разрешены только JPEG, PNG."
            )

        self.result = Photo.objects.get(id=self.cleaned_data['id'])
        if self.result.author != (self.cleaned_data['author']).id:
            raise PermissionError(
                "У вас нет прав для изменения этого фото."
            )
        for field, value in self.cleaned_data.items():
            setattr(self.result, field, value)
        self.result.image = self.data['image']
        self.result.save()
        self.response_status = 200
        return self
