from django.contrib.auth.models import User
from models_app.models.user.models import Profile
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
            raise ValueError(
                'Пользователь с таким именем или почтой уже существует'
            )
        try:
            user = User(
                username=self.data['username'],
                email=self.data['email'],
            )
            user.set_password(self.data['password'])
            user.save()
        except Exception as e:
            raise ValueError("Ошибка создания user" + e)
        try:
            profile = Profile.objects.create(
                user=user
            )
        except Exception as e:
            raise ValueError("Ошибка создания profile" + e)
        print("Профиль создан", profile.__str__)
        return user
