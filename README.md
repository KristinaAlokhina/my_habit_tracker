

<p align="center">
  <ins><b><kbd>&nbsp;WEB APPLICATION&nbsp;</kbd></b></ins>
</p>

<h1 align="center" style="font-size: 2.5rem; font-weight: 900; color: #1a1a1a; margin-top: 10px; margin-bottom: 10px; border-bottom: none;">
  🎯 GEWOHNHEITS-TRACKER (HABIT TRACKER)
</h1>

<p align="center">
  <strong>Ein eleganter, performanter und responsiver Web-Tracker zur Verwaltung täglicher Routinen.</strong>
  <br />
  <i>Entwickelt mit Python, FastAPI und verpackt in ein modernes, interaktives Premium-UI.</i>
</p>

<p align="center">
  <a href="#-deutsch">🇩🇪 Deutsch</a> • 
  <a href="#-english">🇺🇸 English</a>
</p>

---

## 🇩🇪 Deutsch

Die Anwendung bietet eine moderne, vollständig interaktive Benutzeroberfläche und wird in einer isolierten Docker-Umgebung ausgeführt.

### 🌐 Live Demo
⚠️ Hinweis: Da das Projekt auf einem kostenlosen Server gehostet wird, kann das Laden beim ersten Öffnen ca. 50 Sekunden dauern (Server-Wake-up-Zeit). Bitte haben Sie ein wenig Geduld.
Die Anwendung ist live auf Render verfügbar:  
👉 **[https://my-habit-tracker-ohs1.onrender.com](https://my-habit-tracker-ohs1.onrender.com)**

### 🚀 Funktionen
* **Modernes Card-Design (UI/UX)**: Jede Gewohnheit wird in einer eleganten, übersichtlichen Karte mit Schatteneffekten dargestellt, was die Lesbarkeit maximiert.
* **Interaktiver Streak-Zähler 🔥**: Ein Klick auf die Checkbox erhöht deine tägliche Erfolgsserie (Streak) automatisch in Echtzeit und färbt die Karte grün. Beim Abwählen sinkt der Zähler wieder.
* **Lokale Datenspeicherung**: Durch die Integration von `LocalStorage` bleiben deine eingetragenen Gewohnheiten und Fortschritte auch nach dem Schließen des Browsers oder Neuladen der Seite dauerhaft erhalten.
* **Dynamisches Löschen**: Jede Gewohnheit besitzt nun einen Lösch-Button (`×`), um Einträge flexibel zu entfernen.
* **Automatische API-Dokumentation**: Integrierte interaktive Swagger UI Dokumentation zur Analyse der Routen.
* **Vollständige Dockerisierung**: Isolierte Laufzeitumgebung, die plattformunabhängig startet.

### 🛠️ Technologien
* **Backend**: Python 3.11, FastAPI (Asynchrones Hochperformanz-Framework)
* **Frontend**: HTML5, Jinja2 Templates, Modernes CSS3 (Custom Properties & Flexbox), Vanilla JavaScript (DOM-Manipulation & LocalStorage)
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

A modern, lightweight, and fully interactive web application to track your daily routines built with **Python**, **FastAPI**, and enhanced **Vanilla JavaScript**.

### 🌐 Live Demo
⚠️ Note: Since the project is hosted on a free tier instance, the initial loading may take about 50 seconds (server spin-up time). Please wait a moment.
The application is live on Render:  
👉 **[https://my-habit-tracker-ohs1.onrender.com](https://my-habit-tracker-ohs1.onrender.com)**

### 🚀 Features
* **Modern Card Layout (UI/UX)**: Clean, component-based card design utilizing modern CSS custom properties and box-shadows for a premium feel.
* **Interactive Streak Tracker 🔥**: Toggling the custom checkbox instantly updates your progress counter in real-time with smooth visual state transitions.
* **Persistent Local Storage**: Leverages the browser's `LocalStorage` API to ensure your personal habits and streaks are never lost upon page refresh.
* **Dynamic Deletion**: Easily remove habits on the fly using the built-in fast delete (`×`) action button.
* **Automated Documentation**: Native integration with Swagger UI, allowing direct interactive endpoint testing.
* **Full Containerization**: Completely isolated and platform-independent Docker environment.

### 🛠️ Technologies
* **Backend**: Python 3.11, FastAPI (High-performance asynchronous framework)
* **Frontend**: HTML5, Jinja2 Template Engine, Modern CSS3, Pure Vanilla JavaScript
* **Server**: Uvicorn (ASGI server implementation)
* **Containerisierung**: Docker

### 📂 Application & Endpoint Structure
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
