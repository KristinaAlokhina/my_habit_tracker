# 1. Basis-Image mit der offiziellen Python-Version definieren
FROM python:3.11-slim

# 2. Arbeitsverzeichnis innerhalb des Containers erstellen
WORKDIR /app

# 3. Die Liste der Abhängigkeiten in den Container kopieren
COPY requirements.txt .

# 4. Notwendige Python-Bibliotheken im Container installieren
RUN pip install --no-cache-dir -r requirements.txt

# 5. Den Quellcode (main.py) in den Container kopieren
COPY main.py .

# 6. Befehl zum Starten des Servers beim Container-Start festlegen
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

