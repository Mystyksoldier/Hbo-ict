montNumber = int(input("geef het nummer van de maand(tussen 1 en 12): "))

monthsDutch = ["januari", "februari",  "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]

if montNumber >= 1 and montNumber <= 12:
  if montNumber >= 3 and montNumber <= 5:
    print("lente")
  elif montNumber >= 6 and montNumber <= 8:
    print("zomer")
  elif montNumber >= 9 and monthsDutch <= 11:
    print("herfst")
  else:
    print("winter")
else:
  print(f"{montNumber} is geen maand nummer!")