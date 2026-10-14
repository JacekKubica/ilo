print("Modyfikacje przekazanych do funkcji liczb i łańcuchów tekstowych nie są widoczne poza funkcją, modyfikacje list są")

def f(l):
    l.append(1)

def g(x):
    x += 7

l = [1, 2, 3]
print(f"l przed wywołaniem f(l) to {l}")
f(l)
print(f"l po wywołaniu f(l) to {l}")

x = 10
print(f"x przed wywołaniem g(x) to {x}")
g(x)
print(f"x po wywołaniu g(x) to {x}")
