with open("penger.obj", "r") as f:
    data = f.read()

vertices = []
edges = []

for l in data.split("\n"):
    if l.split()[0] == "v":
        vertices.append([float(x) for x in l.split()[1:]])
    if l.split()[0] == "f":
        a, b, c = l.split()[1:]
        a = int(a.split("/")[0])
        b = int(b.split("/")[0])
        c = int(c.split("/")[0])
        edges.append([a, b])
        edges.append([b, c])
        edges.append([c, a])

with open("parsed.py", "w") as f:
    f.write("vertices = ")
    f.write(str(vertices))
    f.write("\n")
    f.write("edges = ")
    f.write(str(edges))