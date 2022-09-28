import random
from time import sleep
us = int(input('Escolha: \n1- Pedra\n2- Papel\n3- Tesoura\n'))
pc = random.randint(1, 3)
print(f'JO')
sleep(1)
print(f'KEN')
sleep(1)
print(f'PO')
sleep(0.3)
if us == 1:
    print('Player: Pedra.')
    if pc == 3:
        print('PC: Tesoura.\nVenceu!')
    elif pc == 2:
        print('PC: Papel.\nPerdeu!')
    else:
        print('PC: Pedra\nEmpate!')
elif us == 2:
    print('Player: Papel.')
    if pc == 3:
        print('PC: Tesoura.\nPerdeu!')
    elif pc == 2:
        print('PC: Papel.\nEmpate!')
    else:
        print('PC: Pedra\nVenceu!')
elif us == 3:
    print('Player: Tesoura.')
    if pc == 3:
        print('PC: Tesoura.\nEmpate!')
    elif pc == 2:
        print('PC: Papel.\nVenceu!')
    else:
        print('PC: Pedra\nPerdeu!')
else:
    print('Jogada Inválida!')
