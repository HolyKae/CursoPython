ne = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')
n = int(input('Digite um número de 1 a 10: '))
while n > 10 or n < 1:
    print('De 1 a 10, anta.', end=' ')
    n = int(input('Digite um número de 1 a 10: '))
print(f'Número por extenso:\n{ne[n-1]}')
