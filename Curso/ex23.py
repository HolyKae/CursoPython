n = int(input('Digite um número entre 0 e 9999: '))
while n > 9999 or n < 0:
    print('Número inválido!')
    n = int(input('Digite um número válido entre 0 e 9999: '))
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(n // 1 % 10, n // 10 % 10, n // 100 % 10, n // 1000 % 10))
