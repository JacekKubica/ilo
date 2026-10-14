
def list_reverse(l):
    j = len(l) - 1
    for i in range(len(l)):
        if j <= i:
            break
        l[i], l[j] = l[j], l[i]
        j -= 1




l = [1, 7, 3, 4, 8, 12, 6]
print(l)
list_reverse(l)
print(l)


l2 = [1, 8, 3]
print(l2)
list_reverse(l2)
print(l2)
# 6, 12, 3, 4, 8, 7, 1
#        i     j  