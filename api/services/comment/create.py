from models_app.models.comment.models import Comment
from service_objects.services import Service
from django.core.exceptions import ValidationError


class CreateCommentService(Service):
    class Meta:
        model = Comment
        fields = ['content', 'associated_photo', 'author', 'parent']

    def process(self, author):
        comment = Comment(
            content=self.data['content'],
            associated_photo=self.data['associated_photo'],
            author=author,
            parent=self.data['parent']
            )
        try:
            comment.save()
        except Exception as e:
            raise ValidationError(
                f"Ошибка при создании комментария: {str(e)}"
            )

        return comment
