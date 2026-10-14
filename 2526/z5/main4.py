
d = dict()
d["jabłko"] = "apple"
d["malina"] = "rasberry"

#print(d)
#print(d["jabłko"])
#d["jabłko"] = 1
#print(d["jabłko"])

for k in d:
    print(k)

for k, v in d.items():
    print(k, v)


w = "ala ma kota"
def count_letters(w):
    d = dict()
    for l in w:
        if l not in d:
            d[l] = 0
        d[l] += 1
    return d


d = count_letters(w)
for k, v in d.items():
    print(f"{k}:", v)