FROM ubuntu:22.04

WORKDIR /backend

COPY /backend .

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt