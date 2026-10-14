def copy_list(l):
    ret = []
    for x in l:
        ret.append(x)
    return ret

l = [1, 2, 3]
l2 = l
l[1] = 7
print(l)
print(l2)
