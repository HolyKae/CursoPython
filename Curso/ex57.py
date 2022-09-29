s = ''
while 'M' != s and 'F' != s:
    s = input('Digite o seu sexo [M/F]: ').upper()
    print(s)
    if 'M' != s and 'F' != s:
        print('Digite um valor válido!')
