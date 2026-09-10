from fastapi import FastAPI

app = FastAPI(title="Gewohnheits-Tracker API")

# Temporäre Datenbank im Arbeitsspeicher (In-Memory-Datenbank)
gewohnheiten = [
    {"id": 1, "name": "1 Stunde programmieren", "streak": 5},
    {"id": 2, "name": "Deutsche Vokabeln lernen", "streak": 12},
    {"id": 3, "name": "Sport treiben", "streak": 3}
]

@app.get("/")
def startseite():
    """Gibt eine Willkommensnachricht für die API zurück."""
    return {"nachricht": "Willkommen beim Gewohnheits-Tracker API!"}

@app.get("/gewohnheiten")
def alle_gewohnheiten_anzeigen():
    """Gibt die Liste aller aktuellen Gewohnheiten zurück."""
    return {"gewohnheiten": gewohnheiten}
