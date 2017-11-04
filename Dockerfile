FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip install -r requirements.txt

WORKDIR /code/
