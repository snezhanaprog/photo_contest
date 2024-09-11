from models_app.models.photo.models import Photo
from service_objects.services import Service
from django.core.exceptions import ValidationError


class CreatePhotoService(Service):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'author', 'image', 'status']

    def process(self, author):
        format = ['image/jpeg', 'image/png']
        if self.data['image'].content_type not in format:
            raise ValidationError(
                "Недопустимый тип изображения. Разрешены только JPEG, PNG."
            )

        photo = Photo(
            title=self.data['title'],
            description=self.data['description'],
            author=author,
            image=self.data['image'],
            status=self.data.get('status', 'private')
            )
        try:
            photo.save()
        except Exception as e:
            raise ValidationError(
                f"Ошибка при сохранении фотографии: {str(e)}"
            )

        return photo
