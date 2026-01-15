from .wejscie import read_file
from .statystyka import count_words, avg_word_length

def raport_gen(path):
    text = read_file(path)

    num = count_words(text)
    avg = avg_word_length(text)

    raport = (
        f"Analiza pliku: {path}\n"
        f"Liczba słów: {num}\n"
        f"Średnia długość słowa: {avg:.2f}\n"
    )

    print(raport)
    return raport
