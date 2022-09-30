n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
o = 1
while o > 5 and o == 0:
    print(f'Ta vendo {o} onde aí cabeça de butijão??/???')
    o = int(input('Escolha uma opção:\n1 - [+]\n2 - [*]\n3 - [<>]\n4 - Novos números\n5 - Sair.\n'))
while o != 5:
    o = int(input('Escolha uma opção:\n1 - [+]\n2 - [*]\n3 - [<>]\n4 - Novos números\n5 - Sair.\n'))
    if o == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif o == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
    elif o == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
        elif n1 < n2:
            print(f'{n1} < {n2}')
        else:
            print(f'{n1} = {n2}')
    elif o == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
