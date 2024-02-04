# Задание: Загрузка и обработка файлов с использованием Django и Django REST Framework

## Описание проекта
Этот проект представляет собой простое приложение Django, которое позволяет загружать файлы, сохранять их на сервере, а затем асинхронно обрабатывать с использованием Celery+Redis. Для создания API используется Django REST Framework.

## Установка и запуск проекта
1. Установите Docker на ваш компьютер, если он еще не установлен.
2. Склонируйте репозиторий проекта с помощью команды:
   ```bash
   git clone https://github.com/tawaluk/test_task.git
   ```

4. Соберите и запустите контейнеры Docker.

5. После успешного запуска контейнеров необходимо будет сконфигурировать Ваш nginx файл

6. Дополнительно нужно скопировать статик-файлы из конетйнера
   ```bash
   docker cp name_container:/app/static/. /you_path_to_static/

## Использование API

### Загрузка файла
Для загрузки файла используйте эндпоинт /upload/. Отправьте POST-запрос с файлом в теле запроса.


### Получение списка файлов
Для получения списка всех файлов используйте эндпоинт /files/. Отправьте GET-запрос на этот эндпоинт.