def aantal_kluizen_vrij():
    with open('kluizen.txt', 'r') as file:
        in_use = len(file.readlines())
        totalLockersFree = 12 - in_use
        if totalLockersFree == 0:
            print("Er zijn geen kluizen meer vrij.")
            return -2
        else:
            return (f"Er zijn nog {totalLockersFree} kluizen vrij.")

def nieuwe_kluis():
    if aantal_kluizen_vrij() == 0:
        return -2
    else:
        with open('kluizen.txt', 'r') as file:
            in_use = file.readlines()

        lockers = []
        for locker in in_use:
            lockers.append(int(locker.split(";")[0]))
        for i in range(1, 13):
            if i not in lockers:
                lockerNumber = i
                break
        print(f"Je hebt kluisnummer {lockerNumber}.")
        code = input("Voer een code in: ")
        print(len(code))
        if len(code) > 4 or ";" in code:
            print("De code moet minimaal 4 tekens bevatten. en mag geen ; bevatten")
            return -1
        else:
            with open('kluizen.txt', 'a') as file:
                file.write(f"{lockerNumber};{code}\n")
            return lockerNumber
        
def kluis_openen():
    with open('kluizen.txt', 'r') as file:
        in_use = file.readlines()
    
    lockers = []
    for locker in in_use:
        split_values = locker.strip().split(";")
        lockers.append((split_values[0], split_values[1]))

    input_locker_number = input("welk kluis nummer heb je? ")
    
    found = False

    for locker in lockers:
        if locker[0] == input_locker_number:
            found = True
            break
    
    if not found:
        return (f"Kluis {input_locker_number} is niet in gebruik.")
    else:
        locker_code = input("Voer de code in: ")

    for locker in lockers:
        if locker[0] == input_locker_number and locker[1] == locker_code:
            if locker[1] == locker_code:
                True
            else:
                False

def kluis_teruggeven():
    with open('kluizen.txt', 'r') as file:
        in_use = file.readlines()
    lockers = []
    for locker in in_use:
        split_values = locker.strip().split(";")
        lockers.append((split_values[0], split_values[1]))
    input_locker_number = input("welk kluis nummer heb je? ")
    found = False
    for locker in lockers:
        if locker[0] == input_locker_number:
            found = True
            break
        
    if not found:
        return False
    else:
        locker_code = input("Voer de code in: ")
    combo_found = False
    for locker in lockers:
        if locker[0] == input_locker_number and locker[1] == locker_code:
            combo_found = True
            break
    if combo_found:
        with open('kluizen.txt', 'w') as file:
            for locker in lockers:
                if locker[0] != input_locker_number:
                    file.write(f"{locker[0]};{locker[1]}\n")
        return True

    
print(kluis_teruggeven())

