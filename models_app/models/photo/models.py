from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Photo(models.Model):
    VISIBILITY_CHOICES = [
        ('private', 'На модерации'),
        ('deleted', 'На удалении'),
        ('public', 'Одобрено'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    author = models.ForeignKey(User,
                               related_name='comments',
                               on_delete=models.CASCADE)

    image = models.ImageField(upload_to='images/')
    old_image = models.ImageField(null=True, blank=True)

    image_thumbnail = ImageSpecField(source='images/',
                                     processors=[ResizeToFill(100, 50)],
                                     format='JPEG')

    count_comments = models.IntegerField(default=0)
    count_voices = models.IntegerField(default=0)
    date_publicated = models.DateTimeField(auto_now="True")
    date_created = models.DateTimeField(auto_now_add="True")
    date_deleted = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=20,
                              choices=VISIBILITY_CHOICES,
                              default='private')

    def __str__(self):
        return self.title
