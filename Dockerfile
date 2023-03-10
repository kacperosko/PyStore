FROM python:3.10

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# copy project
COPY . /app/