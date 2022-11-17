import random
n = int(input('Quer quantos números? '))
v = []
for i in range(n):
    n = random.randint(1, 99)
    v.append(n)
while True:
    c = input('Quer continuar? [S/N]').upper()
    if c not in 'SN':
        c = input('buro')
    elif c in 'S':
        n = int(input('Quer quantos números? '))
        for i in range(n):
            n = random.randint(1, 99)
            v.append(n)
    else:
        break
v.sort()
v.reverse()
print(f'Foram pedidos {len(v)} números\n{v}')
if 5 in v:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')


