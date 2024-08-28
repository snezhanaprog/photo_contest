from rest_framework import serializers
from ....models_app.models.voice.models import Voice


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = "__all__"
