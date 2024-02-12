FROM python:3.12-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install gunicorn
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./service /app/service
COPY ./docker /app/docker

RUN chmod +x /app/docker/service/server-entrypoint.sh
RUN chmod +x /app/docker/service/worker-entrypoint.sh
RUN chmod +x /app/docker/service/beat-entrypoint.sh