g = 0
f = 1000
for c in range(1, 6):
    p = float(input(f'Digite o peso da {c}ª pessoa: '))
    if p == 1:
        f = p
        g = p
    else:
        if p < f:
            f = p
        if p > g:
            g = p
print(f'A pessoa mais pesada pesa {g:.2f}Kg e a mais leve pesa {f:.2f}Kg')
