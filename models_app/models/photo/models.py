from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .managers import PhotoManager
from ..base.models import BaseModel
from django.conf import settings


class Photo(BaseModel):
    VISIBILITY_CHOICES = [
        ('private', 'На модерации'),
        ('deleted', 'На удалении'),
        ('public', 'Одобрено'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    author = models.ForeignKey(User,
                               related_name='photos',
                               on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    old_image = models.ImageField(null=True, blank=True)

    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG')

    count_comments = models.IntegerField(default=0)
    count_voices = models.IntegerField(default=0)
    publicated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=20,
                              choices=VISIBILITY_CHOICES,
                              default='private')

    items = PhotoManager()

    class Meta:
        db_table = 'Photo'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        if self.image:
            return f"{settings.MEDIA_URL}{self.image}"
        return None
