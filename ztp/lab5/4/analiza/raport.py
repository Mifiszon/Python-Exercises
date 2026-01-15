from .statystyka import stat

def raport(data, coll, filename="raport.txt"):
    srednia, mediana = stat(data, coll)

    tekst = (
            f"=== RAPORT ANALIZY DANYCH ===\n"
            f"Średnia: {srednia}\n"
            f"Mediana: {mediana}\n"
        )
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(tekst)

    print("Raport zapisano do pliku:", filename)