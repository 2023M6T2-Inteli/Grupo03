FROM osrf/ros:humble-desktop

WORKDIR /backend

COPY . .

RUN apt-get update && apt-get install -y python3-pip

RUN pip install -r requirements.txt

EXPOSE 8000