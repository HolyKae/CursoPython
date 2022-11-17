sp = 0
tg = 0
mp = 0
nmp = ''
c = 1
while True:
    np = input('Digite o nome do produto: ').capitalize()
    pp = float(input('Preço do produto: R$'))
    tg += pp
    if pp >= 1000.00:
        sp += 1
    if c == 1:
        c += 1
        nmp = np
    if pp < mp:
        nmp = np
    m = input('Quer continuar? [S/N]').upper()
    if m not in 'SN':
        print('buro')
        m = input('Quer continuar? [S/N]').upper()
    if m in 'N':
        break
print(f'Foram gastos R${tg}\n{sp} Produtos custam mais que R$1000.00\n{nmp} foi o produto mais barato.')
