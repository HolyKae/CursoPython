n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
o = int(input('Escolha uma opção:\n1 - [+]\n2 - [*]\n3 - [<>]\n4 - Novos números\n5 - Sair.\n'))
while o > 5:
    print(f'Ta vendo {o} onde aí cabeça de butijão??/???')
    o = int(input('Escolha uma opção:\n1 - [+]\n2 - [*]\n3 - [<>]\n4 - Novos números\n5 - Sair.\n'))
while o != 5:
    if o == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
        break
    elif o == 2:
        print(f'{n1} * {n2} = {n1 * n2}')
        break
    elif o == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
        elif n1 < n2:
            print(f'{n1} < {n2}')
        else:
            print(f'{n1} = {n2}')
        break
    elif o == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        break
