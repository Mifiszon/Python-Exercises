import json
from pathlib import Path

FILE = Path(__file__).parent.parent / "data" / "notatki.json"

def read_notes():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open(FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=2)