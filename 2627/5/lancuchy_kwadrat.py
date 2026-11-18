
n = int(input())

s = ""

for i in range(n):
    for j in range(n):
        s = s + "#"
        s += " "
    s += "\n"

s_str = "".join(s)
print(s_str)
