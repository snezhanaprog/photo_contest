from models_app.models.comment.models import Comment
from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class ListCommentService(ServiceWithResult):
    photo_id = forms.IntegerField()
    parent = forms.IntegerField(required=False)

    def process(self):
        self.result = self._comments
        return self

    @property
    def _comments(self):
        return Comment.objects.filter(
            associated_photo=self._photo,
            parent=self._parent
        )

    @property
    def _photo(self):
        return Photo.objects.get(id=self.cleaned_data['photo_id'])

    @property
    def _parent(self):
        try:
            return Comment.objects.get(id=self.cleaned_data['parent'])
        except Comment.DoesNotExist:
            return None
