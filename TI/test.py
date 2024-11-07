
n = 3


binary_str = bin(n)[2:]

result = tuple(int(bit) for bit in binary_str)

print(result)


