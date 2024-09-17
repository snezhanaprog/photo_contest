from django.contrib.auth.models import User
from models_app.models.user.models import Profile
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class RetrieveUserService(ServiceWithResult):
    id = forms.CharField(max_length=50)

    def process(self):
        self.result = {
            'user': self._user,
            'profile': self._profile
        }
        return self

    @property
    def _user(self):
        return User.objects.get(id=self.cleaned_data['id'])

    @property
    def _profile(self):
        return Profile.objects.get(user=self._user)
