# Используйте базовый образ Python
FROM python:3.9

# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файлы зависимостей в контейнер
COPY requirements.txt .

# Установите зависимости
RUN pip install -r requirements.txt

# Скопируйте все файлы проекта в контейнер
COPY . .

# Запустите команду для запуска Django сервера
CMD python manage.py runserver 0.0.0.0:8000
