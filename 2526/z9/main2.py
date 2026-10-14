
def id(x):
    return x

def sqr(x):
    return x * x

# Przybliża całkę z f od a do b z krokiem h
def integrate(f, a, b, h):
    x = a
    ret = 0
    while x < b:
        ret += f(x)
        x += h
    return ret * h

# for i in range(20):
    # print(integrate(sqr, 1, 5, 1 / 2 ** i))

import math
# policz całkę od 0 do b z cos(x)
# dla b = pi / 6, pi /4, pi / 3, pi / 2, pi, 2pi
# for b in [math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2, math.pi, 2 * math.pi]:
    # print(integrate(math.cos, 0, b, 1 / 2 ** 20), math.sin(b))

print(integrate(lambda x: 1 - x * x, 0, 1, 1 / 2 ** 10))


