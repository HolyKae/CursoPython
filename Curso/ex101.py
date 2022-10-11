def voto(n):
    from datetime import date
    a = date.today()
    n = a.year - n
    if n < 16:
        return print('Negado')
    if n > 65 or n < 18:
        return print('Opcional')
    else:
        return print('Obrigatório')


voto(int(input('Digite seu ano de nascimento: ')))
