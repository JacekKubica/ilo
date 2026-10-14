
n = int(input())
m = int(input())

nwd = 1
for i in range(1, n + 1):
    if n % i == 0 and m % i == 0:
        nwd = i

print(f"nwd: {nwd}")


nww = 1
for i in range(1, n * m + 1):
    if i % n == 0 and i % m == 0:
        nww = i
        break

print(f"nww: {nww}")
print(f"nww to: {n * m / nwd}")