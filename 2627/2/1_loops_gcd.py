
x = int(input("Wprowadź liczbę 1\n"))
y = int(input("Wprowadź liczbę 2\n"))

nwd = 1

for i in range(1, x + 1):
    if x % i == 0 and y % i == 0:
        nwd = i

print(nwd)