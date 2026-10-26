FROM python:3.11-slim

# Rendszerfüggőségek (ffmpeg az MP3 konverzióhoz)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Munkamappa
WORKDIR /app

# Python függőségek telepítése a requirements.txt alapján
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Forráskód másolása
COPY . .

EXPOSE 5000

CMD ["python", "src/app.py"]
