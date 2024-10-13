from django.contrib import admin
from models_app.models.photo.models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status', 'publicated_at',
                    'count_comments', 'count_voices')
    list_filter = ('author', 'status', 'publicated_at')
    search_fields = ('title', 'description', 'author__username')

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == 'public':
            return ['author', 'title', 'description', 'image',
                    'old_image', 'status']
        return super().get_readonly_fields(request, obj)


admin.site.register(Photo, PhotoAdmin)
