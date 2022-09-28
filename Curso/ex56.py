mi = 0
hv = 0
nh = ''
im = 0
for c in range(1, 5):
    n = input(f'Nome da {c}ª pessoa: ')
    i = int(input(f'Idade da {c}ª pessoa: '))
    s = int(input(f'Sexo da {c}ª pessoa:\n1- Masculino.\n2- Feminino.\n'))
    mi += i
    if s == 1 and i > hv:
        hv = i
        nh = n
    if s == 2 and i < 20:
        im += 1
print(f'A média da idade de todos é: {mi / 4}\nO homem mais vélho é o {nh}\n{im} Mulheres tem menos de 20 anos.')
