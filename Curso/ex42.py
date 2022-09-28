t1 = float(input('Digite 3 números:\n1º:'))
t2 = float(input('2º:'))
t3 = float(input('3º:'))
if t1 + t2 > t3 and t3 + t2 > t1 and t3 + t1 > t2:
    print('Podem formar um triangulo:')
    if t1 == t2 == t3:
        print('Equilátero')
    elif t1 == t2 or t1 == t3 or t2 == t3:
        print('Isósceles')
    else:
        print('Escaleno.')
else:
    print('Não podem formar um triangulo')
