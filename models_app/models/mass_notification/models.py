from django.db import models
from ..base.models import BaseModel


class MassNotification(BaseModel):
    content = models.CharField(max_length=200)

    class Meta:
        db_table = 'MassNotification'
        verbose_name = 'Массовая нотификация'
        verbose_name_plural = 'Массовые нотификации'

    def __str__(self):
        return str(self.id)
