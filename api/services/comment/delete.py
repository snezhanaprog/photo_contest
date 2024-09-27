from models_app.models.comment.models import Comment
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.contrib.auth.models import User


class DeleteCommentService(ServiceWithResult):
    id = forms.IntegerField()
    author_id = forms.IntegerField()

    custom_validations = ['validate_permission']

    def process(self):
        self.run_custom_validations()
        if self.is_valid() and self._child_comment is None:
            self.result = self._comment
            self._comment.delete()
        return self

    @property
    def _comment(self):
        return Comment.objects.get(id=self.cleaned_data['id'])

    @property
    def _child_comment(self):
        try:
            return Comment.objects.get(parent=self._comment)
        except Exception:
            return None

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])

    def validate_permission(self):
        if self._author != self._comment.author:
            PermissionError("Пользователь не имеет прав на удаление")
