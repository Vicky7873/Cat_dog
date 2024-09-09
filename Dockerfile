FROM python:3.10-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]# Use the official Python image as a base image
FROM python:3.10-slim-buster

# Install system dependencies required for building Python packages and h5py
RUN apt update -y && \
    apt install -y awscli \
    pkg-config \
    build-essential \
    libhdf5-dev \
    libhdf5-serial-dev \
    libblas-dev \
    liblapack-dev \
    gfortran \
    python3-dev \
    && apt clean

# Set the working directory inside the container
WORKDIR /app

# Copy the entire app directory to the working directory
COPY . /app

# Install Python dependencies from the requirements.txt file
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Command to run the Flask app
CMD ["python3", "app.py"]
# for aws