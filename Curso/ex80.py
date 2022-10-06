import random
v = []
for i in range(10):
    n = random.randint(1, 99)
    while n in v:
        n = random.randint(1, 99)
        if n not in v:
            break
    else:
        if i == 0 or n < v[0]:
            v.insert(0, n)
            print(n)
            print(f'O número {n} vai para o começo da lista')
        elif n > v[-1]:
            v.append(n)
            print(n)
            print(f'O número {n} vai para o final da lista')
        else:
            p = 0
            while p < len(v):
                if n <= v[p]:
                    print(n)
                    print(f'O número {n} vai para a {p+1}ª posição na lista')
                    v.insert(p, n)
                    break
                p += 1
    print(v)

