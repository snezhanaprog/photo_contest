from django.contrib.auth.models import User
from service_objects.services import Service


class CreateUserService(Service):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def process(self):
        if not self.data['username']:
            if not self.data['password'] or not self.data['email']:
                raise ValueError('Все поля обязательны для заполнения')

        if User.objects.filter(username=self.data['username']).exists():
            raise ValueError('Пользователь с таким именем уже существует')
        user = User(
            username=self.data['username'],
            email=self.data['email'],
        )
        user.set_password(self.data['password'])
        user.save()

        return user
