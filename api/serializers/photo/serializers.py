from rest_framework import serializers
from models_app.models.photo.models import Photo
from models_app.models.voice.models import Voice
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Photo
        fields = '__all__'

    def get_is_liked(self, obj):
        user = self.context.get("user")
        try:
            voice = Voice.objects.get(
                author=user,
                associated_photo=obj
                )
            if voice:
                return True
        except Exception:
            return False

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['image'] = instance.get_absolute_url()
        author_obj = User.objects.get(id=repr['author'])
        repr['author'] = author_obj.username
        return repr
