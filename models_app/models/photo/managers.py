from django.db import models
from .querysets import PhotoQuerySet


class PhotoManager(models.Manager):
    def get_queryset(self):
        return PhotoQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)

    def filter_by_status(self, status):
        return self.get_queryset().filter_by_status(status)

    def sort_by_count_comments_up(self):
        return self.get_queryset().sort_by_count_comments_up()

    def sort_by_count_comments_down(self):
        return self.get_queryset().sort_by_count_comments_down()

    def sort_by_count_voices_up(self):
        return self.get_queryset().sort_by_count_voices_up()

    def sort_by_count_voices_down(self):
        return self.get_queryset().sort_by_count_voices_down()

    def sort_by_date_publicated_up(self):
        return self.get_queryset().sort_by_date_publicated_up()

    def sort_by_date_publicated_down(self):
        return self.get_queryset().sort_by_date_publicated_down()
