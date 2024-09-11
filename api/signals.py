from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from models_app.models.voice.models import Voice


@receiver(post_save, sender=Voice)
def voice_post_save(sender, instance, created, **kwargs):
    if created:
        photo = instance.associated_photo
        photo.count_voices += 1
        photo.save()


@receiver(pre_delete, sender=Voice)
def voice_pre_delete(sender, instance, **kwargs):
    photo = instance.associated_photo
    if photo:
        photo.count_voices -= 1
        photo.save()
