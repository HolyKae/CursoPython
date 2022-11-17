p = []
while True:
    ap = {'Nome': input('Nome: '), 'Total de jogos': int(input('Quantidade de jogos: ')),
          'Total de gols': 0, 'Jogos': []}
    n = []
    for c in range(ap['Total de jogos']):
        gol = int(input(f'Fez quantos gols no {c + 1}º jogo? '))
        ap['Total de gols'] += gol
        n.append(f'Jogo {c + 1}')
        n.append(gol)
        ap['Jogos'] += [n[:]]
        n.clear()
    p.append(ap)
    s = input('Quer continuar? [S/N]').upper()
    if s not in 'SN':
        print('buro')
        s = input('Quer continuar? [S/N]').upper()
    if 'N' in s:
        break
    print('--' * 20)
print('--' * 20)
for c in range(len(p)):
    print(f'{c} Jogador: {p[c]["Nome"]} Gols:', end=', ')
    for k in range(len(p[c]['Jogos'])):
        print(f'{p[c]["Jogos"][k][1]}', end=' ')
    print(f'Total: {p[c]["Total de gols"]}')
print('--' * 20)
s = int(input('Consulte um código de jogador: [999 para]'))
while s != 999:
    print('--' * 20)
    print(f'O jogador {p[s]["Nome"]} fez {p[s]["Total de gols"]} gols em {p[s]["Total de jogos"]} jogos')
    for k, v in p[s]['Jogos']:
        print(f'===> |{k}: {v} gols', end='|')
        print()
    print('--' * 20)
    s = int(input('Consulte um código de jogador: [999 para]'))
