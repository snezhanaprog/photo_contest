from django.db import models
from django.contrib.auth.models import User
from ..photo.models import Photo


class Voice(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, blank=True)
    date_activated = models.DateTimeField(auto_now_add=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f"photo:{self.photo} author:{self.author}"
