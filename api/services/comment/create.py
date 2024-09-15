from models_app.models.comment.models import Comment
from models_app.models.photo.models import Photo
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class CreateCommentService(ServiceWithResult):
    content = forms.CharField(max_length=500, required=True)
    author = forms.Field(required=True)
    photo = forms.IntegerField(required=True)
    parent = forms.IntegerField(required=False)

    def process(self):
        self.result = self._comment
        return self

    @property
    def _comment(self):
        try:
            return Comment.objects.create(
                content=self.cleaned_data['content'],
                associated_photo=self._photo,
                author=self.cleaned_data['author'],
                parent=self._parent
            )
        except Exception:
            return None

    @property
    def _photo(self):
        try:
            return Photo.objects.get(id=self.cleaned_data['photo'])
        except Exception:
            return None

    @property
    def _parent(self):
        try:
            return Comment.objects.get(id=self.cleaned_data['parent'])
        except Exception:
            return None
