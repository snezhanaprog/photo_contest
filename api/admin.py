from django.contrib import admin
from models_app.models.comment.models import Comment
from models_app.models.photo.models import Photo
from models_app.models.voice.models import Voice
from models_app.models.user.models import Profile

admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(Voice)
admin.site.register(Profile)
