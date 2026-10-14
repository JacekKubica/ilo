
x1 = float(input("Wprowadź współrzędną x środka pierwszego okręgu: "))
y1 = float(input("Wprowadź współrzędną y środka pierwszego okręgu: "))
r1 = float(input("Wprowadź promień pierwszego okręgu: ")             )
x2 = float(input("Wprowadź współrzędną x środka drugiego okręgu: ")  )
y2 = float(input("Wprowadź współrzędną y środka drugiego okręgu: ")  )
r2 = float(input("Wprowadź promień drugiego okręgu: ")               )
d_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
r_sum_sq = (r1 + r2) ** 2
if d_squared < r_sum_sq:
    print("przecinają")
elif d_squared == r_sum_sq:
    print("styczne")
else:
    print("rozłączne")