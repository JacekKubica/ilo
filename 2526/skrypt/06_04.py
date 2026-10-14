def pause():
    input("Wciśnij enter, by kontynuować\n")

print("Słowniki są niesłychanie użyteczną strukturą. Pozwalają one przypisywać wartości do kluczy, w pewnym sensie stanowią uogólnienie indeksowania.")

d = dict()
d["jabłko"] = "apple"
d["malina"] = "rasberry"
print(f"Mamy słownik:\n {d}")

print("Wartość dla klucza 'jabłko'", d["jabłko"])
d["jabłko"] = 1
print("Wartość dla klucza 'jabłko' po modyfikacji wartości", d["jabłko"])
print("Wartość dla klucza 'malina'", d["malina"])

pause()
print("Domyślnie iteracja po słowniku przebiega po jego kluczach - możemy iterować po parach klucz-wartość przy użyciu items.")
for k in d:
    print(k)

for k, v in d.items():
    print(k, v)

pause()
print("Użyjemy słownika do zliczania liter")
w = "ala ma kota"
def count_letters(w):
    d = dict()
    for l in w:
        if l not in d:
            d[l] = 0
        d[l] += 1
    return d


d = count_letters(w)
print(f"W słowie {w} kolejne litery występują następującą liczbę razy:")
for k, v in d.items():
    print(f"{k}:", v)