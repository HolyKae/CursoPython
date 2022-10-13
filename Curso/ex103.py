def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


j = input('Nome: ')
g = input('Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gol=g)
else:
    ficha(j, g)
