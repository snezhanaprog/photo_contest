from django.contrib import admin
from models_app.models.mass_notification.models import MassNotification


class MassNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created_at')
    search_fields = ('content',)


admin.site.register(MassNotification, MassNotificationAdmin)
