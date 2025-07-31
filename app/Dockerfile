FROM python:3.13-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

COPY ../pyproject.toml pyproject.toml

RUN poetry install --only main

COPY . .

CMD uvicorn app.main:app \
    --host "0.0.0.0" \
    --port ${SERVER_PORT} \
    --workers ${WORKERS}
