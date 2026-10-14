# Wprowadź liczbę całkowitą n
# Policz sumę 1 + 2 + ... + n
# Policz sumę liczb parzystych o wartości co najwyżej n, 
  # czyli 1 + 3 + ... + (n lub n - 1, zależy czy n jest parzyste)
# Policz sumę liczb nieparzystych o wartości co najwyżej n

# Przykład: Jeśli n == 3, to suma to 1 + 2 + 3 == 6,
# suma parzystych to 2 == 2
# suma nieparzystych to 1 + 3 == 4

n = int(input("Wprowadź n\n"))
# Tworzymy zmienne, w których będziemy akumulować wyniki
suma = 0
suma_parzyste = 0
suma_nieparzyste = 0
# i in range(1, n + 1) przejdzie po i = 1 do i = n włącznie
for i in range(1, n + 1):
    suma += i
    if i % 2 == 0:
        suma_parzyste += i
    else:
        suma_nieparzyste += i

print(suma, suma_parzyste, suma_nieparzyste)
