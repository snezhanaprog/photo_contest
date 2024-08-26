from django.db import models
from django.db.models import Q


class PhotoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def search(self, query):
        return self.filter(Q(name__icontains=query) |
                           Q(description__icontains=query))

    def filter_by_status(self, status):
        return self.get_queryset().filter_by_date(status=status)

    def sort_by_count_comments_up(self):
        return self.get_queryset().order_by('count_comments')

    def sort_by_count_comments_down(self):
        return self.get_queryset().order_by('-count_comments')

    def sort_by_count_voices_up(self):
        return self.get_queryset().order_by('count_voices')

    def sort_by_count_voices_down(self):
        return self.get_queryset().order_by('-count_voices')

    def sort_by_date_publicated_up(self):
        return self.get_queryset().order_by('date_publicated')

    def sort_by_date_publicated_down(self):
        return self.get_queryset().order_by('-date_publicated')
