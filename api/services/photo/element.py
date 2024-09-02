from models_app.models.photo.models import Photo
from service_objects.services import Service
from django.core.exceptions import ValidationError


class ItemPhotoService(Service):
    class Meta:
        model = Photo
        fields = ['photo_id']

    def process(self):
        try:
            return Photo.objects.get(id=self.cleaned_data['photo_id'])
        except Exception as e:
            raise ValidationError(f"Фотография не найдена: {str(e)}")
