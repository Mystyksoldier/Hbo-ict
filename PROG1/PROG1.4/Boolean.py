import statistics

a = int(6)
b = int(7)
c = statistics.mean([a, b])

voornaam = str("Dave")
tussenvoegsel = str("")
achternaam = str("Havelaar")

mijnnaam = voornaam + " " + tussenvoegsel + " " + achternaam

numberMijnnaam = len(mijnnaam)

if (c > a and c > b):
  print(True)
else:
  print(False)

if numberMijnnaam == numberMijnnaam:
  print(True)
else:
  print(False)

if numberMijnnaam / c >= 5:
  print(True)
else:
  print(False)

if len(tussenvoegsel) == 0:
  print(False)
elif tussenvoegsel in achternaam:
  print(True)
else:
  print(False)
