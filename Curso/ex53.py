f = input('Digite uma frase: ').upper().strip()
p = f.split()
j = ''.join(p)
r = ''
'''Sem for:
   f = input('Digite uma frase: ').upper().strip().replace(' ', '')
   r = f[::-1]
   if...'''
for le in range(len(j) - 1, -1, -1):
    r += j[le]
if j == r:
    print('É Palindromo!')
else:
    print('Não é palindromo.')