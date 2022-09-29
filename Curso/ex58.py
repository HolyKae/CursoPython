import random
n = 7
p = 6
c = 0
while p != n:
    n = random.randint(1, 10)
    p = int(input('Digite um número entre 1 e 10: '))
    if p != n:
        c += 1
        print(f'kk buro {n}')
if p == n:
    print(f'Acerto mizeravi\nErou {c} vzs')

