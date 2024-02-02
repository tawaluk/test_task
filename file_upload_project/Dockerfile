FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

RUN chmod +x run_server.sh
CMD ["./run_server.sh"]