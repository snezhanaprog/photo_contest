from models_app.models.photo.models import Photo
from service_objects.services import Service
from django.core.exceptions import ValidationError


class CreatePhotoService(Service):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'author', 'image',
                  'image_thumbnail', 'count_comments',
                  'count_voices', 'status']

    def process(self):
        format = ['image/jpeg', 'image/png']
        if self.cleaned_data['image'].content_type not in format:
            raise ValidationError(
                "Недопустимый тип изображения. Разрешены только JPEG, PNG."
            )

        photo = Photo(
            title=self.cleaned_data['title'],
            description=self.cleaned_data['description'],
            author=self.cleaned_data['author'],
            image=self.cleaned_data['image'],
            image_thumbnail=self.cleaned_data['image_thumbnail'],
            count_comments=0,
            count_voices=0,
            status=self.cleaned_data.get('status', 'private')
            )

        try:
            photo.save()
        except Exception as e:
            raise ValidationError(
                f"Ошибка при сохранении фотографии: {str(e)}"
            )

        return photo
