from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User


class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/')
    avatar_thumbnail = ImageSpecField(source='avatar/',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
