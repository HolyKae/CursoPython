n = int(input('Digite um número: '))
print(f'Números pares de 1 à {n}:')
for c in range(2, n+1, 2):
    print(c, end=' ')
