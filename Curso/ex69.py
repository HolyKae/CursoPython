si = 0
sm = 0
sg = 0

while True:
    i = int(input('Digite a idade: '))
    s = input('Sexo: [M/F]').upper()
    if s not in 'MF':
        print('buro')
        s = input('Sexo: [M/F]').upper()
    m = input('Quer continuar? [S/N]').upper()
    if m not in 'SN':
        print('buro')
        m = input('Quer continuar? [S/N]').upper()
    if m in 'N':
        break
    else:
        if i >= 18:
            si += 1
        if s in 'F' and i < 20:
            sg += 1
        if s in 'M':
            sm += 1
print(f'{si} Tem mais de 18 anos\n{sm} Homens foram cadastrados\n{sg} São mulheres menores de 20 anos')