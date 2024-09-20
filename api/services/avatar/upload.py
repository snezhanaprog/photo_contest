from models_app.models.user.models import Profile
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class UploadAvatarService(ServiceWithResult):
    avatar = forms.FileInput()
    user_id = forms.IntegerField()

    custom_validations = ['validate_format']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._update
        return self

    @property
    def _user(self):
        return User.objects.get(id=self.cleaned_data['user_id'])

    @property
    def _profile(self):
        return Profile.objects.get(user=self._user)

    def _update(self):
        obj = self._profile
        obj.avatar = self.data['avatar']
        obj.save()
        return obj

    def validate_format(self):
        format = ['image/jpeg', 'image/png']
        if self.data['avatar'].content_type not in format:
            raise ValidationError(
                "Недопустимый тип изображения. Разрешены только JPEG, PNG."
            )
