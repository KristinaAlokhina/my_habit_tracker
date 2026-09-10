# Gewohnheits-Tracker API (Habit Tracker REST-API)

<p align="center">
  <a href="#-deutsch">Deutsch</a> • 
  <a href="#-english">English</a>
</p>

---

## 🇩🇪 Deutsch

### 🚀 Funktionen
* **Strukturierte Datenausgabe**: Vollständige Bereitstellung aller Gewohnheiten und aktuellen Streaks (Erfolgsserien) im standardisierten JSON-Format.
* **Automatische Dokumentation**: Integrierte, interaktive Swagger UI Dokumentation, die ein direktes Testen der API-Endpunkte im Browser ermöglicht.
* **Vollständige Dockerisierung**: Isolierte und plattformunabhängige Laufzeitumgebung, die ohne lokale Python- oder Bibliotheks-Installationen auskommt.
* **Clean Code & Lokalisierung**: Konsistente Umsetzung von Clean-Code-Prinzipien mit durchgehend deutscher Benennung, Struktur und Quellcode-Kommentierung.

### 🛠️ Technologien
* Python 3.11
* Web-Framework: **FastAPI** (modernes, hochperformantes asynchrones Framework)
* Server: **Uvicorn** (ASGI-Server-Implementierung)
* Containerisierung: **Docker**

### 📂 Struktur der Benutzeroberfläche / API
Die Anwendung läuft als Hintergrunddienst (Webserver) и bietet folgende Einstiegspunkte:
* **Hauptseite**: `GET /` — Gibt eine standardisierte Willkommensnachricht zurück.
* **Gewohnheiten-Übersicht**: `GET /gewohnheiten` — Liefert eine dynamische Liste aller getrackten Aktivitäten inklusive IDs und Streaks.
* **Swagger-Interface**: `GET /docs` — Das interaktive Kontrollzentrum zur Analyse der API.

### 📦 Installation & Ausführung

#### Option 1: Starten über Docker (Empfohlen)
Für die Ausführung wird lediglich eine installierte Docker-Umgebung benötigt:
1. Repository klonen:
   ```bash
   git clone https://github.com/KristinaAlokhina/my_habit_tracker
   ```
2. In den Projektordner wechseln:
   ```bash
   cd gewohnheits-tracker
   ```
3. Docker-Image bauen:
   ```bash
   docker build -t gewohnheits-tracker .
   ```
4. Container starten:
   ```bash
   docker run -p 8000:8000 gewohnheits-tracker
   ```
Die Anwendung ist danach unter `[http://localhost:8000/gewohnheiten](https://my-habit-tracker-ohs1.onrender.com/docs)` erreichbar.

---

## 🇺🇸 English

### 🚀 Features
* **Structured Data Output**: Complete delivery of all daily habits and active streaks formatted in standardized JSON.
* **Automated Documentation**: Native integration with Swagger UI, allowing direct interaction and testing of all endpoints from the browser.
* **Full Containerization**: Completely isolated and platform-independent Docker environment, requiring no local Python setups on the host machine.
* **Clean Code Architecture**: High-quality codebase strictly adhering to naming standards, structured routing, and detailed code documentation.

### 🛠️ Technologies
* Python 3.11
* Web Framework: **FastAPI** (modern, high-performance asynchronous framework)
* Server: **Uvicorn** (ASGI server)
* Containerization: **Docker**

### 📂 API & Endpoint Structure
The application runs as a web service and exposes the following functional access points:
* **Root Endpoint**: `GET /` — Returns a standardized API welcome message.
* **Habits Overview**: `GET /gewohnheiten` — Serves a dynamic list of tracked activities containing individual item IDs and streak records.
* **Swagger Interface**: `GET /docs` — An interactive control panel for visual exploration and live testing of the backend service.

### 📦 Installation & Setup

#### Option 1: Run with Docker (Recommended)
Only a local Docker installation is required to deploy this application:
1. Clone the repository:
   ```bash
   git clone https://github.com/KristinaAlokhina/my_habit_tracker
   ```
2. Navigate to the project directory:
   ```bash
   cd gewohnheits-tracker
   ```
3. Build the Docker image:
   ```bash
   docker build -t gewohnheits-tracker .
   ```
4. Launch the container:
   ```bash
   docker run -p 8000:8000 gewohnheits-tracker
   ```
The application will be live at `[http://localhost:8000/gewohnheiten](https://my-habit-tracker-ohs1.onrender.com/docs)`."# my_habit_tracker" 
