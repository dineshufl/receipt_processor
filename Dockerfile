FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 5000 to allow access to the Flask app
EXPOSE 5000

# Define the environment variable for Flask to disable buffered output
ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]