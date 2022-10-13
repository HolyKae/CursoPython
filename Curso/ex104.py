def leiaInt(u):
    n = input(u)
    while not n.isnumeric():
        print('Erro 404. Massa cinzenta não encontrada!')
        n = input(u)
    return n


n = leiaInt('Digite um número: ')
print(f'Você digitou o nº {n}')
