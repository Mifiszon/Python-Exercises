def pisz(path):
    tekst = input("Podaj tekst do zapisania:\n> ")
    with open(path, "w", encoding="utf-8") as file:
        file.write(tekst)
    print("Zapisano do pliku")
