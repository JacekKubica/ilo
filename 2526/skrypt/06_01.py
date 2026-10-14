def pause():
    input("Wciśnij enter, by kontynuować\n")

print("Wielokrotnie używaliśmy łańcuchów tekstowych, natomiast nie wprowadziliśmy systematycznie ich własności.")
print("Pod wieloma względami łańcuchy tekstowe są podobne do list liter.")
a = "avBdfvcx"
b = "12323"
print(f"Po dodaniu {a} + {b} dostajemy łańcuch {a + b}")
pause()
print("Posiadają one wiele użytecznych wbudowanych funkcjonalności, takie jak sprawdzanie, czy dany łańcuch składa się z samych liter / cyfr / białych znaków.")
a = "avBdfvcx"
b = "12323"
c = "   \n"
print(f"Czy {a} składa się z samych liter?", a.isalpha())
print(f"Czy {b} składa się z samych cyfr?", b.isnumeric())
print(f"Czy {c} składa się z samych białych znaków?", c.isspace())
print(f"Czy {a + b} składa się z samych liter?", (a + b).isalpha())
print(f"Czy {a + b} składa się z samych liter lub cyfr?", (a + b).isalnum())
print(f"Czy {a + c + b} składa się z samych liter lub cyfr?", (a + c + b).isalnum())

pause()
print("Możemy po nich iterować. Przy iteracji przez łańcuch tekstowy każdy jego znak jest również łańcuchem o długości 1")
count_digits = 0
count_letters = 0
count_spaces = 0
for x in a + b + c:
    if x.isalpha():
        count_letters +=1
    elif x.isdigit():
        count_digits +=1
    elif x.isspace():
        count_spaces +=1
print(f"W tekście {a + b + c} jest {count_spaces} białych znaków, {count_digits} cyfr, {count_letters} liter.")



