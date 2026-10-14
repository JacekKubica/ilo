l = [1, 7, 3, 4, 8, 12, 6]
print(l)
for i in range(len(l) // 2):
    l[i], l[-i - 1] = l[-i - 1], l[i]
    #temp = l[i]
    #l[i] = l[-i - 1]
    #l[-i - 1] = temp

print(l)