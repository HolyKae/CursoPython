n = int(input('Digite um número: '))
f = int(input('Quantos elementos? '))
c = 0
f1 = n
f2 = n
f3 = 0
while c != f:
    c += 1
    f2 = f2 + f1
    f3 = f2 + f1
    f1 = f2
    print(n, f1, f2, f3)
