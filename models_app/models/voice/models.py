from django.db import models
from django.contrib.auth.models import User
from ..photo.models import Photo
from ..base.models import BaseModel


class Voice(BaseModel):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True, blank=True, related_name="voices")
    associated_photo = models.ForeignKey(Photo,
                                         on_delete=models.CASCADE,
                                         related_name='voices')

    class Meta:
        db_table = 'Voice'
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'

    def __str__(self):
        return f"photo:{self.photo} author:{self.author}"
