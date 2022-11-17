ap = {'Nome': input('Nome: '), 'Total de jogos': int(input('Quantidade de jogos: ')),
      'Total de gols': 0, 'Jogos': []}
n = []
for c in range(ap['Total de jogos']):
    gol = int(input(f'Fez quantos gols no {c+1}º jogo? '))
    ap['Total de gols'] += gol
    n.append(f'Jogo {c+1}')
    n.append(gol)
    ap['Jogos'] += [n[:]]
    n.clear()
print()
print('--'*20)
print(f'O jogador {ap["Nome"]} fez {ap["Total de gols"]} gols em {ap["Total de jogos"]} jogos')
for k, v in ap['Jogos']:
    print(f'===> |{k}: {v} gols', end='|')
    print()
print('--'*20)
