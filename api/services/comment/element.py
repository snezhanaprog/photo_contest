from models_app.models.comment.models import Comment
from service_objects.services import Service
from django.core.exceptions import ValidationError


class ItemCommentService(Service):
    class Meta:
        model = Comment
        fields = ['comment_id']

    def process(self):
        try:
            return Comment.objects.get(id=self.data.get('comment_id'))
        except Exception as e:
            raise ValidationError(f"Комментарий не найден: {str(e)}")
