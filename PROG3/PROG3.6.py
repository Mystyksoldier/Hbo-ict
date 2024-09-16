s = "Guido van Rossum heeft programmeertaal Python bedacht."

filter_letters = "aeiou"

for letter in s:
  if letter in filter_letters:
    print(letter)