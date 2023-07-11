FROM python:3.9

# копирование кода Django-приложения и установка зависимостей
WORKDIR .
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Установка необходимых инструментов для отладки
RUN apt-get update && apt-get install -y redis-tools nano net-tools

# Запуск Redis-сервера и Django runserver
CMD python manage.py runserver 0.0.0.0:8000