print("Poeksperymentujmy trochę z range i pętlami, żeby lepiej je wyczuć")
a = int(input("Wprowadź górny zakres, co najwyżej 15\n"))
while a > 15:
    a = int(input("Zakres musi być mniejszy niż 15!\n"))

b = int(input("Wprowadź dolny zakres\n"))

print(f"W zakresie range({b}, {a}) są następujące liczby:")
for i in range(b, a):
    print(i)
