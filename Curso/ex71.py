n = int(input('Qual o valor a ser sacado? R$'))
n50 = n20 = n10 = n1 = 0
while n - 50 >= 0:
    n50 += 1
    n -= 50
while n - 20 >= 0:
    n20 += 1
    n -= 20
while n - 10 >= 0:
    n10 += 1
    n -= 10
while n - 1 >= 0:
    n1 += 1
    n -= 1
print(f'{n50} cédulas de R$50\n{n20} cédulas de R$20\n{n10} cédulas de R$10\n{n1} cédulas de R$1')
