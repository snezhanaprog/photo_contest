from django.db.models.signals import post_save
from django.dispatch import receiver
from models_app.models.mass_notification.models import MassNotification
from notifications.consumers import notify_user
from notifications.consumers import NotificationConsumer


@receiver(post_save, sender=MassNotification)
def mass_notification_post_save(sender, instance, created, **kwargs):
    print("here", NotificationConsumer.__dict__)
    for user in NotificationConsumer.online_users:
        notify_user(user, instance.content)
