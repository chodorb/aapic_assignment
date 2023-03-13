# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update -y && apt-get install netcat -y
WORKDIR /appic
COPY requirements.txt /appic/
RUN pip install -r requirements.txt
COPY . /appic