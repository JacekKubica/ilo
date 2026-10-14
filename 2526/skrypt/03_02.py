print("Rzadziej użyteczną pętlą jest pętla while, która wykonuje się, dopuki warunek pętli jest spełniony")
n = int(input("Wprowadź liczbę 5\n"))
while n != 5:
    if n > 5:
        n = int(input("Liczba jest za duża!\n"))
    else:
        n = int(input("Liczba jest za mała\n"))

print("Gratulacje, wprowadziłeś 5!")
