from rest_framework import serializers
from models_app.models.photo.models import Photo
from models_app.models.voice.models import Voice
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = '__all__'

    def is_liked_photo(self, author, photo):
        try:
            voice = Voice.objects.get(
                author=author,
                associated_photo=photo
                )
            if voice:
                return True
        except Exception:
            return False

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['image'] = instance.get_absolute_url()

        author_obj = User.objects.get(id=repr['author'])
        photo_obj = Photo.objects.get(id=repr['id'])

        repr['author'] = author_obj.username
        repr['is_liked'] = self.is_liked_photo(
            author=author_obj, photo=photo_obj
        )
        return repr
