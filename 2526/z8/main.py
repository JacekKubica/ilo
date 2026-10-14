
with open("sample.txt", "r", encoding="utf8") as f:
    data = f.read().lower()


def count_letters(txt):
    ret = dict()
    for x in txt:
        if x not in ret:
            ret[x] = 0
        ret[x] += 1
    return ret

def translate(txt, d):
    translated = ""
    for x in txt:
        if x in d:
            translated += d[x]
        else:
            translated += x
    return translated

print(translate("ab", {"a": "b", "b": "a"}) == "ba")

counts = count_letters(data)
alphabet = counts.keys()

def sort_key(x):
    return -x[1]
counts_sorted = sorted(counts.items(), key=sort_key)
print(counts_sorted)