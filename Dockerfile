# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies required for numpy/scipy/scikit-learn
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    gfortran \
    libatlas-base-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip, setuptools, wheel (important for numpy 2.x & sklearn 1.6.x)
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements.txt first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project (Flask app, templates, model files)
COPY . .

# Expose Render's port
EXPOSE 10000

# Run the Flask app with Gunicorn (production server)
# app:app means -> app.py file, app variable inside it
CMD ["gunicorn", "-b", "0.0.0.0:10000", "app:app"]
