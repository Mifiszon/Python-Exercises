import csv

def csvt(path):
    with open(path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        return list(reader)