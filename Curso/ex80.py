import random
v = []
for i in range(5):
    n = random.randint(1, 99)
    if i == 0:
        v.append(n)
    else:
        if n not in v:
            print(n)
            if n > v[-1]:
                v.insert(v[-1], n)
            elif n < v[0]:
                v.insert(0, n)
            else:
                c = 1
                if n < v[c]:
                    v.insert(c, n)
                elif n > v[c]:
                    v.insert(c+1, n)

    print(v)

