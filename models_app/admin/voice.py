from django.contrib import admin
from models_app.models.voice.models import Voice


class VoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'associated_photo', 'created_at')
    list_filter = ('author', 'associated_photo')


admin.site.register(Voice, VoiceAdmin)
