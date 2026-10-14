import random

def str_to_list(s):
    return [x for x in s]

def shuffled_str(s):
    l_s = str_to_list(s)
    random.shuffle(l_s)
    return "".join(l_s)

def translate(to_translate, alphabet, shuffled_alphabet):
    ret = ""
    for x in to_translate:
        idx = 0
        for a in alphabet:
            if a == x:
                break
            idx += 1
        ret += shuffled_alphabet[idx]
    return ret

alphabet = "abc"
shuffled_alphabet = "bca"
s = "acbbcca"
translated = translate(s, alphabet, shuffled_alphabet)
print()
print(s == translate(translated, shuffled_alphabet, alphabet))
