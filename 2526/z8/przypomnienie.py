
l = [1, 3, 6, 9, -1, -100, 12]

def cmp_key(x):
    return -x

print(sorted(l, key=cmp_key))

def cmp_key2(x):
    return x[1]
l2 = [[3, 2], [2, 1]]
print(sorted(l2, key=cmp_key2))

l3 = [[1, 2, 3], [-1, -2], [7, 8]]
def cmp_key3(l):
    return sum(l)

print(sorted(l3, key=cmp_key3))