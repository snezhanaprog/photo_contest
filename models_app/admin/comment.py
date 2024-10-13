from django.contrib import admin
from models_app.models.comment.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'author',
                    'associated_photo', 'created_at')
    list_filter = ('author', 'associated_photo')
    search_fields = ('content',)


admin.site.register(Comment, CommentAdmin)
