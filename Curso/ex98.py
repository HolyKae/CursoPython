def contador():
    for c in range(10):
        print(f'{c + 1}', end=' ')
    print()
    for c in range(10, 0, -2):
        print(f'{c}', end=' ')
    print()
    f = [int(input('Começo: ')), int(input('Fim: ')), int(input('Passo: '))]
    if f[2] == 0:
        f[2] = 1
    if f[0] > f[1]:
        f[2] = -abs(f[2])
        for c in range(f[0], f[1] - 1, f[2]):
            print(f'{c}', end=' ')
    else:
        f[2] = abs(f[2])
        for c in range(f[0], f[1] + 1, f[2]):
            print(f'{c}', end=' ')


contador()
