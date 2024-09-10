FROM python:3.9-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
COPY data/training/model.keras /app/data/training/model.keras

RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python3", "app.py"]
#for aws