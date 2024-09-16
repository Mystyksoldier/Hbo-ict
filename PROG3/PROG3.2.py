age = int(input("geef je leeftijd: "))
pasport = input("heb je een paspoort?: ")

if age >= 18 and pasport == "ja":
  print("Gefeliciteerd je mag stemmen!!")
else:
  print("Je mag niet stemmen :( ")
