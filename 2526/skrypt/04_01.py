print("Często chcemy użyć kawałek kodu ponownie, służą do tego funkcje")
print("Funkcje deklarujemy za pomocą słówka kluczowego def")
print("Jeśli chcemy, żeby funkcja zwracała coś, co ma być przypisane do zmiennej, używamy słówka kluczowego return.")
def input_int():
    a = int(input("Wprowadź liczbę całkowitą\n"))
    return a
    
def input_float():
    a = float(input("Wprowadź liczbę zmiennoprzecinkową\n"))
    return a

x = input_int()
y = input_int()
z = input_float()

print(f"Wprowadzono {x}, {y}, {z}")

