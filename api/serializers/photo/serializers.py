from rest_framework import serializers
from models_app.models.photo.models import Photo
from django.contrib.auth.models import User


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.get_absolute_url()
        author = User.objects.get(id=representation['author'])
        representation['author'] = author.username
        return representation
