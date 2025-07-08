FROM python:3.10-slim

# Встановлюємо системні залежності для aiohttp
RUN apt-get update && apt-get install -y gcc libffi-dev

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файли проєкту
COPY . /app

# Встановлюємо pip та залежності, змушуючи pip використовувати лише бінарні колеса
RUN pip install --upgrade pip
RUN pip install --only-binary=:all: -r requirements.txt

# Запускаємо бота
CMD ["python", "main.py"]
