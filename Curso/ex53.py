f = input('Digite uma frase: ').upper().strip().replace(' ', '')
r = f[::-1]
if f == r:
    print('É Palindromo!')
else:
    print('Não é palindromo.')
