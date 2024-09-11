import random

PrijsProduct = random.randint(10, 150)

print("het bedrag is " + str(PrijsProduct) + " eurocent")

cent1 = 0
cent2 = 0
cent5 = 0
cent10 = 0
cent20 = 0
cent50 = 0

x = int(input("hoeveel geld gooi je in de automaat in eurocent?: "))

if x < PrijsProduct:
    print("u heeft te weinig geld in de automaat gegooid")
else:
    wisselGeld = x - PrijsProduct

    while wisselGeld >= 50:
        wisselGeld -= 50
        cent50 += 1
    while wisselGeld >= 20:
        wisselGeld -= 20
        cent20 += 1
    while wisselGeld >= 10:
        wisselGeld -= 10
        cent10 += 1
    while wisselGeld >= 5:
        wisselGeld -= 5
        cent5 += 1
    while wisselGeld >= 2:
        wisselGeld -= 2
        cent2 += 1
    while wisselGeld >= 1:
        wisselGeld -= 1
        cent1 += 1

    print("aantal munten van 50 eurocent is " + str(cent50))
    print("aantal munten van 20 eurocent is " + str(cent20))
    print("aantal munten van 5 eurocent is " + str(cent5))
    print("aantal munten van 2 eurocent is " + str(cent2))
    print("aantal munten van 1 eurocent is " + str(cent1))





