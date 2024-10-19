import factory
from models_app.models.photo.models import Photo
from models_app.factories.user import UserFactory


class PhotoFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('text', max_nb_chars=100)
    description = factory.Faker('text', max_nb_chars=500)
    author = factory.SubFactory(UserFactory)
    image = factory.django.ImageField()
    old_image = factory.django.ImageField(null=True, blank=True)
    count_comments = 0
    count_voices = 0
    status = 'private'

    class Meta:
        model = Photo
