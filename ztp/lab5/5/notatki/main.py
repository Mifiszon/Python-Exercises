from core.notatnik import add, show, delete

def menu():
    while True:
        print("\n=== NOTATNIK ===")
        print("1. Dodaj notatkę")
        print("2. Pokaż notatki")
        print("3. Usuń notatkę")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            data = input("Wpisz treść notatki: ")
            add(data)
        elif choice == "2":
            show()
        elif choice == "3":
            try:
                num = int(input("Numer notatki do usunięcia: "))
                delete(num)
            except ValueError:
                print("Podaj liczbę!")
        elif choice == "0":
            break
        else:
            print("Niepoprawna opcja!")

if __name__ == "__main__":
    menu()
