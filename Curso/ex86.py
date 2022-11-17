n = [[], [], []]
for l in range(3):
    for c in range(3):
        num = int(input(f'Digite um valor para [{l}][{c}]: '))
        n[l].append(num)
for l in range(3):
    for c in range(3):
        print(f'[{n[l][c]:^5}]', end='   ')
    print()

