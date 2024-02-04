#!/bin/bash

redis-server &

celery -A file_upload_project worker --loglevel=info &

python manage.py runserver 0.0.0.0:8000