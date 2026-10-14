# Funkcja, która dla podanego łańcuchu zwróci najdłuższe słowo w tym łańcuchu
def longest_word(s):
    current_longest = ""
    current = ""
    for l in s:
        if l == " ":
            if len(current) > len(current_longest):
                current_longest = current
            current = ""
        else:
            # to samo co current = current + l
            current += l
    if len(current) > len(current_longest):
        current_longest = current
    return current_longest

print(longest_word("Ala mafdsgdsgds kotagffd"))