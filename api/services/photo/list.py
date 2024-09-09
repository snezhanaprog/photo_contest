from models_app.models.photo.models import Photo
from service_objects.services import Service


class ListPhotoService(Service):

    class Meta:
        model = Photo
        fields = "__all__"

    def process(self, search=None, sort=None):
        return Photo.items.filter_by_status(
            status='public'
            ).search(search).sort_by_field(sort)

    def process_for_author(
        self, author,
        search=None,
        sort=None,
        status='public',
    ):
        if author is None:
            raise ValueError("Автор не может быть None.")
        return Photo.items.filter_by_author(
                author=author
            ).filter_by_status(
                status=status
            ).search(search).sort_by_field(sort)
