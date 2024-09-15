from models_app.models.comment.models import Comment
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class DeleteCommentService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    author = forms.Field(required=True)

    def process(self):
        if self._child_comment is None:
            self.result = self._comment
            self._comment.delete()
        return self

    @property
    def _comment(self):
        try:
            return Comment.objects.get(
                id=self.cleaned_data['id'],
                author=self.cleaned_data['author']
            )
        except Exception:
            return None

    @property
    def _child_comment(self):
        try:
            return Comment.objects.get(parent=self._comment)
        except Exception:
            return None
