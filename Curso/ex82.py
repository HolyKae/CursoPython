import random
n = int(input('Quer quantos números? '))
v = []
p = []
ip = []
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
for i in range(len(v)):
    if v[i] % 2 == 0:
        p.append(v[i])
    else:
        ip.append(v[i])
print(f'Lista:\n{v}\nLista de pares:\n{p}\nLista de ímpares:\n{ip}')