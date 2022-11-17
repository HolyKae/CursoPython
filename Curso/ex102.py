def fat(n, show=False):
    """
    Calcula o fatorial de um número n
    :param n: Número a ser calculado
    :param show: (Opcional) Mostrar ou não a conta
    :return: Resultado do fatorial do número n
    """
    f = 1
    for c in range(n, 1, -1):
        f *= c
        if show:
            print(c, end=' x ')
    if show:
        print('1 = ', end='')
    return f


print(fat(5, True))
