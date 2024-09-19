afstandKM = 70
leeftijd = 11
weekendrit = False

def standaardprijs(afstandKM):
    if afstandKM < 0:
        de_ritprijs = 0
    elif afstandKM <= 50:
        de_ritprijs = afstandKM * 0.80
    elif afstandKM >= 50:
        de_ritprijs = 15 + (afstandKM) * 0.60

    return de_ritprijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs_waarde = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd >= 65:
        if weekendrit:
            return standaardprijs_waarde * 0.65
        else:
            return standaardprijs_waarde * 0.70
    else:
        if weekendrit:
            return standaardprijs_waarde * 0.60
        else:
            return standaardprijs_waarde
        
print(ritprijs(leeftijd, weekendrit, afstandKM))