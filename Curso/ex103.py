def ficha(j='', g=0):
    j = input('Nome: ')
    g = input('Gols: ')
    if j == '':
        j = '<desconhecido>'
    if g == '':
        g = 0
    return print(f'O jogador {j} fez {g} gol(s) no campeonato.')


ficha()
