import datetime

n = {}
h = datetime.date.today()
n['Nome'] = input('Nome: ')
n['Idade'] = h.year - int(input('Ano de Nascimento: '))
ct = int(input('Carteira de trabalho: (0 = não tem)'))
if ct != 0:
    n['CTPS'] = ct
    ac = int(input('Ano de contratação: '))
    n['Contratação'] = ac
    n['Salário'] = float(input('Salário: R$'))
    n['Aposentadoria'] = (35 - (h.year - ac)) + n['Idade']
for k, v in n.items():
    print(f'|{k}: {v:>2}', end='|')
