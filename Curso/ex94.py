c = i = 0
p = []
m = []
v = []
while True:
    t = {'Nome': input('Nome: '), 'Sexo': input('Sexo [M/F]: '), 'Idade': int(input('Idade: '))}
    if t['Sexo'] not in 'MF':
        print('buro')
        t['Sexo'] = input('Sexo [M/F]: ')
    p.append(t)
    if 'F' in t['Sexo']:
        m.append(t)
    i += t['Idade']
    c += 1
    s = input('Quer continuar? [S/N]').upper()
    if s not in 'SN':
        print('buro')
        s = input('Quer continuar? [S/N]').upper()
    if 'N' in s:
        i = i / c
        break
for u in range(len(p)):
    if p[u]['Idade'] > i:
        v.append(p[u])
print(f'Foram cadastradas {c} pessoas, com a média de idade de {i} anos\nLista:')
for u in range(len(p)):
    for k, h in p[u].items():
        print(f'|{k}: {h:>2}', end='|')
    print()
print('\nLista de mulheres:')
for u in range(len(m)):
    for k, h in m[u].items():
        print(f'|{k}: {h:>2}', end='|')
    print()
print('\nLista dos mais velhos:')
for u in range(len(v)):
    for k, h in v[u].items():
        print(f'|{k}: {h:>2}', end='|')