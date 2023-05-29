FROM osrf/ros:humble-desktop

WORKDIR /backend

COPY . .

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --no-cache-dir --upgrade -r requirements.txt
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
