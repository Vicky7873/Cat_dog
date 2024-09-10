FROM python:3.9-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
COPY data/training/model.keras /app/data/training/model.keras
EXPOSE 8080
CMD ["python3", "app.py"]
#for aws