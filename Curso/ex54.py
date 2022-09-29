from datetime import date
d = date.today().year
ma = 0
me = 0
for c in range(1, 8):
    p = int(input(f'Digite o ano de nascimento da {c}ª Pessoa: '))
    if d - p >= 21:
        ma += 1
    else:
        me += 1
print(f'{ma} São maiores de idade e {me} são menores.')
