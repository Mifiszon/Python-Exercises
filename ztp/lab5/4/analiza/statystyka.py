import statistics

def stat(data, coll):
    values = []

    for value in data:   
        try:
            values.append(int(value[coll]))
        except TypeError:
            continue
        
    avg = statistics.mean(values)
    mediana = statistics.median(values)

    return avg, mediana
        