s = 'S'
d = so = ma = me = 0
while s in 'S':
    c = int(input('Digite um número: '))
    so += c
    d += 1
    if d == 1:
        ma = me = c
    else:
        if c < ma:
            ma = c
        if c > me:
            me = c
    s = input('Quer continuar? [S/N]').upper().strip() [0]
print(f'Maior: {ma}\nMenor: {me}\nMédia: {so / d}')
