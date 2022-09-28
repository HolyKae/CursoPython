n1 = int(input(f'Digite um número: '))
n2 = int(input(f'Digite outro número: '))
if n1 > n2:
    print(f'O primeiro é maior {n1} > {n2}')
elif n2 > n1:
    print(f'O segundo é maior: {n1} < {n2}')
else:
    print(f'Os dois são iguais: {n1} = {n2}')
