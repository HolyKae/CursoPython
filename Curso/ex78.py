import random
v = []
for i in range(5):
    n = random.randint(1, 99)
    if n not in v:
        v.append(n)
p = v[:]
v.sort()
print(p)
print(f'Maior: {v[-1]:.<5}Posiçôes: ', end='')
for i in range(len(p)):
    if v[-1] == p[i]:
        print(f'{i+1}', end=' ')
print('')
print(f'Menor: {v[0]:.<5}Posiçôes: ', end='')
for i in range(len(p)):
    if v[0] == p[i]:
        print(f'{i+1}', end=' ')