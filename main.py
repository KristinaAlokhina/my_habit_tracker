from datetime import date, datetime
import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

# Initialisierung der FastAPI-App mit einem deutschen Titel
app = FastAPI(title="Gewohnheits-Tracker API")

current_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(current_dir, "templates")

if not os.path.exists(templates_dir):
  templates_dir = "templates"

templates = Jinja2Templates(directory=templates_dir)

# Erweitere die Datenstruktur um ein Datum (last_completed),
# damit wir prüfen können, ob ein Tag verpasst wurde.
gewohnheiten = [
    {
        "id": 1,
        "name": "1 Stunde programmieren",
        "streak": 5,
        "last_completed": str(date.today()),
    },
    {
        "id": 2,
        "name": "Deutsche Vokabeln lernen",
        "streak": 12,
        "last_completed": str(date.today()),
    },
    {
        "id": 3,
        "name": "Sport treiben",
        "streak": 3,
        "last_completed": str(date.today()),
    },
]


@app.get("/", response_class=HTMLResponse)
def startseite(request: Request):
  """Zeigt die HTML-Startseite an und übergibt die aktuelle Liste der Gewohnheiten."""
  return templates.TemplateResponse(
      "index.html", {"request": request, "gewohnheiten": gewohnheiten}
  )


@app.get("/gewohnheiten")
def alle_gewohnheiten_anzeigen():
  """Gibt die Liste aller Gewohnheiten im JSON-Format für die API zurück."""
  return {"gewohnheiten": gewohnheiten}


@app.post("/add")
def neue_gewohnheit_hinzufuegen(name: str = Form(...)):
  """Nimmt eine neue Gewohnheit entgegen.

  Verwendet einen sicheren ID-Generator, falls Einträge gelöscht wurden.
  """
  new_id = max([h["id"] for h in gewohnheiten], default=0) + 1
  gewohnheiten.append({
      "id": new_id,
      "name": name,
      "streak": 0,
      "last_completed": None,
  })
  return RedirectResponse(url="/", status_code=303)


@app.post("/check/{habit_id}")
def gewohnheit_erledigen(habit_id: int):
  """Prüft das Datum:

  - Wenn heute schon erledigt: Ignorieren oder Streak halten.
  - Wenn gestern erledigt: Streak um 1 erhöhen.
  - Wenn länger als 1 Tag her (verpasst): Streak bricht ab und wird auf 1 zurückgesetzt.
  """
  heute = date.today()

  for habit in gewohnheiten:
    if habit["id"] == habit_id:
      letztes_datum_str = habit.get("last_completed")

      if not letztes_datum_str:
        # Noch nie gemacht -> Startet bei Streak 1
        habit["streak"] = 1
      else:
        letztes_datum = datetime.strptime(
            letztes_datum_str, "%Y-%m-%d"
        ).date()
        differenz = (heute - letztes_datum).days

        if differenz == 0:
          # Heute wurde es schon erledigt, evtl. nichts tun oder so lassen
          pass
        elif differenz == 1:
          # Gestern gemacht -> Streak erfolgreich fortgeführt!
          habit["streak"] += 1
        else:
          # Mehr als 1 Tag verpasst -> Streak wird zurückgesetzt (fängt wieder bei 1 an)
          habit["streak"] = 1

      # Datum auf heute aktualisieren
      habit["last_completed"] = str(heute)
      break

  return RedirectResponse(url="/", status_code=303)
    
