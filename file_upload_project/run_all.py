import subprocess
import time

def start_django():
    subprocess.Popen(['python', 'manage.py', 'runserver'])

def start_celery():
    subprocess.Popen(['celery', '-A', 'file_upload_project', 'worker', '--loglevel=info'])

def start_redis():
    subprocess.Popen(['redis-server'])

def run_migrations():
    makemigrations_process = subprocess.Popen(['python', 'manage.py', 'makimigrations'])
    makemigrations_process.wait()
    migration_process = subprocess.Popen(['python', 'manage.py', 'migrate'])
    migration_process.wait()

def collect_static():
    subprocess.run(['python', 'manage.py', 'collectstatic', '--noinput'])

if __name__ == '__main__':
    start_redis()
    time.sleep(2)
    start_celery()
    time.sleep(2)
    run_migrations()
    collect_static()
    start_django()
