n1 = float(input('Nota 1:'))
n2 = float(input('Nota 2:'))
m = (n1+n2)/2
print(f'{m:.1f}')
if m < 5:
    print('REPROVADO')
elif m >= 7:
    print('APROVADO!')
else:
    print('RECUPERAÇÃO')
