<p align="center">
  <img src="https://shields.io" alt="Version">
  <img src="https://shields.io" alt="Python">
  <img src="https://shields.io" alt="FastAPI">
  <img src="https://shields.io" alt="Docker">
  <img src="https://shields.io" alt="Bootstrap">
</p>

---

<p align="center">
  <ins><b><kbd>&nbsp;WEB APPLICATION&nbsp;</kbd></b></ins>
</p>

<h1 align="center" style="font-size: 2.5rem; font-weight: 900; color: #1a1a1a; margin-top: 10px; margin-bottom: 10px; border-bottom: none;">
  🎯 GEWOHNHEITS-TRACKER (HABIT TRACKER)
</h1>

<p align="center">
  <strong>Ein eleganter, performanter und responsiver Web-Tracker zur Verwaltung täglicher Routinen.</strong>
  <br />
  <i>Entwickelt mit Python, FastAPI und verpackt in ein modernes Premium-UI.</i>
</p>

<p align="center">
  <a href="#-deutsch">🇩🇪 Deutsch</a> • 
  <a href="#-english">🇺🇸 English</a>
</p>

---

## 🇩🇪 Deutsch

Die Anwendung bietet eine ansprechende HTML-Benutzeroberfläche und wird vollautomatisch in einer isolierten Docker-Umgebung ausgeführt.

### 🌐 Live Demo
⚠️ Hinweis: Da das Projekt auf einem kostenlosen Server gehostet wird, kann das Laden beim ersten Öffnen ca. 50 Sekunden dauern (Server-Wake-up-Zeit). Bitte haben Sie ein wenig Geduld.
Die Anwendung ist live auf Render verfügbar:  
👉 **[https://my-habit-tracker-ohs1.onrender.com](https://my-habit-tracker-ohs1.onrender.com)**

### 🚀 Funktionen
* **Interaktive Benutzeroberfläche**: Ein sauberes, modernes HTML-Interface (Bootstrap 5) zur Verwaltung deiner Gewohnheiten im Webbrowser.
* **Dynamische Verwaltung**: Neue Gewohnheiten können direkt über ein Formular hinzugefügt werden.
* **Streak-Zähler 🔥**: Mit einem Klick auf den Erledigt-Haken (`✓`) wird deine tägliche Erfolgsserie (Streak) in Echtzeit erhöht.
* **Automatische API-Dokumentation**: Integrierte interaktive Swagger UI Dokumentation zur Analyse der Routen.
* **Vollständige Dockerisierung**: Isolierte Laufzeitumgebung, die plattformunabhängig ohne lokale Python-Installationen startet.
* **Clean Code**: Strukturierte Architektur nach Clean-Code-Prinzipien mit durchgehender deutscher Dokumentation und Quellcode-Kommentierung.

### 🛠️ Technologien
* **Backend**: Python 3.11, FastAPI (Asynchrones Hochperformanz-Framework)
* **Frontend**: HTML5, Jinja2 Templates, Bootstrap 5 & Bootstrap Icons
* **Server**: Uvicorn (ASGI-Server)
* **Containerisierung**: Docker & Docker Compose

### 📂 Struktur der Anwendung & Endpunkte
Der Webserver stellt folgende funktionale Einstiegspunkte bereit:
* **`GET /` (Hauptseite)**: Das visuelle Kontrollzentrum mit der Übersicht aller Gewohnheiten und dem Formular.
* **`GET /gewohnheiten`**: Liefert die rohen Daten aller Aktivitäten im standardisierten JSON-Format.
* **`POST /add`**: Endpunkt zur Verarbeitung und Speicherung neu angelegter Gewohnheiten.
* **`POST /check/{habit_id}`**: Erhöht die Erfolgsserie (Streak) einer spezifischen Gewohnheit um einen Tag.
* **`GET /docs`**: Die interaktive Swagger-UI-Testumgebung für Entwickler.

### 📦 Installation & Ausführung

#### Option 1: Starten über Docker (Empfohlen)
Es wird lediglich eine installierte Docker-Umgebung benötigt:
1. Repository klonen:
   ```bash
   git clone https://github.com/KristinaAlokhina/my_habit_tracker
   ```
2. In den Projektordner wechseln:
   ```bash
   cd my_habit_tracker
   ```
3. Docker-Image bauen:
   ```bash
   docker build -t gewohnheits-tracker .
   ```
4. Container starten:
   ```bash
   docker run -p 8000:8000 gewohnheits-tracker
   ```
Die Anwendung ist danach lokal unter **[http://localhost:8000](http://localhost:8000)** erreichbar.

---

## 🇺🇸 English

A modern, lightweight, and interactive web application to track your daily routines built with **Python** and **FastAPI**. It includes a beautiful HTML user interface and deploys automatically within an isolated Docker container.

### 🌐 Live Demo
⚠️ Note: Since the project is hosted on a free tier instance, the initial loading may take about 50 seconds (server spin-up time). Please wait a moment.
The application is live on Render:  
👉 **[https://my-habit-tracker-ohs1.onrender.com](https://my-habit-tracker-ohs1.onrender.com)**

### 🚀 Features
* **Interactive UI**: A clean and modern responsive web interface (Bootstrap 5) for managing daily routines directly inside the browser.
* **Dynamic Content Creation**: Add new habits instantly through a simple and clear form field.
* **Streak Tracker 🔥**: Click the complete button (`✓`) to boost your daily active streak instantly in real-time.
* **Automated Documentation**: Native integration with Swagger UI, allowing direct interactive endpoint testing.
* **Full Containerization**: Completely isolated and platform-independent Docker environment requiring no local host setups.
* **Clean Code Architecture**: High-quality codebase strictly adhering to clean design principles and detailed code documentation.

### 🛠️ Technologies
* **Backend**: Python 3.11, FastAPI (High-performance asynchronous framework)
* **Frontend**: HTML5, Jinja2 Template Engine, Bootstrap 5 & Bootstrap Icons
* **Server**: Uvicorn (ASGI server implementation)
* **Containerization**: Docker

### 📂 Application & Endpoint Structure
The running web service exposes the following functional access points:
* **`GET /` (Root Endpoint)**: Serves the visual frontend dashboard displaying active habits and forms.
* **`GET /gewohnheiten`**: Delivers raw data of all activities formatted in standardized JSON.
* **`POST /add`**: Endpoint handling safe submittal and validation of incoming user habits.
* **`POST /check/{habit_id}`**: Route increments active streaks of selected records by 1 unit.
* **`GET /docs`**: An interactive Swagger control panel for backend service analysis.

### 📦 Installation & Setup

#### Option 1: Run with Docker (Recommended)
Only a local Docker installation is required to deploy this service:
1. Clone the repository:
   ```bash
   git clone https://github.com/KristinaAlokhina/my_habit_tracker
   ```
2. Navigate to the project directory:
   ```bash
   cd my_habit_tracker
   ```
3. Build the Docker image:
   ```bash
   docker build -t gewohnheits-tracker .
   ```
4. Launch the container:
   ```bash
   docker run -p 8000:8000 gewohnheits-tracker
   ```
The application will be live at **[http://localhost:8000](http://localhost:8000)**.

---
<p align="center">
  Proudly developed by <a href="https://github.com/KristinaAlokhina">KristinaAlokhina</a> • © 2026
</p>
