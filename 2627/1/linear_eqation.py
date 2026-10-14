
# Ćwiczenie 1:
# Napisz program, który dla wprowadzony liczb a, b
# wypisze rozwiązania równania ax + b = 0.
# Obsłuż przypadki, kiedy a lub b = 0.

a = float(input("Wprowadź a: "))
b = float(input("Wprowadź b: "))

if a == 0 and b == 0:
    print("Tożsamościowe")
elif a == 0 and b != 0:
    print("Sprzeczne")
else:
    print(-b / a)




