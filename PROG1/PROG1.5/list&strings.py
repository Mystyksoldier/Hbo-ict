favorieten = ['The Last Dinner Party']

vraag = input("wil je een artiest toevoegen aan je favorieten? ")

if vraag == "ja":
    newFavoriet = input("welke artiest wil je toevoegen? ")
    favorieten.append(newFavoriet)
    print("uw huidige favorieten zijn: ", favorieten)
elif vraag == "nee":
    print("oke uw huidige favorieten zijn: ", favorieten)
else:
    print("dat is geen geldig antwoord")

vraag2 = input("wilt u de tweede artiest uit uw favorieten aanpassen? ")
if vraag2 == "ja":
    favorieten[1] = input("wat is de nieuwe artiest? ")
    print("uw huidige favorieten zijn: ", favorieten)
elif vraag2 == "nee":
    print("oke uw huidige favorieten zijn: ", favorieten)
else:
    print("dat is geen geldig antwoord")