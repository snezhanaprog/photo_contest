import factory
from models_app.models.voice.models import Voice
from models_app.factories.user import UserFactory
from models_app.factories.photo import PhotoFactory


class VoiceFactory(factory.django.DjangoModelFactory):
    author = factory.SubFactory(UserFactory)
    associated_photo = factory.SubFactory(PhotoFactory)

    class Meta:
        model = Voice
