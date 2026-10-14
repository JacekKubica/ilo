
# Deklaracja listy
l = [1, 7, 9, 3]

# Wypisanie listy i jej długłości, tj. liczby elementów
print(l, len(l))

# Dodanie wartości na koniec listy
l.append(10)
print(l, len(l))

# Przykład indeksowania listy; indeks 0 odpowiada początkowemu elementowi listy, -1 końcowemu
print(l[0], l[1], l[2], l[-1])

print("wypisywanie pętlą")
# range(len(l)) to to samo co range(0, len(l)), więc pierwszy argument możemy pominąć
for i in range(len(l)):
    print(l[i])

# W przypadku, gdy nie interesuje nas indeks listy, możemy powyższą składnię uprościć
# i przejść pętlą po wartościach, nie po indeksach; poniższa petla jest równoważna
# powyższej.
for x in l:
    print(x)

# Przykład: utworzenie listy z tymi samymi elementami co l, jednak w odwrotnej kolejności
# Zaczynamy od pustej listy
odwrocona_l = []
# Będzie nam potrzebny indeks
for i in range(len(l)):
    # Dla i = 0 mamy -i - 1 == -1, czyli pierwszy element od końca
    # Dla i = 1 mamy -i - 1 == -2, czyli drugi element od końca
    # itd.
    odwrocona_l.append(l[-i - 1])

print(odwrocona_l)