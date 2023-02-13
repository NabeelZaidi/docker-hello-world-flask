FROM python:3.8.2-alpine3.11

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

COPY . /app
WORKDIR /app

RUN apk update && \
    apk add --no-cache build-base unixodbc-dev tzdata && \
    pip install -r requirements.txt

RUN pip install pyodbc
RUN pip install -r requirements.txt

RUN apt-get install curl
RUN apt-get install apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list

RUN apt-get update
ENV ACCEPT_EULA=y DEBIAN_FRONTEND=noninteractive
RUN apt-get install mssql-tools unixodbc-dev -y

ENTRYPOINT FLASK_APP=/app/server.py flask run --host=0.0.0.0 --port=80
