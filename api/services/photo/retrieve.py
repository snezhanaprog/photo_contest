from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import Service


class RetrievePhotoService(Service):
    id = forms.IntegerField(required=True)

    def process(self):
        return Photo.objects.get(id=self.cleaned_data['id'])
