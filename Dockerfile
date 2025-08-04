FROM python:3.11-slim
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN ls -l /app  # optional: DEBUG verify files

EXPOSE 5000
CMD ["python", "app.py"]
