from models_app.models.photo.models import Photo
from service_objects.services import Service
from django.core.exceptions import ValidationError


class UpdatePhotoService(Service):
    class Meta:
        model = Photo
        fields = ['photo_id', 'title', 'description', 'image', 'status']

    def process(self, author=None):
        format = ['image/jpeg', 'image/png']
        if self.cleaned_data['image'].content_type not in format:
            raise ValidationError(
                "Недопустимый тип изображения. Разрешены только JPEG, PNG."
            )

        try:
            photo = Photo.objects.get(id=self.cleaned_data['photo_id'])
            if photo.author != author:
                raise PermissionError(
                    "У вас нет прав для изменения этого фото."
                )
            for field, value in self.cleaned_data.items():
                setattr(photo, field, value)
            photo.save()
            return photo
        except Exception as e:
            raise ValidationError(f"Фотография не найдена: {str(e)}")
