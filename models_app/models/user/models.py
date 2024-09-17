from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from ..base.models import BaseModel
from django.conf import settings


class Profile(BaseModel):
    avatar = models.ImageField(upload_to='avatars/', default="default.jpg")
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        if self.user:
            return str(self.user.username)
        return str(self.user)

    def get_absolute_url(self):
        if self.avatar:
            return f"{settings.MEDIA_URL}{self.avatar}"
        return None
