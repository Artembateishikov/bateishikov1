p = 1

for n in range(1,21):
    a = 2 * n**2 + 5 * n + 1
    b = n**3 / 4 + 2 * n**2 + 1
    p = p * a/b

print(p)