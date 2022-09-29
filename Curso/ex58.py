import random
n = random.randint(1, 10)
c = 0
a = False
while not a:
    p = int(input('Digite um número entre 1 e 10: '))
    if p == n:
        a = True
        print(f'Acerto mizeravi\nErou {c} vzs')
    else:
        if p > n:
            print(f'kk buro')
            print('Menos')
        elif p < n:
            print(f'kk buro')
            print('Mais')
    c += 1

