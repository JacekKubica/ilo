
l = [1, 7, 3, 4, 8, 12, 6]
print(l)
temp = []
for i in range(len(l)):
    temp.append(l[-i - 1])

l = temp
print(l)