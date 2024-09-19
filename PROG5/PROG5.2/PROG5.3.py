data = open("PROG5/PROG5.2/oefening_5_2_kaartnummers.txt", "r")

def count_lines_and_get_the_biggest_number(data):
    numberList = []
    data = data.split("\n")
    
    for i in range(len(data)):
        data[i] = data[i].split(", ")
        numberList.append(int(data[i][0]))

    bigNumber = max(numberList)

    return (f"Deze file telt {len(data)} regels\nHet grootste kaartnummer is: {bigNumber} en dat staat op regel {numberList.index(bigNumber) + 1}")

print(count_lines_and_get_the_biggest_number(data.read()))
