
import random
l = [1, 2, 3, 4, 5, 6]
print(l)
random.shuffle(l)
print(l)

l2 = [x * x for x in l]
print(l2)

def str_to_list(s):
    # ret = []
    # for x in s:
        # ret.append(x)
    # return ret
    # ^ to powyżej jest równoważne
    return [x for x in s]

def shuffled_str(s):
    l_s = str_to_list(s)
    random.shuffle(l_s)
    # return "".join(l_s)
    # równoważnie do tego powyżej
    ret = ""
    for x in l_s:
        ret += x
    return ret

s = "abcdefgh"
s_shuffled = shuffled_str(s)
print(s_shuffled)
#random.shuffle(s)
