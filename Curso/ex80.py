import random
v = []
for i in range(5):
    n = random.randint(1, 99)
    if i == 0:
        print(f'O número {n} é o primeiro da lista')
        v.append(n)
    else:
        if n not in v:
            print(n, end=' ')
            if n > v[-1]:
                print(f'Vai ser adicionado á última posição da lista')
                v.insert(v[-1], n)
            elif n < v[0]:
                print(f'Vai ser adicionado á primeira posição da lista')
                v.insert(0, n)
            else:
                c = 1
                if n < v[c]:
                    print(f'vai ser adicionado á posição {c} da lista')
                    v.insert(c, n)
                elif n > v[c]:
                    print(f'vai ser adicionado á posição {c+1} da lista')
                    v.insert(c+1, n)
    print(v)

