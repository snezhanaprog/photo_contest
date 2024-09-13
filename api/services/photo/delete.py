from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import Service


class DeletePhotoService(Service):
    id = forms.IntegerField(required=True)
    author = forms.Field()

    def process(self):
        self.result = Photo.objects.get(id=self.cleaned_data['id'])
        if self.result.author != self.cleaned_data['author']:
            raise PermissionError(
                "У вас нет прав для удаления этого фото."
            )
        self.result.delete()
        self.response_status = 204
        return self
