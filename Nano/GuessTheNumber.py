import random

TheNumber = random.randint(1, 100)

coupons = 5

print(TheNumber)

for coupon in range(1, coupons + 1):
  TheGuess = input("Raad het cijder tussen de 1 en de 100?: ")
  print(TheNumber)
  if TheNumber == int(TheGuess):
    print("hoera je hebt nummer " + str(TheNumber) + " geraden.")
    break
  else:
    print("je hebt het fout probeer het opnieuw. :(")

if coupon == coupons and TheGuess != TheNumber:
  print("je hebt het spel verloren take the L")