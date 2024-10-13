from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from models_app.models.voice.models import Voice
from notifications.consumers import notify_user


@receiver(post_save, sender=Voice)
def voice_post_save(sender, instance, created, **kwargs):
    if created:
        photo = instance.associated_photo
        photo.count_voices += 1
        photo.change_counters = True
        photo.save()
        notify_user(
            instance.author,
            f'Пользователь {instance.author} поставил лайк' +
            f' на ваше фото "{photo.title}"! ' +
            f'Всего голосов на фото {photo.count_voices}'
        )


@receiver(pre_delete, sender=Voice)
def voice_pre_delete(sender, instance, **kwargs):
    photo = instance.associated_photo
    print("hey")
    if photo:
        photo.count_voices -= 1
        photo.change_counters = True
        photo.save()
        notify_user(
            instance.author,
            f'Пользователь {instance.author} убрал лайк' +
            f' с вашего фото "{photo.title}"!' +
            f'Всего голосов на фото {photo.count_voices}'
        )
