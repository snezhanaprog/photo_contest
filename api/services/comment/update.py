from models_app.models.comment.models import Comment
from service_objects.services import Service
from django.core.exceptions import ValidationError


class UpdateCommentService(Service):
    class Meta:
        model = Comment
        fields = ['comment_id']

    def process(self, author=None):
        try:
            comment = Comment.objects.get(id=self.data['comment_id'])
            if comment.author != author:
                raise PermissionError(
                    "У вас нет прав для изменения этого фото."
                )
            for field, value in self.data.items():
                setattr(comment, field, value)
            comment.save()
            return comment
        except Exception as e:
            raise ValidationError(f"Комментарий не найден: {str(e)}")
