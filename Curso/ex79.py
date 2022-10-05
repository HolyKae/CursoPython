import random
v = []
for i in range(10):
    n = random.randint(1, 99)
    if n not in v:
        v.append(n)
v.sort()
print(v)
