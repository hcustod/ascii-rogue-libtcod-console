FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y \
    libgl1 \
    libxcursor1 \
    libxrandr2 \
    libxinerama1 \
    libxi6 \
    libxcomposite1 \
    libasound2 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libx11-6 \
    libxrender1 \
    libxss1 \
    libxtst6 \
    libwayland-cursor0 \
    libwayland-egl1 \
    libwayland-client0 \
    libwayland-server0 \
    libegl1 \
    libgles2 \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
