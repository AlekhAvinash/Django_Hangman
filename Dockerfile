FROM python:3.9-slim-buster

ENV HOME=/home/app/webapp
RUN mkdir -p $HOME

WORKDIR $HOME
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY . $DockerHOME  
RUN pip install -r requirements.txt
EXPOSE 8000