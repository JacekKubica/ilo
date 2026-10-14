def pause():
    input("Wciśnij enter, by kontynuować\n")

print("Instrukcje warunkowe i pętle to nie wszystko - do ciekawszych zastosowań potrzebna jest pamięć")
print("Jeśli nie znamy z góry określonej liczby wartości, które chcemy zapamiętać, używamy do tego list.")
pause()
print("Listę deklarujemy przez nawisy kwadratowe z podanymi w środku elementami po przecinku")
pause()
l1 = [1, 2, 3]
l2 = [7, 8, 9]
print("Listy możemy wypisywać:", l1, l2)
pause()
print("List można dodawać, tworzy to połączoną listę; l1 + l2 = ", l1 + l2)
pause()

l1.append(9)

print(f"Do list można dokładać elementy, po użyciu l1.append(9) mamy l1 = {l1}")
pause()
print("Po listach możemy przejść funkcją for podobnie jak po zakresie")

l2_sum = 0
for x in l2:
    l2_sum += x

print("Suma elemntów w l2 =", l2_sum)
pause()
print("Długość (czyli liczbę elementów listy) możemy dostać wywołując funkcję len; len(l2) =", len(l2))
pause()
print(f"Możemy się odwoływać do kolejnych elementów listy, indeks zero odpowiada pierwszemu elementowi: l1[0] = {l1[0]}, l1[1] = {l1[1]}, l1[2] = {l1[2]}")
pause()
print(f"Możemy się odwoływać do elementów listy od końca, indeks -1 odpowiada ostatniemu elementowi: l1[-1] = {l1[-1]}, l1[-2] = {l1[-2]}")
pause()
print("Łącząc naszą wiedzę możemy napisać powyższą pętlę bardziej explicite")

l2_sum = 0
for i in range(len(l2)):
    l2_sum += x

print("Suma elemntów w l2 =", l2_sum)