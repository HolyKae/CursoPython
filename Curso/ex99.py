import random


def maior(* n):
    m = 0
    print('Os valores foram: ', end='')
    for c in n:
        print(c, end=' ')
        if m == 0:
            m = c
        else:
            if c > m:
                m = c
    print(f'\nE o maior valor foi: {m}')


maior(9, 8, 2, 4, 5, 3, 6)
