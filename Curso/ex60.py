n = int(input('Digite um número: '))
f = n
print(n, end=' * ')
while n != 2:
    n = n-1
    f *= n
    print(n, end=' * ')
print(f'{1}: {f}')

'''Com FOR
n = int(input('Digite um número: '))
print(n, end=' * ')
for c in range(n-1, 1, -1):
    n *= c
    print(c, end=' * ')
print(f'{1}: {n}')'''
