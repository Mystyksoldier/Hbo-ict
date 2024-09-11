import statistics

cijferPROJA = 7.5
cijferPROG = 7.5
cijferMOD = 7.5

totaaleCijferLijst = [cijferPROJA, cijferPROG, cijferMOD]

Test = len(totaaleCijferLijst)

avrage = statistics.mean(totaaleCijferLijst)

result = avrage * 30 * Test

print(result)

