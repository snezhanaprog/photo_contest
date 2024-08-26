from django.db import models
from django.contrib.auth.models import User
from ..photo.models import Photo


class Comment(models.Model):
    content = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True,
                               related_name='subcomments',
                               on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, null=True, blank=True,
                              related_name='subcomments',
                              on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='comments',
                               on_delete=models.SET_NULL)

    def __str__(self):
        return self.content
