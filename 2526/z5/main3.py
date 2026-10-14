# Funkcja, która dla napisu postaci
# Ala ma kota
# zwróci napis postaci
# AlaMaKota
# tj. spacje mają zniknąć oraz pierwsza po spacji ma stać się wielka


# jem jabłko czerwone -> jemJabłkoCzerwone

def toCamelCase(s):
    after_space = False
    ret = ""
    for l in s:
        if l == " ":
            after_space = True
        elif after_space:
            ret += l.upper()
            after_space = False
        else:
            ret += l
    return ret

print(toCamelCase("Ala ma kota"))
print(toCamelCase("jem jabłko czerwone"))
