def rechthoek(x, y):
    result = ""
    for i in range(x):
        result += "#" * y + "\n"
    return result

print(rechthoek(3, 4))
