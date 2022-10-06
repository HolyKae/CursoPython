import random
n = int(input('Quer quantos números? '))
v = []
for i in range(n):
    u = random.randint(1, 99)
    if u not in v:
        v.append(u)
    else:
        n += 1
        while u in v:
            u = random.randint(1, 99)
        v.append(u)
    print(n)
while True:
    c = input('Quer continuar? [S/N]').upper()
    if c not in 'SN':
        c = input('buro')
    elif c in 'S':
        n = int(input('Quer quantos números? '))
        for i in range(n):
            u = random.randint(1, 99)
            if u not in v:
                v.append(u)
            else:
                n += 1
                while u in v:
                    u = random.randint(1, 99)
                v.append(u)
            print(n)
    else:
        break
v.sort()
print(v)
