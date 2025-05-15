# Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala dependências básicas do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc python3-dev musl-dev && \
    rm -rf /var/lib/apt/lists/*

# Instala dependências do projeto
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia todo o projeto
COPY . .

# Entrypoint para rodar migrations e criar superuser automaticamente
CMD ["sh", "-c", "python manage.py migrate && python manage.py createsuperuser --noinput || true && python manage.py runserver 0.0.0.0:8000"]
