FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD ./src/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y gettext

ADD ./docker/backend/wsgi-entrypoint.sh /

ADD ./src .
RUN ["chmod", "+x", "/wsgi-entrypoint.sh"]
EXPOSE 8000