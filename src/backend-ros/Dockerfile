FROM osrf/ros:humble-desktop

WORKDIR /backend-ros

COPY /backend-ros .

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt