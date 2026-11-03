n = int(input("Wprowadź liczbę całkowitą - tyle elementów ciągu wypiszemy"))

a_before_last = 1
a_last = 1
print("0:", a_before_last)
print("1:", a_last)

for i in range(n - 2):
    temp = a_last
    a_last = a_last + a_before_last
    a_before_last = temp
    print(i + 2, ":", a_last)

