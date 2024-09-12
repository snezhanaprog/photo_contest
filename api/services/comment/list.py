from models_app.models.comment.models import Comment
from models_app.models.photo.models import Photo
from service_objects.services import Service


class ListCommentService(Service):

    class Meta:
        model = Comment
        fields = "__all__"

    def process(self, parent=None):
        photo = Photo.objects.get(id=self.data['photo_id'])
        comments = Comment.objects.filter(
            associated_photo=photo, parent=parent
            )
        return comments
