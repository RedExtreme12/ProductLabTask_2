FROM python:3.9-alpine3.16

RUN apk add postgresql-client build-base postgresql-dev
COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt

COPY core /core

WORKDIR /core

EXPOSE 8000

RUN adduser --disabled-password service-user

USER service-user