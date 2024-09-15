from django.contrib.auth.models import User
from models_app.models.user.models import Profile
from django import forms
from utils.django_service_objects.service_objects.services import ServiceWithResult  # noqa: E501


class CreateUserService(ServiceWithResult):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

    custom_validations = ['validate_data']

    def process(self):
        self.run_custom_validations()
        if self.is_valid():
            self.result = self._user
            self.result.save()
            self._profile
        return self

    @property
    def _user(self):
        try:
            user = User(
                username=self.cleaned_data['username'],
                email=self.cleaned_data['email'],
            )
            user.set_password(self.cleaned_data['password'])
            return user
        except Exception:
            return None

    @property
    def _profile(self):
        try:
            Profile.objects.create(user=self._user)
        except Exception:
            return None

    def validate_data(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        if User.objects.filter(username=username).exists():
            raise ValueError('Пользователь с таким именем уже существует')
        if User.objects.filter(email=email).exists():
            raise ValueError('Пользователь с такой почтой уже существует')
