from django.contrib.auth.models import User
from models_app.models.user.models import Profile
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class RetrieveUserService(ServiceWithResult):
    username = forms.CharField(max_length=50, required=True)

    def process(self):
        self.result = {
            'user': self._user,
            'profile': self._profile
        }
        return self

    @property
    def _user(self):
        try:
            return User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return None

    @property
    def _profile(self):
        try:
            return Profile.objects.get(user=self._user)
        except User.DoesNotExist:
            return None
