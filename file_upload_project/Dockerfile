FROM python:3.10
RUN apt-get update && apt-get install -y redis-server && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

CMD redis-server & celery -A file_upload_project worker --loglevel=info &

CMD python manage.py runserver 0.0.0.0:8000