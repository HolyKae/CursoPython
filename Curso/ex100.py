def sort(n):
    import random
    for c in range(5):
        n.append(random.randint(1, 50))
    print(f'Os valores sorteados foram: ', end='')
    for c in range(len(n)):
        print(num[c], end=' ')


def somPar(n):
    p = 0
    for c in range(len(n)):
        if n[c] % 2 == 0:
            p += n[c]
    print(f'A soma dos pares é: {p}')


num = []
sort(num)
print()
somPar(num)
