import math

x1 = input("wat is het eerste cijfer van coördinaat x? ")
x2 = input("wat is het tweede cijfer van coördinaat x? ")
y1 = input("wat is het eerste cijfer van coördinaat y? ")
y2 = input("wat is het tweede cijfer van coördinaat y? ")

result = math.sqrt((float(x1) - float(x2)) ** 2 + (float(y1) - float(y2)) ** 2) ** 0.5

print(f"Afstand tussen ({x1},{x2}) en ({y1},{y2}): {result}")