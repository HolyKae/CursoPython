g = ('Lapis', 1, 'Borracha', 0.50, 'Caderno', 15, 'Estojo', 25, 'Mochila', 120)
for i in range(len(g)):
    if i % 2 == 0:
        print(f'{g[i]:}', end=('.' * (20 - len(g[i]))))
        print(f'R${g[i+1]:7.2f}')
