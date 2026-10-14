
def sum_on_range(f, n):
    # returns f(0) + f(1) + ... + f(n-1)
    # returns 0    + 0 +... + 0
    # returns 1    + 1 +... + 1
    ret = 0
    for i in range(n):
        ret += f(i)
    return ret

def zero(x):
    return 0

def one(x):
    return 1

def id(x):
    return x

def square(x):
    return x * x

print(sum_on_range(zero, 10))
print(sum_on_range(one, 10))
print(sum_on_range(id, 10)) # (9 + 1) * 9 / 2 == 45
print(sum_on_range(square, 10))
    