import random
n = int(input('Quer quantos palpites? '))
p = []
pal = []
cont = 0
for c in range(n):
    while cont != 6:
        for i in range(6):
            num = random.randint(1, 60)
            while num in p:
                num = random.randint(1, 60)
            else:
                p.append(num)
                cont += 1
    pal.append(p[:])
    p.clear()
    cont = 0
for c in range(n):
    pal[c].sort()
    print(f'Palpite {c + 1}: {pal[c]}')
