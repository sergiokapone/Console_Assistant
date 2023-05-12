# Указываем базовый образ
FROM python:3.10-alpine

# Устанавливаем переменную окружения для запуска приложения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем рабочую директорию для приложения
WORKDIR /app

# Копируем файлы приложения в рабочую директорию
COPY . /app

RUN apk update \
    && apk add --no-cache gcc musl-dev \
    && pip install pipenv \
    && pipenv install --system --deploy \
    && pip install pipenv
    
CMD ["pipenv", "run", "assistant"]
