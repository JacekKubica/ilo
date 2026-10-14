
n = int(input("Podaj liczbę naturalna"))
suma = 0
for i in range(n + 1):
    if i == 0:
        print("zaczynas od zera!")
    suma = suma + i
    # suma += i

print(f"suma to {suma}")


iloczyn = 1
for i in range(1, n + 1):
    if i % 2 == 1:
        iloczyn = iloczyn * i

print(f"iloczyn to {iloczyn}")


# ćwiczenie prostsze: wypisać wszystkie dzielniki podanej liczby
# trudniejsze: wypisać największy wspólny dzielnik 
             # i najmniejszą wspólną wielokrotność dwóch liczb
