n1 = int(input('Digite 3 números: \n1º:'))
n2 = int(input('2º:'))
n3 = int(input('3º:'))
me = n1

if n1 > n3 > n2:
    me = n2
if n1 > n2 > n3:
    me = n3

ma = n1

if n1 < n3 < n2:
    ma = n2
if n1 < n2 < n3:
    ma = n3

print('Maior: {}'.format(ma))
print('Menor: {}'.format(me))
