# Use an official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY ALL FILES explicitly
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the Flask app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
