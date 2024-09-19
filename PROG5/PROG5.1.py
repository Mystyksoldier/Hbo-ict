import statistics

x = input("schrijf een zin: ")

def gemiddelde(x):
    number_list = []
    y = x.split()
    for word in y:
        number_list.append(len(word))

    result = float(statistics.mean(number_list))
    return (f"De gemiddelde lengte van de woorden in de zin is: {result}")

print(gemiddelde(x))