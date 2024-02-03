from celery import Celery, shared_task

from .models import File
import time


@shared_task
def process_file(file_id):

    file = File.objects.get(id=file_id)
    file.processed = True
    file.save()

