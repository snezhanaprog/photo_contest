from rest_framework import serializers
from models_app.models.photo.models import Photo
from api.services.photo.create import CreatePhotoService


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'

    def create(self, validated_data):
        return CreatePhotoService.create_photo(**validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = instance.get_absolute_url()
        return representation
