from django.core.exceptions import ValidationError
from models_app.models.photo.models import Photo
from service_objects.services import Service


class DeletePhotoService(Service):
    class Meta:
        model = Photo
        fields = ['photo_id']

    def process(self, author=None):
        try:
            photo = Photo.objects.get(id=self.cleaned_data['photo_id'])
            if photo.author != author:
                raise PermissionError(
                    "У вас нет прав для удаления этого фото."
                )
            photo.delete()
            return photo
        except Exception:
            raise ValidationError("Ошибка удаления")
