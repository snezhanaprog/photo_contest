from models_app.models.comment.models import Comment
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class RetrieveCommentService(ServiceWithResult):
    id = forms.IntegerField()

    def process(self):
        self.result = self._comment
        return self

    @property
    def _comment(self):
        return Comment.objects.get(id=self.cleaned_data['id'])
