from models_app.models.voice.models import Voice
from models_app.models.photo.models import Photo
from service_objects.services import Service
from django.core.exceptions import ValidationError


class DeleteVoiceService(Service):
    class Meta:
        model = Voice
        fields = ['author', 'associated_photo'],

    def process(self, author):
        print("del")
        try:
            photo = Photo.objects.get(id=self.data['photo_id'])
            voice = Voice.objects.get(author=author, associated_photo=photo)
            voice.delete()
            return voice
        except Exception:
            raise ValidationError("Ошибка удаления")
