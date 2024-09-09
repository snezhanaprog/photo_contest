from django.contrib.auth.models import User
from models_app.models.user.models import Profile
from service_objects.services import Service


class ElementUserService(Service):
    class Meta:
        model = User
        fields = ['username']

    def process(self):
        username = self.data.get('username')

        if not username:
            raise ValueError('Имя пользователя обязательно для передачи')

        try:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)

        except User.DoesNotExist:
            raise ValueError('Пользователь не найден')
        except Profile.DoesNotExist:
            raise ValueError('Профиль для данного пользователя не найден')

        return {
            'user': user,
            'profile': profile
        }
