FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y unixodbc unixodbc-dev
RUN apt-get update && apt-get install -y curl apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17


RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
