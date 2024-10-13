from celery import shared_task
from django.db.models import Q


@shared_task()
def delete_photos():
    from models_app.models.photo.models import Photo
    for photo in Photo.objects.filter(
        Q(status="deleted") | Q(status="block")
    ):
        photo.delete()
