from django.apps import AppConfig


class ModelsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'models_app'

    def ready(self) -> None:
        from .models.voice.signals import voice_post_save  # noqa: F401
        from .models.voice.signals import voice_pre_delete  # noqa: F401
        from .models.comment.signals import comment_post_save  # noqa: F401
        from .models.comment.signals import comment_pre_delete  # noqa: F401
        from .models.photo.signals import photo_post_save  # noqa: F401
        from .models.mass_notification.signals import mass_notification_post_save  # noqa: F401 E501
