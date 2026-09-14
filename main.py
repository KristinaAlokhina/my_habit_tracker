import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# Initialisierung der FastAPI-App mit einem deutschen Titel
app = FastAPI(title="Gewohnheits-Tracker API")



current_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(current_dir, "templates")


if not os.path.exists(templates_dir):
    templates_dir = "templates"

templates = Jinja2Templates(directory=templates_dir)


# Temporäre In-Memory-Datenbank für die Gewohnheiten
gewohnheiten = [
    {"id": 1, "name": "1 Stunde programmieren", "streak": 5},
    {"id": 2, "name": "Deutsche Vokabeln lernen", "streak": 12},
    {"id": 3, "name": "Sport treiben", "streak": 3}
]

@app.get("/", response_class=HTMLResponse)
def startseite(request: Request):
    """Zeigt die HTML-Startseite an und übergibt die aktuelle Liste der Gewohnheiten."""
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "gewohnheiten": gewohnheiten}
    )

@app.get("/gewohnheiten")
def alle_gewohnheiten_anzeigen():
    """Gibt die Liste aller Gewohnheiten im JSON-Format für die API zurück."""
    return {"gewohnheiten": gewohnheiten}

@app.post("/add")
def neue_gewohnheit_hinzufuegen(name: str = Form(...)):
    """Nimmt eine neue Gewohnheit aus dem Formular entgegen und speichert sie mit Streak 0."""
    neue_id = len(gewohnheiten) + 1
    gewohnheiten.append({"id": neue_id, "name": name, "streak": 0})
    # Leitet den Benutzer nach dem Hinzufügen zurück zur Startseite weiter
    return RedirectResponse(url="/", status_code=303)

@app.post("/check/{habit_id}")
def gewohnheit_erledigen(habit_id: int):
    """Sucht die Gewohnheit nach ID und erhöht den aktuellen Streak um 1 Tag."""
    for habit in gewohnheiten:
        if habit["id"] == habit_id:
            habit["streak"] += 1
            break
    # Aktualisiert die Startseite, um den neuen Streak direkt anzuzeigen
    return RedirectResponse(url="/", status_code=303)
