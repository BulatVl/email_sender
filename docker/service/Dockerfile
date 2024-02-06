FROM python:3.12-alpine

RUN apk update && apk add python3-dev gcc libc-dev

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./service /app/service
ADD ./docker /app/docker

RUN chmod +x /app/docker/service/server-entrypoint.sh
RUN chmod +x /app/docker/service/worker-entrypoint.sh