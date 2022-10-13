def escreva(n):
    print('-' * (len(n)+2))
    print(f'{n}'.center(len(n)+2))
    print('-' * (len(n)+2))


while True:
    escreva('Sistema de ajuda PyHelp')
    h = input('Função ou Biblioteca > ')
    f = h.upper()
    if 'FIM' in f:
        escreva('Até logo!')
        break
    escreva(f'Acessando Manual do comando {h}')
    help(h)

