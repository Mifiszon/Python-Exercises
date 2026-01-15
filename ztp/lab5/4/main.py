from analiza.csvtools import csvt
from analiza.statystyka import stat

dane = csvt("../2/osoby.csv")
srednia, mediana = stat(dane, "Wiek")

print(f"Średnia wieku: {srednia}")
print(f"Mediana wieku: {mediana}")
