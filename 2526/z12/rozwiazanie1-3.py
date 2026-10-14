
def geometric(q, N):
    ret = 0
    for i in range(N + 1):
        ret += q ** i
    return ret


def harmonic(x):
    N = 1
    suma = 0
    while suma < x:
        suma += 1 / N
        N += 1
    return N - 1
    
def riemann_thm(x, N):
    suma = 0
    index_pos = 1
    index_neg = 2
    for i in range(N):
        if suma <= x:
            suma += 1 / index_pos
            index_pos += 2
        else:
            suma -= 1 / index_neg
            index_neg += 2
    return suma




print(geometric(.5, 10))
print(harmonic(15))
print(riemann_thm(-1, 10000000))

