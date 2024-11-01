# Используем официальный образ Python как базовый
FROM python:3.10

# это переменная окружения, которая означает, что Python не будет пытаться создавать файлы .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# выходные данные python, т.е. потоки stdout и stderr, отправляются прямо на терминал
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости проекта в контейнер
COPY req.txt ./

# Устанавливаем зависимости проекта
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r req.txt

# Копируем исходный код проекта в контейнер
COPY . .

# устанавливаем Google последней стабильной версии
RUN apt update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i --force-depends google-chrome-stable_current_amd64.deb; exit 0
RUN apt-get install -f -y
