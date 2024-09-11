from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self) -> None:
        from api.signals import voice_post_save  # noqa: F401
        from api.signals import voice_pre_delete  # noqa: F401
