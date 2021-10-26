FROM python:rc-alpine3.13
USER root

RUN apk update
RUN apk --update add vim
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
COPY ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
EXPOSE 5000