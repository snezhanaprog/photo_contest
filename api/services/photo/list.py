from models_app.models.photo.models import Photo
from service_objects.services import Service


class ListPhotoService(Service):
    class Meta:
        model = Photo
        fields = "__all__"

    def process(self):
        return Photo.objects.all()
