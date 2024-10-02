import factory
from models_app.models.comment.models import Comment
from models_app.factories.photo import PhotoFactory
from models_app.factories.user import UserFactory


class CommentFactory(factory.django.DjangoModelFactory):
    content = factory.Faker('text', max_nb_chars=200)
    author = factory.SubFactory(UserFactory)
    associated_photo = factory.SubFactory(PhotoFactory)
    parent = factory.LazyAttribute(lambda o: None)

    class Meta:
        model = Comment
