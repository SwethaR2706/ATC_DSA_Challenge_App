# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install OpenJDK-17
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk-headless && \
    apt-get clean;

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

# Set work directory
WORKDIR /app

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
