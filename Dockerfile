# Alap image
FROM python:3.9-slim

# Dolgozói könyvtár
WORKDIR /app

# Függőségek másolása
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Flask kód másolása
COPY app.py app.py

# API futtatása
CMD ["python", "app.py"]

