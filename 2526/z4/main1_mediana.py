
# Definicja:
# Jeśli mamy nieparzystą liczbę liczb, to ustawiamy je od najmniejszej
# do największej i ich mediana to środkowa z tych liczb
# Przykład 5 7 1, to medianą jest 5, bo ustawiamy 1 5 7 i 5 jest na
# środku


# Poniższy kod wprowadza trzy liczby z klawiatury i wylicza ich
# medianę oraz średnią arytmetyczną

# input zwraca łańcuch tekstowy wprowadzony przez użytkownika (do pierwszego
# wciśnięcia enter); jeśli chcemy wprowadzone dane używać jako liczbę zmienną
# zmiennoprzecinkową, musimy dokonać tzw. konwersji łańcuchu tekstowego
# do floata, do czego służy wywołanie float
a = float(input("Wprowadź liczbę 1\n"))
b = float(input("Wprowadź liczbę 2\n"))
c = float(input("Wprowadź liczbę 3\n"))
print(f"Wprowoadzono {a}, {b}, {c}")



# będziemy śledzili wszystkie operacje na przykładzie a b c == 5 3 1
# po wykoaniu tego ifa będziemy mieli a b c == 3 5 1
if a > b:
    # to ponizej to pelny zapis operacji 'a, b = b, a'; poniżej używamy już skrótowego zapisu
    temp = a
    a = b
    b = temp
# po tym a b c == 3 1 5
if b > c:
    b, c = c, b
# po tym a b c == 1 3 5
if a > b:
    a, b = b, a

print(f"Posortowane liczby to {a}, {b}, {c}")
print(f"Mediana to {b}")
print(f"Średnia to {(a + b + c) / 3}")
