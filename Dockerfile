FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir gpt4all flask flask-cors
COPY script.py /app/script.py
CMD ["python", "script.py"]
