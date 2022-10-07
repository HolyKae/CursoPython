n = [[], [], []]
lin = 0
col = 0
for c in range(9):
    num = int(input(f'Digite um valor para [{col}][{lin}]: '))
    n[col].append(num)
    lin += 1
    if lin == 3:
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
