import factory
from django.contrib.auth.models import User
from models_app.models.user.models import Profile


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('text', max_nb_chars=100)
    password = factory.Faker('text', max_nb_chars=100)
    email = factory.Faker('text', max_nb_chars=100)

    class Meta:
        model = User


class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    avatar = factory.django.ImageField()

    class Meta:
        model = Profile
