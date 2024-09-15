from rest_framework import serializers
from models_app.models.comment.models import Comment
from django.contrib.auth.models import User


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        author_obj = User.objects.get(id=repr['author'])
        repr['author'] = author_obj.username
        return repr
