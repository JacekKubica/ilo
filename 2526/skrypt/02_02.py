print("Program sprawdza, ile rozwiązań w liczbach rzeczywistych ma równanie kwadratowe a * x * x + b * x + c  o wprowadzonych współczynnikach a, b, c")
a = float(input("Wprowadź współczynnik a\n"))
b = float(input("Wprowadź współczynnik b\n"))
c = float(input("Wprowadź współczynnik c\n"))

delta = b * b - 4 * a * c
if delta == 0:
    print("Jedno")
elif delta > 0:
    print("Dwa")
else:
    print("Zero")
