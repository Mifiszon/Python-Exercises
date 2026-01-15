"""
Moduł matematyka.py
Zawiera funkcje arytmetyczne: srednia, wariancja.
Autor: Michał Ogiba
"""
import math

def srednia(lista_liczb):
    """Zwraca średnią arytemtyczną dowolnej listy liczb."""
    num = 0
    counter = 0
    for liczba in lista_liczb:
        num += liczba
        counter += 1
    avg = num/counter
    return avg

def wariancja(lista_liczb):
    """Zwraca wariancję dowolnej listy liczb."""
    num = 0
    counter = 0
    w = 0
    for liczba in lista_liczb:
        num += liczba
        counter += 1
    avg = num/counter
    for l in lista_liczb:
        w += (l - avg) * (l - avg)
    wariancja = w/counter
    return wariancja