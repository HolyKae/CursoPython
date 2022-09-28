n = int(input('Escreva um número: '))
c = int(input('1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))
if c == 1:
    print(f'{bin(n)[2:]}')
elif c == 2:
    print(f'{oct(n)[2:]}')
elif c == 3:
    print(f'{hex(n)[2:]}')
