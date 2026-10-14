# Wprowadź trzy liczby całkowite i sprawdź czy ich suma jest
# liczbą parzystą czy nieparzystą


# jak w poprzednim przykładzie, tylko dokonujemy konwersji do typu
# całkowitego przez użycie int
a = int(input("Wprowadź liczbę 1\n"))
b = int(input("Wprowadź liczbę 2\n"))
c = int(input("Wprowadź liczbę 3\n"))
print(f"Wprowadzono {a}, {b}, {c}")

suma = a + b + c
# operacja % 2 zwraca resztę z dzielenia przez 2
if suma % 2 == 0:
    print(f"suma to {suma} i jest liczbą parzystą")
# instrukcja else musi znajdować się na tym samym poziomie wcięcia, co if, któremu odpowiada
else:
    print(f"suma to {suma} i jest liczbą nieparzystą")