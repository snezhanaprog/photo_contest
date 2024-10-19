from rest_framework import serializers
from models_app.models.user.models import Profile
from django.contrib.auth.models import User
from library.sociallib import google
from library.register.register import register_social_user
from django.conf import settings


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


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data['sub']
        except Exception as e:
            raise Exception(e)
        if user_data['aud'] != settings.GOOGLE_CLIENT_ID:

            raise Exception('oops, who are you?')

        user_id = user_data['sub']
        email = user_data['email']
        name = user_data['name']
        provider = 'google'

        return register_social_user(
            provider=provider, user_id=user_id, email=email, name=name)
