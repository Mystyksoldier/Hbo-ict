list = [4, 3, -5]

def kwadraten_som(grondgetallen):
    kwadraten = []
    for getal in grondgetallen:
        if getal > 0:
            kwadraten.append(getal ** 2)

    return sum(kwadraten)

print(kwadraten_som(list))
