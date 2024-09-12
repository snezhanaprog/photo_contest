from django.core.exceptions import ValidationError
from models_app.models.comment.models import Comment
from service_objects.services import Service


class DeleteCommentService(Service):
    class Meta:
        model = Comment
        fields = ['comment_id']

    def process(self, author=None):
        try:
            comment = Comment.objects.get(id=self.data['comment_id'])
            if comment.author != author:
                raise PermissionError(
                    "У вас нет прав для удаления этого комментария."
                )
            comment.delete()
            return comment
        except Exception:
            raise ValidationError("Ошибка удаления")
