# Базовый образ
FROM python:3.12-slim

# Установка необходимых зависимостей
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install setuptools
# Установка Poetry
ENV POETRY_VERSION=1.8.0
RUN pip install "poetry==$POETRY_VERSION"

# Настройка рабочей директории
WORKDIR /app

# Копируем только необходимые файлы для установки зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Копируем остальные файлы проекта
COPY . .

# Команда запуска
CMD ["poetry", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]
