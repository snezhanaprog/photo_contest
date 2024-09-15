from models_app.models.comment.models import Comment
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class UpdateCommentService(ServiceWithResult):
    id = forms.IntegerField(required=True)
    content = forms.CharField(max_length=500, required=True)
    author = forms.Field(required=True)

    def process(self):
        self.result = self._update()
        return self

    def _update(self):
        obj = self._comment
        obj.content = self.cleaned_data['content']
        obj.save()
        return obj

    @property
    def _comment(self):
        try:
            return Comment.objects.get(
                id=self.cleaned_data['id'],
                author=self.cleaned_data['author']
            )
        except Exception:
            return None
