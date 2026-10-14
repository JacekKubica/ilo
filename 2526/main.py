
def total_price(path):
    with open(path, "r") as f:
        data = f.read()
    tot = 0
    for l in data.split("\n"):
        p = l.split(":")[1]
        p = p.strip()
        tot += float(p)
    return tot
        
def add_item(path, name, price):
    with open(path, "r") as f:
        data = f.read()
    data += f"\n{name}: {price}"
    with open(path, "w") as f:
        f.write(data)

def remove_item(path, line_number):
    with open(path, "r") as f:
        data = f.read()
    new_data = ""
    lines = data.split("\n")
    for i in range(len(lines)):
        if i + 1 == line_number:
            continue
        new_data += lines[i] + "\n"
    with open(path, "w") as f:
        f.write(new_data.strip())


def remove_item_by_name(path, name):
    with open(path, "r") as f:
        data = f.read()
    new_data = ""
    lines = data.split("\n")
    for l in lines:
        if l.split(":")[0] == name:
            continue
        new_data += l + "\n"
    with open(path, "w") as f:
        f.write(new_data.strip())





p = total_price("data.txt")
print(p)
add_item("data.txt", "jablko", 1.1)
remove_item("data.txt", 1)
remove_item_by_name("data.txt", "woda mineralna")


def stats(path):
    with open("data2.txt", "r") as f:
        data = f.read().lower()
    longest = 0
    shortest = 10000
    words = data.split()
    nonwhite_tot_length = 0
    for w in words:
        if len(w) > longest:
            longest = len(w)
        if len(w) < shortest:
            shortest = len(w)
        nonwhite_tot_length += len(w)
    avg = nonwhite_tot_length / len(words)
    res = ""
    res += f"word count: {len(words)}\n"
    res += f"longest: {longest}\n"
    res += f"shortest: {shortest}\n"
    res += f"avg: {avg}\n"
    characters_counts = calculate_characters_counts(path)
    res += f"counts: {characters_counts}\n"
    with open("stats.txt", "w") as f:
        f.write(res)



def calculate_characters_counts(data):
    with open("data2.txt", "r") as f:
        data = f.read().lower()
    characters_counts = dict()
    for x in data:
        if x not in characters_counts:
            characters_counts[x] = 0
        characters_counts[x] += 1
    for k in characters_counts:
        characters_counts[k] = f"{characters_counts[k] / len(data) * 100}%"
    return characters_counts

stats("data2.txt")

alphabet = list(calculate_characters_counts("data2.txt").keys())
import random
from copy import deepcopy
alphabet2 = deepcopy(alphabet)
random.shuffle(alphabet2)

plain_to_enc = dict()
enc_to_plain = dict()
for i in range(len(alphabet)):
    plain_to_enc[alphabet[i]] = alphabet2[i]
    enc_to_plain[alphabet2[i]] = alphabet[i]

def encrypt(data, d):
    ret = ""
    for x in data:
        ret += d[x]
    return data


with open("data2.txt", "r") as f:
    data = f.read().lower()
print(encrypt(encrypt(data, plain_to_enc), enc_to_plain) == data)







