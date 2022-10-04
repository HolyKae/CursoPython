p = tuple(input(f'Digite a {c+1}ª palavra.\n').upper() for c in range(4))
print(p)
for i in range(len(p)):
    u = p[i]
    n = 0
    l = ''
    for v in 'AEIOU':
        if v in u:
            n += 1
    print(f'{u} tem {n} vogais e elas são:', end=' ')
    for l in 'AEIOU':
        if l in u:
            print(l, end=' ')
    print()


