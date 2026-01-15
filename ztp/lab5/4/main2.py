from analiza.csvtools import csvt
from analiza.raport import raport

dane = csvt("../2/osoby.csv")

raport(dane, "Wiek")