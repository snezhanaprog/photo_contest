from models_app.models.voice.models import Voice
from models_app.models.photo.models import Photo
from service_objects.services import Service


class StatusVoiceService(Service):
    class Meta:
        model = Voice
        fields = ['author', 'associated_photo']

    def process(self, author):
        try:
            photo = Photo.objects.get(id=int(self.data['photo_id']))
            Voice.objects.get(
                author=author, associated_photo=photo)
            return True
        except Exception:
            return False
