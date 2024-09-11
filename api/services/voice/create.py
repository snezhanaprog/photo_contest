from models_app.models.voice.models import Voice
from models_app.models.photo.models import Photo
from service_objects.services import Service
from django.core.exceptions import ValidationError


class CreateVoiceService(Service):
    class Meta:
        model = Voice
        fields = ['associated_photo', 'author']

    def process(self, author):
        photo = Photo.objects.get(id=int(self.data['photo_id']))
        voice = Voice(
            author=author,
            associated_photo=photo,
            )
        try:
            voice.save()
        except Exception as e:
            raise ValidationError(
                f"Ошибка при постановке голоса: {str(e)}"
            )
        return voice
