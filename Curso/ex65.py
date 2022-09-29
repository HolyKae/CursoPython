s = 'S'
d = 0
so = 0
ma = 0
me = 0
while s == 'S':
    d += 1
    c = int(input('Digite um número: '))
    s = input('Quer continuar? [S/N]').upper()
    so += c
    if d == 1:
        ma = c
        me = c
    if c < ma:
        ma = c
    if c > me:
        me = c
print(f'Maior: {ma}\nMenor: {me}\nMédia: {so / d}')
