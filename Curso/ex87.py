n = [[], [], []]
lin = 0
col = 0
par = 0
ma2 = 0
som = 0
for c in range(9):
    num = int(input(f'Digite um valor para [{col}][{lin}]: '))
    n[col].append(num)
    if n[col][lin] % 2 == 0:
        par += n[col][lin]
    lin += 1
    if lin == 3:
        som += num
        lin = 0
    if (c + 1) % 3 == 0:
        col += 1
lin = 0
col = 0
for c in range(9):
    print(f'[{n[col][lin]:^5}]', end='   ')
    lin += 1
    if lin == 3:
        lin = 0
        print()
        print()
    if (c + 1) % 3 == 0:
        col += 1
n[1].sort()
print(f'A soma da 3º coluna é: {som}\nA soma dos números pares é: {par}\nO maior número da segunda linha é: {n[1][-1]}')
