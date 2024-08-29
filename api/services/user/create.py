from django.contrib.auth.models import User
from ..base import base


class CreateUserService(base.Service):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def process(self):
        user = User(
            username=self.data['username'],
            email=self.data['email'],
        )
        user.set_password(self.data['password'])
        user.save()

        return user
