
x = int(input("Wprowadź liczbę: "))

if x < 0:
    print("Ujemna")
elif x == 0:
    print("Zero")
else:
    print("Dodatnia")

# Ćwiczenie: wypisz, czy liczba jest parzysta czy nie
if x % 2 == 0:
    print("Parzysta")
else:
    print("Nieparzysta")