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

ENTRYPOINT FLASK_APP=/app/server.py flask run --host=0.0.0.0 --port=80
