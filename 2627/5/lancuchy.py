
s1 = "Cześć"
s2 = input("Podaj imię i nazwisko\n")

# wynikowy = s1 + " " + s2
wynikowy = f"{s1}: {s2.lower()}!"

print(wynikowy)
for x in wynikowy:
    print(x)
