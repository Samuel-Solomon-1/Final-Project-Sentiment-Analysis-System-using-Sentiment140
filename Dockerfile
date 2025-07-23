# Use a minimal Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files into the container
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY api/ ./api/
COPY model/ ./model/

# Set the working directory to api/
WORKDIR /app/api

# Expose port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]