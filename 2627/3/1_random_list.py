import random

x = int(input("Wprowadź zakres elementów"))

# Losowanie elementu z zakresu x
l = []
for i in range(x):
    l.append(i + 1)

r = random.choice(l)
print("Losowa wartośc z zakresu 1 do x włącznie to", r)
