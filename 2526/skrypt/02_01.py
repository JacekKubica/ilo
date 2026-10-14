print("Żeby zrobić cokolwiek ciekawego, musimy umieć oznajmić programowi, żeby zrobił coś pod jakimś warunkiem")
print("Poniższy kod rozróżnia, czy liczba wprowadzona przez użytkownika jest parzysta, czy nie")
x = int(input("Wprowadź liczbę całkowitą\n"))
print("Poniższe wyjście zależy od wprowadzonego wejścia. W kodzie proszę zwrócić uwagę na wcięcia - w języku python określają one, jakie operacje wykonają się przy danym warunku (a dalej w danej pętli, funkcji etc.); proszę też zwrócić uwagę na dwukropek.")
if x % 2 == 0:
    print("Wprowadziłeś liczbę parzystą!")
else:
    print("Wprowadziłeś liczbę nieparzystą!")