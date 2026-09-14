from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Gewohnheits-Tracker API")

# Hier sagen wir FastAPI, wo unsere HTML-Dateien liegen
templates = Jinja2Templates(directory="templates")

# Temporäre Datenbank im Arbeitsspeicher (In-Memory-Datenbank)
gewohnheiten = [
    {"id": 1, "name": "1 Stunde programmieren", "streak": 5},
    {"id": 2, "name": "Deutsche Vokabeln lernen", "streak": 12},
    {"id": 3, "name": "Sport treiben", "streak": 3}
]

@app.get("/", response_class=HTMLResponse)
def startseite(request: Request):
    """Zeigt die schöne HTML-Startseite an und übergibt die Gewohnheiten."""
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "gewohnheiten": gewohnheiten}
    )

@app.get("/gewohnheiten")
def alle_gewohnheiten_anzeigen():
    """Gibt die Liste aller aktuellen Gewohnheiten als JSON zurück (für die API)."""
    return {"gewohnheiten": gewohnheiten}
