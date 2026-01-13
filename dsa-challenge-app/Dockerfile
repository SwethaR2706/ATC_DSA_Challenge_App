# Use specific Debian Bookworm image for stability
FROM python:3.11-bookworm

# Install default Java (usually OpenJDK 17 on Bookworm)
RUN apt-get update --fix-missing && \
    apt-get install -y default-jdk-headless && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME (Default location for Debian)
ENV JAVA_HOME /usr/lib/jvm/default-java

# Set work directory
WORKDIR /app

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000", "--timeout", "120"]
