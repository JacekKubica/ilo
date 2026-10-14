print("Argumenty funkcji mogą mieć wartości domyślne")


def print_product(n, print_intermediate=False):
    x = 1
    for i in range(1, n + 1):
        x *= i
        if print_intermediate:
            print(f"Iloczyn od 1 do {i} =", x)
    print(f"Iloczyn od 1 do {n} =", x)

print("Wywołanie z wartością domyślną")
print_product(3)
print("Wywołanie z wartością równą domyślnej, podaną explicite")
print_product(3, False)
print("Wywołanie z wartością inną niż domyślna")
print_product(3, True)