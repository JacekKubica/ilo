import random

n = int(input("ile losujemy "))
x = int(input("z zakresu 1 do ile losujemy "))

lista_z_ktorej_losujemy = []
for i in range(1, x + 1):
    lista_z_ktorej_losujemy.append(i)

lista = []
for i in range(n):
    x = random.choice(lista_z_ktorej_losujemy)
    lista.append(x)

print("wylosowana lista:", lista)

# 2. liczenie sumy
suma = 0

# Sposób 1:
# for i in range(n):
#     suma = suma + lista[i]

# Sposób 2:
# for i in range(len(lista)):
#     suma += lista[i]

# Sposób 3:
# for x in lista:
#     suma += x

# Sposób 4:
suma = sum(lista)

print("suma", suma)



