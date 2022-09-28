n = int(input('Digite um número: '))
print(f'Números pares de 1 à {n}:')
for c in range(1, n+1):
    if c % 2 == 0:
        print(c)
