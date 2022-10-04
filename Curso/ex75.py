n = tuple(input(f'Digite o {c+1}º número: ') for c in range(4))
f = n.count(9)
if f == 0:
    print(f'O número 9 não apareceu nenhuma vez.')
else:
    print(f'O número 9 apareceu {f} vezes.')
f = n.index('3')
if f == 0:
    print('O número 3 não apareceu.')
else:
    print(f'O número 3 apareceu na {f+1}ª posição.')
print('Os números pares foram:', end=' ')
for i in range(len(n)):
    if int(n[i]) % 2 == 0:
        c = n[i]
        print(c, end=' ')
