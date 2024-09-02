from rest_framework import serializers
from models_app.models.photo.models import Photo
from api.services.photo.create import CreatePhotoService


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'author', 'image', 'image_thumbnail',
                  'count_comments', 'count_voices', 'status']

    def create(self, validated_data):
        return CreatePhotoService.create_photo(**validated_data)
