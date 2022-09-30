import random
v = 0
while True:
    pn = int(input('Digite um número: '))
    pe = input('Par ou Ímpar? [P/I]').upper()
    if pe not in 'IP':
        print('buro')
        pe = input('Par ou Ímpar? [P/I]').upper()
    cn = random.randint(1, 10)
    s = pn + cn
    if pe in 'P' and s % 2 == 0:
        v += 1
        print(f'Player: {pn} ---- PC: {cn} ---- {pn} + {cn} = {s}\nGANHOU')
        print('Boh saidera kek')
    elif pe in 'I' and s % 2 == 1:
        v += 1
        print(f'Player: {pn} ---- PC: {cn} ---- {pn} + {cn} = {s}\nGANHOU')
        print('Boh saidera kek')
    else:
        print(f'Player: {pn} ---- PC: {cn} ---- {pn} + {cn} = {s}\nPERDEU KKKJKJKJ buro')
        print('flws')
        break
print(f'Ganhou {v} vezes')
