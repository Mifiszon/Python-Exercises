def czytaj(path):
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
        print("\nZawartość pliku:")
        print(data)