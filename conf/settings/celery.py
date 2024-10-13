import os
from celery import Celery


CELERY_ACCEPT_CONTENT = ['json', 'application/x-python-serialize']
CELERY_TASK_SERIALIZER = 'pickle'

CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

app = Celery("models_app")

app.conf.update(task_track_started=True, task_send_sent_event=True)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
    "delete_photos": {
        "task": "models_app.tasks.tasks.delete_photos",
        'schedule': 60.0,
    },
}
from models_app.tasks.tasks import delete_photos  # noqa: F401 E402
