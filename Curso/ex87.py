n = [[], [], []]
par = 0
som = 0
for l in range(3):
    for c in range(3):
        num = int(input(f'Digite um valor para [{l}][{c}]: '))
        n[l].append(num)
        if n[l][c] % 2 == 0:
            par += n[l][c]
        if c == 2:
            som += num
for l in range(3):
    for c in range(3):
        print(f'[{n[l][c]:^5}]', end='   ')
    print()
n[1].sort()
print(f'A soma da 3º coluna é: {som}\nA soma dos números pares é: {par}\nO maior número da segunda linha é: {n[1][-1]}')
