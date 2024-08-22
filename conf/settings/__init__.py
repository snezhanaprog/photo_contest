from decouple import config
from split_settings.tools import include


# django.py
include(
    'django.py',
    'database.py',
    'celery.py',
    'logger.py',
    'rest_framework.py',
    'swagger.py'
)