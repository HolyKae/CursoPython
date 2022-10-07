n = {}
n['Nome'] = input('Nome: ')
n['Nota'] = int(input(f'Digite a média de {n["Nome"]}: '))
if n['Nota'] >= 7:
    n['Situação'] = 'APROVADO'
else:
    n['Situação'] = 'REPROVADO'
for k, v in n.items():
        print(f'|{k}: {v:>2}', end='|')
