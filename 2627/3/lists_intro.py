
lista = []
lista2 = [5, 11, 3]

# Wypisywanie list
print("lista", lista)
print("lista2", lista2)

# Odnoszenie się do elementów listy
print("lista2, element 0.", lista2[0])
print("lista2, element 1.", lista2[1])
print("lista2, element 2.", lista2[2])

# Dodawanie elementów do listy
lista2.append(13)
print("lista2 po dodaniu 13", lista2)

# Dynamiczna lista
n = int(input("Wprowadź liczbę\n"))
for i in range(n):
    lista.append(i * i)

print("lista po dodaniu n elementów", lista)
