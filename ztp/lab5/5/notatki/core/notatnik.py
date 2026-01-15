from .pliki import read_notes, save_notes

def add(data):
    notes = read_notes()
    notes.append(data)
    save_notes(notes)

def show():
    notes = read_notes()
    for i, n in enumerate(notes, start=1):
        print(f"{i}. {n}")

def delete(num):
    notes = read_notes()
    notes.pop(num - 1)
    save_notes(notes)
    print("Usunięto notatkę.")