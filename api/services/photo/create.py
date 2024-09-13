from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import Service
from django.core.exceptions import ValidationError


class CreatePhotoService(Service):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=500)
    image = forms.FileInput()
    author = forms.Field()

    def process(self):
        format = ['image/jpeg', 'image/png']
        print(self.__dict__)
        if self.data['image'].content_type not in format:
            raise ValidationError(
                "Недопустимый тип изображения. Разрешены только JPEG, PNG."
            )

        self.result = Photo(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            author=self.cleaned_data['author'],
            image=self.data['image']
        )
        self.result.save()
        self.response_status = 200
        return self
