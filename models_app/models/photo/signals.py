from django.db.models.signals import post_save
from django.dispatch import receiver
from models_app.models.photo.models import Photo
from notifications.consumers import notify_user


@receiver(post_save, sender=Photo)
def photo_post_save(sender, instance, created, **kwargs):
    if not created:
        if instance.status == "private":
            notify_user(
                instance.author,
                f'Ваша фотография {instance.title} отправлена на модерацию!')
        if instance.status == "public":
            notify_user(instance.author,
                        f'Ваша фотография {instance.title} одобрена!')
