FROM python:3.11-alpine

WORKDIR /home/app

RUN pip3 install gpiozero

