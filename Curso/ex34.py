s = float(input('Salário: R$'))
if s >= 1250:
    print('O salário ficou: R${:.2f}'.format(s * 1.15))
else:
    print('O salário ficou: R${:.2f}'.format(s * 1.10))
