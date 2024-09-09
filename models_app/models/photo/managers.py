from django.db import models
from django.db.models import Q


class PhotoQuerySet(models.QuerySet):
    def search(self, query):
        return self.filter(Q(title__icontains=query) |
                           Q(description__icontains=query))

    def filter_by_status(self, status):
        return self.filter(status=status)

    def filter_by_author(self, author):
        return self.filter(author=author)

    def sort_by_field(self, field):
        return self.order_by(field)


class PhotoManager(models.Manager):
    def get_queryset(self):
        return PhotoQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)

    def filter_by_status(self, status):
        return self.get_queryset().filter_by_status(status=status)

    def filter_by_author(self, author):
        return self.get_queryset().filter_by_author(author=author)

    def sort_by_field(self, field):
        return self.get_queryset().sort_by_field(field=field)
