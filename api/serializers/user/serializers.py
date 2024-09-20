from rest_framework import serializers
from models_app.models.user.models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['avatar'] = instance.get_absolute_url()
        if hasattr(instance, 'user'):
            user_obj = instance.user
            representation['user'] = user_obj.username
        return representation
