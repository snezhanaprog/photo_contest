from django.contrib.auth.models import User
from models_app.models.user.models import Profile
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501
from utils.django_service_objects.service_objects.errors import NotFound


class RetrieveUserService(ServiceWithResult):
    id = forms.IntegerField()

    custom_validations = [
        'validate_presence_user',
        'validate_presence_profile'
    ]

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
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

    def validate_presence_user(self):
        if not self._user:
            self.add_error(
                "id",
                NotFound(
                    message=f"Not found user with id = {
                        self.cleaned_data['id']}"
                ),
            )

    def validate_presence_profile(self):
        if not self._profile:
            self.add_error(
                "id",
                NotFound(
                    message=f"Not found profile with user id = {
                        self.cleaned_data['id']}"
                ),
            )
