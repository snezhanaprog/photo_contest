from django.contrib.auth.models import User
from service_objects.services import Service


class CreateUserService(Service):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def process(self):
        user = User(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
        )
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
