data = open("PROG5/PROG5.2/oefening_5_2_kaartnummers.txt", "r")

def pretty_print(data):
    data = data.split("\n")
    for i in range(len(data)):
        data[i] = data[i].split(", ")
        print(f"{data[i][1]} heeft kaartnummer: {data[i][0]}")

pretty_print(data.read())
