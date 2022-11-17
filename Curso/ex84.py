p = [str(input('Nome: ')), int(input('Peso: '))]
al = [p[:]]
m = p[1]
c = 1
while True:
    d = input('Quer continuar? [S/N]').upper()
    if d not in 'SN':
        print('buro')
        d = input('Quer continuar? [S/N]').upper()
    elif d in 'S':
        c += 1
        p = [str(input('Nome: ')), int(input('Peso: '))]
        al.append(p[:])
        m += p[1]
    else:
        m = m / c
        break
g = []
f = []
for i in range(len(al)):
    if al[i][1] >= m:
        g.append(al[i])
    else:
        f.append(al[i])
print(f'{c} Pessoas foram cadastradas.\nMais pesadas:\n{g}\nMais leves:\n{f}')
