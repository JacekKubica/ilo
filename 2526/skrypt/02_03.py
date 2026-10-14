print("Pojedynczy warunek jest niewystarczający, żeby wyrazić wszystkie interesujące logiczne zależnośc. Dlatego istnieją operatory logiczne and (oba warunki są spełnione) oraz or (przynajmniej jeden jest)")
x = float(input("Wprowadź liczbę zmiennoprzecinkową"))
y = float(input("Wprowadź liczbę zmiennoprzecinkową"))
if x > 0 and y > 0:
    print("Obie liczby są dodatnie")
elif x > 0 or y > 0:
    print("Przynajmniej jedna liczba jest dodatnia")
else:
    print("Obie liczby są niedodatnie")
