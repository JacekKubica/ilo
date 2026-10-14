print("Instrukcje warunkowe nie wystarczą do osiągnięcia zbyt ciekawych celów, kluczowa jest możliwość powtarzania operacji dynamiczną liczbę razy.")
print("Służą do tego pętle.")
print("Najpowszechniejszą pętlą jest pętla for, która robi coś dla określonych elementów.")
n = int(input("Wprowadź liczbę całkowitą\n"))
suma = 0
print("Funkcja range(n + 1) przebiegnie liczby od 0 do n + 1, wyłączając ostatni (czyli od 0 do n włącznie)")
for i in range(n + 1):
    suma += i

print(f"suma od 0 do {n} = ", suma)

