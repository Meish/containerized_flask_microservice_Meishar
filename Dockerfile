FROM python:3.8-slim-buster

WORKDIR /app

COPY . app.py /app/

# EXPOSE 8080

RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt
