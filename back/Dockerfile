# Dockerfile

# pull the official docker image
FROM python:3.10.9

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /back

COPY requirements.txt requirements.txt

# install dependencies
RUN pip install -r requirements.txt