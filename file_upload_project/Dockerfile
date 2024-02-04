FROM python:3.10
RUN apt-get update && apt-get install -y redis-server && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app
RUN python manage.py migrate

RUN python manage.py collectstatic --noinput

COPY run_server.sh /app/run_server.sh

RUN chmod +x /app/run_server.sh

CMD ["./run_server.sh"]