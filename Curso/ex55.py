g = 0
f = 1000
for c in range(1, 6):
    p = float(input(f'Digite o peso da {c}ª pessoa: '))
    if p < f:
        f = p
    elif p > g:
        g = p
print(f'A pessoa mais pesada pesa {g:.2f}Kg e a mais leve pesa {f:.2f}Kg')
