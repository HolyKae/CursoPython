c = float(input('Valor da casa: R$'))
s = float(input('Salário: R$'))
a = int(input('Em quantos anos: '))
p = c / (a * 12)
print('O valor da prestação é: R${:.2f}'.format(p))
if p > s * 0.30:
    print('O empréstimo não foi aprovado!')
else:
    print('Aprovado!')
