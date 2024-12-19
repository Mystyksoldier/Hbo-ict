#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Oriëntatie op AI

Final assignment: statistiek

(c) 2019 Hogeschool Utrecht,
Bart van Eijkelenburg
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Werk onderstaande functies uit. Elke functie krijgt een niet-lege en
ongesorteerde lijst *lst* met gehele getallen (int) als argument.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

# TODO: Vul hier je naam, klas en studentnummer in.
naam = "Dave Havelaar"
klas = "v1b"
studentnummer = 1882008


"""
1. Pseudocode derde kwartiel

Pseudocode:
SORTEREN lst IN OPELOPENDE VOLGORDE
SPLITS lst IN TWEE HELFTEN:
    RECHTERHELFT = ELEMENTEN NA DE MEDIAAN
BEREKEN MEDIAAN VAN RECHTERHELFT ALS Q3
GEEF Q3 TERUG
"""

"""
2. Pseudocode frequentie

Pseudocode:
INITIEER freqs ALS LEGE DICTIONARY
VOOR ELKE waarde IN lst:
    ALS waarde NIET IN freqs:
        STEL freqs[waarde] IN OP 0
    INCREMENTEER freqs[waarde] MET 1
GEEF freqs TERUG
"""

"""
3. Implementatie mean
"""
def mean(lst):
    """
    Bepaal het gemiddelde van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het gemiddelde van de gegeven getallen.
    """
    return sum(lst) / len(lst) if lst else 0

"""
4. Implementatie q1
"""
def q1(lst):
    """
    Bepaal het eerste kwartiel Q1 van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het eerste kwartiel Q1 van de gegeven getallen.
    """
    lst = sorted(lst)  # Sorteer de lijst
    n = len(lst)  # Lengte van de lijst
    half = n // 2  # Halverwege de lijst

    # Neem de onderste helft
    lower_half = lst[:half]

    # Bereken de mediaan van de onderste helft (Q1)
    m = len(lower_half)
    if m % 2 == 0:  # Even aantal elementen
        return float((lower_half[m // 2 - 1] + lower_half[m // 2]) / 2)
    else:  # Oneven aantal elementen
        return float(lower_half[m // 2])

"""
5. Implementatie q3
"""
def q3(lst):
    """
    Bepaal het derde kwartiel Q3 van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: Het derde kwartiel Q3 van de gegeven getallen.
    """
    lst = sorted(lst)  # Sorteer de lijst
    n = len(lst)  # Lengte van de lijst
    half = (n + 1) // 2  # Start van de bovenste helft

    # Neem de bovenste helft
    upper_half = lst[half:]

    # Bereken de mediaan van de bovenste helft (Q3)
    m = len(upper_half)
    if m % 2 == 0:  # Even aantal elementen
        return float((upper_half[m // 2 - 1] + upper_half[m // 2]) / 2)
    else:  # Oneven aantal elementen
        return float(upper_half[m // 2])


"""
6. Implementatie var
"""
def var(lst):
    """
    Bepaal de variantie van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De variantie van de gegeven getallen.
    """
    m = mean(lst)
    return sum((x - m) ** 2 for x in lst) / len(lst) if lst else 0

"""
7. Implementatie std
"""
def std(lst):
    """
    Bepaal de standaardafwijking van een lijst getallen.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        float: De standaardafwijking van de gegeven getallen.
    """
    return var(lst) ** 0.5

"""
8. Implementatie freq
"""
def freq(lst):
    """
    Bepaal de frequenties van alle getallen in een lijst.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        dict: Een dictionary met als 'key' de waardes die voorkomen in de lijst
            en als 'value' het aantal voorkomens (de frequentie) van die waarde.

    Examples:
        >> freq([0, 0, 4, 7, 7])
        {0: 2, 4: 1, 7: 2}

        >> freq([1, 1, 2, 3, 2, 1])
        {1: 3, 2: 2, 3: 1}
    """
    freqs = {}
    for value in lst:
        if value not in freqs:
            freqs[value] = 0
        freqs[value] += 1
    return freqs

"""
9. Implementatie modes
"""
def modes(lst):
    """
    Bepaal alle modi van een lijst getallen.

    Hint: maak gebruik van `freq()`.

    Args:
        lst (list): Een lijst met gehele getallen.

    Returns:
        list: Een gesorteerde lijst van de modi van de gegeven getallen.

    Examples:
        >> modes([0, 0, 4, 7, 7])
        [0, 7]

        >> modes([1, 1, 2, 3, 2, 1])
        [1]
    """
    freqs = freq(lst)
    max_freq = max(freqs.values())
    modi = [key for key, value in freqs.items() if value == max_freq]
    return sorted(modi)


"""
(Optioneel)
10. Implementatie rel_cum_freq
    Implementeer onderstaande functie om de relatieve cumulatieve frequenties van een lijst getallen te berekenen.
    
"""
def rel_cum_freq(lst):
    """
    Bepaal de relatieve cumulatieve frequenties van een lijst met meetpunten.

    Args:
        lst (list): Een (mogelijk ongesorteerde) lijst met meetpunten.

    Returns:
        dict: Een lijst met als 'key' de waardes die voorkomen in de lijst
         en als 'value' de cumulatieve relatieve frequentie van die waarde.

    Example:
        >> rel_cum_freq(['b', 'd', 'a', 'b'])
        {'a': 0.25, 'b': 0.75, 'd': 1.0}
    """
    rel_cum_freqs = dict()
    return rel_cum_freqs



"""
# XXX>
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import os
import sys

def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.
    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_mean():
    testcases = [
        (([4, 2, 5, 8, 6],), 5.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 3.0)
    ]

    for case in testcases:
        __my_assert_args(mean, case[0], case[1])


def test_mean_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(mean, (lst_test,), statistics.mean(lst_test), False)


def test_q1():
    testcases = [
        (([4, 2, 5, 8, 6],), 3.0),
        (([1, 3, 4, 6, 4, 2],), 2.0),
        (([1, 3, 5, 6, 1, 4, 2],), 1.0),
        (([5, 7, 4, 4, 6, 2, 8],), 4.0),
        (([0, 5, 5, 6, 7, 7, 12],), 5.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 1.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 7.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 5.0),
        (([0, 1, 2, 2, 2, 2, 3, 5, 5],), 1.5),

    ]

    for case in testcases:
        __my_assert_args(q1, case[0], case[1])


def test_q3():
    testcases = [
        (([4, 2, 5, 8, 6],), 7.0),
        (([1, 3, 4, 6, 4, 2],), 4.0),
        (([1, 3, 5, 6, 2, 4, 1],), 5.0),
        (([5, 7, 4, 4, 6, 2, 8],), 7.0),
        (([0, 5, 5, 6, 7, 7, 12],), 7.0),
        (([1, 4, 3, 5, 6, 2, 4, 1],), 4.5),
        (([3, 5, 7, 8, 9, 11, 15, 16, 20, 21],), 16.0),
        (([1, 2, 5, 6, 7, 9, 12, 15, 18, 19, 27],), 18.0),
        (([0, 1, 2, 2, 2, 2, 3, 5, 5],), 4.0),

    ]

    for case in testcases:
        __my_assert_args(q3, case[0], case[1])


def test_var():
    testcases = [
        (([4, 2, 5, 8, 6],), 4.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 2.25)
    ]

    for case in testcases:
        __my_assert_args(var, case[0], case[1])


def test_var_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(var, (lst_test,), statistics.pvariance(lst_test), False)


def test_std():
    testcases = [
        (([4, 2, 5, 8, 6],), 2.0),
        (([1, 3, 2, 4, 6, 2, 4, 2],), 1.5)
    ]

    for case in testcases:
        __my_assert_args(std, case[0], case[1])


def test_std_simulated():
    import random
    import statistics

    for lst_size in range(1, 11):
        lst_test = [random.choice(range(5)) for _ in range(lst_size)]
        __my_assert_args(std, (lst_test,), statistics.pstdev(lst_test), False)


def test_freq():
    testcases = [
        (([4, 2, 5, 8, 6],), {2: 1, 4: 1, 5: 1, 6: 1, 8: 1}),
        (([1, 3, 4, 6, 4, 2],), {1: 1, 2: 1, 3: 1, 4: 2, 6: 1}),
        (([1, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}),
        (([1, 4, 3, 5, 6, 2, 4, 1],), {1: 2, 2: 1, 3: 1, 4: 2, 5: 1, 6: 1})
    ]

    for case in testcases:
        __my_assert_args(freq, case[0], case[1])


def test_modes():
    testcases = [
        (([4, 2, 5, 8, 6],), [2, 4, 5, 6, 8]),
        (([1, 3, 4, 6, 4, 2],), [4]),
        (([1, 3, 4, 6, 2, 4, 2],), [2, 4]),
        (([1, 3, 2, 4, 6, 2, 4, 2],), [2])
    ]

    for case in testcases:
        __my_assert_args(modes, case[0], case[1])

def test_modes_simulated():
    if sys.version_info[0] >= 3 and sys.version_info[1] >= 8:
        import random
        import statistics
        for lst_size in range(1, 11):
            lst_test = [random.choice(range(5)) for _ in range(lst_size)]
            __my_assert_args(modes, (lst_test,), sorted(statistics.multimode(lst_test)))


def test_rel_cum_freq(): 
    testcases = [
        ((['a', 'b', 'c'],), {'a': 0.3333333333333333, 'b': 0.6666666666666666, 'c': 1.0} ),
        ((['b', 'd', 'a', 'b'],), {'a': 0.25, 'b': 0.75, 'd': 1.0} ),
        ((['a', 'a', 'b', 'a', 'a'],), {'a': 0.8, 'b': 1} ),
    ]

    for case in testcases:
        __my_assert_args(rel_cum_freq, case[0], case[1])

def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    os.system("")

    try:
        print("\x1b[32m")   # Groene tekstkleur
        test_id()

        test_mean()
        test_mean_simulated()
        print("Je functie mean(lst) werkt goed!")

        test_q1()
        print("Je functie q1(lst) werkt goed!")

        test_q3()
        print("Je functie q3(lst) werkt goed!")

        test_var()
        test_var_simulated()
        print("Je functie var(lst) werkt goed!")

        test_std()
        test_std_simulated()
        print("Je functie std(lst) werkt goed!")

        test_freq()
        print("Je functie freq(lst) werkt goed!")

        test_modes()
        test_modes_simulated()
        print("Je functie modes(lst) werkt goed!")

        test_rel_cum_freq()
        print("Je functie rel_cum_freq(lst) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()