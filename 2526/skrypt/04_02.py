print("Funkcji możemy podawać argumenty")


def input_int():
    a = int(input("Wprowadź liczbę całkowitą\n"))
    return a

def print_product(n):
    x = 1
    for i in range(1, n + 1):
        x *= i
    print(f"Iloczyn od 1 do {n} =", x)

print_product(input_int())
print_product(input_int())
print_product(input_int())
    



