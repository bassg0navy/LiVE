# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=run.py
ENV FLASK_ENV=development
RUN apt-get upgrade
#    apt-get install net-tools \
#    apt-get install iputils-ping
CMD [ "python3", "-m" , "flask", "run", "-p", "5001", "--host=0.0.0.0"]
