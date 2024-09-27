from models_app.models.comment.models import Comment
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.contrib.auth.models import User


class UpdateCommentService(ServiceWithResult):
    id = forms.IntegerField()
    content = forms.CharField(max_length=500)
    author_id = forms.IntegerField()

    custom_validations = ['validate_permission']

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
        return Comment.objects.get(id=self.cleaned_data['id'])

    @property
    def _author(self):
        return User.objects.get(id=self.cleaned_data['author_id'])

    def validate_permission(self):
        if self._author != self._comment.author:
            PermissionError("Пользователь не имеет прав на изменение")
