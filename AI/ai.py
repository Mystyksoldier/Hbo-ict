def faculty(n):
    fac = 1
    for i in range(1, n):
        fac = fac * i
    return fac

def facultitieit_iterative(n):
    if n == 0:
        return 1
    return n * facultitieit_iterative(n-1)

list = [4, 3, 2, 6, 7, 8, 8, 1, 5]

def merge(n):
    

print(merge(list))

print(faculty(5))
print(facultitieit_iterative(5))