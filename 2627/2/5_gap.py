
x = int(input("Wprowadź rok"))

# sposób pierwszy
if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print("Przestępny")
else:
    print("Zwykły")


if x % 400 == 0:
    print("Przestepny")
elif x % 100 == 0:
    print("Zwykły")
elif x % 4 == 0:
    print("Przestępny")
else:
    print("Zwykły")