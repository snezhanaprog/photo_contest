from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from models_app.models.comment.models import Comment


@receiver(post_save, sender=Comment)
def comment_post_save(sender, instance, created, **kwargs):
    if created:
        photo = instance.associated_photo
        photo.count_comments += 1
        photo.save()


@receiver(pre_delete, sender=Comment)
def comment_pre_delete(sender, instance, **kwargs):
    photo = instance.associated_photo
    if photo:
        photo.count_comments -= 1
        photo.save()
