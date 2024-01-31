FROM python:3.12-alpine

COPY requirements.txt /temp/requrements.txt
COPY service/service /service
WORKDIR /service
EXPOSE 8000

RUN pip3 install -r /temp/requrements.txt

RUN adduser --disabled-password service-user

USER service-user